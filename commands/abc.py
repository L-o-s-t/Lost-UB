from bot import *


class ABC(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def abc(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use ABC", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use ABC", color=embedcolor("red"))
        else:
            await log(ctx, description="This user used the command ABC", color=embedcolor())
            embed = discord.embeds.Embed(
                colour=embedcolor(),
                title="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            await ctx.reply(embed=embed)


def setup(userbot):
    userbot.add_cog(ABC(userbot))
