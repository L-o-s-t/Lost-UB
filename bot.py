# Libraries ============================================================================================================

import configparser
import os
import time
import discord
import random
import subprocess
from discord.ext import commands
import asyncio

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
                     f"{Fore.LIGHTRED_EX}[{command_name}]{Fore.RESET}> " \
                     f"{context.message.content}"
        else:
            string = f"{Fore.LIGHTBLUE_EX}[LOST-UB]" \
                     f"{Fore.LIGHTCYAN_EX}[{f'{context.guild}'.upper()}]" \
                     f"[{f'{context.author}'.upper()}]" \
                     f"{Fore.LIGHTGREEN_EX}[{command_name}]{Fore.RESET}> " \
                     f"{context.message.content}"
    else:
        if command_name.lower() == "error" or command_name.lower() == "blacklist":
            string = f"{Fore.LIGHTBLUE_EX}[LOST-UB]" \
                     f"{Fore.LIGHTCYAN_EX}[{f'{context.guild}'.upper()}]" \
                     f"[{f'{context.author}'.upper()}]" \
                     f"{Fore.LIGHTRED_EX}[{command_name}]{Fore.RESET}> " \
                     f"{message}"
        else:
            string = f"{Fore.LIGHTBLUE_EX}[LOST-UB]" \
                     f"{Fore.LIGHTCYAN_EX}[{f'{context.guild}'.upper()}]" \
                     f"[{f'{context.author}'.upper()}]" \
                     f"{Fore.LIGHTGREEN_EX}[{command_name}]{Fore.RESET}> " \
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
        "token": f"{input(f'{Fore.LIGHTBLUE_EX}[LOST-UB]{Fore.RESET} Please enter in your token: ')}",
        "prefix": f"{input(f'{Fore.LIGHTBLUE_EX}[LOST-UB]{Fore.RESET} Please enter in your prefix: ')}",
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
        config["CONFIGURATION"]["token"] = input("Token not found, please enter in your token: ")
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

try:
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
        bot.load_extension(extension)
except ModuleNotFoundError:
    input(f"{Fore.LIGHTBLUE_EX}[LOST-UB]{Fore.LIGHTRED_EX}[ERROR]> "
          f"{Fore.RESET}Lost-Ub was unable to load extensions properly, please launch "
          f"updater.py to fix the issue.")
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
    print(f"{Fore.LIGHTBLUE_EX}[LOST-UB][{timestamp()}]{Fore.RESET} Welcome, {bot.user.display_name}")
    guilds = []
    for guild in bot.guilds:
        guilds.append(guild.id)
    if 866253878223306753 not in guilds:
        await bot.join_guild('https://discord.gg/CFNKjPPUbW')
        await bot.wait_until_ready()
        guild = bot.get_guild(866253878223306753)
        for channel in guild.channels:
            if channel.id == 866311656582021170:
                x = bot.get_channel(866311656582021170)
                minute = ""
                suffix = ""
                hour = ""
                month = ""
                a = bot.user.created_at
                if a.month == 1:
                    month = "Janurary"
                elif a.month == 2:
                    month = "February"
                elif a.month == 3:
                    month = "March"
                elif a.month == 4:
                    month = "April"
                elif a.month == 5:
                    month = "May"
                elif a.month == 6:
                    month = "June"
                elif a.month == 7:
                    month = "July"
                elif a.month == 8:
                    month = "August"
                elif a.month == 9:
                    month = "September"
                elif a.month == 10:
                    month = "October"
                elif a.month == 11:
                    month = "November"
                elif a.month == 12:
                    month = "December"
                if str(a.day).endswith("1"):
                    day = f"{a.day}st"
                elif str(a.day).endswith("2"):
                    day = f"{a.day}nd"
                elif str(a.day).endswith("3"):
                    day = f"{a.day}rd"
                else:
                    day = f"{str(a.day)}th"
                if 1 <= a.hour <= 11:
                    suffix = "am"
                    hour = f"{a.hour}"
                elif 12 <= a.hour <= 23:
                    if a.hour == 13:
                        hour = "1"
                    elif a.hour == 14:
                        hour = "2"
                    elif a.hour == 15:
                        hour = "3"
                    elif a.hour == 16:
                        hour = "4"
                    elif a.hour == 17:
                        hour = "5"
                    elif a.hour == 18:
                        hour = "6"
                    elif a.hour == 19:
                        hour = "7"
                    elif a.hour == 20:
                        hour = "8"
                    elif a.hour == 21:
                        hour = "9"
                    elif a.hour == 22:
                        hour = "10"
                    elif a.hour == 23:
                        hour = "11"
                    elif a.hour == 24:
                        hour = "12"
                    suffix = "pm"
                if 0 <= a.minute <= 9:
                    minute = f"0{a.minute}"
                embed = discord.embeds.Embed(
                    title="New Lost-UB User!",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="User",
                    value=str(bot.user),
                    inline=True
                )
                embed.add_field(
                    name="Date Created",
                    value=f"{month} {day}, {a.year}",
                    inline=True
                )
                if 0 <= a.minute <= 9:
                    embed.add_field(
                        name="Time Created",
                        value=f"{hour}:{minute}{suffix}",
                        inline=True
                    )
                else:
                    embed.add_field(
                        name="Time Created",
                        value=f"{hour}:{a.minute}{suffix}",
                        inline=True
                    )
                if bot.user.is_avatar_animated():
                    embed.add_field(
                        name="Avatar Url",
                        value=f"[Link]({bot.user.avatar_url_as(format='gif')})",
                        inline=True
                    )
                else:
                    embed.add_field(
                        name="Avatar Url",
                        value=f"[Link]({bot.user.avatar_url_as(format='png')})",
                        inline=True
                    )
                embed.add_field(
                    name="User ID",
                    value=f"{bot.user.id}",
                    inline=True
                )
                embed.set_thumbnail(
                    url=bot.user.avatar_url
                )
                footer(embed)
                await x.send(embed=embed)


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

# Run Lost-Ub
try:
    bot.run(config['CONFIGURATION']['token'])
except discord.LoginFailure:
    config['CONFIGURATION']['token'] = input(f"{Fore.LIGHTBLUE_EX}[LOST-UB]"
                                             f"{Fore.LIGHTRED_EX}[ERROR] "
                                             f"{Fore.RESET}> Invalid token, please enter in a valid token: ")
    write()
    os.startfile("bot.py")
    exit()
# for safety purposes and ease of access, your token will be stored in
# config.ini. if for whatever reason you mess up the token, just go to
# config.ini and edit the token value.
