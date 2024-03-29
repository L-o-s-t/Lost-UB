from bot import *


class Server(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def serverinfo(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use SERVERINFO"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use SERVERINFO"))
        else:
            print(log(ctx, description="This user used the command SERVERINFO"))
            name = str(ctx.guild.name)

            owner = str(ctx.guild.owner)
            guild_id = str(ctx.guild.id)
            region = str(ctx.guild.region)
            membercount = str(ctx.guild.member_count)

            icon = ctx.guild.icon_url

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
                print(log(ctx, "BLACKLIST", "This user attempted to use SERVERICON"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use SERVERICON"))
        else:
            print(log(ctx, description="This user used the command HELP"))
            if '.png' in str(ctx.guild.icon_url_as(format='png')):
                    await simple_codeblock(ctx, f"[ Server Icon Link ]\n"
                                                f"{ctx.guild.icon_url_as(format='png')}")
            else:
                await simple_codeblock(ctx, f"[ Server Icon Link ]\n"
                                            f"This guild does not have an icon.")


def setup(userbot):
    userbot.add_cog(Server(userbot))
