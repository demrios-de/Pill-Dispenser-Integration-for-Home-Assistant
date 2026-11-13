# Home Assistant Pill Dispenser Integration

[![HACS](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

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
- 43 buttons for control (alarms, dispense, dismiss, fix)
- 10 switches for tray enabled status
- Multi-language (EN, DE)

#### 🆕 New in v1.1.0 *(requires updated Pill Dispenser firmware – pending merge of PR in `Shaztech/Pilldispenser`)*
> **Note:** On older dispenser firmware versions, the integration automatically falls back to standard 30-second polling and keeps all core features working seamlessly.

- **Real-time Webhook Push (`/api/ha_webhook`)**: Instant state updates in Home Assistant without polling delay
- **Batched Status API (`/api/status`)**: Fetches all states in 1 request instead of 80
- **10 Holiday / Pause Mode Switches**: Pause or resume scheduled alerts per tray (`/tray_pause`)
- **10 Advance Tray Buttons & `pill_dispenser.displace` Service**: Advance any tray by 1 step via button or 1–30 steps via service (`/displace`)
- **3 Diagnostic Sensors**: Wi-Fi signal strength (RSSI), free heap memory & device uptime
- **Firmware Update Entity**: Check for new GitHub releases and install OTA updates directly from Home Assistant


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

### Documentation

- [Medication Tracking Examples](docs/MEDICATION_TRACKING.md)
- [Dashboard Examples](docs/DASHBOARD_EXAMPLES.md)
- [Add Translations](custom_components/pill_dispenser/TRANSLATIONS.md)

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
- 43 Buttons zur Steuerung (Alarme, Ausgabe, Alarm deaktivieren, Justieren)
- 10 Schalter für den Fach-Status
- Mehrsprachig (EN, DE)

#### 🆕 Neu in v1.1.0 *(erfordert aktualisierte Pill-Dispenser-Firmware – sobald der Pull Request in `Shaztech/Pilldispenser` angenommen wurde)*
> **Hinweis:** Mit älteren Firmware-Versionen fällt die Integration automatisch auf das bisherige 30-Sekunden-Polling zurück – alle Grundfunktionen laufen weiterhin ohne Einschränkung.

- **Echtzeit-Push per Webhook (`/api/ha_webhook`)**: Sofortige Status-Aktualisierung in Home Assistant ohne Polling-Verzögerung
- **Gebündelte Status-API (`/api/status`)**: Ruft alle Daten in 1 Anfrage statt 80 Einzelabfragen ab
- **10 Urlaubs- / Pause-Modus-Schalter**: Pausiert oder aktiviert geplante Alarme pro Fach (`/tray_pause`)
- **10 Vorschieben-Buttons & Dienst `pill_dispenser.displace`**: Schiebt ein Fach per Button um 1 Schritt oder per Dienst um 1–30 Schritte vor (`/displace`)
- **3 Diagnose-Sensoren**: WLAN-Signalstärke (RSSI), freier Speicher & Laufzeit
- **Firmware-Update-Entität**: Prüft GitHub-Releases und startet OTA-Updates direkt aus Home Assistant


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

### Dokumentation

- [Medikamenten-Tracking Beispiele](docs/MEDICATION_TRACKING.md)
- [Dashboard Beispiele](docs/DASHBOARD_EXAMPLES.md)
- [Übersetzungen hinzufügen](custom_components/pill_dispenser/TRANSLATIONS.md)

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
