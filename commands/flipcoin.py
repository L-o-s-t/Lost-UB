from bot import *


class FlipCoin(commands.Cog):
    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def flipcoin(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use FLIPCOIN", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use FLIPCOIN", color=embedcolor("red"))
        else:
            await log(ctx, description="This user used the command FLIPCOIN", color=embedcolor())
            side = random.choice(['heads', 'tails'])
            await ctx.reply(f"it's {side}")


def setup(userbot):
    userbot.add_cog(FlipCoin(userbot))
