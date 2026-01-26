# Blueprints

Automation blueprints for tracking medication intake.

## Available Blueprints

### Medication Tracking
Automatically track when medication is dispensed and mark it as taken.

**Import:** 
[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/blob/main/blueprints/medication_tracking.yaml)

### Daily Reset
Reset all "taken today" toggles at midnight.

**Import:**
[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/blob/main/blueprints/daily_reset.yaml)

### Medication Reminder
Get reminded if you forgot to take your medication.

**Import:**
[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/blob/main/blueprints/medication_reminder.yaml)

### Weekly Report
Receive a weekly summary of medication intake.

**Import:**
[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/demrios-de/Pill-Dispenser-Integration-for-Home-Assistant/blob/main/blueprints/weekly_report.yaml)

## Setup Guide

See [docs/BLUEPRINTS.md](../docs/BLUEPRINTS.md) for complete setup instructions.

## Requirements

- Input Boolean helpers (one per medication)
- Input Text helpers (optional, for custom names)
- Counter helpers (optional, for statistics)
- Mobile app for notifications (optional)

## Quick Start

1. Create helpers (Settings → Helpers)
2. Click "Import Blueprint" badge above
3. Create automation from blueprint
4. Configure and save

Done! Your medication tracking is now active.
