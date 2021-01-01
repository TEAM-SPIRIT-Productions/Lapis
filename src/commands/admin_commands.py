import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import os
import json

from lazuli.database import Lazuli


class AdminCommands(commands.Cog, name='AdminCommands'):
    """
        Cog class that handles all admin commands.
    """

    def __init__(self, bot):
        self.bot = bot

        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/config.json') as f:
            self.config = json.load(f)

        self.database = Lazuli()
        # Lazuli will automatically connect to localhost
        # If config is not using default then we change it to custom settings
        if not self.config['USE_DEFAULT_DB']:
            self.database = Lazuli(
                host=self.config['DATABASE_HOST'],
                schema=self.config['DATABASE_NAME'],
                user=self.config['DATABASE_USER'],
                password=self.config['DATABASE_CONFIG'],
                port=self.config['DATABASE_PORT'],
            )

    @commands.command(name='hello_admin', pass_context=True)
    @has_permissions(administrator=True)
    async def hello_admin(self, ctx, *, member: discord.Member = None):
        await ctx.send('Hello admin!')


def setup(bot):
    bot.add_cog(AdminCommands(bot))
