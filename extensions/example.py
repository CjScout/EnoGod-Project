from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        pass
	
    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        await ctx.send(f'Pong')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExampleCog(bot))