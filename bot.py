"""
Dauerhaft laufender Moderations-Bot.

Erzwingt in der Kategorie "📰 REDAKTION", dass ausschliesslich Nachrichten mit
Bildanhang gepostet werden duerfen. Textnachrichten ohne Anhang werden
automatisch geloescht und der Autor kurz per Hinweis informiert.

Ausfuehren (dauerhaft, z.B. per systemd/pm2/Docker):
    python bot.py
"""

import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["DISCORD_BOT_TOKEN"]
REDAKTION_CATEGORY_NAME = "📰 REDAKTION"

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)


def has_image_attachment(message: discord.Message) -> bool:
    if not message.attachments:
        return False
    return any(
        attachment.content_type and attachment.content_type.startswith("image/")
        for attachment in message.attachments
    )


@client.event
async def on_ready():
    print(f"Eingeloggt als {client.user} - Redaktions-Moderation aktiv.")


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    category = getattr(message.channel, "category", None)
    if category is None or category.name != REDAKTION_CATEGORY_NAME:
        return

    if has_image_attachment(message):
        return

    try:
        await message.delete()
        await message.channel.send(
            f"{message.author.mention} In diesem Kanal sind nur Fotos erlaubt.",
            delete_after=6,
        )
    except discord.Forbidden:
        pass


if __name__ == "__main__":
    client.run(TOKEN)
