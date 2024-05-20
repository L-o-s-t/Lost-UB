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
from git import Repo
import winshell
import win32com.client

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


def codeblock_footer():
    return f"# Logged in as {bot.user.display_name} | Lost-UB"



def simple_codeblock(context, text, reply: bool = False):
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


def log(context, title: str = "Command Usage", description: str = None):
    if context.guild is None:
        context.guild = "Direct Messages"
    return f"[{title} - {description}][{context.guild}][{context.author}][{timestamp()}]"

# Checks ===============================================================================================================

if not os.path.exists('config.ini'):
    config['CONFIGURATION'] = {
        "token": "None",
        "prefix": "~>",
        "autoupdate": "True",
        "AFK": "False",
        "afk_msg": "I'm afk",
        "afk_legit": "True",
        "silentsteal": "False",
        "silentsave": "False",
        "blacklist": "False",
        "whitelist": "False",
        "automock": "False"
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
        config["CONFIGURATION"]["token"] = "None"
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
    if not config.has_option("CONFIGURATION", "blacklist"):
        config["CONFIGURATION"]["blacklist"] = "False"
        write()
    if not config.has_option("CONFIGURATION", "whitelist"):
        config["CONFIGURATION"]["whitelist"] = "False"
        write()
    if not config.has_option("CONFIGURATION", "automock"):
        config["CONFIGURATION"]["automock"] = "False"
        write()
    if not config.has_option("CONFIGURATION", "autoupdate"):
        config["CONFIGURATION"]["autoupdate"] = "True"
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
        'commands.server',
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
        print(f"[LOST-UB]> Checking for updates...")

        Repo.clone_from("https://github.com/L-o-s-t/Lost-UB", "repo/").index.remove(['.github'],
                                                                                    True, r=True)

        # Checks if README.md exists, if not it will create it
        if not os.path.exists("README.md"):
            print(f"[LOST-UB]> Readme.md not found, creating new one...")
            os.replace("repo/README.md", "README.md")

        if not os.path.exists("data/server_logo.png"):
            print(f"[LOST-UB]> Server_logo.png not found, creating new one...")
            os.replace("repo/data/server_logo.png", "data/server_logo.png")

        # Checks if commands.md exists, if not then it will create it.
        if not os.path.exists("commands.md"):
            print(f"[LOST-UB]> Commands.md not found, creating new one...")
            os.replace("repo/commands.md", "commands.md")

        # Checks if bot.pyw exists, if not it will create it
        with open("repo/bot.py", "r", encoding="utf8") as new:
            newbot = new.read()
        with open("bot.py", "r", encoding="utf8") as old:
            oldbot = old.read()
        if newbot != oldbot:
            require_restart = True
            with open("bot.py", "w+", encoding="utf8") as mainfile:
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
            try:
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
                    'commands.server',
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
        else:
            input(f"[LOST-UB]> No restarts required, press enter to continue...")
            break


# When bot connects
@bot.event
async def on_connect():
    print("connected.")

@bot.command(aliases=['quit'])
async def disconnect(ctx):
    if ctx.author == bot.user:
        log_channel = bot.get_channel(int(config["CONFIGURATION"]["log_output"]))
        message = f"```ini\n" \
                  f"[ Disconnected ]\n" \
                  f"Lost.ub successfully logged out.\n\n" \
                  f"[ User ]\n" \
                  f"{bot.user}\n\n" \
                  f"[ Time ]\n" \
                  f"{timestamp()}\n\n" \
                  f"{codeblock_footer()}\n" \
                  f"```"
        await log_channel.send(message)
        exit()


# Command Errors
@bot.event
async def on_command_error(ctx, error):
    if permission_check(ctx):
        if config["CONFIGURATION"]["blacklist"] == "True":
            print(log(ctx, title="BLACKLIST", description=f"{ctx.author} is blacklisted."))
        elif config["CONFIGURATION"]["whitelist"] == "True":
            print(log(ctx, title="WHITELIST", description=f"{ctx.author} is whitelisted."))
    else:
        if isinstance(error, commands.CommandNotFound):
            print(log(ctx, title="Command Error", description=f"Command not found."))
        elif isinstance(error, commands.MissingRequiredArgument):
            print(log(ctx, title="Command Error", description=f"Missing required argument(s)."))
        elif isinstance(error, commands.MemberNotFound):
            print(log(ctx, title="Command Error", description=f"Member not found."))
        elif isinstance(error, commands.MissingPermissions):
            print(log(ctx, title="Command Error", description=f"Missing permission(s)."))
        elif 'ValueError' in str(error):
            print(log(ctx, title="Command Error", description=f"Invalid Argument(s). | {error}"))
        else:
            print(log(ctx, title="Command Error", description=f"Error: {error}"))
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            print(log(ctx, title="Command Error", description=f"Unable to delete command message."))

# Run Lost-Ub
if config["CONFIGURATION"]["token"] == "None":
    token_input = input("The token you've provided returned an error, please enter in a valid token: ")
    config["CONFIGURATION"]["token"] = token_input
    write()
    os.startfile("bot.py")
    exit()
else:
    try:
        bot.run(config['CONFIGURATION']['token'])
    except discord.LoginFailure:
        token_input = input(f"[LOST-UB][ERROR]> Invalid token, please enter in a valid token: ")
        config["CONFIGURATION"]["token"] = token_input
        write()
        os.startfile("bot.py")
        exit()
