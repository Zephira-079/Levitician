from discord.ext import commands
import discord
import random
from asyncio import sleep
from sympy import sympify

class Scripts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def text_loop(self, ctx, iterator: int = 1, *text: str):
        await ctx.message.delete()
        for _ in range(iterator):
            await sleep(random.random() * 2)
            await ctx.send(" ".join(text))
            
    @commands.command(aliases=["random","choice"])
    async def randint(self, ctx, *numbers: int):
        if len(numbers) == 0 and isinstance(numbers, float):
            await ctx.send(f"result: {random.randint(0, 1)}")
        elif len(numbers) == 1 and isinstance(numbers, float):
            await ctx.send(f"result: {random.randint(0, numbers[0])}")
        elif len(numbers) == 2 and isinstance(numbers, float):
            await ctx.send(f"result: {random.randint(numbers[0], numbers[1])}")
        elif len(numbers) > 2 and isinstance(numbers, float):
            await ctx.send(f"result: {random.choice(numbers)}")

    @commands.command(aliases=["math","expr","calc","calculate"])
    async def expression(self, ctx, *text: str):
        await ctx.send(sympify(" ".join(text)))

async def setup(bot):
    await bot.add_cog(Scripts(bot))