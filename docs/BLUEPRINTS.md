# Medication Tracking with Blueprints

Track your medication intake with pre-built automation blueprints.

## What You Get

- Automatic tracking when medication is dispensed
- Daily reset at midnight
- Reminders for forgotten medications
- Weekly statistics and reports

## Quick Setup

### 1. Create Helpers

**For each medication:**

Settings → Devices & Services → Helpers → Create Helper

**Toggle (required):**
- Name: "Morning Aspirin Taken"
- Icon: mdi:pill

**Text (optional but recommended):**
- Name: "Aspirin Name"
- Value: "Aspirin 100mg"

**Counter (optional):**
- Name: "Aspirin Count"
- Minimum: 0

### 2. Import Blueprints

Go to Settings → Automations & Scenes → Blueprints

Click the import badges in [blueprints/README.md](../blueprints/README.md)

### 3. Create Automations

**For tracking:**
1. Create automation from "Medication Tracking" blueprint
2. Select your tray's dispensed sensor
3. Select your "taken today" toggle
4. Optional: Select counter and notification device
5. Save

**For daily reset:**
1. Create automation from "Daily Reset" blueprint
2. Select all "taken today" toggles
3. Save

**For reminders:**
1. Create automation from "Medication Reminder" blueprint
2. Set reminder time
3. Select "taken today" toggle
4. Select notification device
5. Save

## Example: Track 3 Medications

**Helpers needed:**
- 3 toggles (taken today)
- 3 text inputs (names)
- 3 counters (statistics)

**Automations needed:**
- 3 tracking automations (one per med)
- 1 daily reset (resets all 3)
- 3 reminder automations (one per med)
- 3 weekly reports (one per med)

Total: 10 automations, all created from blueprints!

## Dashboard Example

```yaml
type: entities
title: Medication Tracking
entities:
  - input_boolean.morning_aspirin_taken
  - input_boolean.lunch_blood_pressure_taken
  - input_boolean.evening_vitamin_taken
  - type: section
  - counter.aspirin_count
  - counter.blood_pressure_count
  - counter.vitamin_count
```

## Troubleshooting

**Blueprint won't import:**
- Make sure repository is public
- Or download and import manually

**Automation not triggering:**
- Check if sensor changes to "Yes"
- Check if toggle is "off"
- View automation traces

**No notifications:**
- Check mobile app is installed
- Test notification manually first

## Alternative

If blueprints don't work for you, see [MEDICATION_TRACKING.md](MEDICATION_TRACKING.md) for manual YAML configuration.
