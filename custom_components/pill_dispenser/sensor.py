"""Sensor platform for Pill Dispenser."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.entity import DeviceInfo

from . import PillDispenserCoordinator
from .const import DOMAIN, TRAY_COLORS


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Pill Dispenser sensors."""
    coordinator: PillDispenserCoordinator = hass.data[DOMAIN][entry.entry_id]
    
    entities = []
    
    # Create sensors for each tray (1-10)
    for tray_id in range(1, 11):
        entities.extend([
            PillDispenserTraySensor(coordinator, entry, tray_id, "name"),
            PillDispenserTraySensor(coordinator, entry, tray_id, "color"),
            PillDispenserTraySensor(coordinator, entry, tray_id, "installed"),
            PillDispenserTraySensor(coordinator, entry, tray_id, "enabled"),
            PillDispenserTraySensor(coordinator, entry, tray_id, "triggered"),
            PillDispenserTraySensor(coordinator, entry, tray_id, "dispensed"),
            PillDispenserTraySensor(coordinator, entry, tray_id, "dismissed"),
            PillDispenserTraySensor(coordinator, entry, tray_id, "time"),
        ])
    
    async_add_entities(entities)


class PillDispenserTraySensor(CoordinatorEntity, SensorEntity):
    """Representation of a Pill Dispenser Tray Sensor."""

    def __init__(
        self,
        coordinator: PillDispenserCoordinator,
        entry: ConfigEntry,
        tray_id: int,
        sensor_type: str,
    ) -> None:
        super().__init__(coordinator)
        self._tray_id = tray_id
        self._sensor_type = sensor_type
        self._attr_unique_id = f"{entry.entry_id}_tray_{tray_id}_{sensor_type}"
        
        # Set translation key for automatic translation
        self._attr_translation_key = f"tray_{sensor_type}"
        self._attr_translation_placeholders = {"tray_id": str(tray_id)}
        
        # Set friendly names (fallback if translation not available)
        type_names = {
            "name": "Name",
            "color": "Color",
            "installed": "Installed",
            "enabled": "Enabled",
            "triggered": "Triggered",
            "dispensed": "Dispensed",
            "dismissed": "Dismissed",
            "time": "Alarm Time",
        }
        
        self._attr_has_entity_name = True
        
        # Link to device
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.host)},
        )

    @property
    def native_value(self) -> str | None:
        if self.coordinator.data is None:
            return None
        
        tray_data = self.coordinator.data.get("trays", {}).get(self._tray_id, {})
        value = tray_data.get(self._sensor_type, "")
        
        # Convert color codes to names
        if self._sensor_type == "color" and value in TRAY_COLORS:
            return TRAY_COLORS[value]
        
        # Convert 0/1 to Yes/No for boolean values
        if self._sensor_type in ["installed", "enabled", "triggered", "dispensed", "dismissed"]:
            return "Yes" if value == "1" else "No"
        
        return value

    @property
    def icon(self) -> str:
        icons = {
            "name": "mdi:pill",
            "color": "mdi:palette",
            "installed": "mdi:check-circle",
            "enabled": "mdi:toggle-switch",
            "triggered": "mdi:bell-ring",
            "dispensed": "mdi:check",
            "dismissed": "mdi:close-circle",
            "time": "mdi:clock",
        }
        return icons.get(self._sensor_type, "mdi:pill")

    @property
    def extra_state_attributes(self) -> dict[str, any]:
        if self.coordinator.data is None:
            return {}
        
        tray_data = self.coordinator.data.get("trays", {}).get(self._tray_id, {})
        
        # Add tray info as attributes for easy access in automations
        attributes = {
            "tray_number": self._tray_id,
        }
        
        # Add tray name if this is not the name sensor itself
        if self._sensor_type != "name":
            tray_name = tray_data.get("name", "")
            if tray_name:
                attributes["tray_name"] = tray_name
        
        return attributes
