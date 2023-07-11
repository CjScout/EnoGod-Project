import discord
from discord.ext import commands

class voiceCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass
	
    @commands.command()
    async def join(self, ctx):
        print("JoinVoice")
        channel = ctx.author.voice.channel
        await channel.connect()
    
    @commands.command()
    async def leave(self, ctx):
        print("LeaveVoice")
        await ctx.voice_client.disconnect()

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(voiceCog(bot))