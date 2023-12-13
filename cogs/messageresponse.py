from discord.ext import commands
import discord
import config
import random

from modulesf.utility import Utility

class MessageResponse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.fetch_json = Utility().fetch_json

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if random.randint(0, 200) > 180:
            response_text = f'{random.choice(self.fetch_json("motivation.json"))} {str(message.author.mention)}'
            await message.channel.send(response_text)


async def setup(bot):
    await bot.add_cog(MessageResponse(bot))