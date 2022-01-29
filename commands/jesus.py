from bot import *


class Jesus(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def jesus(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use JESUS", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use JESUS", color=embedcolor("red"))
        else:
            await log(ctx, description="This user used the command JESUS", color=embedcolor())
            embed = discord.embeds.Embed(
                title="You need jesus. Come and receive some of my help my child",
                colour=embedcolor())
            embed.set_image(url='https://preventsatan.com/wp-content/uploads/2019/06/Jesus-name-powerful.jpg')
            try:
                await ctx.reply(embed=embed)
            except Exception as e:
                await ctx.send("You need the permission, \"Embed Links\", to use this!")


def setup(userbot):
    userbot.add_cog(Jesus(userbot))
