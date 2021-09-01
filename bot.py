import asyncio
import configparser
import os
import time
import discord
import random
import subprocess
from discord.ext import commands

print("""                                                                                                               
                                  :::            ::::::::           ::::::::       :::::::::::
                                 :+:           :+:    :+:         :+:    :+:          :+:
                                +:+           +:+    +:+         +:+                 +:+
                               +#+           +#+    +:+         +#++:++#++          +#+
                              +#+           +#+    +#+                +#+          +#+
                             #+#           #+#    #+#         #+#    #+#          #+#
                            ##########     ########           ########           ###     
                                 
################################################# LOST.#0404 ###########################################################
""")

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

os.system('cls')
print(f"""{Fore.BLUE}{Style.BRIGHT}                                                                                            
                                  :::            ::::::::           ::::::::       :::::::::::
                                 :+:           :+:    :+:         :+:    :+:          :+:
                                +:+           +:+    +:+         +:+                 +:+
                               +#+           +#+    +:+         +#++:++#++          +#+
                              +#+           +#+    +#+                +#+          +#+
                             #+#           #+#    #+#         #+#    #+#          #+#
                            ##########     ########           ########           ###     

{Fore.LIGHTBLUE_EX}
################################################# LOST.#0404 ###########################################################
""")

# Functions & Setters ==================================================================================================

config = configparser.ConfigParser()


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
        if command_name.lower() == "error":
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
        if command_name.lower() == "error":
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


games = 3
fun = 9
tools = 8
admin = 4

# Checks ===============================================================================================================


# Checks to see if "config.ini" exists, if not then it will create one.
if not os.path.exists('config.ini'):
    config['CONFIGURATION'] = {
        "logging": f"{input('Enable logs? (true/false): ')}",
        "token": f"{input(f'{Fore.LIGHTBLUE_EX}[LOST-UB]{Fore.RESET} Please enter in your token: ')}",
        "prefix": f"{input(f'{Fore.LIGHTBLUE_EX}[LOST-UB]{Fore.RESET} Please enter in your prefix: ')}",
        "AFK": "False",
        "afk_msg": "I'm afk",
        "afk_legit": "True",
        "silentsteal": "False",
        "silentsave": "False",
        "embedcolor": "light blue",
        "blacklist": "False",
        "rich_presence": "True"
    }
    write()
    while True:
        if config['CONFIGURATION']['logging'].lower() != "true" and \
                config['CONFIGURATION']['logging'].lower() != "false":
            config['CONFIGURATION']['logging'] = input("Enable logs? Yes or No?: ")
        elif config['CONFIGURATION']['logging'].lower() == "true":
            break
        elif config['CONFIGURATION']['logging'].lower() == "false":
            break
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
    if not config.has_option("CONFIGURATION", "logging"):
        config["CONFIGURATION"]["logging"] = "True"
        write()
    elif config["CONFIGURATION"]["logging"] != "True" or config["CONFIGURATION"]["logging"] != "False":
        config["CONFIGURATION"]["logging"] = "True"
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

if not os.path.exists('data'):
    os.mkdir('data')
if not os.path.exists('data/avatars'):
    os.mkdir('data/avatars')
if not os.path.exists('data/blacklist.txt'):
    open('data/blacklist.txt', 'a+')


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


bot = commands.Bot(command_prefix=f"{config['CONFIGURATION']['prefix']}", help_command=None, user_bot=True,
                   guild_subscriptions=False, case_insensitive=True, chunk_guilds_at_startup=False)

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
    print(f"{Fore.LIGHTBLUE_EX}[LOST-UB][{timestamp()}]{Fore.RESET} Welcome, {bot.user.display_name}.")
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


# Help =================================================================================================================


@bot.command(aliases=['help'])
async def info(ctx, module: str = None):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        log(ctx, "HELP")
        if module is None:
            try:
                embed = discord.embeds.Embed(
                    title="Command Categories\n",
                    description=f"Choose a category\n"
                                f"Command usage: {get_prefix()}help [category]",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Games",
                    value=f"Total Commands: {games}",
                    inline=True
                )
                embed.add_field(
                    name="Fun",
                    value=f"Total Commands: {fun}",
                    inline=True
                )
                embed.add_field(
                    name="Tools",
                    value=f"Total Commands: {tools}",
                    inline=True
                )
                embed.add_field(
                    name="Admin",
                    value=f"Total Commands: {admin}",
                    inline=True
                )
                embed.set_thumbnail(
                    url="https://i.ibb.co/6PGdDFg/Logo2.png"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await ctx.reply(f"```ini\n"
                                f"[Command Categories]\n"
                                f"Choose a category\n"
                                f"Command usage: {get_prefix()}help [category]\n\n"
                                f"[ Games ]\n"
                                f"Total Commands: {games}\n\n"
                                f"[ Fun ]\n"
                                f"Total Commands: {fun}\n\n"
                                f"[ Tools ]\n"
                                f"Total Commands: {tools}\n\n"
                                f"[ Admin ]\n"
                                f"Total Commands: {admin}\n\n"
                                f"{codeblock_footer()}"
                                f"```")
        elif module.lower() == "games" or module.lower() == "game":
            try:
                embed = discord.embeds.Embed(
                    title="Game Commands",
                    description=f"Your prefix is: ``{get_prefix()}``\n"
                                f"**[]** = required, **()** = optional.",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Games",
                    value=f"**Rock, Paper, Scissors** | {get_prefix()}rps\n"
                          f"**Battle** | {get_prefix()}battle\n"
                          f"**Fight**  | {get_prefix()}fight [@member]",
                    inline=True
                )
                embed.set_thumbnail(
                    url="https://i.ibb.co/6PGdDFg/Logo2.png"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await ctx.reply(f"```ini\n"
                                f"[ Game Commands ]\n"
                                f"Your prefix is: {get_prefix()}\n"
                                f"[] = required, () = optional.\n\n"
                                f"[ Games ]\n"
                                f"Rock, Paper, Scissors | {get_prefix()}rps\n"
                                f"Battle | {get_prefix()}battle\n"
                                f"Fight  | {get_prefix()}fight [@member]\n\n"
                                f"{codeblock_footer()}"
                                f"```")
        elif module.lower() == "fun":
            try:
                embed = discord.embeds.Embed(
                    title="Fun Commands",
                    description=f"Your prefix is: ``{get_prefix()}``\n"
                                f"**[]** = required, **()** = optional.",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Fun",
                    value=f"**DickSize**      | {get_prefix()}dicksize [@member]\n"
                          f"**FlipCoin**      | {get_prefix()}flipcoin\n"
                          f"**8Ball**         | {get_prefix()}8ball [question]\n"
                          f"**GhostPing**     | {get_prefix()}ghostping [@member]\n"
                          f"**GhostPingAll**  | {get_prefix()}ghostpingall [@member]\n"
                          f"**IQ Rating**     | {get_prefix()}iq [@member]\n"
                          f"**Dice Roll**     | {get_prefix()}rolladice\n"
                          f"**Spam**          | {get_prefix()}spam [delay] [count] [message]\n"
                          f"**SpamAll**       | {get_prefix()}spamall [message]",
                    inline=True

                )
                embed.set_thumbnail(
                    url="https://i.ibb.co/6PGdDFg/Logo2.png"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await ctx.reply(f"```ini\n"
                                f"[ Fun Commands ]\n"
                                f"Your prefix is: {get_prefix()}\n"
                                f"[] = required, () = optional.\n\n"
                                f"[ Fun ]\n"
                                f"DickSize      | {get_prefix()}dicksize [@member]\n"
                                f"FlipCoin      | {get_prefix()}flipcoin\n"
                                f"8Ball         | {get_prefix()}8ball [question]\n"
                                f"GhostPing     | {get_prefix()}ghostping [@member]\n"
                                f"GhostPingAll  | {get_prefix()}ghostpingall [@member]\n"
                                f"IQ Rating     | {get_prefix()}iq [@member]\n"
                                f"Dice Roll     | {get_prefix()}rolladice\n"
                                f"Spam          | {get_prefix()}spam [delay] [count] [message]\n"
                                f"SpamAll       | {get_prefix()}spamall [message]\n\n"
                                f"{codeblock_footer()}"
                                f"```")
        elif module.lower() == "tools" or module.lower() == "tool":
            try:
                embed = discord.embeds.Embed(
                    title="Tools Commands",
                    description=f"Your prefix is: ``{get_prefix()}``\n"
                                f"**[]** = required, **()** = optional.",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Tools",
                    value=f"**StealPFP**   | {get_prefix()}stealpfp [@member]\n"
                          f"**SavePFP**    | {get_prefix()}savepfp [@member]\n"
                          f"**PFP**        | {get_prefix()}pfp [@member]\n"
                          f"**AFK**        | {get_prefix()}afk\n"
                          f"**ServerInfo** | {get_prefix()}serverinfo\n"
                          f"**ServerIcon** | {get_prefix()}servericon\n"
                          f"**UserInfo**   | {get_prefix()}userinfo [@member]\n"
                          f"**Calculate**  | {get_prefix()}calculate [number] [operator] [number]\n"
                          f"**SendEmbed**  | {get_prefix()}sendembed [title] | [description]\n"
                          f"**Poll**       | {get_prefix()}poll\n"
                          f"**Blacklist**  | {get_prefix()}blacklist (add/remove) (@member)\n",
                    inline=True
                )
                embed.set_thumbnail(
                    url="https://i.ibb.co/6PGdDFg/Logo2.png"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await ctx.reply(f"```ini\n"
                                f"[ Tools Commands ]\n"
                                f"Your prefix is: {get_prefix()}\n"
                                f"[] = required, () = optional.\n\n"
                                f"[ Tools ]\n"
                                f"StealPFP   | {get_prefix()}stealpfp [@member]\n"
                                f"SavePFP    | {get_prefix()}savepfp [@member]\n"
                                f"PFP        | {get_prefix()}pfp [@member]\n"
                                f"AFK        | {get_prefix()}afk\n"
                                f"ServerInfo | {get_prefix()}serverinfo\n"
                                f"ServerIcon | {get_prefix()}servericon\n"
                                f"UserInfo   | {get_prefix()}userinfo [@member]\n"
                                f"Calculate  | {get_prefix()}calculate [number] [operator] [number]\n\n"
                                f"{codeblock_footer()}"
                                f"```")
        elif module.lower() == "admin":
            try:
                embed = discord.embeds.Embed(
                    title="Admin Commands",
                    description=f"Your prefix is: ``{get_prefix()}``\n"
                                f"**[]** = required, **()** = optional.",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Admin",
                    value=f"**Kick**   | {get_prefix()}stealpfp [@member]\n"
                          f"**Ban**    | {get_prefix()}savepfp [@member]\n"
                          f"**Warn**        | {get_prefix()}pfp [@member]\n"
                          f"**Warnings**        | {get_prefix()}afk",
                    inline=True
                )
                embed.set_thumbnail(
                    url="https://i.ibb.co/6PGdDFg/Logo2.png"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await ctx.reply(f"```ini\n"
                                f"[ Admin Commands ]\n"
                                f"Your prefix is: {get_prefix()}\n"
                                f"[] = required, () = optional.\n\n"
                                f"[ Admin ]\n"
                                f"Kick   | {get_prefix()}stealpfp [@member]\n"
                                f"Ban    | {get_prefix()}savepfp [@member]\n"
                                f"Warn        | {get_prefix()}pfp [@member]\n"
                                f"Warnings        | {get_prefix()}afk\n\n"
                                f"{codeblock_footer()}"
                                f"```")
        else:
            try:
                embed = discord.embeds.Embed(
                    title="Category Not Found",
                    description=f"Your prefix is: ``{get_prefix()}``\n",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Categories",
                    value=f"- Games\n"
                          f"- Fun\n"
                          f"- Tools\n"
                          f"- Admin",
                    inline=True
                )
                embed.set_thumbnail(
                    url="https://i.ibb.co/6PGdDFg/Logo2.png"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await ctx.reply(f"```ini\n"
                                f"[ Category Not Found ]\n"
                                f"Your prefix is: {get_prefix()}\n\n"
                                f"[ Categories ]\n"
                                f"- Games\n"
                                f"- Fun\n"
                                f"- Tools\n"
                                f"- Admin\n\n"
                                f"{codeblock_footer()} | Server Code: CFNKjPPUbW\n"
                                f"```")


# Rock, paper, scissors ================================================================================================


@bot.command()
async def rps(ctx):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        log(ctx, "RPS")
        try:
            embed = discord.embeds.Embed(
                title="Rock, Paper, Scissors Game",
                description="What is your choice?",
                colour=embedcolor()
            )
            embed.add_field(
                name="Choices",
                value="Rock, Paper, Scissors"
            )
            embed.set_footer(
                text=f"Logged in as {bot.user} | Lost-UB",
                icon_url=bot.user.avatar_url
            )
            await ctx.reply(embed=embed)

            def check(m):
                return m.author == ctx.author

            try:
                rps_choice = random.choice(['rock', 'paper', 'scissors'])
                answer = await bot.wait_for("message", check=check, timeout=60.0)
                result = ""
                if answer.content.lower() == "rock":
                    if rps_choice == "rock":
                        result = "It's a tie!"
                    elif rps_choice == "paper":
                        result = "You lost!"
                    elif rps_choice == "scissors":
                        result = "You won!"
                elif answer.content.lower() == "paper":
                    if rps_choice == "rock":
                        result = "You won!"
                    elif rps_choice == "paper":
                        result = "It's a tie!"
                    elif rps_choice == "scissors":
                        result = "You lost!"
                elif answer.content.lower() == "scissors":
                    if rps_choice == "rock":
                        result = "You lost!"
                    elif rps_choice == "paper":
                        result = "You won!"
                    elif rps_choice == "scissors":
                        result = "It's a tie!"
                else:
                    await answer.reply("Those weren't any of the choices!")
                    return
                embed = discord.embeds.Embed(
                    title="Rock Paper Scissors Game Results!",
                    description=f"{result}",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Your Choice",
                    value=f"{answer.content.lower()}"
                )
                embed.add_field(
                    name="CPU's Choice",
                    value=f"{rps_choice}"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except asyncio.TimeoutError:
                await ctx.reply("You took too long to respond!")
        except discord.Forbidden:
            await ctx.reply(f"```ini\n"
                            f"[ Rock, Paper, Scissors Game]\n"
                            f"What is your choice?\n\n"
                            f"[ Choices ]\n"
                            f"Rock\n"
                            f"Paper\n"
                            f"Scissors\n\n"
                            f"{codeblock_footer()}"
                            f"```")

            def check(m):
                return m.author == ctx.author

            try:
                rps_choice = random.choice(['rock', 'paper', 'scissors'])
                answer = await bot.wait_for("message", check=check, timeout=60.0)
                result = ""
                if answer.content.lower() == "rock":
                    if rps_choice == "rock":
                        result = "It's a tie!"
                    elif rps_choice == "paper":
                        result = "You lost!"
                    elif rps_choice == "scissors":
                        result = "You won!"
                elif answer.content.lower() == "paper":
                    if rps_choice == "rock":
                        result = "You won!"
                    elif rps_choice == "paper":
                        result = "It's a tie!"
                    elif rps_choice == "scissors":
                        result = "You lost!"
                elif answer.content.lower() == "scissors":
                    if rps_choice == "rock":
                        result = "You lost!"
                    elif rps_choice == "paper":
                        result = "You won!"
                    elif rps_choice == "scissors":
                        result = "It's a tie!"
                else:
                    await answer.reply("Those weren't any of the choices!")
                    return
                await ctx.reply(f"```ini\n"
                                f"[ Rock, Paper, Scissors Game Results! ]\n"
                                f"{result}\n\n"
                                f"[ Your Choice ]\n"
                                f"{answer.content.lower()}\n\n"
                                f"[ CPU's Choice ]\n"
                                f"{rps_choice}\n\n"
                                f"{codeblock_footer()}"
                                f"```")
            except asyncio.TimeoutError:
                await ctx.reply("You took too long to respond!")


# Prefix ===============================================================================================================


@bot.command()
async def prefix(ctx, x):
    if ctx.author == bot.user:
        log(ctx, "PREFIX")
        config["CONFIGURATION"]["prefix"] = x
        write()
        bot.command_prefix = x
        await ctx.reply(f'Prefix changed to: ``{x}``')


# Dicksize =============================================================================================================


@bot.command()
async def dicksize(ctx, member: discord.Member):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        desc = ''
        log(ctx, "DICKSIZE")
        size = random.randrange(0, 12)
        if size >= 6:
            desc = "That's a schlong dong!"
        elif size < 6:
            desc = "so smol! 🥺"
        try:
            embed = discord.embeds.Embed(
                title=f"{member.display_name}'s Dick Size",
                description=desc,
                colour=embedcolor()
            )
            embed.add_field(
                name="Size",
                value=f"{size} inches"
            )
            embed.add_field(
                name="Demonstration",
                value=f"8{size * '='}D"
            )
            embed.set_footer(
                text=f"Logged in as {bot.user} | Lost-UB",
                icon_url=bot.user.avatar_url
            )
            await ctx.reply(embed=embed)
        except discord.Forbidden:
            await ctx.reply(f"```ini\n"
                            f"[ {member.display_name}'s Dick Size ]\n"
                            f"{desc}\n\n"
                            f"[ Size ]\n"
                            f"{size} inches\n\n"
                            f"[ Demonstration ]\n"
                            f"8{size * '='}D\n\n"
                            f"{codeblock_footer()}"
                            f"```")


# Flipcoin =============================================================================================================


@bot.command()
async def flipcoin(ctx):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        log(ctx, "FLIPCOIN")
        side = random.choice(['heads', 'tails'])
        await ctx.reply(f"it's {side}")


# 8ball ================================================================================================================


@bot.command(aliases=['8ball'])
async def eightball(ctx, *, question: str = None):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        log(ctx, "8BALL")
        if question is None:
            await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}8ball (question)')
        else:
            answers = random.choice(['It is Certain.',
                                     'It is decidedly so.',
                                     'Without a doubt.',
                                     'Yes definitely.',
                                     'You may rely on it.',
                                     'As I see it, yes.',
                                     'Most likely.',
                                     'Outlook good.',
                                     'Yes.',
                                     'Signs point to yes.',
                                     'Reply hazy, try again.',
                                     'Ask again later.',
                                     'Better not tell you now.',
                                     'Cannot predict now.',
                                     'Concentrate and ask again.',
                                     'Don\'t count on it.',
                                     'My reply is no.',
                                     'My sources say no.',
                                     'Outlook not so good.',
                                     'Very doubtful.'])
            try:
                embed = discord.embeds.Embed(
                    title="Eight Ball",
                    description=f"{question}",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Answer",
                    value=f"{answers}"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await ctx.reply(f"```ini\n"
                                f"[ Eight Ball ]\n"
                                f"{question}\n\n"
                                f"[ Answer ]\n"
                                f"{answers}\n\n"
                                f"{codeblock_footer()}"
                                f"```")


# Ghost Ping ===========================================================================================================


@bot.command()
async def ghostping(ctx, member: discord.Member):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        log(ctx, "GHOSTPING")
        msg = await ctx.send(f'{member}')
        await msg.delete()
        await ctx.message.delete()


# IQ Rating ============================================================================================================

@bot.command()
async def iq(ctx, member: discord.Member):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        log(ctx, "IQ")
        result = ""
        iq_rating = random.randrange(0, 199)
        if iq_rating <= 69:
            result = "Extremely Low"
        elif 70 <= iq_rating <= 79:
            result = "Borderline"
        elif 80 <= iq_rating <= 89:
            result = "Low Average"
        elif 90 <= iq_rating <= 109:
            result = "Average"
        elif 110 <= iq_rating <= 119:
            result = "High Average"
        elif 120 <= iq_rating <= 129:
            result = "Superior"
        elif iq_rating >= 130:
            result = "Very Superior"
        try:
            embed = discord.embeds.Embed(
                title=f"{member.display_name}'s IQ Rating",
                description=f"{member}'s IQ is {iq_rating}",
                colour=embedcolor()
            )
            embed.add_field(
                name="Rating",
                value=f"{result}"
            )
            embed.add_field(
                name="IQ Classification",
                value="130 and above: Very Superior\n"
                      "120 - 129:     Superior\n"
                      "110 - 119:     High Average\n"
                      "90 - 109:      Average\n"
                      "80 - 89:       Low Average\n"
                      "70 - 79:       Borderline\n"
                      "69 and below:  Extremely Low"
            )
            embed.set_footer(
                text=f"Logged in as {bot.user} | Lost-UB",
                icon_url=bot.user.avatar_url
            )
            await ctx.reply(embed=embed)
        except discord.Forbidden:
            await ctx.reply(f"```ini\n"
                            f"[ {member.display_name}'s IQ Rating ]\n"
                            f"{member.display_name}'s IQ is [ {iq_rating} ]\n\n"
                            f"[ IQ Classification ]\n"
                            "130 and above: Very Superior\n"
                            f"120 - 129:     Superior\n"
                            f"110 - 119:     High Average\n"
                            f"90 - 109:      Average\n"
                            f"80 - 89:       Low Average\n"
                            f"70 - 79:       Borderline\n"
                            f"69 and below:  Extremely Low\n\n"
                            f"{codeblock_footer()}"
                            f"```")


# AFK ==================================================================================================================


@bot.command()
async def afk(ctx):
    if ctx.author == bot.user:
        if config['CONFIGURATION']['logging'] == "True":
            print(f"[LOST-UB] afk command ran by {ctx.author.display_name}")
        if config["CONFIGURATION"]["AFK"] == "True":
            config["CONFIGURATION"]["AFK"] = "False"
            write()
            await ctx.reply("Successfully set! AFK has been turned off.")
        elif config["CONFIGURATION"]["AFK"] == "False":
            config["CONFIGURATION"]["AFK"] = "True"
            write()
            await ctx.reply("Successfully set! AFK has been turned on.")


@bot.event
async def on_message(ctx):
    if config["CONFIGURATION"]["AFK"] == "True":
        if f'<@{bot.user.id}>' in ctx.content or f'<@!{bot.user.id}>' in ctx.content:
            if config['CONFIGURATION']['afk_legit'] == "True":
                time.sleep(random.randrange(5, 10))
                async with ctx.channel.typing():
                    await asyncio.sleep(5)
            await ctx.reply(config["CONFIGURATION"]["afk_msg"])
    await bot.process_commands(ctx)


# Profile Picture ======================================================================================================

@bot.command()
async def stealpfp(ctx, member: discord.Member):
    if ctx.author == bot.user:
        if config['CONFIGURATION']['logging'] == "True":
            print(f"[LOST-UB] Stole {member.display_name}'s avatar")
        if config['CONFIGURATION']['silentsteal'] == "True":
            await ctx.message.delete()
        if member.is_avatar_animated():
            await member.avatar_url.save(f"data\\avatars\\{member.id}.gif")
            with open(f'data/avatars/{member.id}.gif', 'rb') as image:
                await bot.user.edit(avatar=image.read())
        else:
            await member.avatar_url.save(f"data\\avatars\\{member.id}.png")
            with open(f'data/avatars/{member.id}.png', 'rb') as image:
                await bot.user.edit(avatar=image.read())
        if config['CONFIGURATION']['silentsteal'] == "False":
            embed = discord.embeds.Embed(
                title="Avatar Stolen!",
                colour=embedcolor()
            )
            embed.add_field(
                name="User",
                value=member.display_name
            )
            embed.add_field(
                name="Avatar",
                value=f"[Link]({member.avatar_url})"
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(
                text=f"Logged in as {bot.user} | Lost-UB",
                icon_url=bot.user.avatar_url
            )
            await ctx.reply(embed=embed)


@bot.command()
async def pfp(ctx, member: discord.Member):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        if config['CONFIGURATION']['logging'] == "True":
            print(f"[LOST-UB] pfp command ran by {ctx.author.display_name}")
        embed = discord.embeds.Embed(
            title="Profile Picture",
            colour=embedcolor()
        )
        embed.add_field(
            name="Link",
            value=f"[Click Me]({member.avatar_url_as(format='jpg')})"
        )
        embed.add_field(
            name="User",
            value=f"{member.display_name}"
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(
            text=f"Logged in as {bot.user} | Lost-UB",
            icon_url=bot.user.avatar_url
        )
        await ctx.reply(embed=embed)


@bot.command()
async def savepfp(ctx, member: discord.Member):
    if ctx.author == bot.user:
        if config['CONFIGURATION']['logging'] == "True":
            print(f"[LOST-UB] {member.display_name}'s avatar was saved as {member.id}.png.")
        if config['CONFIGURATION']['silentsave'] == "True":
            await ctx.message.delete()
        if member.is_avatar_animated():
            await member.avatar_url.save(f"data\\avatars\\{member.id}.gif")
        else:
            await member.avatar_url.save(f"data\\avatars\\{member.id}.png")
        if config['CONFIGURATION']['silentsave'] == "False":
            embed = discord.embeds.Embed(
                title="Avatar Saved!",
                description=f"{member.display_name}'s avatar was saved.",
                colour=embedcolor()
            )
            embed.add_field(
                name="User",
                value=str(member)
            )
            embed.add_field(
                name="Avatar",
                value=f"[Link]({member.avatar_url})"
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(
                text=f"Logged in as {bot.user} | Lost-UB",
                icon_url=bot.user.avatar_url
            )
            await ctx.reply(embed=embed)


@savepfp.error
async def savepfp_error(ctx, error):
    if ctx.author == bot.user:
        if isinstance(error, commands.MemberNotFound):
            await ctx.reply("Member not found.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"Missing arguments | {get_prefix()}savepfp (@member)")


@pfp.error
async def pfp_error(ctx, error):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        if isinstance(error, commands.MemberNotFound):
            await ctx.reply("Member not found.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"Missing arguments | {get_prefix()}pfp (@member)")


# Settings =============================================================================================================


@bot.command()
async def settings(ctx, section: str = None, setting: str = None, *, value: str = None):
    def sections_embed(context):
        section_embed = discord.embeds.Embed(
            title="Settings",
            description=f"Command usage: {get_prefix()}settings (section) (setting) (value)",
            colour=embedcolor()
        )
        section_embed.add_field(
            name="Sections",
            value="- afk\n"
                  "- pfp\n"
                  "- customization\n"
                  "- configuration"
        )
        return context.reply(embed=section_embed)

    def settings_embed(context, setting_name, description):
        setting_desc_embed = discord.embeds.Embed(
            title=f"{setting_name} Setting",
            description=f"{description}",
            colour=embedcolor()
        )
        return context.reply(embed=setting_desc_embed)

    if config['CONFIGURATION']['logging'] == "True":
        print(f"[LOST-UB] settings command ran by {ctx.author.display_name}")
    if ctx.author == bot.user:
        if section is None:
            await sections_embed(ctx)
        elif section.lower() == "afk":
            if setting is None:
                embed = discord.embeds.Embed(
                    title="AFK Section",
                    description=f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Settings",
                    value=f"- legit | {config['CONFIGURATION']['afk_legit']}\n"
                          f"- message | {config['CONFIGURATION']['afk_msg']}"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            elif setting.lower() == "legit":
                if value is None:
                    await settings_embed(ctx, "Legit AFK", "Legit afk sends a typing indicator to make it seem like "
                                                           "you aren't user-botting.")
                elif value.lower() == "true":
                    config['CONFIGURATION']['afk_legit'] = "True"
                    write()
                    embed = discord.embeds.Embed(
                        title="AFK Legit Setting",
                        description=f"This has been turned on!",
                        colour=embedcolor()
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                elif value.lower() == "false":
                    config['CONFIGURATION']['afk_legit'] = "False"
                    write()
                    embed = discord.embeds.Embed(
                        title="AFK Legit Setting",
                        description=f"This has been turned off!",
                        colour=embedcolor()
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                else:
                    embed = discord.embeds.Embed(
                        title="AFK Legit Setting",
                        description=f"Value has to be ``True`` or ``False``!",
                        colour=embedcolor()
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
            elif setting.lower() == "message":
                if value is None:
                    await settings_embed(ctx, "AFK Message", "Set the message to send to users when AFK is enabled.")
                else:
                    config["CONFIGURATION"]["afk_msg"] = value
                    write()
                    await ctx.reply(f"AFK message has been set to: ``{value}``")
            else:
                embed = discord.embeds.Embed(
                    title="AFK Section",
                    description=f"Setting not found.\n"
                                f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Settings",
                    value=f"- legit | {config['CONFIGURATION']['afk_legit']}"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
        elif section.lower() == "pfp":
            if setting is None:
                embed = discord.embeds.Embed(
                    title="PFP Section",
                    description=f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Settings",
                    value=f"- silentsteal | {config['CONFIGURATION']['silentsteal']}\n"
                          f"- silentsave  | {config['CONFIGURATION']['silentsave']}"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            elif setting.lower() == "silentsteal":
                if value is None:
                    await settings_embed(ctx, "SilentSteal", "Doesn't send any messages after cmd and deletes command "
                                                             "message.")
                elif value.lower() == "true":
                    config['CONFIGURATION']['silentsteal'] = "True"
                    write()
                    embed = discord.embeds.Embed(
                        title="SilentSteal Setting",
                        description=f"This has been turned on!",
                        colour=embedcolor()
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                elif value.lower() == "false":
                    config['CONFIGURATION']['silentsteal'] = "False"
                    write()
                    embed = discord.embeds.Embed(
                        title="SilentSteal Setting",
                        description=f"This has been turned off!",
                        colour=embedcolor()
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                else:
                    embed = discord.embeds.Embed(
                        title="SilentSteal Setting",
                        description=f"Value has to be ``True`` or ``False``!",
                        colour=embedcolor()
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
            elif setting.lower() == "silentsave":
                if value is None:
                    embed = discord.embeds.Embed(
                        title="SilentSave Setting",
                        description=f"Doesn't send any messages after cmd and deletes command message.",
                        colour=embedcolor()
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                elif value.lower() == "true":
                    await settings_embed(ctx, "SilentSave", "Doesn't send any messages after cmd and deletes command "
                                                            "message.")
                elif value.lower() == "false":
                    config['CONFIGURATION']['silentsave'] = "False"
                    write()
                    embed = discord.embeds.Embed(
                        title="SilentSave Setting",
                        description=f"This has been turned off!",
                        colour=embedcolor()
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                else:
                    embed = discord.embeds.Embed(
                        title="SilentSave Setting",
                        description=f"Value has to be ``True`` or ``False``!",
                        colour=embedcolor()
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
            else:
                embed = discord.embeds.Embed(
                    title="StealPFP Section",
                    description=f"Setting not found.\n"
                                f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Settings",
                    value=f"- silent | {config['CONFIGURATION']['silentsteal']}"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
        elif section.lower() == "customization":
            if setting is None:
                embed = discord.embeds.Embed(
                    title="Customization Section",
                    description=f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Settings",
                    value=f"- embedcolor | {config['CONFIGURATION']['embedcolor']}"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            elif setting.lower() == "embedcolor":
                if value is None:
                    await settings_embed(ctx, "EmbedColor", "Changes the color of all embed messages sent.\n"
                                                            "**All Available Colors**"
                                                            "- Red\n"
                                                            "- Light Red\n"
                                                            "- Orange\n"
                                                            "- Light Orange\n"
                                                            "- Yellow\n"
                                                            "- Green\n"
                                                            "- Light Green\n"
                                                            "- Blue\n"
                                                            "- Light Blue\n"
                                                            "- Purple\n"
                                                            "- Light Purple\n"
                                                            "- Pink\n"
                                                            "- Light Pink")
                elif value.lower() == "red":
                    config['CONFIGURATION']['embedcolor'] = "red"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "light red":
                    config['CONFIGURATION']['embedcolor'] = "light red"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "orange":
                    config['CONFIGURATION']['embedcolor'] = "orange"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "light orange":
                    config['CONFIGURATION']['embedcolor'] = "light orange"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "yellow":
                    config['CONFIGURATION']['embedcolor'] = "yellow"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "green":
                    config['CONFIGURATION']['embedcolor'] = "green"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "light green":
                    config['CONFIGURATION']['embedcolor'] = "light green"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "blue":
                    config['CONFIGURATION']['embedcolor'] = "blue"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "light blue":
                    config['CONFIGURATION']['embedcolor'] = "light blue"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "purple":
                    config['CONFIGURATION']['embedcolor'] = "purple"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "light purple":
                    config['CONFIGURATION']['embedcolor'] = "light purple"
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "pink":
                    config['CONFIGURATION']['embedcolor'] = "pink"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "light pink":
                    config['CONFIGURATION']['embedcolor'] = "light pink"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                else:
                    embed = discord.embeds.Embed(
                        title="EmbedColor Setting",
                        description="Invalid Value",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="Colors",
                        value="- Red\n"
                              "- Light Red\n"
                              "- Orange\n"
                              "- Light Orange\n"
                              "- Yellow\n"
                              "- Green\n"
                              "- Light Green\n"
                              "- Blue\n"
                              "- Light Blue\n"
                              "- Purple\n"
                              "- Light Purple\n"
                              "- Pink\n"
                              "- Light Pink"
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
            else:
                embed = discord.embeds.Embed(
                    title="EmbedColor Section",
                    description=f"Setting not found.\n"
                                f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Settings",
                    value=f"- embedcolor | {config['CONFIGURATION']['embedcolor']}"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
        elif section.lower() == "configuration" or section.lower() == "config":
            if setting is None:
                embed = discord.embeds.Embed(
                    title="Configuration Section",
                    description=f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Settings",
                    value=f"- blacklist | {config['CONFIGURATION']['blacklist']}\n"
                          f"- richpresence | {config['CONFIGURATION']['rich_presence']}"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            elif setting.lower() == "blacklist":
                if value is None:
                    await settings_embed(ctx, "Blacklist", "Prevent users from using the bot.")
                elif value.lower() == "true":
                    config['CONFIGURATION']['blacklist'] = "True"
                    write()
                    await settings_embed(ctx, "Blacklist", "Blacklist has been turned on")
                elif value.lower() == "false":
                    config['CONFIGURATION']['blacklist'] = "False"
                    write()
                    await settings_embed(ctx, "Blacklist", "Blacklist has been turned off")
                else:
                    await settings_embed(ctx, "Blacklist", "Invalid value, must be ``true`` or ``false``")
            elif setting.lower() == "richpresence":
                if value is None:
                    await settings_embed(ctx, "Discord Rich Presence", "Enables Lost-UB's status in your profile.")
                elif value.lower() == "true":
                    config['CONFIGURATION']['rich_presence'] = "True"
                    write()
                    await settings_embed(ctx, "Discord Rich Presence",
                                         "Rich Presence is now enabled. You will need to restart Lost-UB")
                elif value.lower() == "false":
                    config['CONFIGURATION']['rich_presence'] = "False"
                    write()
                    await settings_embed(ctx, "Discord Rich Presence",
                                         "Rich Presence is now disabled. You will need to restart Lost-UB")
                else:
                    await settings_embed(ctx, "Discord Rich PResence",
                                         "Invalid value, must be ``true`` or ``false``")

        else:
            await sections_embed(ctx)


# Dice Roll ============================================================================================================


@bot.command()
async def rolladice(ctx):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        if config['CONFIGURATION']['logging'] == "True":
            print(f"[LOST-UB] rps command ran by {ctx.author.display_name}")
        number = random.randrange(1, 7)
        embed = discord.embeds.Embed(
            title="Dice Roll",
            description=f"You rolled a {number}",
            colour=embedcolor()
        )
        embed.set_footer(
            text=f"Logged in as {bot.user} | Lost-UB",
            icon_url=bot.user.avatar_url
        )
        await ctx.reply(embed=embed)


# Jesus ================================================================================================================

@bot.command()
async def jesus(ctx):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        embed = discord.embeds.Embed(
            title="You need jesus. Come and receive some of my help my child",
            colour=embedcolor())
        embed.set_image(url='https://preventsatan.com/wp-content/uploads/2019/06/Jesus-name-powerful.jpg')
        await ctx.reply(embed=embed)


# server info ==========================================================================================================

@bot.command()
async def serverinfo(ctx):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        name = str(ctx.guild.name)

        owner = str(ctx.guild.owner)
        guild_id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        membercount = str(ctx.guild.member_count)

        icon = ctx.guild.icon_url

        embed = discord.Embed(
            title=name + "Server Info",
            color=embedcolor()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=guild_id, inline=True)
        embed.add_field(name="Server Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=membercount, inline=True)

        await ctx.send(embed=embed)


# abc ==================================================================================================================

@bot.command()
async def abc(ctx):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        embed = discord.embeds.Embed(
            colour=embedcolor(),
            title="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        await ctx.reply(embed=embed)


# server icon ==========================================================================================================

@bot.command()
async def servericon(ctx):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        embed = discord.embeds.Embed()

        embed.add_field(
            name="Server Icon Link",
            value=f"[========>]({ctx.guild.icon_url_as(format='jpg')})")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.reply(embed=embed)


# warnings =============================================================================================================

@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member, *, reason: str = None):
    if bot.user == ctx.author:
        if reason is None:
            await ctx.reply("You must enter a reason for this warning.")
        else:
            if not os.path.exists("data/warnings"):
                os.mkdir("data/warnings")
            if not os.path.exists(f"data/warnings/{ctx.guild.id}"):
                os.mkdir(f"data/warnings/{ctx.guild.id}")
            with open(f"data/warnings/{ctx.guild.id}/{member.id}.txt", "a+") as warnings_file:
                old = warnings_file.read()
                local_time = time.localtime()
                warnings_file.write(f"{old}"
                                    f"[{local_time.tm_mon}/{local_time.tm_mday}/{local_time.tm_year}] {reason}\n")
                warnings_file = open(f"data/warnings/{ctx.guild.id}/{member.id}.txt", "r")
                count = 0
                warnings_file_content = warnings_file.read()
                lines = warnings_file_content.split("\n")
                for x in lines:
                    if x:
                        count += 1
            embed = discord.embeds.Embed(
                title="User Warned",
                description=f"Command Author: {ctx.author}",
                colour=embedcolor()
            )
            embed.add_field(
                name="User",
                value=f"{member}",
                inline=True
            )
            embed.add_field(
                name="Reason",
                value=reason,
                inline=True
            )
            embed.add_field(
                name="Warnings",
                value=f"{count + 1}",
                inline=True
            )
            embed.set_thumbnail(
                url=member.avatar_url
            )
            await ctx.reply(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def warnings(ctx, member: discord.Member):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        if not os.path.exists(f"data/warnings/{ctx.guild.id}/{member.id}.txt"):
            embed = discord.embeds.Embed(
                title="User Warnings",
                description="This user doesn't have any warnings yet",
                colour=embedcolor()
            )
            await ctx.reply(embed=embed)
        else:
            with open(f"data/warnings/{ctx.guild.id}/{member.id}.txt", "r"):
                warns = ""
                warnings_file = open(f"data/warnings/{ctx.guild.id}/{member.id}.txt", "r")
                count = 0
                remainder = 0
                warnings_file_content = warnings_file.read()
                lines = warnings_file_content.split("\n")
                for x in lines:
                    if x:
                        count += 1
                        if count <= 5:
                            warns += f"{x}\n"
                        else:
                            remainder += 1
                if remainder == 0:
                    embed = discord.embeds.Embed(
                        title="User Warnings",
                        description=f"{member} has {count} warnings"
                                    f"```{warns}```",
                        colour=embedcolor()
                    )
                else:
                    embed = discord.embeds.Embed(
                        title="User Warnings",
                        description=f"{member} has {count} warnings"
                                    f"```{warns}"
                                    f"+ {remainder} more```",
                        colour=embedcolor()
                    )
                await ctx.reply(embed=embed)


@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply('You are missing permissions!')
    elif isinstance(error, commands.MemberNotFound):
        await ctx.reply('Member not found!')


@warnings.error
async def warnings_error(ctx, error):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply('You are missing permissions!')
        elif isinstance(error, commands.MemberNotFound):
            await ctx.reply('Member not found!')


# User info ============================================================================================================


@bot.command()
async def userinfo(ctx, member: discord.Member):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        if config['CONFIGURATION']['logging'] == "True":
            print(f"[LOST-UB] userinfo command ran by {ctx.author.display_name}")
        minute = ""
        friends = ""
        guilds = ""
        roles = ""
        gay = random.randrange(1, 101)
        if member == bot.user:
            gay = "very straight for using Lost-UB!"
        elif gay >= 50:
            gay = "yes"
        elif gay <= 49:
            gay = "no"
        for role in member.roles:
            roles += f"- {role}\n"
        if member != bot.user:
            list_of_guilds = await member.mutual_guilds()
            for guild in list_of_guilds:
                guilds += f"- {guild}\n"
        else:
            guilds = "None"
        if member != bot.user and not member.bot:
            list_of_friends = await member.mutual_friends()
            for friend in list_of_friends:
                friends += f"- {friend}\n"
        elif member.bot:
            friends = "bots don't have friends"
        else:
            friends = "no one"
        suffix = ""
        hour = ""
        month = ""
        a = member.created_at
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
            title="User Info",
            colour=embedcolor()
        )
        embed.add_field(
            name="User",
            value=str(member),
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
        embed.set_footer(
            text=f"Logged in as {ctx.author} | Lost-UB",
            icon_url=bot.user.avatar_url
        )
        if member.is_avatar_animated():
            embed.add_field(
                name="Avatar Url",
                value=f"[Link]({member.avatar_url_as(format='gif')})",
                inline=True
            )
        else:
            embed.add_field(
                name="Avatar Url",
                value=f"[Link]({member.avatar_url_as(format='png')})",
                inline=True
            )
        embed.add_field(
            name="Roles",
            value=f"{roles}",
            inline=True
        )
        embed.add_field(
            name="User ID",
            value=f"{member.id}",
            inline=True
        )
        embed.add_field(
            name="Mutual Friends",
            value=f"{friends}",
            inline=True
        )
        embed.add_field(
            name="Mutual Guilds",
            value=f"{guilds}",
            inline=True
        )
        embed.add_field(
            name="Gay?",
            value=f"{gay}",
            inline=True
        )
        embed.set_thumbnail(
            url=member.avatar_url
        )
        await ctx.reply(embed=embed)


@userinfo.error
async def userinfo_error(ctx, error):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"Incorrect arguments | {get_prefix()}userinfo (@member)")
        else:
            print("Error when running userinfo")


# Kick =================================================================================================================

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason: str = None):
    if ctx.author == bot.user:
        embed = discord.embeds.Embed(
            title="User Kicked",
            description=f"Command Author: {ctx.author}",
            colour=embedcolor()
        )
        embed.add_field(
            name="User",
            value=f"{member}"
        )
        embed.add_field(
            name="Reason",
            value=reason
        )
        embed.set_thumbnail(
            url=member.avatar_url
        )
        if reason is None:
            await member.kick(reason=f"You have been kicked by {ctx.author}")
            await member.send(f"You have been kicked from {ctx.guild}")
        else:
            await member.kick(reason=f"You have been kicked by {ctx.author} for: {reason}")
            await member.send(f"You have been kicked from {ctx.guild} for: {reason}")
        await ctx.reply(embed=embed)
    else:
        return


@kick.error
async def kick_error(ctx, error):
    if ctx.author == bot.user:
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"Invalid arguments | {get_prefix()}kick (@member)")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.reply("Member not found")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("Missing permissions")
        else:
            await ctx.reply(error)


# Ban ==================================================================================================================

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason: str = None):
    if ctx.author == bot.user:
        embed = discord.embeds.Embed(
            title="User Banned",
            description=f"Command Author: {ctx.author}",
            colour=embedcolor()
        )
        embed.add_field(
            name="User",
            value=f"{member}"
        )
        embed.add_field(
            name="Reason",
            value=reason
        )
        embed.set_thumbnail(
            url=member.avatar_url
        )
        if reason is None:
            await member.ban(reason=f"You have been banned by {ctx.author}")
            await member.send(f"You have been banned from {ctx.guild}")
        else:
            await member.ban(reason=f"You have been banned by {ctx.author} for: {reason}")
            await member.send(f"You have been banned from {ctx.guild} for: {reason}")
        await ctx.reply(embed=embed)
    else:
        return


@ban.error
async def ban_error(ctx, error):
    if ctx.author == bot.user:
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"Invalid arguments | {get_prefix()}ban (@member)")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.reply("Member not found")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply("Missing permissions")
        else:
            await ctx.reply(error)


# Calculate ============================================================================================================

@bot.command(aliases=['calc'])
async def calculate(ctx, first_number: str = None, operator: str = None, second_number: str = None):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        log(ctx, "CALCULATE")
        operators = ['*', '/', '+', '-']
        result = ""
        if not first_number.isnumeric():
            await ctx.message.delete()
            log(ctx, "ERROR", f"Invalid argument(s). {first_number} is not a number.")
        else:
            if operator not in operators:
                await ctx.message.delete()
                log(ctx, "ERROR", f"Invalid argument(s). {operator} is not an operator.")
            else:
                if not second_number.isnumeric():
                    await ctx.message.delete()
                    log(ctx, "ERROR", f"Invalid argument(s). {first_number} is not a number.")
                else:
                    if operator == "*":
                        result = int(first_number) * int(second_number)
                    elif operator == "/":
                        result = int(first_number) / int(second_number)
                    elif operator == "+":
                        result = int(first_number) + int(second_number)
                    elif operator == "-":
                        result = int(first_number) - int(second_number)
                    try:
                        embed = discord.embeds.Embed(
                            title="Calculator",
                            description=f"Equation: {first_number} {operator} {second_number}\n"
                                        f"```{result}```",
                            colour=embedcolor()
                        )
                        await ctx.reply(embed=embed)
                    except discord.Forbidden:
                        await simple_codeblock(ctx,
                                               f"[ Calculator ]\n"
                                               f"Equation: {first_number} {operator} {second_number}\n"
                                               f"Result: {result}")


# Blacklist ============================================================================================================

@bot.command()
async def blacklist(ctx, action: str = None, member: discord.Member = None):
    if ctx.author == bot.user:
        log(ctx, "BLACKLIST")
        if action is None:
            count = 10
            total = 0
            remainder = 0
            black_list = open("data/blacklist.txt", "r")
            temp = ""
            file_content = black_list.read()
            lines = file_content.split("\n")
            for x in lines:
                if x:
                    if count != 0:
                        try:
                            user = await bot.fetch_user(int(x))
                        except discord.NotFound:
                            user = "UNKNOWN USER"
                        temp += f"- {user} ({x})\n"
                        count -= 1
                        total += 1
                    else:
                        remainder += 1
                        total += 1

            if remainder > 0:
                embed = discord.embeds.Embed(
                    title="Blacklisted Users",
                    description=f"**These users are not allowed to use any commands.**\n"
                                f"```{temp}"
                                f"+ {remainder} more...```"
                                f"Total Blacklisted Users: {total}",
                    colour=embedcolor()
                )
            else:
                if total == 0:
                    embed = discord.embeds.Embed(
                        title="Blacklisted Users",
                        description=f"**No blacklisted users yet...**\n",
                        colour=embedcolor()
                    )
                else:
                    embed = discord.embeds.Embed(
                        title="Blacklisted Users",
                        description=f"**These users are not allowed to use any commands.**\n"
                                    f"```{temp}\n```"
                                    f"Total Blacklisted Users: {total}",
                        colour=embedcolor()
                    )
            embed.set_footer(
                text=f"Logged in as {bot.user} | Lost-UB",
                icon_url=bot.user.avatar_url
            )
            try:
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                if remainder > 0:
                    string = f"These users are not allowed to use any commands.\n" \
                             f"```{temp}" \
                             f"+ {remainder} more...```" \
                             f"Total Blacklisted Users: {total}"
                else:
                    if total == 0:
                        string = f"No blacklisted users yet...\n"
                    else:
                        string = f"These users are not allowed to use any commands:\n\n" \
                                 f"{temp}\n" \
                                 f"[ Total Blacklisted Users ]\n" \
                                 f"{total}"
                await simple_codeblock(ctx,
                                       f"[ Blacklisted Users ]\n"
                                       f"{string}")
        elif action.lower() == "add":
            if member is None:
                await ctx.reply(f"Command usage {get_prefix()}blacklist add (@member)")
            else:
                oldfile = open("data/blacklist.txt", "r")
                oldfile_content = oldfile.read()
                lines = oldfile_content.split("\n")
                if f"{member.id}" in lines:
                    await ctx.reply("That user is already blacklisted.")
                else:
                    with open("data/blacklist.txt", "a+") as oldfile:
                        oldfile.write(f"{oldfile.read()}"
                                      f"{member.id}\n")
                    embed = discord.embeds.Embed(
                        title="Blacklisted User Added",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="User",
                        value=f"{member}",
                        inline=True
                    )
                    embed.add_field(
                        name="ID",
                        value=f"{member.id}",
                        inline=True
                    )
                    embed.set_thumbnail(
                        url=f"{member.avatar_url}"
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    try:
                        await ctx.reply(embed=embed)
                    except discord.Forbidden:
                        await simple_codeblock(ctx,
                                               f"[ Blacklisted User Added ]\n\n"
                                               f"[ User ]\n"
                                               f"{member}\n\n"
                                               f"[ ID ]\n"
                                               f"{member.id}")
        elif action.lower() == "remove":
            if member is None:
                await ctx.reply(f"Command usage {get_prefix()}blacklist remove (@member)")
            else:
                temp = ""
                black_list = open("data/blacklist.txt", "r")
                black_list_content = black_list.read()
                lines = black_list_content.split("\n")
                if f"{member.id}" in lines:
                    for x in lines:
                        if x:
                            if int(x) == member.id:
                                pass
                            else:
                                temp += f"{x}\n"
                    with open("data/blacklist.txt", "w") as file:
                        file.write(temp)
                    embed = discord.embeds.Embed(
                        title="Blacklisted User Removed",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="User",
                        value=f"{member}",
                        inline=True
                    )
                    embed.add_field(
                        name="ID",
                        value=f"{member.id}",
                        inline=True
                    )
                    embed.set_thumbnail(
                        url=f"{member.avatar_url}"
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    try:
                        await ctx.reply(embed=embed)
                    except discord.Forbidden:
                        await simple_codeblock(ctx,
                                               f"[ Blacklisted User Removed ]\n\n"
                                               f"[ User ]\n"
                                               f"{member}\n\n"
                                               f"[ ID ]\n"
                                               f"{member.id}")
                else:
                    await ctx.reply("That user isn't blacklisted.")


# Battle ===============================================================================================================

@bot.command()
async def battle(ctx):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        log(ctx, "BATTLE")
        player_hp = 100
        enemy_hp = 100

        embed = discord.embeds.Embed(
            title="Battle",
            description=f"You started a battle! What would you like to do?\n"
                        f"- Attack\n"
                        f"- Defend\n"
                        f"- Run\n",
            colour=embedcolor()
        )
        embed.add_field(
            name="Your Health",
            value=f"{player_hp}"
        )
        embed.add_field(
            name="Enemy Health",
            value=f"{enemy_hp}"
        )
        footer(embed)
        try:
            await ctx.reply(embed=embed)
        except discord.Forbidden:
            await simple_codeblock(ctx,
                                   f"[ Battle ]\n"
                                   f"You started a battle! What would you like to do?\n\n"
                                   f"[ Choices ]\n"
                                   f"- Attack\n"
                                   f"- Defend\n"
                                   f"- Run")

        def check(m):
            return m.author == ctx.author

        while True:
            if enemy_hp > 0 and player_hp > 0:
                action = await bot.wait_for('message', check=check, timeout=60.0)
                if action.content.lower() == "attack":
                    enemy_action = random.randint(0, 100)
                    player_damage = random.randint(0, 30)
                    if enemy_action >= 50:  # Enemy will attack
                        enemy_damage = random.randint(0, 30)
                        enemy_hp -= player_damage
                        player_hp -= enemy_damage
                        embed = discord.embeds.Embed(
                            title="Battle",
                            description=f"You dealt {player_damage} damage to the enemy!\n"
                                        f"The enemy also dealt {enemy_damage} damage to you!\n"
                                        f"What would you like to do next?",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Your Health",
                            value=f"{player_hp}"
                        )
                        embed.add_field(
                            name="Enemy Health",
                            value=f"{enemy_hp}"
                        )
                        footer(embed)
                        try:
                            await ctx.reply(embed=embed)
                        except discord.Forbidden:
                            await simple_codeblock(ctx,
                                                   f"[ Battle ]\n"
                                                   f"You dealt {player_damage} damage to the enemy!\n"
                                                   f"The enemy also dealt {enemy_damage} damage to you!\n"
                                                   f"What would you like to do next?\n\n"
                                                   f"[ Your Health ]\n"
                                                   f"{player_hp}\n\n"
                                                   f"[ Enemy Health ]\n"
                                                   f"{enemy_hp}")
                    elif enemy_action <= 49:  # Enemy will defend
                        enemy_shield_effectiveness = random.choice([0.25, 0.50, 0.75, 1.0])
                        player_damage = player_damage * enemy_shield_effectiveness
                        enemy_hp -= player_damage
                        embed = discord.embeds.Embed(
                            title="Battle",
                            description=f"The enemy blocked your attack, so your attack only dealt {player_damage} "
                                        f"damage!\n"
                                        f"What would you like to do next?",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Your Health",
                            value=f"{player_hp}"
                        )
                        embed.add_field(
                            name="Enemy Health",
                            value=f"{enemy_hp}"
                        )
                        footer(embed)
                        try:
                            await ctx.reply(embed=embed)
                        except discord.Forbidden:
                            await simple_codeblock(ctx,
                                                   f"[ Battle ]\n"
                                                   f"The enemy blocked your attack, "
                                                   f"so your attack only dealt {player_damage} "
                                                   f"damage!\n"
                                                   f"What would you like to do next?\n\n"
                                                   f"[ Your Health ]\n"
                                                   f"{player_hp}\n\n"
                                                   f"[ Enemy Health ]\n"
                                                   f"{enemy_hp}")
                elif action.content.lower() == "defend":
                    enemy_action = random.randint(0, 100)
                    enemy_damage = random.randint(0, 30)
                    if enemy_action >= 50:  # Enemy will attack
                        player_shield_effectiveness = random.choice([0.25, 0.50, 0.75, 1.0])
                        enemy_damage = enemy_damage * player_shield_effectiveness
                        player_hp -= enemy_damage
                        embed = discord.embeds.Embed(
                            title="Battle",
                            description=f"You blocked the enemy's attack, so their attack only dealt {enemy_damage} "
                                        f"damage!\n"
                                        f"What would you like to do next?",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Your Health",
                            value=f"{player_hp}"
                        )
                        embed.add_field(
                            name="Enemy Health",
                            value=f"{enemy_hp}"
                        )
                        footer(embed)
                        try:
                            await ctx.reply(embed=embed)
                        except discord.Forbidden:
                            await simple_codeblock(ctx,
                                                   f"[ Battle ]\n"
                                                   f"You blocked the enemy's attack, "
                                                   f"so their attack only dealt {enemy_damage} "
                                                   f"damage!\n"
                                                   f"What would you like to do next?\n\n"
                                                   f"[ Your Health ]\n"
                                                   f"{player_hp}\n\n"
                                                   f"[ Enemy Health ]\n"
                                                   f"{enemy_hp}")
                    elif enemy_action <= 49:  # Enemy will defend
                        embed = discord.embeds.Embed(
                            title="Battle",
                            description=f"You both defended each other, blocking each other like idiots!\n"
                                        f"What would you like to do next?",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Your Health",
                            value=f"{player_hp}"
                        )
                        embed.add_field(
                            name="Enemy Health",
                            value=f"{enemy_hp}"
                        )
                        footer(embed)
                        try:
                            await ctx.reply(embed=embed)
                        except discord.Forbidden:
                            await simple_codeblock(ctx,
                                                   f" [ Battle ]\n"
                                                   f"You both defended each other, blocking each other like idiots!\n"
                                                   f"What would you like to do next?\n\n"
                                                   f"[ Your Health ]\n"
                                                   f"{player_hp}\n\n"
                                                   f"[ Enemy Health ]\n"
                                                   f"{enemy_hp}")
                elif action.content.lower() == "run":
                    embed = discord.embeds.Embed(
                        title="Battle",
                        description=f"You forfeit! The enemy wins!",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="Your Health",
                        value=f"{player_hp}"
                    )
                    embed.add_field(
                        name="Enemy Health",
                        value=f"{enemy_hp}"
                    )
                    footer(embed)
                    try:
                        await ctx.reply(embed=embed)
                    except discord.Forbidden:
                        await simple_codeblock(ctx,
                                               f"[ Battle ]\n"
                                               f"You forfeit! The enemy wins!\n\n"
                                               f"[ Your Health ]\n"
                                               f"{player_hp}\n\n"
                                               f"[ Enemy Health ]\n"
                                               f"{enemy_hp}")
                    break
                else:
                    embed = discord.embeds.Embed(
                        title="Battle",
                        description=f"Invalid action!\n"
                                    f"- Attack\n"
                                    f"- Defend\n"
                                    f"- Run",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="Your Health",
                        value=f"{player_hp}"
                    )
                    embed.add_field(
                        name="Enemy Health",
                        value=f"{enemy_hp}"
                    )
                    footer(embed)
                    try:
                        await ctx.reply(embed=embed)
                    except discord.Forbidden:
                        await simple_codeblock(ctx,
                                               f"[ Battle ]\n"
                                               f"Invalid action!\n\n"
                                               f"[ Choices ]\n"
                                               f"- Attack\n"
                                               f"- Defend\n"
                                               f"- Run")
            elif enemy_hp > 0 and player_hp <= 0:
                embed = discord.embeds.Embed(
                    title="Battle",
                    description=f"The enemy wins! You lose!",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Your Health",
                    value=f"{player_hp}"
                )
                embed.add_field(
                    name="Enemy Health",
                    value=f"{enemy_hp}"
                )
                footer(embed)
                try:
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await simple_codeblock(ctx,
                                           f"[ Battle ]\n"
                                           f"The enemy wins! You lose!\n\n"
                                           f"[ Your Health ]\n"
                                           f"{player_hp}\n\n"
                                           f"[ Enemy Health ]\n"
                                           f"{enemy_hp}")
                break
            elif enemy_hp <= 0 and player_hp > 0:
                embed = discord.embeds.Embed(
                    title="Battle",
                    description=f"You won! The enemy loses!",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Your Health",
                    value=f"{player_hp}"
                )
                embed.add_field(
                    name="Enemy Health",
                    value=f"{enemy_hp}"
                )
                footer(embed)
                try:
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await simple_codeblock(ctx,
                                           f"[ Battle ]\n"
                                           f"You won! The enemy loses!\n\n"
                                           f"[ Your Health ]\n"
                                           f"{player_hp}\n\n"
                                           f"[ Enemy Health ]\n"
                                           f"{enemy_hp}")
                break
            elif enemy_hp <= 0 and player_hp <= 0:
                embed = discord.embeds.Embed(
                    title="Battle",
                    description=f"It's a tie!",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Your Health",
                    value=f"{player_hp}"
                )
                embed.add_field(
                    name="Enemy Health",
                    value=f"{enemy_hp}"
                )
                footer(embed)
                try:
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await simple_codeblock(ctx,
                                           f"[ Battle ]\n"
                                           f"It's a tie!\n\n"
                                           f"[ Your Health ]\n"
                                           f"{player_hp}\n\n"
                                           f"[ Enemy Health ]\n"
                                           f"{enemy_hp}")
                break


# ======================================================================================================================


@bot.command()
async def fight(ctx, member: discord.Member):
    if blacklist_check(ctx):
        await ctx.reply("You are blacklisted!")
    else:
        log(ctx, "FIGHT")
        if member != ctx.author:
            member = await bot.fetch_user(member.id)
            player_health = 100
            player2_health = 100
            player_shield_effectiveness = 0
            player2_shield_effectiveness = 0
            match = 0

            def check(m):
                return m.author == ctx.author

            def check2(m):
                return m.author == member

            embed = discord.embeds.Embed(
                title="Fight",
                description=f"{ctx.author.display_name} started a fight with {member.display_name}!\n"
                            f"It is {ctx.author.display_name}'s turn.",
                colour=embedcolor()
            )
            embed.add_field(
                name=f"{ctx.author.display_name}'s Health",
                value=f"{player_health}",
                inline=True
            )
            embed.add_field(
                name=f"{member.display_name}'s Health",
                value=f"{player2_health}",
                inline=True
            )
            embed.add_field(
                name="Choices",
                value="- Attack\n"
                      "- Defend\n"
                      "- Run",
                inline=True
            )
            footer(embed)
            try:
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await simple_codeblock(ctx,
                                       f"[ Fight ]\n"
                                       f"{ctx.author.display_name} started a fight with {member.display_name}!\n"
                                       f"It is {ctx.author.display_name}'s turn.\n\n"
                                       f"[ {ctx.author.display_name}'s Health ]\n"
                                       f"{player_health}\n\n"
                                       f"[ {member.display_name}'s Health ]\n"
                                       f"{player2_health}\n\n"
                                       f"[ Choices ]\n"
                                       f"- Attack\n"
                                       f"- Defend\n"
                                       f"- Run")

            while True:
                if match % 2 == 0:  # Player 1's Turn
                    if player_health > 0 and player2_health > 0:
                        action = await bot.wait_for('message', check=check, timeout=60.0)
                        if action.content.lower() == "attack":
                            if player2_shield_effectiveness != 0.0:
                                player_damage = player2_shield_effectiveness * random.randint(0, 30)
                                player2_health -= player_damage
                                player2_shield_effectiveness = 0
                            else:
                                player_damage = random.randint(0, 30)
                                player2_health -= player_damage

                            embed = discord.embeds.Embed(
                                title="Fight",
                                description=f"{ctx.author.display_name} dealt {player_damage} to"
                                            f" {member.display_name}!\n"
                                            f"It is now {member.display_name}'s turn.",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name=f"{ctx.author.display_name}'s Health",
                                value=f"{player_health}",
                                inline=True
                            )
                            embed.add_field(
                                name=f"{member.display_name}'s Health",
                                value=f"{player2_health}",
                                inline=True
                            )
                            embed.add_field(
                                name="Choices",
                                value="- Attack\n"
                                      "- Defend\n"
                                      "- Run",
                                inline=True
                            )
                            footer(embed)
                            try:
                                await action.reply(embed=embed)
                            except discord.Forbidden:
                                await simple_codeblock(ctx,
                                                       f"[ Fight ]\n"
                                                       f"{ctx.author.display_name} dealt {player_damage} to"
                                                       f" {member.display_name}!\n"
                                                       f"It is now {member.display_name}'s turn.\n\n"
                                                       f"[ {ctx.author.display_name}'s Health ]\n"
                                                       f"{player_health}\n\n"
                                                       f"[ {member.display_name}'s Health ]\n"
                                                       f"{player2_health}\n\n"
                                                       f"[ Choices ]\n"
                                                       f"- Attack\n"
                                                       f"- Defend\n"
                                                       f"- Run")

                        elif action.content.lower() == "defend":
                            player_shield_effectiveness = random.choice([0.0, 1.0])

                            embed = discord.embeds.Embed(
                                title="Fight",
                                description=f"{ctx.author.display_name} decided to defend themselves.\n"
                                            f"It is now {member.display_name}'s turn.",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name=f"{ctx.author.display_name}'s Health",
                                value=f"{player_health}",
                                inline=True
                            )
                            embed.add_field(
                                name=f"{member.display_name}'s Health",
                                value=f"{player2_health}",
                                inline=True
                            )
                            embed.add_field(
                                name="Choices",
                                value="- Attack\n"
                                      "- Defend\n"
                                      "- Run",
                                inline=True
                            )
                            footer(embed)
                            try:
                                await action.reply(embed=embed)
                            except discord.Forbidden:
                                await simple_codeblock(ctx,
                                                       f"[ Fight ]\n"
                                                       f"{ctx.author.display_name} decided to defend themselves.\n"
                                                       f"It is now {member.display_name}'s turn.\n\n"
                                                       f"[ {ctx.author.display_name}'s Health ]\n"
                                                       f"{player_health}\n\n"
                                                       f"[ {member.display_name}'s Health ]\n"
                                                       f"{player2_health}\n\n"
                                                       f"[ Choices ]\n"
                                                       f"- Attack\n"
                                                       f"- Defend\n"
                                                       f"- Run")

                        elif action.content.lower() == "run":

                            embed = discord.embeds.Embed(
                                title="Fight",
                                description=f"{ctx.author.display_name} forfeits! "
                                            f"{member.display_name} wins the fight!",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name=f"{ctx.author.display_name}'s Health",
                                value=f"{player_health}",
                                inline=True
                            )
                            embed.add_field(
                                name=f"{member.display_name}'s Health",
                                value=f"{player2_health}",
                                inline=True
                            )
                            footer(embed)
                            try:
                                await action.reply(embed=embed)
                            except discord.Forbidden:
                                await simple_codeblock(ctx,
                                                       f"[ Fight ]\n"
                                                       f"{ctx.author.display_name} forfeits! "
                                                       f"{member.display_name} wins the fight!\n\n"
                                                       f"[ {ctx.author.display_name}'s Health ]\n"
                                                       f"{player_health}\n\n"
                                                       f"[ {member.display_name}'s Health ]\n"
                                                       f"{player2_health}")

                            break
                    elif player_health > 0 and player2_health < 0:
                        embed = discord.embeds.Embed(
                            title="Fight",
                            description=f"{ctx.author.display_name} wins the fight!",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name=f"{ctx.author.display_name}'s Health",
                            value=f"{player_health}",
                            inline=True
                        )
                        embed.add_field(
                            name=f"{member.display_name}'s Health",
                            value=f"{player2_health}",
                            inline=True
                        )
                        footer(embed)
                        try:
                            await ctx.send(embed=embed)
                        except discord.Forbidden:
                            await simple_codeblock(ctx,
                                                   f"[ Fight ]\n"
                                                   f"{ctx.author.display_name} wins the fight!\n\n"
                                                   f"[ {ctx.author.display_name}'s Health ]\n"
                                                   f"{player_health}\n\n"
                                                   f"[ {member.display_name}'s Health ]\n"
                                                   f"{player2_health}")
                        break
                    elif player_health < 0 and player2_health > 0:
                        embed = discord.embeds.Embed(
                            title="Fight",
                            description=f"{member.display_name} wins the fight!",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name=f"{ctx.author.display_name}'s Health",
                            value=f"{player_health}",
                            inline=True
                        )
                        embed.add_field(
                            name=f"{member.display_name}'s Health",
                            value=f"{player2_health}",
                            inline=True
                        )
                        footer(embed)
                        try:
                            await ctx.send(embed=embed)
                        except discord.Forbidden:
                            await simple_codeblock(ctx,
                                                   f"[ Fight ]\n"
                                                   f"{member.display_name} wins the fight!\n\n"
                                                   f"[ {ctx.author.display_name}'s Health ]\n"
                                                   f"{player_health}\n\n"
                                                   f"[ {member.display_name}'s Health ]\n"
                                                   f"{player2_health}")
                        break
                    match += 1
                elif match % 2 == 1:  # Player 2's Turn
                    if player_health > 0 and player2_health > 0:
                        action = await bot.wait_for('message', check=check2, timeout=60.0)
                        if action.content.lower() == "attack":
                            if player_shield_effectiveness != 0.0:
                                player2_damage = player_shield_effectiveness * random.randint(0, 30)
                                player_health -= player2_damage
                                player_shield_effectiveness = 0
                            else:
                                player2_damage = random.randint(0, 30)
                                player_health -= player2_damage

                            embed = discord.embeds.Embed(
                                title="Fight",
                                description=f"{member.display_name} dealt {player2_damage} to "
                                            f"{ctx.author.display_name}!\n"
                                            f"It is now {ctx.author.display_name}'s turn.",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name=f"{ctx.author.display_name}'s Health",
                                value=f"{player_health}",
                                inline=True
                            )
                            embed.add_field(
                                name=f"{member.display_name}'s Health",
                                value=f"{player2_health}",
                                inline=True
                            )
                            embed.add_field(
                                name="Choices",
                                value="- Attack\n"
                                      "- Defend\n"
                                      "- Run",
                                inline=True
                            )
                            footer(embed)
                            try:
                                await action.reply(embed=embed)
                            except discord.Forbidden:
                                await simple_codeblock(ctx,
                                                       f"[ Fight ]\n"
                                                       f"{member.display_name} dealt {player2_damage} to"
                                                       f" {ctx.author.display_name}!\n"
                                                       f"It is now {ctx.author.display_name}'s turn.\n\n"
                                                       f"[ {ctx.author.display_name}'s Health ]\n"
                                                       f"{player_health}\n\n"
                                                       f"[ {member.display_name}'s Health ]\n"
                                                       f"{player2_health}\n\n"
                                                       f"[ Choices ]\n"
                                                       f"- Attack\n"
                                                       f"- Defend\n"
                                                       f"- Run")

                        elif action.content.lower() == "defend":
                            player2_shield_effectiveness = random.choice([0.0, 1.0])

                            embed = discord.embeds.Embed(
                                title="Fight",
                                description=f"{member.display_name} decided to defend themselves.\n"
                                            f"It is now {ctx.author.display_name}'s turn.",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name=f"{ctx.author.display_name}'s Health",
                                value=f"{player_health}",
                                inline=True
                            )
                            embed.add_field(
                                name=f"{member.display_name}'s Health",
                                value=f"{player2_health}",
                                inline=True
                            )
                            embed.add_field(
                                name="Choices",
                                value="- Attack\n"
                                      "- Defend\n"
                                      "- Run",
                                inline=True
                            )
                            footer(embed)
                            try:
                                await action.reply(embed=embed)
                            except discord.Forbidden:
                                await simple_codeblock(ctx,
                                                       f"[ Fight ]\n"
                                                       f"{member.display_name} decided to defend themselves.\n"
                                                       f"It is now {ctx.author.display_name}'s turn.\n\n"
                                                       f"[ {ctx.author.display_name}'s Health ]\n"
                                                       f"{player_health}\n\n"
                                                       f"[ {member.display_name}'s Health ]\n"
                                                       f"{player2_health}\n\n"
                                                       f"[ Choices ]\n"
                                                       f"- Attack\n"
                                                       f"- Defend\n"
                                                       f"- Run")

                        elif action.content.lower() == "run":

                            embed = discord.embeds.Embed(
                                title="Fight",
                                description=f"{member.display_name} forfeits! "
                                            f"{ctx.author.display_name} wins the fight!",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name=f"{ctx.author.display_name}'s Health",
                                value=f"{player_health}",
                                inline=True
                            )
                            embed.add_field(
                                name=f"{member.display_name}'s Health",
                                value=f"{player2_health}",
                                inline=True
                            )
                            embed.add_field(
                                name="Choices",
                                value="- Attack\n"
                                      "- Defend\n"
                                      "- Run",
                                inline=True
                            )
                            footer(embed)
                            try:
                                await action.reply(embed=embed)
                            except discord.Forbidden:
                                await simple_codeblock(ctx,
                                                       f"[ Fight ]\n"
                                                       f"{member.display_name} forfeits! "
                                                       f"{ctx.author.display_name} wins the fight!\n\n"
                                                       f"[ {ctx.author.display_name}'s Health ]\n"
                                                       f"{player_health}\n\n"
                                                       f"[ {member.display_name}'s Health ]\n"
                                                       f"{player2_health}")

                            break
                    elif player_health > 0 and player2_health < 0:
                        embed = discord.embeds.Embed(
                            title="Fight",
                            description=f"{ctx.author.display_name} wins the fight!",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name=f"{ctx.author.display_name}'s Health",
                            value=f"{player_health}",
                            inline=True
                        )
                        embed.add_field(
                            name=f"{member.display_name}'s Health",
                            value=f"{player2_health}",
                            inline=True
                        )
                        embed.add_field(
                            name="Choices",
                            value="- Attack\n"
                                  "- Defend\n"
                                  "- Run",
                            inline=True
                        )
                        footer(embed)
                        try:
                            await ctx.send(embed=embed)
                        except discord.Forbidden:
                            await simple_codeblock(ctx,
                                                   f"[ Fight ]\n"
                                                   f"{member.display_name} wins the fight!\n\n"
                                                   f"[ {ctx.author.display_name}'s Health ]\n"
                                                   f"{player_health}\n\n"
                                                   f"[ {member.display_name}'s Health ]\n"
                                                   f"{player2_health}")
                        break
                    elif player_health < 0 and player2_health > 0:
                        embed = discord.embeds.Embed(
                            title="Fight",
                            description=f"{ctx.author.display_name} wins the fight!",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name=f"{ctx.author.display_name}'s Health",
                            value=f"{player_health}",
                            inline=True
                        )
                        embed.add_field(
                            name=f"{member.display_name}'s Health",
                            value=f"{player2_health}",
                            inline=True
                        )
                        embed.add_field(
                            name="Choices",
                            value="- Attack\n"
                                  "- Defend\n"
                                  "- Run",
                            inline=True
                        )
                        footer(embed)
                        try:
                            await ctx.send(embed=embed)
                        except discord.Forbidden:
                            await simple_codeblock(ctx,
                                                   f"[ Fight ]\n"
                                                   f"{ctx.author.display_name} wins the fight!\n\n"
                                                   f"[ {ctx.author.display_name}'s Health ]\n"
                                                   f"{player_health}\n\n"
                                                   f"[ {member.display_name}'s Health ]\n"
                                                   f"{player2_health}")
                        break
                    match += 1
        else:
            await ctx.reply("You can't fight yourself.")


# ======================================================================================================================

@bot.command()
async def spam(ctx, delay: str = None, count: str = None, *, message: str = None):
    if bot.user == ctx.author:
        log(ctx, "SPAM")
        await ctx.message.delete()
        if delay is None:
            log(ctx, "ERROR", f"Missing required arguments. {get_prefix()}spam [delay] [count] [message]")
        elif not delay.isnumeric():
            log(ctx, "ERROR", f"Invalid arguments, '{delay}' is not a number.")
        else:
            if count is None:
                log(ctx, "ERROR", f"Missing required arguments. {get_prefix()}spam [delay] [count] [message]")
            elif not count.isnumeric():
                log(ctx, "ERROR", f"Invalid arguments, '{count}' is not a number.")
            else:
                if message is None:
                    log(ctx, "ERROR", f"Missing required arguments. "
                                      f"{get_prefix()}spam [delay] [count] [message]")
                elif message is None:
                    log(ctx, "ERROR", f"You have to specify what you want to spam!")
                else:
                    counter = 0
                    while counter < int(count):
                        await ctx.send(message)
                        time.sleep(int(delay))
                        counter += 1


# Poll =================================================================================================================

@bot.command()
async def poll(ctx, *, arguments: str = None):
    if arguments is None:
        await ctx.message.delete()
        log(ctx, "ERROR", "Missing required arguments.")
    else:
        title, description = arguments.split('| ')
        await ctx.message.delete()
        embed = discord.embeds.Embed(
            title=title,
            description=description,
            colour=embedcolor()
        )
        footer(embed)
        try:
            msg = await ctx.send(embed=embed)
        except discord.Forbidden:
            msg = await simple_codeblock(ctx, f"[ {title} ]\n"
                                              f"{description}", reply=False)
        await msg.add_reaction('✅')
        await msg.add_reaction('❎')


# Embed ================================================================================================================

@bot.command()
async def sendembed(ctx, *, arguments: str = None):
    if arguments is None:
        await ctx.message.delete()
        log(ctx, "ERROR", "Missing required arguments.")
    else:
        title, description = arguments.split("| ")
        await ctx.message.delete()
        embed = discord.embeds.Embed(
            title=title,
            description=description,
            colour=embedcolor()
        )
        footer(embed)
        try:
            await ctx.send(embed=embed)
        except discord.Forbidden:
            log(ctx, "ERROR", "Unable to send embedded message. Missing Permission(s).")


# ======================================================================================================================

@bot.command()
async def spamall(ctx, *, message: str = None):
    if ctx.author == bot.user:
        log(ctx, "SPAMALL")
        await ctx.message.delete()
        if message is None:
            log(ctx, "ERROR", f"You must specify a message. {get_prefix()}spamall [message]")
        else:
            for channels in ctx.guild.channels:
                try:
                    await channels.send(message)
                except AttributeError:
                    pass
                except discord.Forbidden:
                    pass


# ======================================================================================================================

@bot.command()
async def ghostpingall(ctx, member: discord.Member = None):
    if ctx.author == bot.user:
        log(ctx, "GHOSTPINGALL")
        await ctx.message.delete()
        if member is None:
            log(ctx, "ERROR", "Member not found")
        else:
            for channels in ctx.guild.channels:
                try:
                    ghost = await channels.send(member.mention)
                    await ghost.delete()
                except AttributeError:
                    pass
                except discord.Forbidden:
                    pass


# ======================================================================================================================

try:
    bot.run(config['CONFIGURATION']['token'])
except discord.LoginFailure:
    input(f"{Fore.LIGHTBLUE_EX}[LOST-UB]"
          f"{Fore.LIGHTRED_EX}[ERROR] "
          f"{Fore.RESET}Invalid Token. Please enter in a valid token in \"config.ini\" for Lost-UB to work.")
    exit()
# for safety purposes and ease of access, your token will be stored in
# config.ini. if for whatever reason you mess up the token, just go to
# config.ini and edit the token value.
