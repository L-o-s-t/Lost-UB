from bot import *


class Jesus(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def jesus(self, ctx):
        if blacklist_check(ctx):
            await ctx.reply("You are blacklisted!")
        else:
            log(ctx, "JESUS")
            embed = discord.embeds.Embed(
                title="You need jesus. Come and receive some of my help my child",
                colour=embedcolor())
            embed.set_image(url='https://preventsatan.com/wp-content/uploads/2019/06/Jesus-name-powerful.jpg')
            try:
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                log(ctx, "ERROR", "You need the permission, \"Embed Links\", to use this!")


def setup(userbot):
    userbot.add_cog(Jesus(userbot))
