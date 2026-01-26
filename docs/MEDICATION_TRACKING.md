# Medikamenten-Tracking - Einfache Lösung (ohne Code-Änderung)

## Ziel:
Tracke ob Medikamente genommen wurden mit custom Namen und Historie.

## Lösung: Helper + Automationen

### Schritt 1: Helper erstellen

**Für jedes Tray das du tracken willst:**

1. **Einstellungen → Geräte & Dienste → Helper**
2. **Helper hinzufügen → Schalter (Toggle)**
3. **Name:** `Morgen Aspirin genommen`
4. **Icon:** `mdi:pill`
5. **Erstellen**

**Wiederhole für jedes Medikament:**
- `input_boolean.morgen_aspirin_genommen`
- `input_boolean.mittag_blutdruck_genommen`
- `input_boolean.abend_vitamin_genommen`

### Schritt 2: Counter für Statistik (optional)

1. **Helper hinzufügen → Zähler**
2. **Name:** `Aspirin genommen (Total)`
3. **Icon:** `mdi:counter`
4. **Minimum:** 0
5. **Schritt:** 1

### Schritt 3: Automatische Reset-Automation

```yaml
automation:
  - alias: "Reset Medication Taken Daily"
    trigger:
      - platform: time
        at: "00:00:00"
    action:
      - service: input_boolean.turn_off
        target:
          entity_id:
            - input_boolean.morgen_aspirin_genommen
            - input_boolean.mittag_blutdruck_genommen
            - input_boolean.abend_vitamin_genommen
```

### Schritt 4: Tracking Automation

```yaml
automation:
  - alias: "Track Aspirin Einnahme"
    trigger:
      - platform: state
        entity_id: sensor.pill_dispenser_tray_1_dispensed
        to: "Yes"
    condition:
      - condition: state
        entity_id: input_boolean.morgen_aspirin_genommen
        state: "off"
    action:
      # Markiere als genommen
      - service: input_boolean.turn_on
        target:
          entity_id: input_boolean.morgen_aspirin_genommen
      
      # Zähle hoch
      - service: counter.increment
        target:
          entity_id: counter.aspirin_genommen_total
      
      # Benachrichtigung
      - service: notify.mobile_app
        data:
          title: "✅ Medikament genommen"
          message: "Aspirin wurde um {{ now().strftime('%H:%M') }} Uhr eingenommen"
```

### Schritt 5: Erinnerung wenn nicht genommen

```yaml
automation:
  - alias: "Erinnerung: Aspirin noch nicht genommen"
    trigger:
      - platform: time
        at: "09:00:00"  # Jeden Morgen um 9 Uhr
    condition:
      - condition: state
        entity_id: input_boolean.morgen_aspirin_genommen
        state: "off"
    action:
      - service: notify.mobile_app
        data:
          title: "⚠️ Medikament vergessen?"
          message: "Du hast dein Morgen-Aspirin noch nicht genommen!"
```

### Schritt 6: Dashboard Card

```yaml
type: entities
title: Medikamenten-Tracking
entities:
  # Status heute
  - entity: input_boolean.morgen_aspirin_genommen
    name: Aspirin (Morgen)
  - entity: input_boolean.mittag_blutdruck_genommen
    name: Blutdruck-Tablette (Mittag)
  - entity: input_boolean.abend_vitamin_genommen
    name: Vitamin D (Abend)
  
  # Statistiken
  - type: section
    label: Statistiken
  - entity: counter.aspirin_genommen_total
    name: Aspirin (Gesamt)
  
  # Pill Dispenser Status
  - type: section
    label: Pill Dispenser
  - entity: sensor.pill_dispenser_tray_1_triggered
    name: Alarm aktiv
  - entity: button.pill_dispenser_dispense_current
    name: Manuell ausgeben
```

## Vorteile dieser Lösung:

✅ **Keine Code-Änderung nötig** - Alles mit HA-Bordmitteln
✅ **Flexible Namen** - Benenne wie du willst
✅ **Historie** - HA speichert alles automatisch
✅ **Statistiken** - Nutze die History-Grafiken
✅ **Einfach zu ändern** - Keine Integration-Updates nötig

## Historie anschauen:

### Methode 1: History Graph

```yaml
type: history-graph
title: Medikamenten-Historie
entities:
  - input_boolean.morgen_aspirin_genommen
  - input_boolean.mittag_blutdruck_genommen
  - input_boolean.abend_vitamin_genommen
hours_to_show: 168  # 7 Tage
```

### Methode 2: Statistics Card

```yaml
type: statistics-graph
title: Einnahmen diese Woche
entities:
  - counter.aspirin_genommen_total
stat_types:
  - sum
period: week
```

### Methode 3: Logbook

```
Einstellungen → Logbuch
Filter: input_boolean.morgen_aspirin_genommen
→ Siehst komplette Historie
```

## Erweitert: Wöchentlicher Bericht

```yaml
automation:
  - alias: "Wöchentlicher Medikamenten-Bericht"
    trigger:
      - platform: time
        at: "20:00:00"
      - platform: time_pattern
        weekday: 6  # Sonntag
    action:
      - service: notify.mobile_app
        data:
          title: "📊 Wochenübersicht Medikamente"
          message: >
            Aspirin: {{ states('counter.aspirin_genommen_total') }} von 7 Tagen
            Blutdruck: {{ states('counter.blutdruck_genommen_total') }} von 7 Tagen
            
            {% if states('counter.aspirin_genommen_total')|int < 7 %}
            ⚠️ Du hast {{ 7 - states('counter.aspirin_genommen_total')|int }} Dosen vergessen!
            {% else %}
            ✅ Perfekt! Alle Medikamente genommen!
            {% endif %}
      
      # Reset Counter
      - service: counter.reset
        target:
          entity_id:
            - counter.aspirin_genommen_total
            - counter.blutdruck_genommen_total
```

## Bonus: Kalender-Integration

```yaml
# Erstelle Kalender-Einträge für genommene Medikamente
automation:
  - alias: "Log zu Google Kalender"
    trigger:
      - platform: state
        entity_id: input_boolean.morgen_aspirin_genommen
        to: "on"
    action:
      - service: calendar.create_event
        target:
          entity_id: calendar.medikamente
        data:
          summary: "💊 Aspirin genommen"
          start: "{{ now().isoformat() }}"
          end: "{{ (now() + timedelta(minutes=5)).isoformat() }}"
```

## Custom Namen pro Tray

### Methode: Text Helper

1. **Helper → Text**
2. **Name:** `Tray 1 Medikament`
3. **Wert:** `Aspirin 100mg`

**In Automationen nutzen:**
```yaml
message: >
  {{ states('input_text.tray_1_medikament') }} wurde genommen
  # → "Aspirin 100mg wurde genommen"
```

## Vollständiges Beispiel:

```yaml
# configuration.yaml

input_boolean:
  morgen_aspirin_genommen:
    name: Aspirin (Morgen) genommen
    icon: mdi:pill
  
  mittag_blutdruck_genommen:
    name: Blutdruck-Tablette genommen
    icon: mdi:heart-pulse

input_text:
  tray_1_medikament:
    name: Tray 1 Medikament
    initial: Aspirin 100mg
  
  tray_2_medikament:
    name: Tray 2 Medikament
    initial: Blutdrucktablette

counter:
  aspirin_genommen_total:
    name: Aspirin genommen (Total)
    icon: mdi:counter
  
  blutdruck_genommen_total:
    name: Blutdruck genommen (Total)
    icon: mdi:counter

automation:
  # Täglicher Reset
  - alias: "Reset Medication Daily"
    trigger:
      - platform: time
        at: "00:00:00"
    action:
      - service: input_boolean.turn_off
        target:
          entity_id:
            - input_boolean.morgen_aspirin_genommen
            - input_boolean.mittag_blutdruck_genommen
  
  # Tracking
  - alias: "Track Tray 1 (Aspirin)"
    trigger:
      - platform: state
        entity_id: sensor.pill_dispenser_tray_1_dispensed
        to: "Yes"
    action:
      - service: input_boolean.turn_on
        target:
          entity_id: input_boolean.morgen_aspirin_genommen
      - service: counter.increment
        target:
          entity_id: counter.aspirin_genommen_total
      - service: notify.mobile_app
        data:
          message: "{{ states('input_text.tray_1_medikament') }} genommen ✅"
  
  # Erinnerung
  - alias: "Erinnerung Aspirin"
    trigger:
      - platform: time
        at: "09:00:00"
    condition:
      - condition: state
        entity_id: input_boolean.morgen_aspirin_genommen
        state: "off"
    action:
      - service: notify.mobile_app
        data:
          title: "Medikament vergessen?"
          message: "{{ states('input_text.tray_1_medikament') }} noch nicht genommen!"
```

## Vorteile:

✅ **Funktioniert sofort** - Keine Integration-Änderung
✅ **Flexibel** - Namen jederzeit änderbar
✅ **Historie** - Automatisch gespeichert
✅ **Statistiken** - Eingebaute Grafiken
✅ **Berichte** - Tägliche/Wöchentliche Zusammenfassungen
✅ **Benachrichtigungen** - Bei vergessenen Medikamenten

## Nachteile:

❌ Etwas mehr Konfiguration
❌ Mehrere Automationen nötig

---

**Möchtest du dass ich Option 2 zeige (direkt in die Integration eingebaut)? Das wäre komplexer, aber alles in einem!**
