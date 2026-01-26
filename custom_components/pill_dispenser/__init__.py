"""The Pill Dispenser integration."""
from __future__ import annotations

import logging
from datetime import timedelta

import aiohttp
import async_timeout

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_NAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

_LOGGER = logging.getLogger(__name__)

DOMAIN = "pill_dispenser"
PLATFORMS = [Platform.SENSOR, Platform.BUTTON, Platform.SWITCH]

SCAN_INTERVAL = timedelta(seconds=30)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Pill Dispenser from a config entry."""
    host = entry.data[CONF_HOST]
    name = entry.data.get(CONF_NAME, f"Pill Dispenser ({host})")
    
    coordinator = PillDispenserCoordinator(hass, host, entry)
    await coordinator.async_config_entry_first_refresh()
    
    # Create device registry entry
    device_registry = dr.async_get(hass)
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={(DOMAIN, host)},
        manufacturer="Shaztech",
        name=name,
        model="Pill Dispenser",
        sw_version="1.0.0",
        configuration_url=f"http://{host}",
    )
    
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator
    
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    
    return unload_ok


class PillDispenserCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Pill Dispenser data."""

    def __init__(self, hass: HomeAssistant, host: str, entry: ConfigEntry) -> None:
        self.host = host
        self.entry = entry
        self.session = async_get_clientsession(hass)
        
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=SCAN_INTERVAL,
        )

    async def _async_update_data(self):
        """Update data via library."""
        data = {"trays": {}}
        
        try:
            async with async_timeout.timeout(10):
                # Get data for all 10 trays
                for tray_id in range(1, 11):
                    tray_data = {}
                    
                    # Get all tray information
                    tray_data["name"] = await self._get_tray_info("tr_name", tray_id)
                    tray_data["color"] = await self._get_tray_info("tr_color", tray_id)
                    tray_data["installed"] = await self._get_tray_info("tr_inst", tray_id)
                    tray_data["enabled"] = await self._get_tray_info("tr_enab", tray_id)
                    tray_data["triggered"] = await self._get_tray_info("tr_trig", tray_id)
                    tray_data["dispensed"] = await self._get_tray_info("tr_disp", tray_id)
                    tray_data["dismissed"] = await self._get_tray_info("tr_dism", tray_id)
                    tray_data["time"] = await self._get_tray_info("tr_time", tray_id)
                    
                    data["trays"][tray_id] = tray_data
                    
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")
        
        return data

    async def _get_tray_info(self, endpoint: str, tray_id: int) -> str:
        """Get information for a specific tray."""
        url = f"http://{self.host}/{endpoint}?id={tray_id}"
        try:
            async with self.session.get(url) as response:
                if response.status == 200:
                    return (await response.text()).strip()
                return ""
        except Exception as err:
            _LOGGER.debug(f"Error getting {endpoint} for tray {tray_id}: {err}")
            return ""

    async def async_call_endpoint(self, endpoint: str, params: dict = None) -> bool:
        """Call an endpoint on the pill dispenser."""
        url = f"http://{self.host}/{endpoint}"
        if params:
            param_str = "&".join([f"{k}={v}" for k, v in params.items()])
            url = f"{url}?{param_str}"
        
        try:
            async with async_timeout.timeout(10):
                async with self.session.get(url) as response:
                    return response.status == 200
        except Exception as err:
            _LOGGER.error(f"Error calling {endpoint}: {err}")
            return False
