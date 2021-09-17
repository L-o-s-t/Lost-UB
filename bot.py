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

try:
    from git import Repo
except ModuleNotFoundError:
    process = subprocess.Popen("py -m pip install GitPython",
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)
    process.wait()
    from git import Repo
try:
    import pypresence
except ModuleNotFoundError:
    print("[LOST-UB] PyPresence is not found, installing package...")
    process = subprocess.Popen("py -m pip install pypresence",
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)
    process.wait()
    print("[LOST-UB] Finished installing PyPresence")
    import pypresence
try:
    from colorama import Fore, Back, Style, init

    init(convert=True)
except ModuleNotFoundError:
    print("[LOST-UB] Colorama is not found, installing package...")
    process = subprocess.Popen("py -m pip install colorama",
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.STDOUT)
    process.wait()
    print("[LOST-UB] Finished installing Colorama")
    from colorama import Fore, Back, Style, init

    init(convert=True)

if os.path.exists("repo"):
    process = subprocess.run("echo y | rmdir /s repo",
                             shell=True,
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.STDOUT)

# Functions & Setters ==================================================================================================

os.system("title " + "Lost.")

config = configparser.ConfigParser()

games = 3
fun = 13
tools = 8
admin = 4


def write():
    config.write(open('config.ini', 'w'))


def get_prefix():
    return config["CONFIGURATION"]["prefix"]


def test(ctx):
    return print(f"{ctx.author}: {ctx.content}")


def blacklist_check(ctx):
    if config['CONFIGURATION']['blacklist'] == "True":
        with open("data/blacklist.txt", "r") as file:
            content = file.read().split("\n")
            if f"{ctx.author.id}" in content:
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


def embedcolor():
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


def log(context, command_name, message: str = None):
    if context.guild is None:
        context.guild = "dms"
    if message is None:
        if command_name.lower() == "error" or command_name.lower() == "blacklist":
            string = f"{Fore.LIGHTBLUE_EX}[LOST-UB]" \
                     f"{Fore.LIGHTCYAN_EX}[{f'{context.guild}'.upper()}]" \
                     f"[{f'{context.author}'.upper()}]" \
                     f"{Fore.LIGHTRED_EX}[{command_name}]{Fore.LIGHTWHITE_EX}> " \
                     f"{context.message.content}"
        else:
            string = f"{Fore.LIGHTBLUE_EX}[LOST-UB]" \
                     f"{Fore.LIGHTCYAN_EX}[{f'{context.guild}'.upper()}]" \
                     f"[{f'{context.author}'.upper()}]" \
                     f"{Fore.LIGHTGREEN_EX}[{command_name}]{Fore.LIGHTWHITE_EX}> " \
                     f"{context.message.content}"
    else:
        if command_name.lower() == "error" or command_name.lower() == "blacklist":
            string = f"{Fore.LIGHTBLUE_EX}[LOST-UB]" \
                     f"{Fore.LIGHTCYAN_EX}[{f'{context.guild}'.upper()}]" \
                     f"[{f'{context.author}'.upper()}]" \
                     f"{Fore.LIGHTRED_EX}[{command_name}]{Fore.LIGHTWHITE_EX}> " \
                     f"{message}"
        else:
            string = f"{Fore.LIGHTBLUE_EX}[LOST-UB]" \
                     f"{Fore.LIGHTCYAN_EX}[{f'{context.guild}'.upper()}]" \
                     f"[{f'{context.author}'.upper()}]" \
                     f"{Fore.LIGHTGREEN_EX}[{command_name}]{Fore.LIGHTWHITE_EX}> " \
                     f"{message}"
    return print(string)


# Checks ===============================================================================================================

if not os.path.exists('config.ini'):
    print(f"""{Fore.LIGHTBLUE_EX}{Style.BRIGHT}                                                                                            
                                  :::            ::::::::           ::::::::       :::::::::::
                                 :+:           :+:    :+:         :+:    :+:          :+:
                                +:+           +:+    +:+         +:+                 +:+
                               +#+           +#+    +:+         +#++:++#++          +#+
                              +#+           +#+    +#+                +#+          +#+
                             #+#           #+#    #+#         #+#    #+#          #+#
                            ##########     ########           ########           ###     

                                                   LOST.#0404
    """)
    config['CONFIGURATION'] = {
        "token": f"{input(f'{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} Please enter in your token: ')}",
        "prefix": f"{input(f'{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} Please enter in your prefix: ')}",
        "AFK": "False",
        "afk_msg": "I'm afk",
        "afk_legit": "True",
        "silentsteal": "False",
        "silentsave": "False",
        "embedcolor": "light blue",
        "blacklist": "False",
        "rich_presence": "True",
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
        config["CONFIGURATION"]["token"] = input("{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} "
                                                 "Token not found, please enter in your token: ")
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
    if not config.has_option("CONFIGURATION", "rich_presence"):
        config["CONFIGURATION"]["rich_presence"] = "True"
        write()
    if not config.has_option("CONFIGURATION", "automock"):
        config["CONFIGURATION"]["automock"] = "False"
        write()

if not os.path.exists('data'):
    os.mkdir('data')
if not os.path.exists('data/avatars'):
    os.mkdir('data/avatars')
if not os.path.exists('data/blacklist.txt'):
    open('data/blacklist.txt', 'a+')
if not os.path.exists('data/automock.txt'):
    open('data/automock.txt', 'a+')

# Bot ==================================================================================================================

bot = commands.Bot(command_prefix=f"{config['CONFIGURATION']['prefix']}", help_command=None, user_bot=True,
                   guild_subscriptions=False, case_insensitive=True, chunk_guilds_at_startup=False)

try:
    os.system("cls")
    print(f"""{Fore.LIGHTBLUE_EX}{Style.BRIGHT}                                                                                            
                                      :::            ::::::::           ::::::::       :::::::::::
                                     :+:           :+:    :+:         :+:    :+:          :+:
                                    +:+           +:+    +:+         +:+                 +:+
                                   +#+           +#+    +:+         +#++:++#++          +#+
                                  +#+           +#+    +#+                +#+          +#+
                                 #+#           #+#    #+#         #+#    #+#          #+#
                                ##########     ########           ########           ###     

                                                       LOST.#0404
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
        'commands.space'
    ]
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            successful = False
            folder, command = extension.split(".")
            print(f"{Fore.LIGHTBLUE_EX}[LOST-UB]{Fore.LIGHTRED_EX}[ERROR]> "
                  f"{Fore.LIGHTWHITE_EX}Lost-Ub was unable to load {command} properly.")
            pass
    if successful is False:
        input(f"{Fore.LIGHTBLUE_EX}[LOST-UB]{Fore.LIGHTRED_EX}[ERROR]> {Fore.LIGHTWHITE_EX}"
              f"These commands weren't loaded correctly.\n"
              f"{Fore.LIGHTBLUE_EX}[LOST-UB]{Fore.LIGHTRED_EX}[ERROR]> {Fore.LIGHTWHITE_EX}"
              f"An update may fix this. Press enter to continue...")
        os.system("cls")
except ModuleNotFoundError:
    input(f"{Fore.LIGHTBLUE_EX}[LOST-UB]{Fore.LIGHTRED_EX}[ERROR]> "
          f"{Fore.LIGHTWHITE_EX}Lost-Ub was unable to load commands properly, restart and check for updates.")
    exit()

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
    print(f"{Fore.LIGHTBLUE_EX}[LOST-UB][{timestamp()}]{Fore.LIGHTWHITE_EX} Welcome, {bot.user.display_name}")
    guilds = []
    for guild in bot.guilds:
        guilds.append(guild.id)
    if 866253878223306753 not in guilds:
        await bot.join_guild('https://discord.gg/CFNKjPPUbW')


# Command Errors
@bot.event
async def on_command_error(ctx, error):
    if blacklist_check(ctx):
        return
    else:
        if isinstance(error, commands.CommandNotFound):
            log(ctx, "ERROR", f"Command not found. | {ctx.message.content}")
        elif isinstance(error, commands.MissingRequiredArgument):
            log(ctx, "ERROR", "Missing required argument(s).")
        elif isinstance(error, commands.MemberNotFound):
            log(ctx, "ERROR", "Member not found.")
        elif isinstance(error, commands.MissingPermissions):
            log(ctx, "ERROR", "Missing permission(s).")
        elif 'ValueError' in str(error):
            log(ctx, "ERROR", f"Invalid Argument(s). | {error}")
        else:
            log(ctx, "ERROR", f"{error}")
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            log(ctx, "ERROR", "Unable to delete command message.")

while True:
    os.system("cls")
    print(f"""{Fore.LIGHTBLUE_EX}{Style.BRIGHT}                                                                                            
                                  :::            ::::::::           ::::::::       :::::::::::
                                 :+:           :+:    :+:         :+:    :+:          :+:
                                +:+           +:+    +:+         +:+                 +:+
                               +#+           +#+    +:+         +#++:++#++          +#+
                              +#+           +#+    +#+                +#+          +#+
                             #+#           #+#    #+#         #+#    #+#          #+#
                            ##########     ########           ########           ###     

                                                   LOST.#0404
        """)
    update_prompt = input(f"{Fore.LIGHTBLUE_EX}[LOST-UB]> {Fore.LIGHTWHITE_EX}"
                          f"Would you like to check for updates? [yes/no]: ")
    if update_prompt.lower() == "yes" or update_prompt.lower() == "y":
        os.system('cls')
        print(f"""{Fore.BLUE}{Style.BRIGHT}                                                                                            
                                  :::            ::::::::           ::::::::       :::::::::::
                                 :+:           :+:    :+:         :+:    :+:          :+:
                                +:+           +:+    +:+         +:+                 +:+
                               +#+           +#+    +:+         +#++:++#++          +#+
                              +#+           +#+    +#+                +#+          +#+
                             #+#           #+#    #+#         #+#    #+#          #+#
                            ##########     ########           ########           ###     

                                                   LOST.#0404
        """)
        print(f"{Fore.LIGHTBLUE_EX}[LOST-UB]> {Fore.LIGHTWHITE_EX}Checking for updates...")

        Repo.clone_from("https://github.com/L-o-s-t/Lost-UB", "repo/").index.remove(['.github'],
                                                                                    True, r=True)

        # Checks if README.md exists, if not it will create it
        if not os.path.exists("README.md"):
            print(f"{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} Readme.md not found, creating new one...")
            os.replace("repo/README.md", "README.md")

        # Checks if commands.md exists, if not then it will create it.
        if not os.path.exists("commands.md"):
            print(f"{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} Commands.md not found, creating new one...")
            os.replace("repo/commands.md", "commands.md")

        # Checks if bot.py exists, if not it will create it
        with open("repo/bot.py", "r", encoding="utf8") as new:
            newbot = new.read()
        with open("bot.py", "r", encoding="utf8") as old:
            oldbot = old.read()
        if newbot != oldbot:
            while True:
                action = input(
                    f"{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} An update that requires a restart has "
                    f"been found, would you like to update? [yes/no]: ")
                if action.lower() == "yes" or action.lower() == "y":
                    with open("bot.py", "w+", encoding="utf8") as mainfile:
                        mainfile.write(newbot)
                    input(f'{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} '
                          f'Successfully updated. Press enter to restart the program.')
                    os.startfile('bot.py')
                    exit()
                elif action.lower() == "no" or action.lower() == "n":
                    print(f"{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} Checking for updates in commands...")
                    break
                else:
                    continue

        elif newbot == oldbot:
            print(f"{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} Main file is up to date...")

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
                        else:
                            continue
            else:
                shutil.copy(f"repo/commands/{cmd}", f"commands/{cmd}")
                new_cmds += 1

        if new_cmds == 0:
            add_msg = "No new commands were found."
        elif new_cmds == 1:
            add_msg = "Added 1 new command."
        else:
            add_msg = f"Added {new_cmds} commands."

        if updated_cmds == 0:
            update_msg = "No commands were updated."
        elif updated_cmds == 1:
            update_msg = "Updated 1 command."
        else:
            update_msg = f"Updated {new_cmds} commands."

        if updated_cmds > 0 or new_cmds > 0:
            input(f"{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} {update_msg}\n"
                  f"{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} {add_msg}\n"
                  f"{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} "
                  f"Finished! A restart will be needed for changes to work. Press enter to restart...")
            os.startfile("bot.py")
            exit()
        else:
            input(f"{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} {update_msg}\n"
                  f"{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} {add_msg}\n"
                  f"{Fore.LIGHTBLUE_EX}[LOST-UB]>{Fore.LIGHTWHITE_EX} Finished! Press enter to continue...")

        process = subprocess.run("echo y | rmdir /s repo",
                                 shell=True,
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.STDOUT)
        break
    elif update_prompt.lower() == "no" or update_prompt.lower() == "n":
        break
    else:
        os.system("cls")
        continue

# Run Lost-Ub
try:
    os.system('cls')
    print(f"""{Fore.BLUE}{Style.BRIGHT}                                                                                            
                                  :::            ::::::::           ::::::::       :::::::::::
                                 :+:           :+:    :+:         :+:    :+:          :+:
                                +:+           +:+    +:+         +:+                 +:+
                               +#+           +#+    +:+         +#++:++#++          +#+
                              +#+           +#+    +#+                +#+          +#+
                             #+#           #+#    #+#         #+#    #+#          #+#
                            ##########     ########           ########           ###     

                                                   LOST.#0404
""")
    bot.run(config['CONFIGURATION']['token'])
except discord.LoginFailure:
    config['CONFIGURATION']['token'] = input(f"{Fore.LIGHTBLUE_EX}[LOST-UB]"
                                             f"{Fore.LIGHTRED_EX}[ERROR] "
                                             f"{Fore.LIGHTWHITE_EX}> Invalid token, please enter in a valid token: ")
    write()
    os.startfile("bot.py")
    exit()
# for safety purposes and ease of access, your token will be stored in
# config.ini. if for whatever reason you mess up the token, just go to
# config.ini and edit the token value.
