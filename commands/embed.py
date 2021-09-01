from bot import *


class Embed(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def sendembed(self, ctx, *, arguments: str = None):
        if arguments is None:
            await ctx.message.delete()
            log(ctx, "ERROR", "Missing required arguments.")
        else:
            title, description = arguments.split("| ")
            await ctx.message.delete()
            embed = discord.embeds.Embed(
                title=title,
                description=description,
                colour=embedcolor()
            )
            footer(embed)
            try:
                await ctx.send(embed=embed)
            except discord.Forbidden:
                log(ctx, "ERROR", "Unable to send embedded message. Missing Permission(s).")


def setup(userbot):
    userbot.add_cog(Embed(userbot))
