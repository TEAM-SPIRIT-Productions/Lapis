import discord
from discord.ext import commands


class UserCommands(commands.Cog, name='UserCommands'):
    """
        Cog class that handles all user commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', pass_context=True)
    async def hello_world(self, ctx, *, member: discord.Member = None):
        await ctx.send('Hello from Lapis!')


def setup(bot):
    bot.add_cog(UserCommands(bot))
