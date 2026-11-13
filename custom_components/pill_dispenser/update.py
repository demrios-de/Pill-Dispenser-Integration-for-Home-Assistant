from __future__ import annotations

import asyncio
from datetime import timedelta
import logging
from typing import Any

from homeassistant.components.update import (
    UpdateDeviceClass,
    UpdateEntity,
    UpdateEntityFeature,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import PillDispenserCoordinator
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: PillDispenserCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([PillDispenserFirmwareUpdate(coordinator, entry)])


class PillDispenserFirmwareUpdate(CoordinatorEntity, UpdateEntity):

    _attr_device_class = UpdateDeviceClass.FIRMWARE
    _attr_supported_features = UpdateEntityFeature.INSTALL
    _attr_has_entity_name = True
    _attr_translation_key = "firmware"

    def __init__(
        self,
        coordinator: PillDispenserCoordinator,
        entry: ConfigEntry,
    ) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_firmware_update"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.host)},
        )
        self._latest_version: str | None = None
        self._update_available: bool = False
        self._in_progress: bool = False

    @property
    def available(self) -> bool:
        return (
            self.coordinator.data is not None
            and self.coordinator.supports_enhanced_api
            and super().available
        )

    @property
    def installed_version(self) -> str | None:
        if self.coordinator.data is None:
            return None
        return self.coordinator.data.get("system", {}).get("version")

    @property
    def latest_version(self) -> str | None:
        if self._latest_version:
            return self._latest_version
        return self.installed_version

    @property
    def in_progress(self) -> bool:
        return self._in_progress

    async def async_update(self) -> None:
        info = await self.coordinator.async_check_github_update()
        if info:
            self._latest_version = info.get("latest_version") or self.installed_version
            self._update_available = bool(info.get("update_available", False))

    async def async_install(
        self, version: str | None, backup: bool, **kwargs: Any
    ) -> None:
        self._in_progress = True
        self.async_write_ha_state()
        try:
            await self.coordinator.async_call_endpoint("api/ota_github", method="POST")
            await asyncio.sleep(45)
            await self.coordinator.async_request_refresh()
        finally:
            self._in_progress = False
            self.async_write_ha_state()
