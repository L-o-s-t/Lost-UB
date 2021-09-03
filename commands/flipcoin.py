from bot import *


class FlipCoin(commands.Cog):
    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def flipcoin(self, ctx):
        if blacklist_check(ctx):
            log(ctx, "BLACKLIST", f"{ctx.author.display_name} tried to use the command FLIPCOIN.")
        else:
            log(ctx, "FLIPCOIN")
            side = random.choice(['heads', 'tails'])
            await ctx.reply(f"it's {side}")


def setup(userbot):
    userbot.add_cog(FlipCoin(userbot))
