import discord
from discord.ext import commands
import subprocess
import string

class pingCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        pass
	
    @discord.ext.commands.has_any_role(981683382108958790, 688450976704757812)

    @commands.command()
    async def ping(self, ctx):
        ip = ctx.message.content.replace('!ping ', '')
        output = subprocess.run(['ping', ip], stdout=subprocess.PIPE).stdout.decode('utf-8')
        await ctx.send("```" + output + "```")
        await ctx.message.delete()


async def setup(bot: commands.Bot):
    await bot.add_cog(pingCog(bot))