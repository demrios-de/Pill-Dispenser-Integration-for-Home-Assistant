# Changelog

All notable changes to this project will be documented in this file.

## - 2026-11-13

> **Compatibility Note:** All new API-based features below require the corresponding firmware update on the Pill Dispenser (currently submitted as a Pull Request to `Shaztech/Pilldispenser`). When connected to older firmware versions, the integration automatically falls back to legacy polling so existing setups continue working without changes.

### Added
- **Batched JSON polling (`/api/status`)**: Fetches all device and tray states in a single HTTP request instead of 80 individual requests (with automatic fallback for older firmware).
- **Real-time Webhook Push (`/api/ha_webhook`)**: Automatically registers a local Home Assistant webhook on the dispenser for instant state updates without polling delay *(requires updated firmware)*.
- **Holiday / Pause Mode Switches**: Added 10 switches (`tray_paused`) to pause or resume scheduled alerts per tray (`/tray_pause`) *(requires updated firmware)*.
- **Advance Tray Controls (`/displace`)**: Added 10 buttons (`Advance Tray X` for 1 step) and the `pill_dispenser.displace` service (1–30 steps) for easy refilling and resetting *(requires updated firmware)*.
- **Diagnostic Sensors**: Added Wi-Fi signal strength (`rssi`), free heap memory (`free_heap`), and device uptime (`uptime_sec`) *(requires updated firmware)*.
- **Firmware Update Entity**: Added native Home Assistant `update` entity to check GitHub releases (`/api/update_check`) and install OTA updates (`/api/ota_github`) *(requires updated firmware)*.

### Fixed
- Replaced deprecated `async_timeout` with Python's built-in `asyncio.timeout` for Home Assistant 2026+ compatibility.
- Removed non-standard `_meta` list key from translation JSON files to prevent placeholder validation errors in Home Assistant 2026+.


## [1.0.0] - 2026-01-26

### Added
- Initial release
- Support for all 10 trays
- 80 sensors (name, color, installed, enabled, triggered, dispensed, dismissed, time)
- 43 buttons (alarms, dispense, dismiss, fix functions)
- 10 switches (tray enabled/disabled status)
- UI configuration flow
- Multi-language support (English, German, French)
- Translation system with placeholders
- Custom device naming
- Automatic polling (30 second interval)
- HACS compatibility
- Blueprints for medication tracking
- Documentation for setup and usage

### Features
- Local network communication (no cloud required)
- Device grouping (all entities under one device)
- Custom icons for integration
- Tray name and number attributes on sensors
- Professional documentation

## [Unreleased]

### Planned
- Additional language translations
- More automation blueprints
- Enhanced error handling
- Statistics and history tracking
