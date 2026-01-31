"""Button platform for Pill Dispenser."""
from homeassistant.components.button import ButtonEntity
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
    """Set up the Pill Dispenser buttons."""
    coordinator: PillDispenserCoordinator = hass.data[DOMAIN][entry.entry_id]
    
    entities = []
    
    # Add general action buttons
    entities.extend([
        PillDispenserAlarmButton(coordinator, entry),
        PillDispenserDispenseButton(coordinator, entry),
        PillDispenserDismissButton(coordinator, entry),
    ])
    
    # Add custom alarm buttons (1-10 as examples)
    for alarm_id in range(1, 11):
        entities.append(PillDispenserCustomAlarmButton(coordinator, entry, alarm_id))
    
    # Add dropout buttons for each tray
    for tray_id in range(1, 11):
        entities.append(PillDispenserDropoutButton(coordinator, entry, tray_id))
        entities.append(PillDispenserFixButton(coordinator, entry, tray_id))
    
    async_add_entities(entities)


class PillDispenserAlarmButton(CoordinatorEntity, ButtonEntity):
    """Button to play the default alarm."""

    def __init__(
        self,
        coordinator: PillDispenserCoordinator,
        entry: ConfigEntry,
    ) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_alarm_default"
        self._attr_translation_key = "alarm_default"
        self._attr_icon = "mdi:bell-ring"
        self._attr_has_entity_name = True
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.host)},
        )

    async def async_press(self) -> None:
        """Handle the button press."""
        await self.coordinator.async_call_endpoint("alarm")
        await self.coordinator.async_request_refresh()


class PillDispenserCustomAlarmButton(CoordinatorEntity, ButtonEntity):
    """Button to play a custom alarm."""

    def __init__(
        self,
        coordinator: PillDispenserCoordinator,
        entry: ConfigEntry,
        alarm_id: int,
    ) -> None:
        super().__init__(coordinator)
        self._alarm_id = alarm_id
        self._attr_unique_id = f"{entry.entry_id}_alarm_{alarm_id}"
        self._attr_translation_key = "alarm_custom"
        self._attr_translation_placeholders = {"alarm_id": str(alarm_id)}
        self._attr_icon = "mdi:bell"
        self._attr_has_entity_name = True
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.host)},
        )

    async def async_press(self) -> None:
        """Handle the button press."""
        await self.coordinator.async_call_endpoint("alarm", {"id": self._alarm_id})
        await self.coordinator.async_request_refresh()


class PillDispenserDispenseButton(CoordinatorEntity, ButtonEntity):
    """Button to dispense the current tray in alert."""

    def __init__(
        self,
        coordinator: PillDispenserCoordinator,
        entry: ConfigEntry,
    ) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_dispense"
        self._attr_translation_key = "dispense"
        self._attr_icon = "mdi:pill"
        self._attr_has_entity_name = True
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.host)},
        )

    async def async_press(self) -> None:
        """Handle the button press."""
        await self.coordinator.async_call_endpoint("dispense")
        await self.coordinator.async_request_refresh()


class PillDispenserDropoutButton(CoordinatorEntity, ButtonEntity):
    """Button to drop a pill from a specific tray."""

    def __init__(
        self,
        coordinator: PillDispenserCoordinator,
        entry: ConfigEntry,
        tray_id: int,
    ) -> None:
        super().__init__(coordinator)
        self._tray_id = tray_id
        self._attr_unique_id = f"{entry.entry_id}_dropout_{tray_id}"
        self._attr_translation_key = "dropout"
        self._attr_translation_placeholders = {"tray_id": str(tray_id)}
        self._attr_icon = "mdi:arrow-down-bold-circle"
        self._attr_has_entity_name = True
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.host)},
        )

    async def async_press(self) -> None:
        """Handle the button press."""
        await self.coordinator.async_call_endpoint("dropout", {"tray": self._tray_id})
        await self.coordinator.async_request_refresh()


class PillDispenserDismissButton(CoordinatorEntity, ButtonEntity):
    """Button to dismiss the current alarm."""

    def __init__(
        self,
        coordinator: PillDispenserCoordinator,
        entry: ConfigEntry,
    ) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_dismiss"
        self._attr_translation_key = "dismiss"
        self._attr_icon = "mdi:bell-off"
        self._attr_has_entity_name = True
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.host)},
        )

    async def async_press(self) -> None:
        """Handle the button press."""
        await self.coordinator.async_call_endpoint("dismiss")
        await self.coordinator.async_request_refresh()


class PillDispenserFixButton(CoordinatorEntity, ButtonEntity):
    """Button to make a half step to fix a tray."""

    def __init__(
        self,
        coordinator: PillDispenserCoordinator,
        entry: ConfigEntry,
        tray_id: int,
    ) -> None:
        super().__init__(coordinator)
        self._tray_id = tray_id
        self._attr_unique_id = f"{entry.entry_id}_fix_{tray_id}"
        self._attr_translation_key = "fix"
        self._attr_translation_placeholders = {"tray_id": str(tray_id)}
        self._attr_icon = "mdi:wrench"
        self._attr_has_entity_name = True
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.host)},
        )

    async def async_press(self) -> None:
        """Handle the button press."""
        await self.coordinator.async_call_endpoint("fix", {"tray": self._tray_id})
        await self.coordinator.async_request_refresh()
