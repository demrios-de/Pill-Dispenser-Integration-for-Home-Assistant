# Pill Dispenser Integration for Home Assistant

Control your [Shaztech Pill Dispenser](https://github.com/Shaztech/Pilldispenser) with Home Assistant.

## Installation

### Via HACS (Custom Repository)

1. Open HACS → Integrations
2. Click three dots (⋮) → Custom repositories
3. Add: `https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant`
4. Category: Integration
5. Install "Pill Dispenser"
6. Restart Home Assistant

### Manual

1. Download latest release from [GitHub](https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/releases)
2. Extract to `custom_components/pill_dispenser/`
3. Restart Home Assistant

## Configuration

1. Go to Settings → Devices & Services
2. Click "Add Integration"
3. Search for "Pill Dispenser"
4. Enter IP address (e.g., `192.168.1.100`)
5. Optional: Set custom name

## Features

- 80 sensors (10 trays × 8 properties each)
- 43 buttons (alarms, dispense, dismiss, fix)
- 10 switches (tray status)
- Automatic polling every 30 seconds
- Multi-language support (EN, DE, FR)

### Sensors

Each tray provides:
- Name
- Color (LED)
- Installed status
- Enabled status
- Triggered status
- Dispensed status
- Dismissed status
- Alarm time

### Buttons

- Play default alarm
- Play custom alarms (1-10)
- Dispense current tray
- Dismiss alarm
- Drop specific tray (1-10)
- Fix tray alignment (1-10)

## Example Automation

```yaml
automation:
  - alias: "Medication Reminder"
    trigger:
      - platform: state
        entity_id: sensor.pill_dispenser_tray_1_triggered
        to: "Yes"
    action:
      - service: notify.mobile_app
        data:
          title: "Time for Medication"
          message: "Please take your pills"
```

## Troubleshooting

**Integration not found:**
- Restart Home Assistant after installation
- Check `config/custom_components/pill_dispenser/` exists

**Cannot connect:**
- Verify IP address
- Ensure device is powered on and on network
- Try: `ping 192.168.1.100`

**Icons not showing:**
- Clear browser cache (Ctrl+Shift+R)
- Restart Home Assistant
- Reload integration

## Support

- [Report Issues](https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/issues)
- [Request Features](https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/issues)
- [Home Assistant Community](https://community.home-assistant.io/)

## Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit translations
- Create pull requests

## Credits

- Hardware: [Shaztech Pill Dispenser](https://github.com/Shaztech/Pilldispenser)
- Integration: Community contribution

## License

MIT License - see [LICENSE](LICENSE)

## Disclaimer

This is a community integration, not officially affiliated with Shaztech or Home Assistant. Use at your own risk.
