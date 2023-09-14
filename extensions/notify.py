import discord
import array
from discord.ext import commands, tasks
from asyncio import sleep
import subprocess

class statusCog(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.check.start()

    global arr
    
    arr = array.array('i',(0 for i in range(0,256)))

    @commands.command()
    async def status(self, ctx):
        staus = "Status\n"
        for hmm in range(0, 99):
            staus += "10.1.10." + str(hmm) + ": " + str(arr[hmm]) + "\n"
        await ctx.send(staus)
        staus = "Status\n"
        for hmm in range(100, 199):
            staus += "10.1.10." + str(hmm) + ": " + str(arr[hmm]) + "\n"
        await ctx.send(staus)
        staus = "Status\n"
        for hmm in range(200, 256):
            staus += "10.1.10." + str(hmm) + ": " + str(arr[hmm]) + "\n"
        await ctx.send(staus)
        
        await ctx.message.delete()

    def cog_unload(self):
        self.check.cancel()
	
    @tasks.loop(seconds=1800.0)
    async def check(self):
        channel = self.bot.get_channel(1128125427421040774)
        vc = await channel.connect()
        await vc.disconnect()

        for hmm in range(0, 256):
            ip = "10.0.0." + str(hmm)
            output = subprocess.Popen(["ping.exe", "-n", "1", ip],stdout = subprocess.PIPE).communicate()[0]
            if ('unreachable' in str(output)):
                result = 0
            else:
                result = 1

            print(ip + ": " + str(result))

            if result == arr[hmm]:
                print("No change")
            else:
                if result == 0:
                    arr[hmm] = result
                    voice = discord.utils.get(vc.voice_clients, guild=1128125426783498310)

                    if voice == None:
                        channel = self.bot.get_channel(1128125427421040774)
                        vc = await channel.connect()
                        vc.play(discord.FFmpegPCMAudio("D:/Personal Files/Desktop/Projects/EnoGod Project/extensions/dust.mp3"), after=lambda e: print(f"WentOffline"))
                        vc.source = discord.PCMVolumeTransformer(vc.source, 1)
            
                        while vc.is_playing():
                            await sleep(1)
                        await vc.disconnect()
                    
                    message = self.bot.get_channel(1128125427421040773)
                    await message.send(ip + " says goodbye")


                if result == 1:
                    arr[hmm] = result
                    voice = discord.utils.get(vc.voice_clients, guild=1128125426783498310)

                    if voice == None:
                        channel = self.bot.get_channel(1128125427421040774)
                        vc = await channel.connect()
                        vc.play(discord.FFmpegPCMAudio("D:/Personal Files/Desktop/Projects/EnoGod Project/extensions/hello.mp3"), after=lambda e: print(f"Went Online"))
                        vc.source = discord.PCMVolumeTransformer(vc.source, 1)
            
                        while vc.is_playing():
                            await sleep(1)
                        await vc.disconnect()
                    
                    message = self.bot.get_channel(1128125427421040773)
                    await message.send(ip + " says hello")

            await sleep(10)

    @check.before_loop
    async def before_check(self):
        print('waiting...')
        await self.bot.wait_until_ready()

async def setup(bot: commands.Bot):
    await bot.add_cog(statusCog(bot))