"""
    @author Brandon
    Main entry point of the program.
"""
import discord
from discord.ext import commands
import json
import os

from discord.ext.commands import has_permissions

with open(os.path.dirname(os.path.abspath(__file__)) + '/config.json', 'r') as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=config['COMMAND_PREFIX'])
# remove the default help command so we can format it nicer
bot.remove_command('help')
print("Loading various commands....")
# Load all commands
bot.load_extension("commands.user_commands")
bot.load_extension("commands.admin_commands")


@bot.event
async def on_ready():
    print("Bot has successfully started!")


@bot.event
async def on_member_join(member):
    """
    When a member joins assign them a role from config.json
    """
    print(f"{member} has joined the discord server!")
    if config['ADD_ROLE']:
        print(f"Attempting to add role for {member}.")
        try:
            role = discord.utils.get(member.guild.roles, name=config['ROLE_TO_GIVE'])
            await member.add_roles(role)
        except Exception as e:
            print(f"Error encountered while attempting to assign role:\n{e}")


@bot.command(name='reload', pass_context=True)
@has_permissions(ban_members=True)
async def reload_cogs(ctx):
    """
    Command for reloading cog commands
    """
    try:
        bot.reload_extension('commands.user_commands')
        bot.reload_extension('commands.admin_commands')
        print("Successfully reloaded cogs!")
        await ctx.send("Successfully reloaded cogs!")
    except Exception as e:
        print("Error occurred while reloading cogs:", e)
        await ctx.send("Error occurred while reloading cogs.")


@bot.command(name='help', pass_context=True)
async def help_command(ctx):
    """
    Help command that lists all commands from the cog
    Changes depending on whether user is an administrator or not.
    """
    user_cog = bot.get_cog('UserCommands')
    cmd_list = [command.name + "\n" for command in user_cog.get_commands()]
    cmd_list_str = ""

    for cmd in cmd_list:
        cmd_list_str += cmd

    embed_msg = discord.Embed(title="Commands", description=f"All bot commands for {config['SERVER_NAME']}",
                              color=int(config['SERVER_COLOR'], 16) + 0x200)
    embed_msg.set_thumbnail(url=config['SERVER_IMG'])
    embed_msg.add_field(name="Player Commands", value=cmd_list_str, inline=False)

    if ctx.author.guild_permissions.administrator:
        # We only add the admin commands if they are an admin on the server
        admin_cog = bot.get_cog('AdminCommands')

        cmd_list = [command.name + "\n" for command in admin_cog.get_commands()]
        cmd_list_str = ""

        for cmd in cmd_list:
            cmd_list_str += cmd

        embed_msg.add_field(name="Admin Commands", value=cmd_list_str)

    embed_msg.set_footer(text=config['SERVER_NAME'])
    await ctx.send(embed=embed_msg)


def main():
    print("Loading bot...")
    bot.run(config['BOT_TOKEN'])


if __name__ == '__main__':
    main()
