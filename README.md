# Home Assistant Pill Dispenser Integration

[![GitHub release](https://img.shields.io/github/v/release/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant)](https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/releases)
[![License](https://img.shields.io/github/license/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant)](LICENSE)
[![HACS](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

[🇬🇧 English](#english) | [🇩🇪 Deutsch](#deutsch)

---

## English

<a name="english"></a>

Control your [Shaztech Pill Dispenser](https://github.com/Shaztech/Pilldispenser) with Home Assistant!

### Quick Install

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=demrios-de&repository=Pill-Dispenser-Integration-for-Home-Assistant&category=integration)

**Via HACS:**
1. Click badge above or add custom repository manually
2. HACS → Integrations → ⋮ → Custom repositories
3. Add: `https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant`
4. Category: Integration
5. Install "Pill Dispenser"
6. Restart Home Assistant

**Manual:**
1. Download from [Releases](https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/releases)
2. Extract to `config/custom_components/pill_dispenser/`
3. Restart Home Assistant

### Setup

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=pill_dispenser)

1. Settings → Devices & Services → Add Integration
2. Search "Pill Dispenser"
3. Enter IP address (e.g., `192.168.1.100`)
4. Optional: Custom name

### Features

- 80 sensors for all tray information
- 43 buttons for control
- 10 switches for status
- Automatic updates every 30 seconds
- Multi-language (EN, DE, FR)

### Example

```yaml
automation:
  - alias: "Medication Reminder"
    trigger:
      platform: state
      entity_id: sensor.pill_dispenser_tray_1_triggered
      to: "Yes"
    action:
      service: notify.mobile_app
      data:
        message: "Time for medication"
```

### Support

- [Report Issues](https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/issues)
- [Documentation](https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant)

---

## Deutsch

<a name="deutsch"></a>

Steuere deinen [Shaztech Pill Dispenser](https://github.com/Shaztech/Pilldispenser) mit Home Assistant!

### Schnellinstallation

[![Öffne deine Home Assistant Instanz und öffne ein Repository im Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=demrios-de&repository=Pill-Dispenser-Integration-for-Home-Assistant&category=integration)

**Via HACS:**
1. Badge oben klicken oder Repository manuell hinzufügen
2. HACS → Integrationen → ⋮ → Benutzerdefinierte Repositories
3. URL: `https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant`
4. Kategorie: Integration
5. "Pill Dispenser" installieren
6. Home Assistant neu starten

**Manuell:**
1. Download von [Releases](https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/releases)
2. Entpacken nach `config/custom_components/pill_dispenser/`
3. Home Assistant neu starten

### Einrichtung

[![Öffne deine Home Assistant Instanz und starte die Einrichtung einer neuen Integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=pill_dispenser)

1. Einstellungen → Geräte & Dienste → Integration hinzufügen
2. Suche "Pill Dispenser"
3. IP-Adresse eingeben (z.B. `192.168.1.100`)
4. Optional: Eigener Name

### Funktionen

- 80 Sensoren für alle Fach-Informationen
- 43 Buttons zur Steuerung
- 10 Schalter für Status
- Automatische Aktualisierung alle 30 Sekunden
- Mehrsprachig (EN, DE, FR)

### Beispiel

```yaml
automation:
  - alias: "Medikamenten-Erinnerung"
    trigger:
      platform: state
      entity_id: sensor.pill_dispenser_tray_1_triggered
      to: "Yes"
    action:
      service: notify.mobile_app
      data:
        message: "Zeit für Medikamente"
```

### Support

- [Fehler melden](https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/issues)
- [Dokumentation](https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant)

---

## License

MIT License - see [LICENSE](LICENSE)

## Credits

- Hardware: [Shaztech Pill Dispenser](https://github.com/Shaztech/Pilldispenser)
- Integration: Community contribution
- Icon: AI-generated

---

**If you find this useful, please ⭐ star this repo!**

**Wenn du das nützlich findest, gib bitte einen ⭐ Stern!**
