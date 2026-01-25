# Home Assistant Pill Dispenser Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![GitHub release](https://img.shields.io/github/v/release/DEIN-USERNAME/ha-pill-dispenser)](https://github.com/DEIN-USERNAME/ha-pill-dispenser/releases)
[![License](https://img.shields.io/github/license/DEIN-USERNAME/ha-pill-dispenser)](LICENSE)

[🇬🇧 English](#english) | [🇩🇪 Deutsch](#deutsch)

---

## English

<a name="english"></a>

Control your [Shaztech Pill Dispenser](https://github.com/Shaztech/Pilldispenser) with Home Assistant!

### Quick Install

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=DEIN-USERNAME&repository=ha-pill-dispenser&category=integration)

Click the badge above to add this integration to HACS, or add it manually:

**Via HACS (recommended):**
1. Open HACS → Integrations
2. Click the three dots (⋮) → Custom repositories
3. Add: `https://github.com/DEIN-USERNAME/ha-pill-dispenser`
4. Category: Integration
5. Click "Add"
6. Search for "Pill Dispenser" and install
7. Restart Home Assistant

**Manual Installation:**
1. Download `pill_dispenser_v1.0.0.zip` from [Releases](https://github.com/DEIN-USERNAME/ha-pill-dispenser/releases)
2. Unzip and copy the `pill_dispenser` folder to `config/custom_components/`
3. Restart Home Assistant

### Features ✨

- 🔔 **80 Sensors** - Complete status information for all 10 trays
- 🎮 **43 Buttons** - All control functions (alarms, dispense, dismiss, fix)
- 🔀 **10 Switches** - Tray enable/disable status
- 🌐 **Easy Setup** - UI-based configuration flow
- 🏷️ **Custom Naming** - Optional device names
- 🌍 **Multilingual** - English, German, French translations
- 📱 **Device Integration** - All entities grouped under one device
- 🔄 **Auto Polling** - Updates every 30 seconds

### Configuration

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=pill_dispenser)

After installation:
1. Go to **Settings → Devices & Services → Add Integration**
2. Search for "Pill Dispenser"
3. Enter your Pill Dispenser IP address (e.g., `192.168.1.100`)
4. Optional: Enter a custom name (default: "Pill Dispenser")
5. Click Submit

### Example Automation

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
          title: "💊 Medication Time!"
          message: >
            {% set tray_name = state_attr('sensor.pill_dispenser_tray_1_triggered', 'tray_name') %}
            Time for: {{ tray_name if tray_name else 'your medication' }}
      - delay: "00:05:00"
      - service: button.press
        target:
          entity_id: button.pill_dispenser_dismiss_alarm
```

### Dashboard Example

```yaml
type: entities
title: Pill Dispenser
entities:
  - entity: sensor.pill_dispenser_tray_1_time
    name: Next Medication
  - entity: sensor.pill_dispenser_tray_1_triggered
    name: Alarm Active
  - entity: button.pill_dispenser_play_default_alarm
    name: Test Alarm
  - entity: button.pill_dispenser_dispense_current
    name: Dispense Now
```

### Entities

#### Sensors (80 total)
For each of the 10 trays:
- Name - Tray name from device
- Color - LED color (Red, Green, Blue, Yellow, Orange, Purple, White, Black)
- Installed - Is tray physically present (Yes/No)
- Enabled - Is tray enabled (Yes/No)
- Triggered - Is alarm currently active (Yes/No)
- Dispensed - Was medication dispensed (Yes/No)
- Dismissed - Was alarm dismissed (Yes/No)
- Alarm Time - Scheduled time for this tray

**Extra Attributes:**
- `tray_number` - Tray number (1-10)
- `tray_name` - Name from the device (for dynamic messages)

#### Buttons (43 total)
- Play Default Alarm
- Play Custom Alarm 1-10
- Dispense Current Tray
- Dismiss Active Alarm
- Drop Tray 1-10 (manual dispense)
- Fix Tray 1-10 (realign mechanism)

#### Switches (10 total)
- Tray 1-10 Enabled (read-only status)

### Requirements

- Home Assistant 2023.x or newer
- [Shaztech Pill Dispenser](https://github.com/Shaztech/Pilldispenser) in your local network
- Python 3.11+

### Troubleshooting

**Integration not found:**
- Make sure you restarted Home Assistant after installation
- Check that files are in `config/custom_components/pill_dispenser/`

**Cannot connect:**
- Verify the IP address is correct
- Ensure the Pill Dispenser is powered on and connected to your network
- Try pinging the device: `ping 192.168.1.100`

**Entities not updating:**
- Check Home Assistant logs: Settings → System → Logs
- The integration polls every 30 seconds

### Support

- 🐛 [Report Bugs](https://github.com/DEIN-USERNAME/ha-pill-dispenser/issues)
- 💡 [Request Features](https://github.com/DEIN-USERNAME/ha-pill-dispenser/issues)
- 💬 [Community Forum](https://community.home-assistant.io/)
- 📖 [Full Documentation](https://github.com/DEIN-USERNAME/ha-pill-dispenser)

### Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

**Need a translation?** See [TRANSLATIONS.md](TRANSLATIONS.md) for instructions!

### License

This Home Assistant integration is licensed under the **MIT License**. See [LICENSE](LICENSE) file for details.

### Credits

- **Hardware & Firmware:** [Shaztech Pill Dispenser](https://github.com/Shaztech/Pilldispenser)
- **Icon Design:** AI-generated
- **Integration Development:** Community contribution

### Disclaimer

This is a community-developed integration and is not officially affiliated with or endorsed by Shaztech or Home Assistant. Use at your own risk.

---

## Deutsch

<a name="deutsch"></a>

Steuere deinen [Shaztech Pill Dispenser](https://github.com/Shaztech/Pilldispenser) mit Home Assistant!

### Schnellinstallation

[![Öffne deine Home Assistant Instanz und öffne ein Repository im Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=DEIN-USERNAME&repository=ha-pill-dispenser&category=integration)

Klicke auf das Badge oben, um die Integration zu HACS hinzuzufügen, oder füge sie manuell hinzu:

**Via HACS (empfohlen):**
1. Öffne HACS → Integrationen
2. Klicke auf die drei Punkte (⋮) → Benutzerdefinierte Repositories
3. Füge hinzu: `https://github.com/DEIN-USERNAME/ha-pill-dispenser`
4. Kategorie: Integration
5. Klicke auf "Hinzufügen"
6. Suche nach "Pill Dispenser" und installiere
7. Starte Home Assistant neu

**Manuelle Installation:**
1. Lade `pill_dispenser_v1.0.0.zip` von [Releases](https://github.com/DEIN-USERNAME/ha-pill-dispenser/releases) herunter
2. Entpacke und kopiere den `pill_dispenser` Ordner nach `config/custom_components/`
3. Starte Home Assistant neu

### Funktionen ✨

- 🔔 **80 Sensoren** - Vollständige Statusinformationen für alle 10 Fächer
- 🎮 **43 Buttons** - Alle Steuerungsfunktionen (Alarme, Ausgabe, Verwerfen, Justieren)
- 🔀 **10 Schalter** - Fach Aktiviert/Deaktiviert Status
- 🌐 **Einfache Einrichtung** - UI-basierter Konfigurationsfluss
- 🏷️ **Eigene Namen** - Optionale Gerätenamen
- 🌍 **Mehrsprachig** - Englisch, Deutsch, Französisch Übersetzungen
- 📱 **Geräteintegration** - Alle Entities unter einem Gerät gruppiert
- 🔄 **Auto-Aktualisierung** - Aktualisiert alle 30 Sekunden

### Konfiguration

[![Öffne deine Home Assistant Instanz und starte die Einrichtung einer neuen Integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=pill_dispenser)

Nach der Installation:
1. Gehe zu **Einstellungen → Geräte & Dienste → Integration hinzufügen**
2. Suche nach "Pill Dispenser"
3. Gib die IP-Adresse deines Pill Dispensers ein (z.B. `192.168.1.100`)
4. Optional: Gib einen benutzerdefinierten Namen ein (Standard: "Pill Dispenser")
5. Klicke auf Senden

### Beispiel-Automation

```yaml
automation:
  - alias: "Medikamenten-Erinnerung"
    trigger:
      - platform: state
        entity_id: sensor.pill_dispenser_tray_1_triggered
        to: "Yes"
    action:
      - service: notify.mobile_app
        data:
          title: "💊 Zeit für Medikamente!"
          message: >
            {% set tray_name = state_attr('sensor.pill_dispenser_tray_1_triggered', 'tray_name') %}
            Zeit für: {{ tray_name if tray_name else 'deine Medikamente' }}
      - delay: "00:05:00"
      - service: button.press
        target:
          entity_id: button.pill_dispenser_dismiss_alarm
```

### Dashboard-Beispiel

```yaml
type: entities
title: Pill Dispenser
entities:
  - entity: sensor.pill_dispenser_tray_1_time
    name: Nächste Medikation
  - entity: sensor.pill_dispenser_tray_1_triggered
    name: Alarm aktiv
  - entity: button.pill_dispenser_play_default_alarm
    name: Alarm testen
  - entity: button.pill_dispenser_dispense_current
    name: Jetzt ausgeben
```

### Entities

#### Sensoren (80 gesamt)
Für jedes der 10 Fächer:
- Name - Fachname vom Gerät
- Farbe - LED-Farbe (Rot, Grün, Blau, Gelb, Orange, Lila, Weiß, Schwarz)
- Installiert - Ist Fach physisch vorhanden (Ja/Nein)
- Aktiviert - Ist Fach aktiviert (Ja/Nein)
- Ausgelöst - Ist Alarm aktuell aktiv (Ja/Nein)
- Ausgegeben - Wurde Medikament ausgegeben (Ja/Nein)
- Verworfen - Wurde Alarm verworfen (Ja/Nein)
- Alarmzeit - Geplante Zeit für dieses Fach

**Zusätzliche Attribute:**
- `tray_number` - Fachnummer (1-10)
- `tray_name` - Name vom Gerät (für dynamische Nachrichten)

#### Buttons (43 gesamt)
- Standard-Alarm abspielen
- Benutzerdefinierten Alarm 1-10 abspielen
- Aktuelles Fach ausgeben
- Aktiven Alarm deaktivieren
- Fach 1-10 ausgeben (manuelle Ausgabe)
- Fach 1-10 justieren (Mechanismus ausrichten)

#### Schalter (10 gesamt)
- Fach 1-10 Aktiviert (nur Status, nicht änderbar)

### Anforderungen

- Home Assistant 2023.x oder neuer
- [Shaztech Pill Dispenser](https://github.com/Shaztech/Pilldispenser) in deinem lokalen Netzwerk
- Python 3.11+

### Fehlerbehebung

**Integration nicht gefunden:**
- Stelle sicher, dass du Home Assistant nach der Installation neu gestartet hast
- Prüfe, ob die Dateien in `config/custom_components/pill_dispenser/` liegen

**Verbindung nicht möglich:**
- Überprüfe, ob die IP-Adresse korrekt ist
- Stelle sicher, dass der Pill Dispenser eingeschaltet und mit deinem Netzwerk verbunden ist
- Versuche das Gerät anzupingen: `ping 192.168.1.100`

**Entities aktualisieren nicht:**
- Prüfe die Home Assistant Logs: Einstellungen → System → Protokolle
- Die Integration aktualisiert alle 30 Sekunden

### Support

- 🐛 [Fehler melden](https://github.com/DEIN-USERNAME/ha-pill-dispenser/issues)
- 💡 [Features vorschlagen](https://github.com/DEIN-USERNAME/ha-pill-dispenser/issues)
- 💬 [Community Forum](https://community.home-assistant.io/)
- 📖 [Vollständige Dokumentation](https://github.com/DEIN-USERNAME/ha-pill-dispenser)

### Mitmachen

Beiträge sind willkommen! Bitte:
1. Fork das Repository
2. Erstelle einen Feature-Branch
3. Mache deine Änderungen
4. Erstelle einen Pull Request

**Übersetzung benötigt?** Siehe [TRANSLATIONS.md](TRANSLATIONS.md) für Anweisungen!

### Lizenz

Diese Home Assistant Integration ist unter der **MIT License** lizenziert. Siehe [LICENSE](LICENSE) Datei für Details.

### Credits

- **Hardware & Firmware:** [Shaztech Pill Dispenser](https://github.com/Shaztech/Pilldispenser)
- **Icon Design:** KI-generiert
- **Integrationsentwicklung:** Community-Beitrag

### Haftungsausschluss

Dies ist eine von der Community entwickelte Integration und ist nicht offiziell mit Shaztech oder Home Assistant verbunden oder von diesen unterstützt. Verwendung auf eigene Gefahr.

---

**If you find this integration useful, please ⭐ star this repository!**

**Wenn du diese Integration nützlich findest, gib dem Repository bitte einen ⭐ Stern!**
