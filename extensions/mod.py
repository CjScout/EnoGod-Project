import discord
from discord.ext import commands
import subprocess
import string

class modCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.wordlist = ["fuck", "shit", "bitch"]
	
    @commands.Cog.listener()
    async def on_ready(self):
        pass
	
    @commands.Cog.listener()
    async def on_message(self, message):
        # ignore messages from the bot itself
        if message.author == self.bot.user:
            return

        # check if the message contains any of the words in the list
        for word in self.wordlist:
            if word in message.content.lower():
                # delete the message and send a warning
                await message.delete()
                await message.channel.send(f"{message.author.mention}, chillax this is a school server.")
                break


async def setup(bot: commands.Bot):
    await bot.add_cog(modCog(bot))