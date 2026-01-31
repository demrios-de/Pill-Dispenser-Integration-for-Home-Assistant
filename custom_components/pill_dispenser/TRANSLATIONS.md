# Übersetzungen hinzufügen

Die Integration unterstützt mehrere Sprachen.

**Aktuell verfügbar:**
- 🇬🇧 English (en)
- 🇩🇪 Deutsch (de)

**Du sprichst eine andere Sprache? Hilf mit! 🌍**

---

## Neue Sprache hinzufügen

### Schritt 1: Datei kopieren

Kopiere `translations/en.json` zu `translations/DEINE_SPRACHE.json`

**Beispiel für Spanisch:**
```bash
cp translations/en.json translations/es.json
```

### Schritt 2: Übersetzen

Öffne die neue Datei und übersetze die Texte.

**Wichtig:**
- ✅ Übersetze nur die Werte (rechts vom `:`)
- ❌ Ändere NICHT die Keys (links vom `:`)
- ❌ Ändere NICHT Platzhalter wie `{tray_id}`

**Beispiel:**

**Englisch (en.json):**
```json
{
  "config": {
    "step": {
      "user": {
        "title": "Configure Pill Dispenser",
        "data": {
          "host": "IP Address"
        }
      }
    }
  }
}
```

**Spanisch (es.json):**
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
  }
}
```

### Schritt 3: Testen

1. Home Assistant neustarten
2. Sprache ändern: **Profil → Sprache → Deine Sprache**
3. Integration neu laden: **Einstellungen → Geräte & Dienste → Pill Dispenser → ⋮ → Neu laden**
4. Check ob alles übersetzt ist

---

## Sprach-Codes

Nutze ISO 639-1 Codes:

| Sprache | Code |
|---------|------|
| Deutsch | `de` |
| Englisch | `en` |
| Spanisch | `es` |
| Französisch | `fr` |
| Italienisch | `it` |
| Niederländisch | `nl` |
| Polnisch | `pl` |
| Portugiesisch | `pt` |
| Russisch | `ru` |
| Chinesisch (vereinfacht) | `zh-Hans` |
| Japanisch | `ja` |

Komplette Liste: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

---

## Was wird übersetzt?

### Config Flow (Setup-Dialog)
- Titel und Beschreibungen
- Input-Felder
- Fehler-Meldungen

### Entity Namen
- Sensor Namen (z.B. "Fach 1 Name")
- Button Namen (z.B. "Fach 1 ausgeben")
- Switch Namen (z.B. "Fach 1 aktiviert")

### States
- "Yes" / "No" → "Ja" / "Nein" (Deutsch)
- "Yes" / "No" → "Oui" / "Non" (Französisch)

---

## Vollständiges Beispiel

Hier die komplette Struktur mit allen Teilen:

<details>
<summary>Klick um es.json Beispiel zu sehen</summary>

```json
{
  "config": {
    "step": {
      "user": {
        "title": "Configurar Pill Dispenser",
        "description": "Conecta tu Pill Dispenser",
        "data": {
          "host": "Dirección IP"
        }
      }
    },
    "error": {
      "cannot_connect": "No se puede conectar",
      "invalid_host": "IP inválida",
      "unknown": "Error desconocido"
    },
    "abort": {
      "already_configured": "Ya configurado"
    }
  },
  "entity": {
    "sensor": {
      "tray_name": {
        "name": "Bandeja {tray_id} Nombre"
      },
      "tray_dispensed": {
        "name": "Bandeja {tray_id} Dispensado",
        "state": {
          "yes": "Sí",
          "no": "No"
        }
      }
    },
    "button": {
      "drop_tray": {
        "name": "Dispensar Bandeja {tray_id}"
      },
      "play_default_alarm": {
        "name": "Reproducir Alarma Predeterminada"
      },
      "play_custom_alarm": {
        "name": "Reproducir Alarma Personalizada"
      },
      "dispense_current": {
        "name": "Dispensar Actual"
      },
      "dismiss_alarm": {
        "name": "Silenciar Alarma"
      },
      "alarm_default": {
        "name": "Alarma Predeterminada"
      },
      "alarm_custom": {
        "name": "Alarma Personalizada"
      },
      "fix_tray": {
        "name": "Reparar Bandeja"
      }
    },
    "switch": {
      "tray_enabled": {
        "name": "Bandeja {tray_id} Activado"
      }
    }
  }
}
```
</details>

---

## Tipps

**Platzhalter behalten:**
```json
❌ "name": "Bandeja 1 Nombre"
✅ "name": "Bandeja {tray_id} Nombre"
```

**Konsistenz:**
Nutze die gleichen Begriffe durch die ganze Datei.
- Tray = Bandeja (nicht wechseln zu Cajón)
- Dispense = Dispensar (nicht wechseln zu Soltar)

**Testen:**
Teste alle Fächer (1-10) um sicherzustellen dass Platzhalter funktionieren!

---

## Pull Request erstellen

Hast du eine Übersetzung fertig?

### 1. Füge dich als Contributor hinzu

Öffne deine Übersetzungsdatei und füge oben einen Kommentar hinzu:

```json
{
  "_meta": {
    "contributors": [
      "Dein Name",
      "Andere Person (falls mehrere mitgeholfen haben)"
    ]
  },
  "config": {
    ...
```

**Beispiel:**
```json
{
  "_meta": {
    "contributors": [
      "Maria Garcia",
      "Juan Rodriguez"
    ]
  },
  "config": {
    "step": {
      "user": {
        "title": "Configurar Pill Dispenser",
        ...
```

**Warum?**
- Dein Name erscheint in der offiziellen Integration! 🎉
- Community sieht wer geholfen hat
- Du bekommst Credit für deine Arbeit

### 2. Pull Request erstellen

1. **Fork** das Repository auf GitHub
2. **Füge** deine `translations/XX.json` hinzu
3. **Erstelle** Pull Request mit Titel: "Add [Sprache] translation"
4. **Beschreibe** kurz:
   ```
   Adds Spanish translation
   
   Translated by: Maria Garcia, Juan Rodriguez
   ```

### 3. Review & Merge

Dein Pull Request wird geprüft und dann gemerged!

**Deine Übersetzung ist dann im nächsten Release! 🚀**

**Danke dass du hilfst die Integration für alle zugänglich zu machen! 🌍**

---

## Probleme?

**Text wird nicht übersetzt:**
- Check: Dateiname korrekt? (`es.json` nicht `spanish.json`)
- Check: Sprache in HA gewechselt?
- Check: Integration neu geladen?

**Fehler beim Laden:**
- Check: JSON valide? (https://jsonlint.com)
- Check: Alle Kommas gesetzt?
- Check: Keine Syntax-Fehler?

**Fragen?** Öffne ein Issue auf GitHub!

---

## Contributors 🌍

**Danke an alle die geholfen haben!**

### 🇬🇧 English
- Original Author

### 🇩🇪 Deutsch
- Original Author

**Dein Name hier? Erstelle eine Übersetzung! ⬆️**
