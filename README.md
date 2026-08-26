# Discord-Server Setup

Automatisiertes Setup fuer den Discord-Server mit folgender Struktur:

- **💬 ALLGEMEIN** (fuer alle Mitglieder sichtbar)
  - `#chat` – allgemeiner Chat
  - `#umfragen` – Abstimmungen (nutzt die native Discord-Umfragefunktion)
  - `#bilder` – Bilder teilen
  - `🔊 Talk` – Sprachkanal
- **🛡️ MODERATION** (nur fuer die Rolle `Moderator`)
  - `#mod-chat`, `#mod-log`, `#berichte`, `#ban-anfragen`
  - `🔊 Mod-Voice`
- **📰 REDAKTION** (nur fuer die Rolle `Redaktion`, unterteilt nach Vereinen)
  - `#fenerbahce`, `#besiktas`, `#galatasaray`, `#trabzonspor`
  - Es duerfen nur Nachrichten mit Bildanhang gepostet werden; alles andere wird
    automatisch vom Moderations-Bot (`bot.py`) geloescht.
- **🎬 CREATOR** (komplett unsichtbar fuer alle ausser der Rolle `Creator`)
  - `#creator-chat`
  - `🔊 Creator-Talk`

## Wichtig: Was der Bot NICHT kann

Discord erlaubt Bots nicht, neue Server zu erstellen – das kann nur ein Mensch
per Klick in der Discord-App ("Server hinzufuegen" → "Server erstellen"). Du
musst also **einmalig selbst einen leeren Server anlegen**, danach erledigt
das Skript den Rest (Rollen, Kategorien, Kanaele, Berechtigungen).

## Einrichtung

1. **Leeren Server erstellen**: In Discord auf `+` → "Server erstellen" klicken.
2. **Entwicklermodus aktivieren**: Discord → Einstellungen → Erweitert →
   Entwicklermodus.
3. **Server-ID kopieren**: Rechtsklick auf den Servernamen → "ID kopieren".
4. **Bot erstellen**: Im [Discord Developer Portal](https://discord.com/developers/applications)
   eine neue Application anlegen, unter "Bot" einen Bot hinzufuegen und das
   Token kopieren. Unter "Privileged Gateway Intents" den **Message Content
   Intent** aktivieren (wird fuer die Foto-Erzwingung in der Redaktion
   benoetigt).
5. **Bot einladen**: Unter "OAuth2" → "URL Generator" die Scopes `bot` und
   die Berechtigung `Administrator` auswaehlen, den generierten Link oeffnen
   und den Bot auf deinen Server einladen.
6. **Umgebungsvariablen setzen**: `.env.example` nach `.env` kopieren und
   `DISCORD_BOT_TOKEN` sowie `DISCORD_GUILD_ID` eintragen.
7. **Abhaengigkeiten installieren**:
   ```
   pip install -r requirements.txt
   ```
8. **Struktur anlegen** (einmalig):
   ```
   python setup_server.py
   ```
9. **Rollen vergeben**: Weise den entsprechenden Mitgliedern manuell die
   Rollen `Moderator`, `Redaktion` bzw. `Creator` zu (Servereinstellungen →
   Mitglieder), damit sie Zugriff auf die jeweiligen Bereiche bekommen.
10. **Moderations-Bot dauerhaft laufen lassen** (fuer die Foto-Regel in der
    Redaktion), z.B. per systemd, pm2 oder Docker:
    ```
    python bot.py
    ```

## Hinweise

- Das Setup-Skript ist mehrfach ausfuehrbar: bereits vorhandene Rollen,
  Kategorien und Kanaele werden nicht doppelt angelegt.
- Die Redaktion ist bewusst in vier eigene Kanaele je Verein unterteilt
  (Fenerbahce, Besiktas, Galatasaray, Trabzonspor), damit Fotos sauber
  getrennt bleiben.
- Die CREATOR-Kategorie ist fuer `@everyone` auf "nicht sichtbar" gesetzt,
  dadurch sehen andere Mitglieder weder die Kanaele noch deren Inhalte.
