from bot import *


class RPS(commands.Cog):
    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def rps(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use RPS", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use RPS", color=embedcolor("red"))
        else:
            await log(ctx, description="This user used the command RPS", color=embedcolor())
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
            except Exception as e:
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


def setup(userbot):
    userbot.add_cog(RPS(userbot))
