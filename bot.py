import asyncio
import configparser
import os
import time
import discord
import random
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

config = configparser.ConfigParser()


def write():
    config.write(open('config.ini', 'w'))


def get_prefix():
    return config["CONFIGURATION"]["prefix"]


def test(ctx):
    return print(f"{ctx.author}: {ctx.content}")


# Checks to see if "config.ini" exists, if not then it will create one.
if not os.path.exists('config.ini'):
    config['CONFIGURATION'] = {
        "token": f"{input('Welcome, please enter in your token: ')}",
        "prefix": f"{input('Please enter in your desired prefix: ')}",
        "logging": f"{input('Enable logs? (true/false): ')}",
        "AFK": "False",
        "afk_msg": "I'm afk",
        "afk_legit": "True",
        "silentsteal": "False",
        "silentsave": "False",
        "embedcolor": "red"
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

if not os.path.exists('avatars/'):
    os.mkdir('avatars/')


def embedcolor():
    if config['CONFIGURATION']['embedcolor'].lower() == "red":
        return discord.Colour.from_rgb(255, 0, 0)
    elif config['CONFIGURATION']['embedcolor'].lower() == "orange":
        return discord.Colour.from_rgb(255, 165, 0)
    elif config['CONFIGURATION']['embedcolor'].lower() == "yellow":
        return discord.Colour.from_rgb(255, 255, 0)
    elif config['CONFIGURATION']['embedcolor'].lower() == "green":
        return discord.Colour.from_rgb(0, 128, 0)
    elif config['CONFIGURATION']['embedcolor'].lower() == "blue":
        return discord.Colour.from_rgb(0, 0, 255)
    elif config['CONFIGURATION']['embedcolor'].lower() == "purple":
        return discord.Colour.from_rgb(128, 0, 128)
    elif config['CONFIGURATION']['embedcolor'].lower() == "pink":
        return discord.Colour.from_rgb(255, 192, 203)


bot: Bot = commands.Bot(command_prefix=f"{config['CONFIGURATION']['prefix']}", help_command=None, user_bot=True,
                        guild_subscriptions=False)


# Prints message to console when bot is ready
@bot.event
async def on_ready():
    print("[LOST-UB] Successfully Logged In.")


# Help =================================================================================================================


@bot.command(aliases=['help'])
async def info(ctx):
    cmds = ''
    for x in bot.all_commands:
        cmds += f"- {x}\n"
    embed = discord.embeds.Embed(
        title="All Commands",
        description=f"Your prefix is: {config['CONFIGURATION']['prefix']}",
        colour=embedcolor()
    )
    embed.add_field(
        name="Commands",
        value=f"{cmds}"
    )
    embed.set_footer(
        text=f"Logged in as {bot.user} | Lost-UB",
        icon_url=bot.user.avatar_url
    )
    await ctx.reply(embed=embed)


# Rock, paper, scissors ================================================================================================


@bot.command()
async def rps(ctx):
    if config['CONFIGURATION']['logging'] == "True":
        print(f"[LOST-UB] rps command ran by {ctx.author.display_name}")
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


# Prefix ===============================================================================================================


@bot.command()
async def prefix(ctx, x):
    if ctx.author == bot.user:
        if config['CONFIGURATION']['logging'] == "True":
            print(f"[LOST-UB] prefix command ran by {ctx.author.display_name}")
        config["CONFIGURATION"]["prefix"] = x
        write()
        bot.command_prefix = x
        await ctx.reply(f'Prefix changed to: ``{x}``')


@prefix.error
async def prefix_error(ctx, error):
    if ctx.author == bot.user:
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}prefix (desired_prefix)')


# Dicksize =============================================================================================================


@bot.command()
async def dicksize(ctx, member: discord.Member):
    desc = ''
    if config['CONFIGURATION']['logging'] == "True":
        print(f"[LOST-UB] dicksize command ran by {ctx.author.display_name}")
    size = random.randrange(0, 12)
    if size >= 6:
        desc = "That's a schlong dong!"
    elif size < 6:
        desc = "so smol! 🥺"
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


@dicksize.error
async def dicksize_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}dicksize (@member)')
    if isinstance(error, commands.MemberNotFound):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}dicksize (@member)')


# Flipcoin =============================================================================================================


@bot.command()
async def flipcoin(ctx):
    if config['CONFIGURATION']['logging'] == "True":
        print(f"[LOST-UB] rps command ran by {ctx.author.display_name}")
    side = random.choice(['heads', 'tails'])
    await ctx.reply(f"it's {side}")


# 8ball ================================================================================================================


@bot.command(aliases=['8ball'])
async def eightball(ctx, *, question: str = None):
    if question is None:
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}8ball (question)')
    else:
        if config['CONFIGURATION']['logging'] == "True":
            print(f"[LOST-UB] 8ball command ran by {ctx.author.display_name}")
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


# Ghost Ping ===========================================================================================================


@bot.command()
async def ghostping(ctx, member: discord.Member):
    if config['CONFIGURATION']['logging'] == "True":
        print(f"[LOST-UB] ghostping command ran by {ctx.author.display_name}")
    msg = await ctx.send(f'{member}')
    await msg.delete()
    await ctx.message.delete()


@ghostping.error
async def ghostping_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}ghostping (@member)')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}ghostping (@member)')


# IQ Rating ============================================================================================================

@bot.command()
async def iq(ctx, member: discord.Member):
    if config['CONFIGURATION']['logging'] == "True":
        print(f"[LOST-UB] iq command ran by {ctx.author.display_name}")
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
    embed = discord.embeds.Embed(
        title="Official IQ Rating",
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


@iq.error
async def iq_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}iq (@member)')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}iq (@member)')


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
            await member.avatar_url.save(f"avatars\\{member.id}.gif")
            with open(f'avatars/{member.id}.gif', 'rb') as image:
                await bot.user.edit(avatar=image.read())
        else:
            await member.avatar_url.save(f"avatars\\{member.id}.png")
            with open(f'avatars/{member.id}.png', 'rb') as image:
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
            print(f"[LOST-UB] {member.display_name}'s avatar was saved.")
        if config['CONFIGURATION']['silentsave'] == "True":
            await ctx.message.delete()
        if member.is_avatar_animated():
            await member.avatar_url.save(f"avatars\\{member.display_name}.gif")
        else:
            await member.avatar_url.save(f"avatars\\{member.display_name}.png")
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
                  "- customization"
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
                    await settings_embed(ctx, "EmbedColor", "Changes the color of all embed messages sent.")
                elif value.lower() == "red":
                    config['CONFIGURATION']['embedcolor'] = "red"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "orange":
                    config['CONFIGURATION']['embedcolor'] = "orange"
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
                elif value.lower() == "blue":
                    config['CONFIGURATION']['embedcolor'] = "blue"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "purple":
                    config['CONFIGURATION']['embedcolor'] = "purple"
                    write()
                    await ctx.reply(f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                elif value.lower() == "pink":
                    config['CONFIGURATION']['embedcolor'] = "pink"
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
                              "- Orange\n"
                              "- Yellow\n"
                              "- Green\n"
                              "- Blue\n"
                              "- Purple\n"
                              "- Pink"
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
        else:
            await sections_embed(ctx)


# Dice Roll ============================================================================================================


@bot.command()
async def rolladice(ctx):
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

# who asked ============================================================================================================


@bot.command()
async def whoasked(ctx):
    embed = discord.embeds.Embed(
        title="I must be a rapist cause i dont remember asking",
        colour=embedcolor())
    await ctx.reply(embed=embed)


# porn hub =============================================================================================================

@bot.command()
async def pornhub(ctx):
    embed = discord.embeds.Embed(
        title="You need jesus. Come and receive some of my help my child",
        colour=embedcolor())
    embed.set_image(url='https://preventsatan.com/wp-content/uploads/2019/06/Jesus-name-powerful.jpg')
    await ctx.reply(embed=embed)


# server info ==========================================================================================================

@bot.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = ctx.guild.icon_url

    embed = discord.Embed(
        title=name + "Server Info",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Server Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)


# abc ==================================================================================================================

@bot.command()
async def abc(ctx):
    embed = discord.embeds.Embed(
        colour=embedcolor(),
        title="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    await ctx.reply(embed=embed)


# server icon ==========================================================================================================

@bot.command()
async def servericon(ctx):
    embed = discord.embeds.Embed()

    embed.add_field(
        name="Server Icon Link",
        value=f"[========>]({ctx.guild.icon_url_as(format='jpg')})")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.reply(embed=embed)


# warnings =============================================================================================================

bot.warnings = {}  # guild_id : {member_id: [count, [(admin_id, reason)]]}


@bot.event
async def on_ready():
    for guild in bot.guilds:
        bot.warnings[guild.id] = {}

        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    bot.warnings[guild.id][member_id][0] += 1
                    bot.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    bot.warnings[guild.id][member_id] = [1, [(admin_id, reason)]]

    print(bot.user.name + " is ready.")


@bot.event
async def on_guild_join(guild):
    bot.warnings[guild.id] = {}


@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member = None, *, reason=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")

    if reason is None:
        return await ctx.send("Please provide a reason for warning this user.")

    try:
        first_warning = False
        bot.warnings[ctx.guild.id][member.id][0] += 1
        bot.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        bot.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = bot.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"{member.mention} now has {count} {'warning' if first_warning else 'warnings'}.")


@bot.command()
@commands.has_permissions(administrator=True)
async def warnings(ctx, member: discord.Member = None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")

    embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in bot.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** given by: {admin.mention} for: *'{reason}'*.\n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError:  # no warnings
        await ctx.send("This user has no warnings.")


@bot.command()
@commands.has_permissions(administrator=True)
async def unwarn(ctx, member: discord.Member = None, *, reason=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")

    try:
        first_warning = True
        bot.warnings[ctx.guild.id][member.id][0] -= 1
        bot.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = False
        bot.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = bot.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"{member.mention} now has {count} {'warning' if first_warning else 'warnings'}.")

@bot.command()
async def userinfo(ctx, member: discord.Member):
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
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f"Incorrect arguments | {get_prefix()}userinfo (@member)")
    else:
        print("Error when running userinfo")


# Kick =================================================================================================================

@bot.command()
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


# ======================================================================================================================

bot.run(config['CONFIGURATION']['token'])
# for safety purposes and ease of access, your token will be stored in
# config.ini. if for whatever reason you mess up the token, just go to
# config.ini and edit the token value.
