from bot import *


class DiceRoll(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def diceroll(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use DICEROLL", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use DICEROLL", color=embedcolor("red"))
        else:
            await log(ctx, description="This user used the command DICEROLL", color=embedcolor())
            number = random.randrange(1, 7)
            try:
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
            except Exception as e:
                await simple_codeblock(ctx, f"[ Dice Roll ]\n"
                                            f"You rolled a {number}")


def setup(userbot):
    userbot.add_cog(DiceRoll(userbot))
