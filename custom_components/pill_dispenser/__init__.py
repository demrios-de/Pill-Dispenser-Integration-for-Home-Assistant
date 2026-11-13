from __future__ import annotations

import logging
from datetime import timedelta

from aiohttp import web
import asyncio
import voluptuous as vol

from homeassistant.components import webhook
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_NAME, Platform
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.network import get_url
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

_LOGGER = logging.getLogger(__name__)

DOMAIN = "pill_dispenser"
PLATFORMS = [Platform.SENSOR, Platform.BUTTON, Platform.SWITCH, Platform.UPDATE]

SCAN_INTERVAL = timedelta(seconds=30)

SERVICE_DISPLACE = "displace"
SERVICE_DISPLACE_SCHEMA = vol.Schema(
    {
        vol.Required("tray"): vol.All(vol.Coerce(int), vol.Range(min=1, max=10)),
        vol.Optional("steps", default=1): vol.All(
            vol.Coerce(int), vol.Range(min=1, max=30)
        ),
    }
)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    host = entry.data[CONF_HOST]
    name = entry.data.get(CONF_NAME, f"Pill Dispenser ({host})")

    coordinator = PillDispenserCoordinator(hass, host, entry)
    await coordinator.async_config_entry_first_refresh()

    sw_version = (
        coordinator.data.get("system", {}).get("version", "1.0.0")
        if coordinator.data
        else "1.0.0"
    )

    device_registry = dr.async_get(hass)
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={(DOMAIN, host)},
        manufacturer="Shaztech",
        name=name,
        model="Pill Dispenser",
        sw_version=sw_version,
        configuration_url=f"http://{host}",
    )

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    webhook_id = f"{DOMAIN}_{entry.entry_id}"

    async def handle_webhook(
        hass: HomeAssistant, webhook_id: str, request: web.Request
    ) -> web.Response:
        try:
            payload = await request.json()
            _LOGGER.debug("Received Pill Dispenser webhook event: %s", payload)
        except Exception:
            _LOGGER.debug("Received webhook ping from Pill Dispenser")
        await coordinator.async_request_refresh()
        return web.Response(text="OK", status=200)

    webhook.async_register(
        hass,
        DOMAIN,
        f"{name} Push",
        webhook_id,
        handle_webhook,
    )
    coordinator.webhook_id = webhook_id

    if coordinator.supports_enhanced_api:
        await coordinator.async_register_webhook_on_device()

    if not hass.services.has_service(DOMAIN, SERVICE_DISPLACE):

        async def handle_displace_service(call: ServiceCall) -> None:
            tray = call.data["tray"]
            steps = call.data["steps"]
            for coord in hass.data.get(DOMAIN, {}).values():
                if isinstance(coord, PillDispenserCoordinator):
                    await coord.async_call_endpoint(
                        "displace", {"tray": tray, "steps": steps}
                    )
                    await coord.async_request_refresh()

        hass.services.async_register(
            DOMAIN,
            SERVICE_DISPLACE,
            handle_displace_service,
            schema=SERVICE_DISPLACE_SCHEMA,
        )

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    coordinator: PillDispenserCoordinator | None = hass.data.get(DOMAIN, {}).get(
        entry.entry_id
    )
    if coordinator and coordinator.webhook_id:
        webhook.async_unregister(hass, coordinator.webhook_id)

    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
        if not hass.data[DOMAIN] and hass.services.has_service(DOMAIN, SERVICE_DISPLACE):
            hass.services.async_remove(DOMAIN, SERVICE_DISPLACE)

    return unload_ok
class PillDispenserCoordinator(DataUpdateCoordinator):

    def __init__(self, hass: HomeAssistant, host: str, entry: ConfigEntry) -> None:
        self.host = host
        self.entry = entry
        self.session = async_get_clientsession(hass)
        self.supports_enhanced_api: bool = False
        self.webhook_id: str | None = None

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=SCAN_INTERVAL,
        )

    async def async_register_webhook_on_device(self) -> None:
        if not self.webhook_id:
            return
        try:
            base_url = get_url(self.hass, allow_external=False)
            webhook_url = f"{base_url}{webhook.async_generate_path(self.webhook_id)}"
            url = f"http://{self.host}/api/ha_webhook"
            async with asyncio.timeout(5):
                async with self.session.post(url, data={"url": webhook_url}) as resp:
                    if resp.status == 200:
                        _LOGGER.debug(
                            "Registered HA webhook %s on Pill Dispenser", webhook_url
                        )
        except Exception as err:
            _LOGGER.debug("Could not register HA webhook on device: %s", err)

    async def _async_update_data(self):
        try:
            async with asyncio.timeout(10):
                status_url = f"http://{self.host}/api/status"
                async with self.session.get(status_url) as response:
                    if response.status == 200:
                        payload = await response.json(content_type=None)
                        self.supports_enhanced_api = True
                        return self._parse_enhanced_status(payload)
        except Exception as err:
            _LOGGER.debug(
                "Enhanced /api/status not available (%s), falling back to legacy polling",
                err,
            )

        self.supports_enhanced_api = False
        return await self._fetch_legacy_data()

    def _parse_enhanced_status(self, payload: dict) -> dict:
        data = {
            "trays": {},
            "system": {
                "version": payload.get("version", ""),
                "hostname": payload.get("hostname", ""),
                "ip": payload.get("ip", self.host),
                "rssi": payload.get("rssi"),
                "free_heap": payload.get("free_heap"),
                "uptime_sec": payload.get("uptime_sec"),
                "installed_trays": payload.get("installed_trays", 0),
                "alert_in_progress": payload.get("alert_in_progress", False),
                "displacement_in_progress": payload.get(
                    "displacement_in_progress", False
                ),
                "mute_sound": payload.get("mute_sound", False),
                "ha_webhook_configured": payload.get("ha_webhook_configured", False),
            },
        }

        for tray_id in range(1, 11):
            data["trays"][tray_id] = {
                "name": "",
                "color": "0",
                "installed": "0",
                "enabled": "0",
                "paused": "0",
                "triggered": "0",
                "dispensed": "0",
                "dismissed": "0",
                "time": "00:00",
            }

        for tray in payload.get("trays", []):
            tray_id = int(tray.get("id", 0))
            if 1 <= tray_id <= 10:
                data["trays"][tray_id] = {
                    "name": str(tray.get("name", "")),
                    "color": str(tray.get("color", "0")),
                    "installed": "1" if tray.get("installed") else "0",
                    "enabled": "1" if tray.get("alert_enabled") else "0",
                    "paused": "1" if tray.get("paused") else "0",
                    "triggered": "1" if tray.get("triggered") else "0",
                    "dispensed": "1" if tray.get("dispensed_today") else "0",
                    "dismissed": "1" if tray.get("dismissed_today") else "0",
                    "time": str(tray.get("time", "00:00")),
                }

        return data

    async def _fetch_legacy_data(self) -> dict:
        data = {"trays": {}, "system": {}}

        try:
            async with asyncio.timeout(15):
                for tray_id in range(1, 11):
                    tray_data = {}
                    tray_data["name"] = await self._get_tray_info("tr_name", tray_id)
                    tray_data["color"] = await self._get_tray_info("tr_color", tray_id)
                    tray_data["installed"] = await self._get_tray_info(
                        "tr_inst", tray_id
                    )
                    tray_data["enabled"] = await self._get_tray_info("tr_enab", tray_id)
                    tray_data["paused"] = "0"
                    tray_data["triggered"] = await self._get_tray_info(
                        "tr_trig", tray_id
                    )
                    tray_data["dispensed"] = await self._get_tray_info(
                        "tr_disp", tray_id
                    )
                    tray_data["dismissed"] = await self._get_tray_info(
                        "tr_dism", tray_id
                    )
                    tray_data["time"] = await self._get_tray_info("tr_time", tray_id)
                    data["trays"][tray_id] = tray_data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}") from err

        return data

    async def _get_tray_info(self, endpoint: str, tray_id: int) -> str:
        url = f"http://{self.host}/{endpoint}?id={tray_id}"
        try:
            async with self.session.get(url) as response:
                if response.status == 200:
                    return (await response.text()).strip()
                return ""
        except Exception as err:
            _LOGGER.debug("Error getting %s for tray %s: %s", endpoint, tray_id, err)
            return ""

    async def async_call_endpoint(
        self, endpoint: str, params: dict | None = None, method: str = "GET"
    ) -> bool:
        url = f"http://{self.host}/{endpoint}"
        if params and method == "GET":
            param_str = "&".join([f"{k}={v}" for k, v in params.items()])
            url = f"{url}?{param_str}"

        try:
            async with asyncio.timeout(10):
                if method == "POST":
                    async with self.session.post(url, data=params) as response:
                        return response.status == 200
                async with self.session.get(url) as response:
                    return response.status == 200
        except Exception as err:
            _LOGGER.error("Error calling %s: %s", endpoint, err)
            return False

    async def async_check_github_update(self) -> dict | None:
        if not self.supports_enhanced_api:
            return None
        url = f"http://{self.host}/api/update_check"
        try:
            async with asyncio.timeout(10):
                async with self.session.get(url) as response:
                    if response.status == 200:
                        return await response.json(content_type=None)
        except Exception as err:
            _LOGGER.debug("Error checking firmware update: %s", err)
        return None
