import asyncio
import configparser
import os
import discord
import random
from discord.ext import commands

print("""
                     ▄█        ▄██████▄     ▄████████     ███          ███    █▄  ▀█████████▄  
                    ███       ███    ███   ███    ███ ▀█████████▄      ███    ███   ███    ███ 
                    ███       ███    ███   ███    █▀     ▀███▀▀██      ███    ███   ███    ███ 
                    ███       ███    ███   ███            ███   ▀      ███    ███  ▄███▄▄▄██▀  
                    ███       ███    ███ ▀███████████     ███          ███    ███ ▀▀███▀▀▀██▄  
                    ███       ███    ███          ███     ███          ███    ███   ███    ██▄ 
                    ███▌    ▄ ███    ███    ▄█    ███     ███          ███    ███   ███    ███ 
                    █████▄▄██  ▀██████▀   ▄████████▀     ▄████▀        ████████▀  ▄█████████▀  
                    ▀                      made by LOST#0404                                               
""")

config = configparser.ConfigParser()


def write():
    config.write(open('config.ini', 'w'))


# Checks to see if "config.ini" exists, if not then it will create one.
if not os.path.exists('config.ini'):
    config['CONFIGURATION'] = {
        "token": f"{input('Welcome, please enter in your token: ')}",
        "prefix": f"{input('Please enter in your desired prefix: ')}",
        "logging": f"{input('Enable logs? (true/false): ')}"
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

bot = commands.Bot(command_prefix=f"{config['CONFIGURATION']['prefix']}", self_bot=True, help_command=None)


# Prints message to console when bot is ready
@bot.event
async def on_ready():
    print("[LOST-UB] Successfully Logged In.")

# Help =================================================================================================================


@bot.command(aliases=['help'])
async def info(ctx):
    embed = discord.embeds.Embed(
        title="All Commands",
        description=f"Your prefix is: {config['CONFIGURATION']['prefix']}",
        colour=discord.Colour.red()
    )
    embed.add_field(
        name="Commands",
        value="- Rock, Paper, Scissors\n"
              "- Prefix\n"
              "- Dicksize\n"
              "- 8Ball\n"
              "- Flipcoin\n"
              "- Ghostping\n"
              "- IQ Rating"
    )
    await ctx.reply(embed=embed)


# Rock, paper, scissors ================================================================================================


@bot.command()
async def rps(ctx):
    if config['CONFIGURATION']['logging'] == "true":
        print(f"[LOST-UB] rps command ran by {ctx.author.display_name}")
    embed = discord.embeds.Embed(
        title="Rock, Paper, Scissors Game",
        description="What is your choice?",
        colour=discord.Colour.blue()
    )
    embed.add_field(
        name="Choices",
        value="Rock, Paper, Scissors"
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
            colour=discord.embeds.Colour.blue()
        )
        embed.add_field(
            name="Your Choice",
            value=f"{answer.content.lower()}"
        )
        embed.add_field(
            name="CPU's Choice",
            value=f"{rps_choice}"
        )
        await ctx.reply(embed=embed)
    except asyncio.TimeoutError:
        await ctx.reply("You took too long to respond!")


# Prefix ===============================================================================================================


@bot.command()
async def prefix(ctx, x):
    if config['CONFIGURATION']['logging'] == "true":
        print(f"[LOST-UB] prefix command ran by {ctx.author.display_name}")
    config["CONFIGURATION"]["prefix"] = x
    write()
    bot.command_prefix = x
    await ctx.reply(f'Prefix changed to: ``{x}``')


@prefix.error
async def prefix_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}prefix (desired_prefix)')


# Dicksize =============================================================================================================


@bot.command()
async def dicksize(ctx, member: discord.Member):
    desc = ''
    if config['CONFIGURATION']['logging'] == "true":
        print(f"[LOST-UB] dicksize command ran by {ctx.author.display_name}")
    if member.id == 691171747138895882:
        size = 16
    else:
        size = random.randrange(0, 12)
    if size >= 6:
        desc = "That's a schlong dong!"
    elif size < 6:
        desc = "so smol! 🥺"
    embed = discord.embeds.Embed(
        title=f"{member.display_name}'s Dick Size",
        description=desc,
        colour=discord.Colour.blue()
    )
    embed.add_field(
        name="Size",
        value=f"{size} inches"
    )
    embed.add_field(
        name="Demonstration",
        value=f"8{size * '='}D"
    )
    await ctx.reply(embed=embed)


@dicksize.error
async def dicksize_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}dicksize (@member)')


@dicksize.error
async def dicksize_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}dicksize (@member)')


# Flipcoin =============================================================================================================


@bot.command()
async def flipcoin(ctx):
    if config['CONFIGURATION']['logging'] == "true":
        print(f"[LOST-UB] rps command ran by {ctx.author.display_name}")
    side = random.choice(['heads', 'tails'])
    await ctx.reply(f"it's {side}")


# 8ball ================================================================================================================


@bot.command(aliases=['8ball'])
async def eightball(ctx, *, question: str = None):
    if question is None:
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}8ball (question)')
    else:
        if config['CONFIGURATION']['logging'] == "true":
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
            description=f"{question}"
        )
        embed.add_field(
            name="Answer",
            value=f"{answers}"
        )
        await ctx.reply(embed=embed)


# Ghost Ping ===========================================================================================================


@bot.command()
async def ghostping(ctx, member: discord.Member):
    msg = await ctx.send(f'{member}')
    await msg.delete()
    await ctx.message.delete()


@ghostping.error
async def ghostping_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}ghostping (@member)')


@ghostping.error
async def ghostping_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}ghostping (@member)')


# IQ Rating ============================================================================================================

@bot.command()
async def iq(ctx, member: discord.Member):
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
        result = "High Averrage"
    elif 120 <= iq_rating <= 129:
        result = "Superior"
    elif iq_rating >= 130:
        result = "Very Superior"
    embed = discord.embeds.Embed(
        title="Official IQ Rating",
        description=f"{member}'s IQ is {iq_rating}",
        colour=discord.colour.Colour.blue()
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
    await ctx.reply(embed=embed)


@iq.error
async def iq_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}iq (@member)')


@iq.error
async def iq_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}iq (@member)')


# ======================================================================================================================


bot.run(config['CONFIGURATION']['token'])
# for safety purposes and ease of access, your token will be stored in
# config.ini. if for whatever reason you mess up the token, just go to
# config.ini and edit the token value.