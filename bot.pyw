# Libraries ============================================================================================================

import configparser
import os
import time
import discord
import shutil
import random
import subprocess
from discord.ext import commands
import asyncio
import datetime
import pypresence
from git import Repo

if os.path.exists("repo"):
    process = subprocess.run("echo y | rmdir /s repo",
                             shell=True,
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.STDOUT)

# Functions & Setters ==================================================================================================

config = configparser.ConfigParser()

games = 4
fun = 13
tools = 9
admin = 4


def write():
    config.write(open('config.ini', 'w'))


def get_prefix():
    return config["CONFIGURATION"]["prefix"]


def test(ctx):
    return print(f"{ctx.author}: {ctx.content}")


def permission_check(ctx):
    if config['CONFIGURATION']['blacklist'] == "True":
        with open("data/blacklist.txt", "r") as file:
            content = file.read().split("\n")
            if f"{ctx.author.id}" in content:
                return True
            else:
                return False
    elif config['CONFIGURATION']['whitelist'] == "True":
        if ctx.author != bot.user:
            with open("data/whitelist.txt", "r") as file:
                content = file.read().split("\n")
                if f"{ctx.author.id}" in content:
                    return False
                else:
                    return True
        else:
            return False
    else:
        return False


def footer(embed):
    return embed.set_footer(
        text=f"Logged in as {bot.user} | Lost-UB",
        icon_url=bot.user.avatar_url
    )


def codeblock_footer():
    return f"# Logged in as {bot.user.display_name} | Lost-UB"


def embedcolor(color=None):
    if color is None:
        if config['CONFIGURATION']['embedcolor'].lower() == "red":
            return discord.Colour.from_rgb(255, 0, 0)
        elif config['CONFIGURATION']['embedcolor'].lower() == "light red":
            return discord.Colour.from_rgb(255, 76, 76)
        elif config['CONFIGURATION']['embedcolor'].lower() == "orange":
            return discord.Colour.from_rgb(255, 165, 0)
        elif config['CONFIGURATION']['embedcolor'].lower() == "light orange":
            return discord.Colour.from_rgb(255, 192, 76)
        elif config['CONFIGURATION']['embedcolor'].lower() == "yellow":
            return discord.Colour.from_rgb(255, 255, 0)
        elif config['CONFIGURATION']['embedcolor'].lower() == "green":
            return discord.Colour.from_rgb(0, 128, 0)
        elif config['CONFIGURATION']['embedcolor'].lower() == "light green":
            return discord.Colour.from_rgb(76, 166, 76)
        elif config['CONFIGURATION']['embedcolor'].lower() == "blue":
            return discord.Colour.from_rgb(0, 0, 255)
        elif config['CONFIGURATION']['embedcolor'].lower() == "light blue":
            return discord.Colour.from_rgb(76, 76, 255)
        elif config['CONFIGURATION']['embedcolor'].lower() == "purple":
            return discord.Colour.from_rgb(128, 0, 128)
        elif config['CONFIGURATION']['embedcolor'].lower() == "light purple":
            return discord.Colour.from_rgb(128, 0, 128)
        elif config['CONFIGURATION']['embedcolor'].lower() == "pink":
            return discord.Colour.from_rgb(255, 192, 203)
        elif config['CONFIGURATION']['embedcolor'].lower() == "light pink":
            return discord.Colour.from_rgb(255, 210, 218)
    else:
        if color.lower() == "red":
            return discord.Colour.from_rgb(255, 0, 0)
        elif color.lower() == "light red":
            return discord.Colour.from_rgb(255, 76, 76)
        elif color.lower() == "orange":
            return discord.Colour.from_rgb(255, 165, 0)
        elif color.lower() == "light orange":
            return discord.Colour.from_rgb(255, 192, 76)
        elif color.lower() == "yellow":
            return discord.Colour.from_rgb(255, 255, 0)
        elif color.lower() == "green":
            return discord.Colour.from_rgb(0, 128, 0)
        elif color.lower() == "light green":
            return discord.Colour.from_rgb(76, 166, 76)
        elif color.lower() == "blue":
            return discord.Colour.from_rgb(0, 0, 255)
        elif color.lower() == "light blue":
            return discord.Colour.from_rgb(76, 76, 255)
        elif color.lower() == "purple":
            return discord.Colour.from_rgb(128, 0, 128)
        elif color.lower() == "light purple":
            return discord.Colour.from_rgb(128, 0, 128)
        elif color.lower() == "pink":
            return discord.Colour.from_rgb(255, 192, 203)
        elif color.lower() == "light pink":
            return discord.Colour.from_rgb(255, 210, 218)
        else:
            return discord.Colour.from_rgb(76, 76, 255)


def simple_embed(context, title, description, thumbnail: str = None, reply: bool = True):
    embed = discord.embeds.Embed(
        title=title,
        description=description,
        colour=embedcolor()
    )
    if thumbnail is None:
        pass
    else:
        embed.set_thumbnail(url=thumbnail)
    footer(embed)
    if reply is True:
        return context.reply(embed=embed)
    else:
        return context.send(embed=embed)


def simple_codeblock(context, text, reply: bool = True):
    if reply is True:
        return context.reply(f"```ini\n"
                             f"{text}\n\n"
                             f"{codeblock_footer()}\n"
                             f"```")
    else:
        return context.send(f"```ini\n"
                            f"{text}\n\n"
                            f"{codeblock_footer()}\n"
                            f"```")


def timestamp():
    current_time = time.localtime()
    if current_time.tm_hour > 12:
        hour = current_time.tm_hour - 12
        suffix = "pm"
    else:
        hour = current_time.tm_hour
        suffix = "am"
    count = 0
    for x in str(current_time.tm_min):
        count += 1
    if count == 1:
        minute = f"0{current_time.tm_min}"
    else:
        minute = current_time.tm_min
    return f"{hour}:{minute}{suffix}"


def log(context, title: str = "Command Usage", description: str = None, color: str = None):
    if context.guild is None:
        context.guild = "dms"
    embed = discord.embeds.Embed(
        title=title,
        description=description,
        colour=color
    )
    embed.add_field(
        name="User",
        value=context.author,
        inline=True
    )
    embed.add_field(
        name="Guild",
        value=context.guild,
        inline=True
    )
    embed.add_field(
        name="Source",
        value=f"[Message]({context.message.jump_url})",
        inline=True
    )
    embed.add_field(
        name="Timestamp",
        value=timestamp(),
        inline=True
    )
    embed.set_thumbnail(url=f"{context.author.avatar_url}")
    footer(embed)
    channel = bot.get_channel(int(config["CONFIGURATION"]["log_output"]))
    return channel.send(embed=embed)
    # if context.guild is None:
    #     context.guild = "dms"
    # if message is None:
    #     if command_name.lower() == "error" or command_name.lower() == "blacklist" or \
    #             command_name.lower() == "ghostping":
    #         string = f"{Fore.LIGHTBLUE_EX}[LOST-UB]" \
    #                  f"{Fore.LIGHTCYAN_EX}[{f'{context.guild}'.upper()}]" \
    #                  f"[{f'{context.author}'.upper()}]" \
    #                  f"{Fore.LIGHTRED_EX}[{command_name}]{Fore.LIGHTWHITE_EX}> " \
    #                  f"{context.message.content}"
    #     else:
    #         string = f"{Fore.LIGHTBLUE_EX}[LOST-UB]" \
    #                  f"{Fore.LIGHTCYAN_EX}[{f'{context.guild}'.upper()}]" \
    #                  f"[{f'{context.author}'.upper()}]" \
    #                  f"{Fore.LIGHTGREEN_EX}[{command_name}]{Fore.LIGHTWHITE_EX}> " \
    #                  f"{context.message.content}"
    # else:
    #     if command_name.lower() == "error" or command_name.lower() == "blacklist" or \
    #             command_name.lower() == "whitelist" or command_name.lower() == "ghostping":
    #         string = f"{Fore.LIGHTBLUE_EX}[LOST-UB]" \
    #                  f"{Fore.LIGHTCYAN_EX}[{f'{context.guild}'.upper()}]" \
    #                  f"[{f'{context.author}'.upper()}]" \
    #                  f"{Fore.LIGHTRED_EX}[{command_name}]{Fore.LIGHTWHITE_EX}> " \
    #                  f"{message}"
    #     else:
    #         string = f"{Fore.LIGHTBLUE_EX}[LOST-UB]" \
    #                  f"{Fore.LIGHTCYAN_EX}[{f'{context.guild}'.upper()}]" \
    #                  f"[{f'{context.author}'.upper()}]" \
    #                  f"{Fore.LIGHTGREEN_EX}[{command_name}]{Fore.LIGHTWHITE_EX}> " \
    #                  f"{message}"
    # return print(string)


# Checks ===============================================================================================================

if not os.path.exists('config.ini'):
    print(f"""                                                                                        
                                  :::            ::::::::           ::::::::       :::::::::::
                                 :+:           :+:    :+:         :+:    :+:          :+:
                                +:+           +:+    +:+         +:+                 +:+
                               +#+           +#+    +:+         +#++:++#++          +#+
                              +#+           +#+    +#+                +#+          +#+
                             #+#           #+#    #+#         #+#    #+#          #+#
                            ##########     ########           ########           ###     

                                                   LOST.#9567
    """)
    config['CONFIGURATION'] = {
        "token": f"{input(f'[LOST-UB]> Please enter in your token: ')}",
        "prefix": f"{input(f'[LOST-UB]> Please enter in your prefix: ')}",
        "autoupdate": "True",
        "AFK": "False",
        "afk_msg": "I'm afk",
        "afk_legit": "True",
        "silentsteal": "False",
        "silentsave": "False",
        "embedcolor": "light blue",
        "blacklist": "False",
        "whitelist": "False",
        "rich_presence": "True",
        "automock": "False",
        "server": "None",
        "log_output": "None"
    }
    write()
else:
    config.read('config.ini')
    if not config.has_option("CONFIGURATION", "AFK"):
        config["CONFIGURATION"]["AFK"] = "False"
        write()
    if config["CONFIGURATION"]["AFK"] == "True":
        config["CONFIGURATION"]["AFK"] = "False"
        write()
    elif config["CONFIGURATION"]["AFK"] != "True" or config["CONFIGURATION"]["AFK"] != "False":
        config["CONFIGURATION"]["AFK"] = "False"
        write()
    if not config.has_option("CONFIGURATION", "prefix"):
        config["CONFIGURATION"]["prefix"] = ">"
        write()
    if not config.has_option("CONFIGURATION", "token"):
        config["CONFIGURATION"]["token"] = input("[LOST-UB]> Token not found, please enter in your token: ")
        write()
    if not config.has_option("CONFIGURATION", "afk_msg"):
        config["CONFIGURATION"]["afk_msg"] = "I'm afk"
        write()
    if not config.has_option("CONFIGURATION", "afk_legit"):
        config["CONFIGURATION"]["afk_legit"] = "True"
        write()
    if not config.has_option("CONFIGURATION", "silentsteal"):
        config["CONFIGURATION"]["silentsteal"] = "False"
        write()
    if not config.has_option("CONFIGURATION", "silentsave"):
        config["CONFIGURATION"]["silentsave"] = "False"
        write()
    if not config.has_option("CONFIGURATION", "embedcolor"):
        config["CONFIGURATION"]["embedcolor"] = "red"
        write()
    if not config.has_option("CONFIGURATION", "blacklist"):
        config["CONFIGURATION"]["blacklist"] = "False"
        write()
    if not config.has_option("CONFIGURATION", "whitelist"):
        config["CONFIGURATION"]["whitelist"] = "False"
        write()
    if not config.has_option("CONFIGURATION", "rich_presence"):
        config["CONFIGURATION"]["rich_presence"] = "True"
        write()
    if not config.has_option("CONFIGURATION", "automock"):
        config["CONFIGURATION"]["automock"] = "False"
        write()
    if not config.has_option("CONFIGURATION", "autoupdate"):
        config["CONFIGURATION"]["autoupdate"] = "True"
        write()
    if not config.has_option("CONFIGURATION", "server"):
        config["CONFIGURATION"]["server"] = "None"
        write()
    if not config.has_option("CONFIGURATION", "log_output"):
        config["CONFIGURATION"]["server"] = "None"
        write()
if config["CONFIGURATION"]["blacklist"] == "True" and config["CONFIGURATION"]["whitelist"] == "True":
    config["CONFIGURATION"]["blacklist"] = "False"
    config["CONFIGURATION"]["whitelist"] = "False"
    write()
    print("Blacklist and whitelist cannot be on at the same time. disabled both.")

if not os.path.exists('data'):
    os.mkdir('data')
if not os.path.exists('data/avatars'):
    os.mkdir('data/avatars')
if not os.path.exists('data/blacklist.txt'):
    open('data/blacklist.txt', 'a+')
if not os.path.exists('data/whitelist.txt'):
    open('data/whitelist.txt', 'a+')
if not os.path.exists('data/automock.txt'):
    open('data/automock.txt', 'a+')
if not os.path.exists('data/logs'):
    os.mkdir('data/logs')
if not os.path.exists('data/logs/loggedusers.txt'):
    open('data/logs/loggedusers.txt', 'a+')
if not os.path.exists('data/logs/users'):
    os.mkdir('data/logs/users')

# Bot ==================================================================================================================

bot = commands.Bot(command_prefix=f"{config['CONFIGURATION']['prefix']}", help_command=None, user_bot=True,
                   case_insensitive=True)

try:
    print(f"""                                                                                         
                                      :::            ::::::::           ::::::::       :::::::::::
                                     :+:           :+:    :+:         :+:    :+:          :+:
                                    +:+           +:+    +:+         +:+                 +:+
                                   +#+           +#+    +:+         +#++:++#++          +#+
                                  +#+           +#+    +#+                +#+          +#+
                                 #+#           #+#    #+#         #+#    #+#          #+#
                                ##########     ########           ########           ###     

                                                       LOST.#9567
        """)
    successful = True
    extensions = [
        'commands.help',
        'commands.rps',
        'commands.dicksize',
        'commands.prefix',
        'commands.flipcoin',
        'commands.eightball',
        'commands.ghostping',
        'commands.iq',
        'commands.afk',
        'commands.pfp',
        'commands.settings',
        'commands.diceroll',
        'commands.jesus',
        'commands.server',
        'commands.abc',
        'commands.warnings',
        'commands.userinfo',
        'commands.kick',
        'commands.ban',
        'commands.calculate',
        'commands.blacklist',
        'commands.battle',
        'commands.fight',
        'commands.spam',
        'commands.poll',
        'commands.embed',
        'commands.mock',
        'commands.cursive',
        'commands.monospace',
        'commands.space',
        'commands.userlog',
        'commands.hangman',
        'commands.whitelist',
        'commands.security'
    ]
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            successful = False
            folder, command = extension.split(".")
            print(f"[LOST-UB][ERROR]> Lost-Ub was unable to load {command} properly.")
            pass
    if successful is False:
        print(f"[LOST-UB][ERROR]> These commands weren't loaded correctly.\n"
              f"[LOST-UB][ERROR]> An update may fix this.")
except ModuleNotFoundError:
    print(f"[LOST-UB][ERROR]> Lost-Ub was unable to load commands properly, restart and check for updates.")
    exit()

if config["CONFIGURATION"]["autoupdate"] == "True":
    while True:
        require_restart = False
        print(f"""                                                                                         
                                  :::            ::::::::           ::::::::       :::::::::::
                                 :+:           :+:    :+:         :+:    :+:          :+:
                                +:+           +:+    +:+         +:+                 +:+
                               +#+           +#+    +:+         +#++:++#++          +#+
                              +#+           +#+    +#+                +#+          +#+
                             #+#           #+#    #+#         #+#    #+#          #+#
                            ##########     ########           ########           ###     

                                                   LOST.#9567
        """)
        print(f"[LOST-UB]> Checking for updates...")

        Repo.clone_from("https://github.com/L-o-s-t/Lost-UB", "repo/").index.remove(['.github'],
                                                                                    True, r=True)

        # Checks if README.md exists, if not it will create it
        if not os.path.exists("README.md"):
            print(f"[LOST-UB]> Readme.md not found, creating new one...")
            os.replace("repo/README.md", "README.md")

        # Checks if commands.md exists, if not then it will create it.
        if not os.path.exists("commands.md"):
            print(f"[LOST-UB]> Commands.md not found, creating new one...")
            os.replace("repo/commands.md", "commands.md")

        # Checks if bot.pyw exists, if not it will create it
        with open("repo/bot.pyw", "r", encoding="utf8") as new:
            newbot = new.read()
        with open("bot.pyw", "r", encoding="utf8") as old:
            oldbot = old.read()
        if newbot != oldbot:
            require_restart = True
            with open("bot.pyw", "w+", encoding="utf8") as mainfile:
                mainfile.write(newbot)
            print(f'[LOST-UB]> '
                  f'Successfully updated Lost-UB. Checking for updates in commands...')

        elif newbot == oldbot:
            print(f"[LOST-UB]> Main file is up to date...")

        if not os.path.exists("commands"):
            os.mkdir("commands")

        # current commands
        current_cmds = []
        for old_cmd in os.listdir("commands"):
            current_cmds.append(old_cmd)

        # latest commands
        latest_cmds = []
        new_cmds = 0
        updated_cmds = 0
        updatedlist = []
        addedlist = []
        for cmd in os.listdir("repo/commands"):
            if cmd in current_cmds:
                with open(f"commands/{cmd}", "r", encoding="utf8") as oldfile:
                    old_content = oldfile.read()
                    with open(f"repo/commands/{cmd}", "r", encoding="utf8") as newfile:
                        new_content = newfile.read()
                        if new_content != old_content:
                            oldfile = open(f"commands/{cmd}", "w", encoding="utf8")
                            oldfile.write(new_content)
                            updated_cmds += 1
                            updatedlist.append(cmd.replace('.py', ''))
                        else:
                            continue
            else:
                shutil.copy(f"repo/commands/{cmd}", f"commands/{cmd}")
                new_cmds += 1
                addedlist.append(cmd.replace('.py', ''))

        if new_cmds == 0:
            add_msg = "No new commands were found."
        elif new_cmds == 1:
            add_msg = "Added 1 new command"
        else:
            add_msg = f"Added {new_cmds} commands"

        if updated_cmds == 0:
            update_msg = "No commands were updated."
        elif updated_cmds == 1:
            update_msg = "Updated 1 command"
        else:
            update_msg = f"Updated {new_cmds} commands"

        update_results = ""
        if updated_cmds > 0:
            require_restart = True
            update_results += f"[LOST-UB]> " \
                              f"{update_msg}: {', '.join(updatedlist)}.\n"
        else:
            update_results += f"[LOST-UB]> {update_msg}\n"
        if new_cmds > 0:
            require_restart = True
            update_results += f"[LOST-UB]> {add_msg}: {', '.join(addedlist)}."
        else:
            update_results += f"[LOST-UB]> {add_msg}"

        print(update_results)

        process = subprocess.run("echo y | rmdir /s repo",
                                 shell=True,
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.STDOUT)
        if require_restart:
            print(f"[LOST-UB]> A restart will be needed for changes to work.")
            os.startfile('bot.pyw')
            exit()
        else:
            print(f"[LOST-UB]> No restarts required, press enter to continue...")
            break

try:
    if config['CONFIGURATION']['rich_presence'] == "True":
        client_id = "878728783585226773"
        start_time = time.time()
        rpc = pypresence.Presence(client_id)
        rpc.connect()
        rpc.update(state="version 3.0",
                   large_image="logo2",
                   details="Free and Open Sourced!",
                   start=int(start_time),
                   buttons=[{"label": "Github Repo", "url": "https://github.com/L-o-s-t/Lost-UB"},
                            {"label": "How to Install", "url": "https://www.youtube.com/watch?v=Fmbia_6jrI0"}])
except pypresence.InvalidPipe:
    print("[LOST-UB] Discord not installed? Rich Presence disabled.")
    pass


# Prints message to console when bot is ready
@bot.event
async def on_connect():
    if config["CONFIGURATION"]["server"] == "None":
        server_icon = open("data/server_logo.png", "rb")
        server = await bot.create_guild("Lost.UB", server_icon.read())
        while True:
            try:
                server = bot.get_guild(server.id)
                break
            except AttributeError:
                time.sleep(5)
        for category in server.categories:
            print(category.name.lower())
            if category.name.lower() == "text channels":
                print(category)
                log_channel = await category.create_text_channel(name="logs")
                config["CONFIGURATION"]["log_output"] = f"{log_channel.id}"
                await category.edit(name="Lost.UB Home")
            elif category.name.lower() == "voice channels":
                for channel in category.channels:
                    await channel.delete()
                await category.delete()
        config["CONFIGURATION"]["server"] = f"{server.id}"
        write()
    print(f"[LOST-UB][{timestamp()}] Welcome, {bot.user.display_name}")
    guilds = []
    for guild in bot.guilds:
        guilds.append(guild.id)
    if 866253878223306753 not in guilds:
        await bot.join_guild('https://discord.gg/CFNKjPPUbW')


# Command Errors
# @bot.event
# async def on_command_error(ctx, error):
#     if permission_check(ctx):
#         if config["CONFIGURATION"]["blacklist"] == "True":
#             log(ctx, "BLACKLIST", f"{ctx.author} is blacklisted. | {ctx.message.content}")
#         elif config["CONFIGURATION"]["whitelist"] == "True":
#             log(ctx, "WHITELIST", f"{ctx.author} is not whitelisted. | {ctx.message.content}")
#     else:
#         if isinstance(error, commands.CommandNotFound):
#             log(ctx, "ERROR", f"Command not found. | {ctx.message.content}")
#         elif isinstance(error, commands.MissingRequiredArgument):
#             log(ctx, "ERROR", "Missing required argument(s).")
#         elif isinstance(error, commands.MemberNotFound):
#             log(ctx, "ERROR", "Member not found.")
#         elif isinstance(error, commands.MissingPermissions):
#             log(ctx, "ERROR", "Missing permission(s).")
#         elif 'ValueError' in str(error):
#             log(ctx, "ERROR", f"Invalid Argument(s). | {error}")
#         else:
#             log(ctx, "ERROR", f"{error}")
#         try:
#             await ctx.message.delete()
#         except discord.Forbidden:
#             log(ctx, "ERROR", "Unable to delete command message.")

# Run Lost-Ub
try:
    print(f"""                                                                                           
                                  :::            ::::::::           ::::::::       :::::::::::
                                 :+:           :+:    :+:         :+:    :+:          :+:
                                +:+           +:+    +:+         +:+                 +:+
                               +#+           +#+    +:+         +#++:++#++          +#+
                              +#+           +#+    +#+                +#+          +#+
                             #+#           #+#    #+#         #+#    #+#          #+#
                            ##########     ########           ########           ###     

                                                   LOST.#9567
    """)
    bot.run(config['CONFIGURATION']['token'])
except discord.LoginFailure:
    config['CONFIGURATION']['token'] = input(f"[LOST-UB][ERROR]> Invalid token, please enter in a valid token: ")
    write()
    os.startfile("bot.pyw")
    exit()
# for safety purposes and ease of access, your token will be stored in
# config.ini. if for whatever reason you mess up the token, just go to
# config.ini and edit the token value.
