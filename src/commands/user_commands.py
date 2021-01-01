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

    @commands.command(name='info')
    async def info(self, ctx):
        # A command that shows some generic server information
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
            # Loop through each dictionary key and add a field for it in embed
            embed.add_field(name=stat, value=info_stat[stat], inline=True)

        embed.set_footer(text=self.config['SERVER_NAME'])
        await ctx.send(embed=embed)

    @commands.command(name='online')
    async def online(self, ctx):
        # Command that sends the user how many players are online
        players_online = self.database.get_online_count()
        plural_or_singular = "players" if players_online != 1 else "player"
        embed = discord.Embed(
            title='Players Online',
            description=f"{players_online} {plural_or_singular} online.",
            color=0x000FF00,
        )
        embed.set_thumbnail(url=self.config['SERVER_IMG'])
        embed.set_footer(text=self.config['SERVER_NAME'])
        await ctx.send(embed=embed)

    @commands.command(name='character', pass_context=True)
    async def character(self, ctx):
        # Command that will send nice embed message with their stats/info
        args = ctx.message.content.split(" ")
        if len(args) < 2:
            await ctx.send("Please provide a character name! !character <name>")
            return
        try:
            character = self.database.get_char_by_name(args[1])
        except Exception as e:
            await ctx.send("That character does not exist!")
            print("Character does not exist error:", e)
            return
        # if they are online make the embed color green else red
        online_color = 0x00FF00 if character.account.is_online() else 0xFF0000
        embed = discord.Embed(
            title="Character Info",
            color=online_color,
            description=f"{character.name}'s Info/Stats",
        )
        embed.set_thumbnail(url=character.get_char_img())
        embed.add_field(name="IGN", value=character.name, inline=True)
        embed.add_field(name="Fame", value=format_num(character.fame), inline=True)
        embed.add_field(name="Level", value=character.level, inline=True)
        embed.add_field(name="Mesos", value=format_num(character.meso), inline=True)
        embed.add_field(name="Job", value=character.get_job_name(), inline=True)
        embed.add_field(name="Donation Points", value=format_num(character.account.dp), inline=False)
        embed.set_footer(text=self.config['SERVER_NAME'])
        await ctx.send(embed=embed)

    @commands.command(name='rankings', pass_context=True)
    async def rankings(self, ctx):
        ranking_types = [
            "fame",
            "level",
            "mesos",
            "rebirths",
        ]
        num_of_players = 5
        args = ctx.message.content.split(" ")
        if len(args) < 2:
            await ctx.send("Please provide a ranking type! !rankings <type>")
            return

        ranking_type = args[1].lower()

        if ranking_type not in ranking_types:
            await ctx.send(f"Please provide a valid ranking type:\n{ranking_types}")
            return

        rankings = None

        if ranking_type == "fame":
            rankings = self.database.get_fame_ranking(num_of_players)
        elif ranking_type == "level":
            rankings = self.database.get_level_ranking(num_of_players)
        elif ranking_type == "mesos":
            rankings = self.database.get_meso_ranking(num_of_players)
        elif ranking_type == "rebirths":
            rankings = self.database.get_rebirth_ranking(num_of_players)

        embed = discord.Embed(
            title=f"{ranking_type.capitalize()} Rankings",
            color=self.get_server_color(),
            description=f"Top 5 characters for {ranking_type.capitalize()}"
        )

        rankings_size = len(rankings)
        worded_num = [
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
        ]
        for i in range(rankings_size):
            player_name = rankings[i][0]
            value = format_num(rankings[i][1])
            embed.add_field(
                name=worded_num[i] + ":",
                value=f"{player_name}: {value} {ranking_type}",
                inline=False,
            )

        embed.set_footer(text=self.config['SERVER_NAME'])
        await ctx.send(embed=embed)


def format_num(x):
    return "{:,}".format(x)


def setup(bot):
    bot.add_cog(UserCommands(bot))
