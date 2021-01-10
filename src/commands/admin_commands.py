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

    def get_server_color(self):
        """
        Converting the hex string in config file to a hex int for color embed
        :return: int
        """
        return int(self.config['SERVER_COLOR'], 16) + 0x200

    @commands.command(name='givemeso', pass_context=True)
    @has_permissions(administrator=True)
    async def give_meso(self, ctx):
        args = ctx.message.content.split(" ")
        if len(args) < 3:
            await ctx.send("Please provide all necessary arguments! !givemeso <name> <amount>")
            return
        player_name = args[1]
        amount = int(args[2])

        try:
            character = self.database.get_char_by_name(player_name)
        except Exception as e:
            await ctx.send("That character does not exist.")
            print("Character does not exist error:", e)
            return

        if character.account.is_online():
            await ctx.send("Make sure the character is offline before giving mesos!")
            return

        embed = discord.Embed(
            title="Mesos",
            color=self.get_server_color(),
            description=f"Successfully gave {character.name} {format_num(amount)} mesos."
        ).set_footer(text=self.config["SERVER_NAME"]).set_thumbnail(url=self.config["SERVER_IMG"])

        new_amount = amount + int(character.meso)
        character.meso = new_amount
        await ctx.send(embed=embed)

    @commands.command(name='givedp', pass_context=True)
    @has_permissions(administrator=True)
    async def give_dp(self, ctx):
        args = ctx.message.content.split(" ")
        if len(args) < 3:
            await ctx.send("Please provide all necessary arguments! !givedp <name> <amount>")
            return
        player_name = args[1]
        amount = int(args[2])

        try:
            character = self.database.get_char_by_name(player_name)
        except Exception as e:
            await ctx.send("That character does not exist.")
            print("Character does not exist error:", e)
            return

        if character.account.is_online():
            await ctx.send("Make sure the character is offline before giving donation points!")
            return

        embed = discord.Embed(
            title="Donation Points",
            color=self.get_server_color(),
            description=f"Successfully gave {character.name} {format_num(amount)} donation points."
        ).set_footer(text=self.config["SERVER_NAME"]).set_thumbnail(url=self.config["SERVER_IMG"])

        new_amount = amount + int(character.account.dp)
        character.account.dp = new_amount
        await ctx.send(embed=embed)

    @commands.command(name='givevp', pass_context=True)
    @has_permissions(administrator=True)
    async def give_vp(self, ctx):
        args = ctx.message.content.split(" ")
        if len(args) < 3:
            await ctx.send("Please provide all necessary arguments! !givevp <name> <amount>")
            return
        player_name = args[1]
        amount = int(args[2])

        try:
            character = self.database.get_char_by_name(player_name)
        except Exception as e:
            await ctx.send("That character does not exist.")
            print("Character does not exist error:", e)
            return

        if character.account.is_online():
            await ctx.send("Make sure the character is offline before giving vote points!")
            return

        embed = discord.Embed(
            title="Vote Points",
            color=self.get_server_color(),
            description=f"Successfully gave {character.name} {format_num(amount)} vote points."
        ).set_footer(text=self.config["SERVER_NAME"]).set_thumbnail(url=self.config["SERVER_IMG"])

        new_amount = amount + int(character.account.vp)
        character.account.vp = new_amount
        await ctx.send(embed=embed)

    @commands.command(name='setname', pass_context=True)
    @has_permissions(administrator=True)
    async def set_name(self, ctx):
        args = ctx.message.content.split(" ")
        if len(args) < 3:
            await ctx.send("Please provide all necessary arguments! !setname <name> <new_name>")
            return
        player_name = args[1]
        new_name = args[2]

        try:
            character = self.database.get_char_by_name(player_name)
        except Exception as e:
            await ctx.send("That character does not exist.")
            print("Character does not exist error:", e)
            return

        if character.account.is_online():
            await ctx.send("Make sure the character is offline before changing their names!")
            return

        embed = discord.Embed(
            title="Name Change",
            color=self.get_server_color(),
            description=f"Successfully changed {character.name}'s name to {new_name}"
        ).set_footer(text=self.config["SERVER_NAME"]).set_thumbnail(url=self.config["SERVER_IMG"])

        character.name = new_name
        await ctx.send(embed=embed)

    @commands.command(name='unban', pass_context=True)
    @has_permissions(administrator=True)
    async def unban(self, ctx):
        args = ctx.message.content.split(" ")
        if len(args) < 2:
            await ctx.send("Please provide all necessary arguments! !unban <name>")
            return
        player_name = args[1]

        try:
            character = self.database.get_char_by_name(player_name)
        except Exception as e:
            await ctx.send("That character does not exist.")
            print("Character does not exist error:", e)
            return

        embed = discord.Embed(
            title="Unban",
            color=self.get_server_color(),
            description=f"Successfully unbanned {character.name}.\nPlease don't get yourself banned again! :)"
        ).set_footer(text=self.config["SERVER_NAME"]).set_thumbnail(url=self.config["SERVER_IMG"])

        character.account.banned = 0
        await ctx.send(embed=embed)

    @commands.command(name='ban', pass_context=True)
    @has_permissions(administrator=True)
    async def ban(self, ctx):
        args = ctx.message.content.split(" ")
        args_size = len(args)
        if args_size < 3:
            await ctx.send("Please provide all necessary arguments! !ban <name> <reason>")
            return

        player_name = args[1]
        ban_reason = ""
        index = 2

        while index < args_size:
            ban_reason += args[index] + " "
            index += 1

        try:
            character = self.database.get_char_by_name(player_name)
        except Exception as e:
            await ctx.send("That character does not exist.")
            print("Character does not exist error:", e)
            return

        if character.account.is_online():
            await ctx.send("Make sure the character is offline before banning!")
            return

        embed = discord.Embed(
            title="Ban",
            color=self.get_server_color(),
            description=f"Successfully banned {character.name}."
        ).set_footer(text=self.config["SERVER_NAME"]).set_thumbnail(url=self.config["SERVER_IMG"])

        character.account.banned = 1
        character.account.ban_reason = ban_reason
        await ctx.send(embed=embed)


def format_num(x):
    return "{:,}".format(x)


def setup(bot):
    bot.add_cog(AdminCommands(bot))
