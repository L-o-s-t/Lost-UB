from bot import *


class Embed(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def sendembed(self, ctx, *, arguments: str = None):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use SENDEMBED", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use SENDEMBED", color=embedcolor("red"))
        else:
            await log(ctx, description="This user used the command SENDEMBED", color=embedcolor())
            if arguments is None:
                await ctx.message.delete()
                await ctx.reply("Missing required arguments.")
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
                        await log(ctx, description="Unable to send embedded message. Missing Permission(s).",
                                  color=embedcolor("red"))
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
                        await log(ctx, description="Unable to send embedded message. Missing Permission(s).",
                                  color=embedcolor())
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
                        await log(ctx, description="Unable to send embedded message. Missing Permission(s).",
                                  color=embedcolor())
                else:
                    await ctx.message.delete()
                    await ctx.send(f"Too many seperators! "
                                   f"Usage: {get_prefix()}sendembed (title) | (description) | (color) | ("
                                   f"thumbnail)")


def setup(userbot):
    userbot.add_cog(Embed(userbot))
