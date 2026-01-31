# Beispiel Dashboard für Medikamenten-Tracking

## Komplettes Dashboard

Kopiere das in eine neue Dashboard-Ansicht:

```yaml
title: Medikamente
path: medikamente
icon: mdi:pill
cards:
  # Status heute
  - type: entities
    title: Heute
    show_header_toggle: false
    entities:
      - entity: input_boolean.morgens_genommen
        name: Morgens
        icon: mdi:white-balance-sunny
      - entity: input_boolean.mittags_genommen
        name: Mittags
        icon: mdi:weather-sunny
      - entity: input_boolean.abends_genommen
        name: Abends
        icon: mdi:weather-sunset
      - entity: input_boolean.nachts_genommen
        name: Nachts
        icon: mdi:weather-night
  
  # Notizen
  - type: entities
    title: Was ist drin?
    show_header_toggle: false
    entities:
      - entity: input_text.morgens_notiz
        name: Morgens
      - entity: input_text.mittags_notiz
        name: Mittags
      - entity: input_text.abends_notiz
        name: Abends
      - entity: input_text.nachts_notiz
        name: Nachts
  
  # Historie letzte Woche
  - type: history-graph
    title: Letzte 7 Tage
    entities:
      - entity: input_boolean.morgens_genommen
        name: Morgens
      - entity: input_boolean.mittags_genommen
        name: Mittags
      - entity: input_boolean.abends_genommen
        name: Abends
      - entity: input_boolean.nachts_genommen
        name: Nachts
    hours_to_show: 168
  
  # Statistiken
  - type: entities
    title: Diese Woche
    show_header_toggle: false
    entities:
      - entity: counter.morgens_einnahmen
        name: Morgens
        icon: mdi:counter
      - entity: counter.mittags_einnahmen
        name: Mittags
        icon: mdi:counter
      - entity: counter.abends_einnahmen
        name: Abends
        icon: mdi:counter
      - entity: counter.nachts_einnahmen
        name: Nachts
        icon: mdi:counter
  
  # Pill Dispenser Controls
  - type: entities
    title: Pill Dispenser
    show_header_toggle: false
    entities:
      - entity: button.pill_dispenser_play_default_alarm
        name: Alarm testen
      - entity: button.pill_dispenser_dispense_current
        name: Jetzt ausgeben
      - entity: button.pill_dispenser_dismiss_alarm
        name: Alarm aus
```

## Kompakte Version (nur das Wichtigste)

```yaml
title: Meds
path: meds
icon: mdi:pill
cards:
  # Heute genommen?
  - type: entities
    title: Status
    entities:
      - input_boolean.morgens_genommen
      - input_boolean.mittags_genommen
      - input_boolean.abends_genommen
      - input_boolean.nachts_genommen
  
  # Historie
  - type: history-graph
    title: Diese Woche
    entities:
      - input_boolean.morgens_genommen
      - input_boolean.mittags_genommen
      - input_boolean.abends_genommen
      - input_boolean.nachts_genommen
    hours_to_show: 168
```

## Mobile-optimiert (weniger Platz)

```yaml
cards:
  # Alles in einer Card
  - type: vertical-stack
    cards:
      - type: entities
        title: 💊 Heute
        entities:
          - input_boolean.morgens_genommen
          - input_boolean.mittags_genommen
          - input_boolean.abends_genommen
      
      - type: history-graph
        entities:
          - input_boolean.morgens_genommen
          - input_boolean.mittags_genommen
          - input_boolean.abends_genommen
        hours_to_show: 168
```

## Mit Pill Dispenser Status

```yaml
cards:
  # Status + Controls
  - type: entities
    title: Medikamente & Dispenser
    entities:
      # Status heute
      - type: section
        label: Heute genommen?
      - input_boolean.morgens_genommen
      - input_boolean.mittags_genommen
      - input_boolean.abends_genommen
      
      # Dispenser Info
      - type: section
        label: Pill Dispenser
      - sensor.pill_dispenser_tray_1_name
      - sensor.pill_dispenser_tray_2_name
      - sensor.pill_dispenser_tray_3_name
      
      # Controls
      - type: section
        label: Aktionen
      - button.pill_dispenser_dispense_current
      - button.pill_dispenser_dismiss_alarm
  
  # Historie
  - type: history-graph
    title: Einnahme-Historie
    entities:
      - input_boolean.morgens_genommen
      - input_boolean.mittags_genommen
      - input_boolean.abends_genommen
    hours_to_show: 168
```

## Tipps

**History Graph anpassen:**
- `hours_to_show: 168` = 7 Tage
- `hours_to_show: 336` = 14 Tage
- `hours_to_show: 720` = 30 Tage

**Farben ändern:**
Home Assistant färbt automatisch:
- Toggle ON = Grün
- Toggle OFF = Grau/Leer

**Refresh-Zeit:**
History aktualisiert sich automatisch.

**Daten-Export:**
Du kannst die Historie auch als CSV exportieren:
- Entwicklerwerkzeuge → Statistiken → Download

## So sieht's aus

**History Graph zeigt:**
```
Morgens  ▓▓▓▓▓░░▓▓▓▓▓▓▓
Mittags  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓
Abends   ▓▓▓▓░░░▓▓▓▓▓▓▓
         Mo Di Mi Do Fr Sa So

▓ = Genommen
░ = Vergessen
```

Du siehst sofort:
- Morgens: Dienstag vergessen
- Mittags: Alles genommen ✓
- Abends: Di+Mi+Do vergessen

Praktisch!
