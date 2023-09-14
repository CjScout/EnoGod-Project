import asyncio, json
import discord
from discord.ext import commands
from discord.utils import get
from asyncio import sleep
import matplotlib.pyplot as plt
import numpy as np

class pollCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        pass
	
    @discord.ext.commands.has_any_role(981683382108958790, 688450976704757812)

    @commands.command()
    async def poll(self, ctx, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        await ctx.message.delete()

        desc = "1️⃣ " + arg2 + "\n" + "2️⃣ " + arg3 + "\n" + "3️⃣ " + arg4 + "\n" + "4️⃣ " + arg5
        embed=discord.Embed(title=arg1, description=desc, color=discord.Color.blue())
        poll = await ctx.send(embed=embed) 

        choices = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']
        for choice in choices:
            await poll.add_reaction(choice)

        await asyncio.sleep(int(arg7)*60*60)

        # get the updated message object
        poll = await poll.channel.fetch_message(poll.id)

        # get a mapping of reactions to their counts
        counts = {react.emoji: react.count - 1 for react in poll.reactions}

        sizes = []
        labels = arg2, arg3, arg4, arg5

        # create a result message
        result = 'The poll is over. Here are the results:\n'
        for choice, count in counts.items():
            result += f'{choice}: {count} votes\n'
            sizes.append(count)

        if (arg6.lower() == "bar"):
            plt.barh(labels, sizes)
            plt.xlabel('# of Votes')
            plt.ylabel('Options')
            plt.title(arg1)
            plt.tight_layout()

        if (arg6.lower() == "pie"):
            x = np.char.array([arg2, arg3, arg4, arg4])
            y = np.array(sizes)
            colors = ['yellowgreen','red','gold','lightskyblue']
            porcent = 100.*y/y.sum()

            patches, texts = plt.pie(y, colors=colors, startangle=90, radius=1.2)
            labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]

            sort_legend = True
            if sort_legend:
                patches, labels, dummy =  zip(*sorted(zip(patches, labels, y), key=lambda x: x[2], reverse=True))

            plt.legend(patches, labels, loc='upper right', bbox_to_anchor=(-0.1, 1.), fontsize=12)

        plt.savefig("poll.jpg", dpi=1000, bbox_inches='tight')

        plt.clf()

        with open('poll.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.channel.send(file=picture)

async def setup(bot: commands.Bot):
    await bot.add_cog(pollCog(bot))