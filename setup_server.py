"""
Einmaliges Setup-Skript fuer den Discord-Server.

Baut folgende Struktur auf einem bereits existierenden (leeren) Discord-Server auf:

1. Kategorie "ALLGEMEIN"   - fuer alle Mitglieder: Chat, Umfragen, Bilder, Voice
2. Kategorie "MODERATION"  - nur fuer die Rolle "Moderator", mit Unterkanaelen
3. Kategorie "REDAKTION"   - nur fuer die Rolle "Redaktion", unterteilt in die vier
                             Vereins-Kanaele (Fenerbahce, Besiktas, Galatasaray,
                             Trabzonspor); dort sind nur Bilder erlaubt (Durchsetzung
                             uebernimmt bot.py)
4. Kategorie "CREATOR"     - komplett unsichtbar fuer alle ausser der Rolle "Creator"

Voraussetzungen:
- Ein Discord-Server (Guild), den du bereits manuell erstellt hast.
- Ein Bot im Discord Developer Portal mit Admin-Rechten, eingeladen auf diesen Server.
- Umgebungsvariablen DISCORD_BOT_TOKEN und DISCORD_GUILD_ID (siehe .env.example / README.md).

Ausfuehren:
    python setup_server.py
"""

import os

import discord
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["DISCORD_BOT_TOKEN"]
GUILD_ID = int(os.environ["DISCORD_GUILD_ID"])

REDAKTION_CHANNELS = ["fenerbahce", "besiktas", "galatasaray", "trabzonspor"]

intents = discord.Intents.default()
intents.guilds = True

client = discord.Client(intents=intents)


async def get_or_create_role(guild: discord.Guild, name: str, **kwargs) -> discord.Role:
    role = get(guild.roles, name=name)
    if role is None:
        role = await guild.create_role(name=name, **kwargs)
        print(f"Rolle erstellt: {name}")
    return role


async def get_or_create_category(
    guild: discord.Guild, name: str, overwrites: dict
) -> discord.CategoryChannel:
    category = get(guild.categories, name=name)
    if category is None:
        category = await guild.create_category(name, overwrites=overwrites)
        print(f"Kategorie erstellt: {name}")
    else:
        await category.edit(overwrites=overwrites)
    return category


async def get_or_create_text_channel(
    guild: discord.Guild, name: str, category: discord.CategoryChannel, **kwargs
) -> discord.TextChannel:
    channel = get(category.text_channels, name=name)
    if channel is None:
        channel = await guild.create_text_channel(name, category=category, **kwargs)
        print(f"  Textkanal erstellt: #{name}")
    return channel


async def get_or_create_voice_channel(
    guild: discord.Guild, name: str, category: discord.CategoryChannel, **kwargs
) -> discord.VoiceChannel:
    channel = get(category.voice_channels, name=name)
    if channel is None:
        channel = await guild.create_voice_channel(name, category=category, **kwargs)
        print(f"  Sprachkanal erstellt: {name}")
    return channel


@client.event
async def on_ready():
    guild = client.get_guild(GUILD_ID)
    if guild is None:
        print(
            "Der Bot ist nicht auf dem angegebenen Server (DISCORD_GUILD_ID). "
            "Bitte zuerst ueber den OAuth2-Einladungslink hinzufuegen."
        )
        await client.close()
        return

    everyone = guild.default_role

    moderator = await get_or_create_role(
        guild, "Moderator", colour=discord.Colour.red(), hoist=True
    )
    redaktion = await get_or_create_role(
        guild, "Redaktion", colour=discord.Colour.blue(), hoist=True
    )
    creator = await get_or_create_role(
        guild, "Creator", colour=discord.Colour.gold(), hoist=True
    )

    # 1. ALLGEMEIN - alle Mitglieder koennen chatten, abstimmen, Bilder posten, sprechen
    allgemein_overwrites = {
        everyone: discord.PermissionOverwrite(
            view_channel=True, send_messages=True, connect=True, speak=True
        ),
    }
    allgemein = await get_or_create_category(guild, "💬 ALLGEMEIN", allgemein_overwrites)
    await get_or_create_text_channel(
        guild, "chat", allgemein, topic="Allgemeiner Chat fuer alle Mitglieder"
    )
    await get_or_create_text_channel(
        guild,
        "umfragen",
        allgemein,
        topic="Hier koennt ihr abstimmen - nutzt die native Discord-Umfragefunktion",
    )
    await get_or_create_text_channel(
        guild, "bilder", allgemein, topic="Teilt hier eure Bilder"
    )
    await get_or_create_voice_channel(guild, "🔊 Talk", allgemein)

    # 2. MODERATION - nur fuer Moderatoren, mit mehreren Unterkanaelen
    mod_overwrites = {
        everyone: discord.PermissionOverwrite(view_channel=False),
        moderator: discord.PermissionOverwrite(
            view_channel=True, send_messages=True, connect=True, speak=True
        ),
    }
    mod_category = await get_or_create_category(guild, "🛡️ MODERATION", mod_overwrites)
    await get_or_create_text_channel(guild, "mod-chat", mod_category)
    await get_or_create_text_channel(guild, "mod-log", mod_category)
    await get_or_create_text_channel(guild, "berichte", mod_category)
    await get_or_create_text_channel(guild, "ban-anfragen", mod_category)
    await get_or_create_voice_channel(guild, "🔊 Mod-Voice", mod_category)

    # 3. REDAKTION - nur fuer die Redaktion, ein Kanal je Verein, nur Bilder
    redaktion_overwrites = {
        everyone: discord.PermissionOverwrite(view_channel=False),
        redaktion: discord.PermissionOverwrite(
            view_channel=True, send_messages=True, attach_files=True
        ),
        moderator: discord.PermissionOverwrite(
            view_channel=True, send_messages=True, attach_files=True
        ),
    }
    redaktion_category = await get_or_create_category(
        guild, "📰 REDAKTION", redaktion_overwrites
    )
    for name in REDAKTION_CHANNELS:
        await get_or_create_text_channel(
            guild,
            name,
            redaktion_category,
            topic="Nur Fotos erlaubt - Nachrichten ohne Bildanhang werden automatisch geloescht (siehe bot.py)",
        )

    # 4. CREATOR - komplett unsichtbar fuer alle ausser der Rolle "Creator"
    creator_overwrites = {
        everyone: discord.PermissionOverwrite(view_channel=False),
        creator: discord.PermissionOverwrite(
            view_channel=True, send_messages=True, connect=True, speak=True
        ),
    }
    creator_category = await get_or_create_category(guild, "🎬 CREATOR", creator_overwrites)
    await get_or_create_text_channel(guild, "creator-chat", creator_category)
    await get_or_create_voice_channel(guild, "🔊 Creator-Talk", creator_category)

    print("\nServer-Setup abgeschlossen!")
    print(
        "Weise nun Mitgliedern manuell die Rollen 'Moderator', 'Redaktion' bzw. "
        "'Creator' zu, damit sie Zugriff auf die jeweiligen Bereiche erhalten."
    )
    await client.close()


if __name__ == "__main__":
    client.run(TOKEN)
