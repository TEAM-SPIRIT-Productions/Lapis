import discord
from discord.ext import commands
from lazuli.database import Lazuli
import json
import os


class UserCommands(commands.Cog, name='UserCommands'):
    """
        Cog class that handles all user commands.
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

    def get_server_color(self):
        """
        Converting the hex string in config file to a hex int for color embed
        :return: int
        """
        return int(self.config['SERVER_COLOR'], 16) + 0x200

    @commands.command(name='info', pass_context=True)
    async def info(self, ctx, *, member: discord.Member = None):
        # Change the stats here for your server
        info_stat = {
            'Exp': '1x',
            'Item': '1x',
            'Meso': '1x',
            'Server State': 'N/A',
            'Server Location': 'N/A',
            'Release Date': 'N/A',
        }
        embed = discord.Embed(
            title=self.config['SERVER_NAME'],
            color=self.get_server_color(),
            description="KMS v316"
        )
        embed.set_thumbnail(url=self.config['SERVER_IMG'])

        for stat in info_stat:
            embed.add_field(name=stat, value=info_stat[stat], inline=True)

        embed.set_footer(text=self.config['SERVER_NAME'])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(UserCommands(bot))
