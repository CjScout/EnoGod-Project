import discord
from discord.ext import commands
from asyncio import sleep

class rickCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        pass
	
    @discord.ext.commands.has_any_role(981683382108958790, 688450976704757812)

    @commands.command()
    async def rick(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("D:/Personal Files/Desktop/Projects/EnoGod Project/extensions/rickroll.mp3"), after=lambda e: print(f"Rick Roll? Rick Roll."))
        vc.source = discord.PCMVolumeTransformer(vc.source, 1)

        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
        await ctx.message.delete()

    @commands.command()
    async def dust(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("D:/Personal Files/Desktop/Projects/EnoGod Project/extensions/dust.mp3"), after=lambda e: print(f"Dust."))
        vc.source = discord.PCMVolumeTransformer(vc.source, 1)

        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
        await ctx.message.delete()
    
    @commands.command()
    async def hello(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("D:/Personal Files/Desktop/Projects/EnoGod Project/extensions/hello.mp3"), after=lambda e: print(f"Hello"))
        vc.source = discord.PCMVolumeTransformer(vc.source, 1)

        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
        await ctx.message.delete()

    @commands.command()
    async def kenobi(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("D:/Personal Files/Desktop/Projects/EnoGod Project/extensions/bold.mp3"), after=lambda e: print(f"Bold"))
        vc.source = discord.PCMVolumeTransformer(vc.source, 1)

        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
        await ctx.message.delete()

    @commands.command()
    async def leave(self, ctx):
        print("LeaveVoice")
        await ctx.voice_client.disconnect()
        await ctx.message.delete()

async def setup(bot: commands.Bot):
    await bot.add_cog(rickCog(bot))