# Döner Ecke – Website (Platzhalter-Version)

Statische Website (reines HTML/CSS/JS, keine Build-Tools nötig) mit
Startseite, vollständiger Speisekarte, Impressum und Datenschutzerklärung.

## Lokal ansehen

Einfach `index.html` im Browser öffnen, oder z. B. mit:

```
cd website
python3 -m http.server 8000
```

und dann `http://localhost:8000` aufrufen.

## Struktur

```
website/
├── index.html          Startseite (Hero, Über uns, Speisekarte-Vorschau,
│                        Galerie, Bewertungen, Kontakt, CTA)
├── speisekarte.html     Vollständige Speisekarte mit Kategorien-Tabs
├── impressum.html       Impressum (Platzhalter nach §5 TMG)
├── datenschutz.html     Datenschutzerklärung (Platzhalter)
└── assets/
    ├── css/style.css
    ├── js/main.js       Mobile-Menü, Speisekarten-Tabs, Footer-Jahr
    └── images/          Hier später echte Fotos ablegen
```

## Was noch fehlt / vor Livegang zu erledigen

**Inhalte, die du später einträgst:**
- [ ] Echte Speisen, Beschreibungen und Preise in `speisekarte.html`
      (und die Vorschau-Kacheln in `index.html`)
- [ ] Ladenname / Logo (aktuell Platzhaltername "Döner Ecke")
- [ ] Adresse, Telefonnummer, E-Mail (an mehreren Stellen im Code als
      `[Platzhalter]` bzw. `tel:+4900000000` markiert)
- [ ] Öffnungszeiten (Kontakt-Bereich auf der Startseite)
- [ ] Echte Fotos (Laden, Gerichte, Team) statt der gestrichelten
      Platzhalter-Boxen
- [ ] Google-Maps-Einbettung mit echter Adresse (aktuell Platzhalter-Box)
- [ ] Social-Media-Links (Instagram/Facebook, aktuell `#`)
- [ ] Über-uns-Text (echte Geschichte statt Lückenfülltext)
- [ ] Echte Kundenbewertungen statt Platzhalter-Testimonials
- [ ] Allergene/Zusatzstoffe je Gericht (gesetzlich vorgeschrieben, LMIV)

**Rechtliches (Deutschland – vor Veröffentlichung nötig):**
- [ ] Impressum vollständig & korrekt ausfüllen (ggf. von Steuerberater/
      Anwalt prüfen lassen)
- [ ] Datenschutzerklärung an tatsächlich genutzte Dienste anpassen
      (z. B. Google Maps, Analyse-Tools, Bestell-/Lieferdienst-Anbindung,
      Kontaktformular)
- [ ] Falls Cookies/Tracking eingesetzt werden: Cookie-Consent-Banner
      ergänzen

**Sinnvolle Erweiterungen (optional, je nach Bedarf):**
- [ ] Online-Bestellsystem / Lieferando-Einbindung / eigener Bestell-Button
- [ ] Speisekarte zusätzlich als PDF-Download
- [ ] Reservierungsformular (falls Sitzplätze vorhanden)
- [ ] Mehrsprachigkeit (z. B. Deutsch/Türkisch/Englisch)
- [ ] Favicon & Social-Media-Vorschaubild (Open-Graph-Tags)
- [ ] Domain, Hosting und SSL-Zertifikat
- [ ] Google-Unternehmensprofil verlinken (für Bewertungen/Karte)
- [ ] Kontaktformular mit Spam-Schutz (falls gewünscht)

Alle Platzhaltertexte sind im Code kursiv formatiert (`placeholder-text`)
oder in eckigen Klammern `[...]`, damit sie beim Durchsuchen leicht zu
finden sind.
