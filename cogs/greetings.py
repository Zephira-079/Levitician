from discord.ext import commands
import discord
import config
import random

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = config.get("on_member_join_channel")
        channel = member.guild.get_channel(int(channel_id))

        response_text = f'{random.choice(self.fetch_json("motivation.json"))} {str(member.mention)}'
        if channel: 
            await channel.send(response_text)

async def setup(bot):
    await bot.add_cog(Greetings(bot))