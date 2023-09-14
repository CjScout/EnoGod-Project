import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
import discord
from discord.ext import commands

class enoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        pass
	
    @discord.ext.commands.has_any_role(981683382108958790, 688450976704757812)

    @commands.command()
    async def eno(self, ctx):
        prompt = ctx.message.content.replace('!eno ', '')
        await ctx.send("One moment please...")
        cookies = json.loads(open("./bing_cookies_.json", encoding="utf-8").read())  # might omit cookies option
        chatbot = await Chatbot.create(cookies=cookies)
        response = await chatbot.ask(prompt=prompt, conversation_style=ConversationStyle.creative, simplify_response=True)
        output = response['text']
        source = response['sources_text']
        await chatbot.close()


        embed=discord.Embed(title=prompt, description=output+"\n\n"+source, color=discord.Color.blue())
        await ctx.send(embed=embed)
        await ctx.message.delete()

async def setup(bot: commands.Bot):
    await bot.add_cog(enoCog(bot))