import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class AdminCommands(commands.Cog, name='AdminCommands'):
    """
        Cog class that handles all admin commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello_admin', pass_context=True)
    @has_permissions(administrator=True)
    async def hello_admin(self, ctx, *, member: discord.Member = None):
        await ctx.send('Hello admin!')


def setup(bot):
    bot.add_cog(AdminCommands(bot))
