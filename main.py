from discord.ext import commands
import discord

EXTENSIONS = ("extensions.example",)
INTENTS = discord.Intents.default()
INTENTS.message_content = True

bot = commands.Bot(
    intents=INTENTS,
    command_prefix="!"
)

@bot.event
async def setup_hook() -> None:
    for extension in EXTENSIONS:
        await bot.load_extension(extension)

bot.run("")