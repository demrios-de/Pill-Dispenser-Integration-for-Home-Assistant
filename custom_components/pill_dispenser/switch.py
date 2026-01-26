"""Switch platform for Pill Dispenser."""
from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.entity import DeviceInfo

from . import PillDispenserCoordinator
from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Pill Dispenser switches."""
    coordinator: PillDispenserCoordinator = hass.data[DOMAIN][entry.entry_id]
    
    entities = []
    
    # Note: The API doesn't seem to provide enable/disable endpoints,
    # so we're creating read-only switches that show the enabled state.
    # If the API supports toggling in the future, the turn_on/turn_off methods can be implemented.
    
    for tray_id in range(1, 11):
        entities.append(PillDispenserTraySwitch(coordinator, entry, tray_id))
    
    async_add_entities(entities)


class PillDispenserTraySwitch(CoordinatorEntity, SwitchEntity):
    """Representation of a Pill Dispenser Tray Enable/Disable switch."""

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
        self._attr_name = f"Tray {tray_id} Enabled"
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
        enabled = tray_data.get("enabled", "0")
        return enabled == "1"

    async def async_turn_on(self, **kwargs):
        """Turn the entity on."""
        # Note: The API documentation doesn't show an endpoint to enable/disable trays
        # This would need to be implemented if such an endpoint exists
        # For now, this is read-only
        pass

    async def async_turn_off(self, **kwargs):
        """Turn the entity off."""
        # Note: The API documentation doesn't show an endpoint to enable/disable trays
        # This would need to be implemented if such an endpoint exists
        # For now, this is read-only
        pass

    @property
    def available(self) -> bool:
        # Check if tray is installed
        if self.coordinator.data is None:
            return False
        
        tray_data = self.coordinator.data.get("trays", {}).get(self._tray_id, {})
        installed = tray_data.get("installed", "0")
        return installed == "1" and super().available
