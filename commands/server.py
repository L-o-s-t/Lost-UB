from bot import *


class Server(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def serverinfo(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use SERVERINFO", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use SERVERINFO", color=embedcolor("red"))
        else:
            await log(ctx, description="This user used the command SERVERINFO", color=embedcolor())
            name = str(ctx.guild.name)

            owner = str(ctx.guild.owner)
            guild_id = str(ctx.guild.id)
            region = str(ctx.guild.region)
            membercount = str(ctx.guild.member_count)

            icon = ctx.guild.icon_url

            try:
                embed = discord.Embed(
                    title=name + "Server Info",
                    color=embedcolor()
                )
                embed.set_thumbnail(url=icon)
                embed.add_field(name="owner", value=owner, inline=True)
                embed.add_field(name="Server ID", value=guild_id, inline=True)
                embed.add_field(name="Server Region", value=region, inline=True)
                embed.add_field(name="Member Count", value=membercount, inline=True)

                await ctx.send(embed=embed)
            except Exception as e:
                await simple_codeblock(ctx, f"[ Server Info ]\n"
                                            f"{ctx.guild.name}\n\n"
                                            f"[ Owner ]\n"
                                            f"{owner}\n\n"
                                            f"[ Server ID ]\n"
                                            f"{guild_id}\n\n"
                                            f"[ Server Region ]\n"
                                            f"{region}\n\n"
                                            f"[ Member Count ]\n"
                                            f"{membercount}")

    @commands.command()
    async def servericon(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use SERVERICON", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use SERVERICON", color=embedcolor("red"))
        else:
            await log(ctx, description="This user used the command HELP", color=embedcolor())
            try:
                embed = discord.embeds.Embed(colour=embedcolor())
                embed.add_field(
                    name="Server Icon Link",
                    value=f"[========>]({ctx.guild.icon_url_as(format='png')})")
                embed.set_thumbnail(url=ctx.guild.icon_url)
                await ctx.reply(embed=embed)
            except Exception as e:
                if '.png' in str(ctx.guild.icon_url_as(format='png')):
                    await simple_codeblock(ctx, f"[ Server Icon Link ]\n"
                                                f"{ctx.guild.icon_url_as(format='png')}")
                else:
                    await simple_codeblock(ctx, f"[ Server Icon Link ]\n"
                                                f"This guild does not have an icon.")


def setup(userbot):
    userbot.add_cog(Server(userbot))
