from discord.ext import commands
import discord

EXTENSIONS = ("extensions.ping", "extensions.rick", "extensions.mod", "extensions.eno", "extensions.poll", "extensions.trivia", "extensions.announce")
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

bot.run("MTA3MDA5MjQ3ODgxMzg0MzU2Ng.GhyAaE.1-7u4F3vYu4PgO5U1jr9RPFP_6YsEvTerQF9QM")