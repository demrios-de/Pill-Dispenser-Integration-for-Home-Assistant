from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import PillDispenserCoordinator
from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: PillDispenserCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []
    for tray_id in range(1, 11):
        entities.append(PillDispenserTraySwitch(coordinator, entry, tray_id))
        entities.append(PillDispenserTrayPauseSwitch(coordinator, entry, tray_id))

    async_add_entities(entities)


class PillDispenserTraySwitch(CoordinatorEntity, SwitchEntity):

    def __init__(
        self,
        coordinator: PillDispenserCoordinator,
        entry: ConfigEntry,
        tray_id: int,
    ) -> None:
        super().__init__(coordinator)
        self._tray_id = tray_id
        self._attr_unique_id = f"{entry.entry_id}_tray_{tray_id}_enabled"
        self._attr_translation_key = "tray_enabled"
        self._attr_translation_placeholders = {"tray_id": str(tray_id)}
        self._attr_icon = "mdi:toggle-switch"
        self._attr_has_entity_name = True
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.host)},
        )

    @property
    def is_on(self) -> bool | None:
        if self.coordinator.data is None:
            return None
        tray_data = self.coordinator.data.get("trays", {}).get(self._tray_id, {})
        return tray_data.get("enabled", "0") == "1"

    async def async_turn_on(self, **kwargs):
        pass

    async def async_turn_off(self, **kwargs):
        pass

    @property
    def available(self) -> bool:
        if self.coordinator.data is None:
            return False
        tray_data = self.coordinator.data.get("trays", {}).get(self._tray_id, {})
        return tray_data.get("installed", "0") == "1" and super().available


class PillDispenserTrayPauseSwitch(CoordinatorEntity, SwitchEntity):

    def __init__(
        self,
        coordinator: PillDispenserCoordinator,
        entry: ConfigEntry,
        tray_id: int,
    ) -> None:
        super().__init__(coordinator)
        self._tray_id = tray_id
        self._attr_unique_id = f"{entry.entry_id}_tray_{tray_id}_paused"
        self._attr_translation_key = "tray_paused"
        self._attr_translation_placeholders = {"tray_id": str(tray_id)}
        self._attr_icon = "mdi:pause-circle-outline"
        self._attr_has_entity_name = True
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.host)},
        )

    @property
    def is_on(self) -> bool | None:
        if self.coordinator.data is None:
            return None
        tray_data = self.coordinator.data.get("trays", {}).get(self._tray_id, {})
        return tray_data.get("paused", "0") == "1"

    async def async_turn_on(self, **kwargs) -> None:
        if await self.coordinator.async_call_endpoint(
            "tray_pause", {"tray": self._tray_id, "paused": 1}
        ):
            await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs) -> None:
        if await self.coordinator.async_call_endpoint(
            "tray_pause", {"tray": self._tray_id, "paused": 0}
        ):
            await self.coordinator.async_request_refresh()

    @property
    def available(self) -> bool:
        if self.coordinator.data is None or not self.coordinator.supports_enhanced_api:
            return False
        tray_data = self.coordinator.data.get("trays", {}).get(self._tray_id, {})
        return tray_data.get("installed", "0") == "1" and super().available
