from discord.ext import commands
import discord

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def say(self, ctx, *text):
        await ctx.message.delete()
        await ctx.send(" ".join(text))

async def setup(bot):
    await bot.add_cog(General(bot))