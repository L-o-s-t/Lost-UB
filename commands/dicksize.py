from bot import *


class DickSize(commands.Cog):

    @commands.command()
    async def dicksize(self, ctx, member: discord.Member):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use DICKSIZE"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use DICKSIZE"))
        else:
            desc = ''
            print(log(ctx, description="This user used the command DICKSIZE"))
            size = random.randrange(0, 12)
            if size >= 6:
                desc = "That's a schlong dong!"
            elif size < 6:
                desc = "so smol! 🥺"
            await simple_codeblock(ctx, f"[ {member.display_name}'s Dick Size ]\n"
                                        f"{desc}\n\n"
                                        f"[ Size ]\n"
                                        f"{size} inches\n\n"
                                        f"[ Demonstration ]\n"
                                        f"8{size * '='}D\n\n")


def setup(userbot):
    userbot.add_cog(DickSize(userbot))
