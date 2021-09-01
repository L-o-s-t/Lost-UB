from bot import *


class FlipCoin(commands.Cog):
    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def flipcoin(self, ctx):
        if blacklist_check(ctx):
            await ctx.reply("You are blacklisted!")
        else:
            log(ctx, "FLIPCOIN")
            side = random.choice(['heads', 'tails'])
            await ctx.reply(f"it's {side}")


def setup(userbot):
    userbot.add_cog(FlipCoin(userbot))
