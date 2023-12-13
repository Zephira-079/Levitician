from discord.ext import commands
import discord
import config

class Creator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["pc"])
    async def purgechannel(self, ctx, channel_id=None):
        if (str(ctx.author) != config.get("creator_username")):
            return
        
        if channel_id is None:
            channel_id = ctx.channel.id

        channel = self.bot.get_channel(int(channel_id))
        if channel is None:
            await ctx.send("Invalid channel ID.", delete_after = 10)
            return

        try:
            await channel.purge(limit=None)
            await ctx.send(f"All messages deleted in {channel.mention}.", delete_after = 10)
        except discord.Forbidden:
            await ctx.send("I don't have permission to delete messages in that channel.", delete_after = 10)

    @commands.command(aliases=["create_link","ci","cl"])
    async def create_invite(self, ctx):
        if (str(ctx.author) != config.get("creator_username")):
            return
        
        channel = ctx.channel
        invite_expiration = 60 * 60 * 24 * 30
        invite_quota = 25
        invite_url = await channel.create_invite(max_age=invite_expiration, max_uses=invite_quota)
        await ctx.message.delete()
        await ctx.send(f'Invite_Link: ``` {invite_url} ```', delete_after=20)

    @commands.command(aliases=["mm"])
    async def move_member(self, ctx, member: discord.Member, channel: discord.VoiceChannel = None):
        if (str(ctx.author) != config.get("creator_username")):
            return
        
        if not channel and ctx.author.voice:
            channel = ctx.author.voice.channel
        await member.move_to(channel)

    @commands.command(aliases=["terminate","shut"])
    async def shutdown(self, ctx):
        if (ctx.author != ctx.guild.owner) or (str(ctx.author) != config.get("creator_username")):
            return
        
        await ctx.send(f"{ctx.author.mention} -_Turning Off_- ~~~")
        await self.bot.close()

    @commands.command(aliases=["delete"])
    async def delete_message(self, ctx, message_id: int):
        if (ctx.author != ctx.guild.owner) or (str(ctx.author) != config.get("creator_username")):
            return
        
        channel = ctx.channel
        message = await channel.fetch_message(message_id)
        await ctx.message.delete()
        await message.delete()

    @commands.command(aliases=["quit_server"])
    async def leave_server(self, ctx):
        if (ctx.author != ctx.guild.owner) or (str(ctx.author) != config.get("creator_username")):
            return
        
        await ctx.send(f"{ctx.author.mention} I'm leaving!!!")
        await self.bot.get_guild(int(ctx.guild.id)).leave()

    @commands.command()
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        if (ctx.author != ctx.guild.owner) or (str(ctx.author) != config.get("creator_username")):
            return
        
        if ctx.author.guild_permissions.kick_members:
            await user.kick(reason=reason)
            await ctx.send(f"{user.mention} has been kicked from the server. Reason: {reason}")
        else:
            await ctx.send("You do not have the required permissions to kick members.")

async def setup(bot):
    await bot.add_cog(Creator(bot))