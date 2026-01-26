# Changelog

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

## [1.0.0] - 2026-01-24

### Hinzugefügt
- Initiale Version der Pill Dispenser Home Assistant Integration
- **80 Sensoren** für Tray-Informationen:
  - Name, Color, Installed, Enabled
  - Triggered, Dispensed, Dismissed, Alarm Time
  - Für alle 10 Trays (1-10)
- **43 Buttons** für Aktionen:
  - Play Default Alarm
  - Play Custom Alarm (1-10)
  - Dispense Current
  - Dismiss Alarm
  - Drop Tray (1-10)
  - Fix Tray (1-10)
- **10 Switches** für Tray Enable/Disable Status (Read-only)
- UI-basierte Konfiguration über Config Flow
- Optionales Namensfeld bei der Einrichtung
  - Eigener Name oder automatisch "Pill Dispenser (IP)"
- Automatisches Polling alle 30 Sekunden
- Device Registry Integration - alle Entities unter einem Gerät gruppiert
- Deutsche und englische Übersetzungen
- HACS Kompatibilität
- Komplette README mit Beispielen und Anleitungen

### Unterstützte API-Endpunkte

#### Aktionen
- `/alarm` - Default Alarm abspielen
- `/alarm?id=X` - Custom Alarm abspielen (1-10)
- `/dispense` - Aktuelles Tray ausgeben
- `/dropout?tray=X` - Spezifisches Tray ausgeben (1-10)
- `/dismiss` - Alarm deaktivieren
- `/fix?tray=X` - Tray justieren (1-10)

#### Informationen (alle 30 Sekunden abgefragt)
- `/tr_name?id=X` - Tray Name
- `/tr_color?id=X` - Tray Farbe (0-7)
- `/tr_inst?id=X` - Tray Installiert (0/1)
- `/tr_enab?id=X` - Tray Aktiviert (0/1)
- `/tr_trig?id=X` - Tray Triggered (0/1)
- `/tr_disp?id=X` - Tray Dispensed (0/1)
- `/tr_dism?id=X` - Tray Dismissed (0/1)
- `/tr_time?id=X` - Tray Alarmzeit

### Features
- **Geräte-Integration**: Alle Entities unter einem Gerät gruppiert
- **Geräteinformationen**:
  - Hersteller: Shaztech
  - Modell: Pill Dispenser
  - Konfiguration-URL: Direkter Link zum Gerät
- **Benutzerfreundlich**: Einfache Einrichtung über die UI
- **Mehrsprachig**: Deutsch und Englisch
- **Flexible Benennung**: Optionaler benutzerdefinierter Name

### Technische Details
- Domain: `pill_dispenser`
- Platforms: Sensor, Button, Switch
- Update Interval: 30 Sekunden
- IoT Class: local_polling
- Config Flow für einfache Einrichtung
- Async/Await Pattern
- DataUpdateCoordinator für effizientes Polling

---

## Versionierung

Dieses Projekt verwendet [Semantic Versioning](https://semver.org/lang/de/):

- **MAJOR** (X.0.0): Inkompatible API-Änderungen
- **MINOR** (0.X.0): Neue Funktionen, abwärtskompatibel
- **PATCH** (0.0.X): Bugfixes, abwärtskompatibel

## Links

- [Pill Dispenser Hardware & Firmware](https://github.com/Shaztech/Pilldispenser)
- [Home Assistant](https://www.home-assistant.io/)
- [HACS](https://hacs.xyz/)
