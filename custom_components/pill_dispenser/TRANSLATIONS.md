# Adding Translations

The integration supports multiple languages. Currently available:
- English (en)
- German (de)
- French (fr)

## Add a New Language

1. Copy `translations/en.json` to `translations/YOUR_LANGUAGE.json`
2. Translate all text values (keep the structure!)
3. Restart Home Assistant

Example for Spanish (`es.json`):
```json
{
  "config": {
    "step": {
      "user": {
        "title": "Configurar Pill Dispenser",
        "data": {
          "host": "Dirección IP"
        }
      }
    }
  },
  "entity": {
    "sensor": {
      "tray_name": {
        "name": "Bandeja {tray_id} Nombre"
      }
    }
  }
}
```

**Important:** Keep placeholders like `{tray_id}` unchanged!

## Language Codes

Use ISO 639-1 codes: `de`, `fr`, `es`, `it`, `nl`, `pl`, `pt`, `ru`, `zh-Hans`, `ja`, etc.

Full list: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

## Testing

1. Change language in Home Assistant: Profile → Language
2. Reload integration: Settings → Devices & Services → Pill Dispenser → ⋮ → Reload
3. Check entity names

## Contributing

Pull requests with new translations are welcome!
