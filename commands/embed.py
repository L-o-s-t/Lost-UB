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
            splits = 0
            for x in arguments:
                if x:
                    if x == "|":
                        splits += 1
            if splits == 1:
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
            elif splits == 2:
                title, description, color = arguments.split("| ")
                await ctx.message.delete()
                embed = discord.embeds.Embed(
                    title=title,
                    description=description,
                    colour=embedcolor(color)
                )
                footer(embed)
                try:
                    await ctx.send(embed=embed)
                except discord.Forbidden:
                    log(ctx, "ERROR", "Unable to send embedded message. Missing Permission(s).")
            elif splits == 3:
                title, description, color, thumbnail = arguments.split(" | ")
                await ctx.message.delete()
                embed = discord.embeds.Embed(
                    title=title,
                    description=description,
                    colour=embedcolor(color)
                )
                embed.set_thumbnail(url=f"{thumbnail}")
                footer(embed)
                try:
                    await ctx.send(embed=embed)
                except discord.Forbidden:
                    log(ctx, "ERROR", "Unable to send embedded message. Missing Permission(s).")
            else:
                await ctx.message.delete()
                log(ctx, "SENDEMBED", f"Too many seperators! "
                                      f"Usage: {get_prefix()}sendembed (title) | (description) | (color) | (thumbnail)")


def setup(userbot):
    userbot.add_cog(Embed(userbot))
