import asyncio, json
import discord
from discord.ext import commands
from discord.utils import get
from asyncio import sleep
import matplotlib.pyplot as plt
import numpy as np

class announceCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        pass
	
    @discord.ext.commands.has_any_role(981683382108958790, 688450976704757812)

    @commands.command()
    async def announce(self, ctx, arg1):
        await ctx.message.delete()

        channel = self.bot.get_channel(688452883418578955)
        await channel.send(arg1)



async def setup(bot: commands.Bot):
    await bot.add_cog(announceCog(bot))