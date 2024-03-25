from bot import *


class Warnings(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: discord.Member, *, reason: str = None):
        print(log(ctx, description="This user used the command WARN"))
        if bot.user == ctx.author:
            if reason is None:
                await ctx.reply("You must enter a reason for this warning.")
            else:
                print(log(ctx, description="This user used the command WARN"))
                if not os.path.exists("data/warnings"):
                    os.mkdir("data/warnings")
                if not os.path.exists(f"data/warnings/{ctx.guild.id}"):
                    os.mkdir(f"data/warnings/{ctx.guild.id}")
                with open(f"data/warnings/{ctx.guild.id}/{member.id}.txt", "a+") as warnings_file:
                    old = warnings_file.read()
                    local_time = time.localtime()
                    warnings_file.write(f"{old}"
                                        f"[{local_time.tm_mon}/{local_time.tm_mday}/{local_time.tm_year}] {reason}\n")
                    warnings_file = open(f"data/warnings/{ctx.guild.id}/{member.id}.txt", "r")
                    count = 0
                    warnings_file_content = warnings_file.read()
                    lines = warnings_file_content.split("\n")
                    for x in lines:
                        if x:
                            count += 1
                await simple_codeblock(ctx, f"[ User Warned ]\n"
                                            f"Command author: {ctx.author}\n\n"
                                            f"[ User ]\n"
                                            f"{member}\n\n"
                                            f"[ Reason ]\n"
                                            f"{reason}\n\n"
                                            f"[ Warnings ]\n"
                                            f"{count + 1}")

    @commands.command(aliases=['warns'])
    @commands.has_permissions(administrator=True)
    async def warnings(self, ctx, member: discord.Member):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use WARNS"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use WARNS"))
        else:
            print(log(ctx, description="This user used the command WARNS"))
            if not os.path.exists(f"data/warnings/{ctx.guild.id}/{member.id}.txt"):
                await simple_codeblock(ctx, f"[ User Warnigs ]\n"
                                            f"This user doesn't have any warnings yet.")
            else:
                with open(f"data/warnings/{ctx.guild.id}/{member.id}.txt", "r"):
                    warns = ""
                    warnings_file = open(f"data/warnings/{ctx.guild.id}/{member.id}.txt", "r")
                    count = 0
                    remainder = 0
                    warnings_file_content = warnings_file.read()
                    lines = warnings_file_content.split("\n")
                    for x in lines:
                        if x:
                            count += 1
                            if count <= 5:
                                warns += f"{x}\n"
                            else:
                                remainder += 1
                    if remainder == 0:
                        await simple_codeblock(ctx,
                                                f"[ User Warnings ]\n"
                                                f"{member} has {count} warnings\n\n"
                                                f"[ Warns ]\n"
                                                f"{warns}")
                    else:
                        await simple_codeblock(ctx,
                                                f"[ User Warnings ]\n"
                                                f"{member} has {count} warnings\n\n"
                                                f"[ Warns ]\n"
                                                f"{warns}"
                                                f"+ {remainder} more")


def setup(userbot):
    userbot.add_cog(Warnings(userbot))
