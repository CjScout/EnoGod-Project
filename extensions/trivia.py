import discord
from discord.ext import commands
import random
import asyncio

class triviaCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        pass
	
    @discord.ext.commands.has_any_role(981683382108958790, 688450976704757812)

    @commands.command()
    async def trivia(self, ctx):
        def read_questions_and_answers(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            questions_and_answers = []
            num_lines = len(lines)
            for i in range(0, num_lines, 2):
                # Ensure we have a pair of lines (question and answer) to process
                if i + 1 < num_lines:
                    question = lines[i].strip()
                    answer = lines[i + 1].strip()
                    questions_and_answers.append((question, answer))

            return questions_and_answers

        def select_random_question_answer(questions_and_answers):
            return random.choice(questions_and_answers)
        
        file_path = "questions_answers.txt"
        questions_and_answers = read_questions_and_answers(file_path)

        random_pair = select_random_question_answer(questions_and_answers)
                
        await ctx.send(random_pair[0])

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        try:
            response = await self.bot.wait_for('message', check=check, timeout=10.0)
            print(response.content)
            if (random_pair[1] == response.content):
                await ctx.send(f'Correct!')
            else:
                await ctx.send(f'Incorrect, the correct answer was ' + str(random_pair[1]))
        except asyncio.TimeoutError:
            await ctx.send('Time is up! You took too long to respond.')

        await ctx.message.delete()

async def setup(bot: commands.Bot):
    await bot.add_cog(triviaCog(bot))