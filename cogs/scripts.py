from discord.ext import commands
import discord
from random import random
from asyncio import sleep

class Scripts(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def text_loop(self, ctx, iterator: int = 1, *text: str):
        await ctx.message.delete()
        for _ in range(iterator):
            await sleep(random() * 2)
            await ctx.send(" ".join(text))
    

async def setup(bot):
    await bot.add_cog(Scripts(bot))