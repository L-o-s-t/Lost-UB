from bot import *


class ABC(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def abc(self, ctx):
        if blacklist_check(ctx):
            log(ctx, "BLACKLIST", f"{ctx.author.display_name} tried to use the command ABC.")
        else:
            log(ctx, "ABC")
            embed = discord.embeds.Embed(
                colour=embedcolor(),
                title="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            await ctx.reply(embed=embed)


def setup(userbot):
    userbot.add_cog(ABC(userbot))
