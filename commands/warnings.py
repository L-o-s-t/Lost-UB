from bot import *


class Warnings(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: discord.Member, *, reason: str = None):
        if bot.user == ctx.author:
            if reason is None:
                await ctx.reply("You must enter a reason for this warning.")
            else:
                log(ctx, "WARN")
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
                try:
                    embed = discord.embeds.Embed(
                        title="User Warned",
                        description=f"Command Author: {ctx.author}",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="User",
                        value=f"{member}",
                        inline=True
                    )
                    embed.add_field(
                        name="Reason",
                        value=reason,
                        inline=True
                    )
                    embed.add_field(
                        name="Warnings",
                        value=f"{count + 1}",
                        inline=True
                    )
                    embed.set_thumbnail(
                        url=member.avatar_url
                    )
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await simple_codeblock(ctx,
                                           f"[ User Warned ]\n"
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
        if blacklist_check(ctx):
            log(ctx, "BLACKLIST", f"{ctx.author.display_name} tried to use the command .")
        else:
            log(ctx, "WARNINGS")
            if not os.path.exists(f"data/warnings/{ctx.guild.id}/{member.id}.txt"):
                embed = discord.embeds.Embed(
                    title="User Warnings",
                    description="This user doesn't have any warnings yet",
                    colour=embedcolor()
                )
                await ctx.reply(embed=embed)
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
                        embed = discord.embeds.Embed(
                            title="User Warnings",
                            description=f"{member} has {count} warnings"
                                        f"```{warns}```",
                            colour=embedcolor()
                        )
                    else:
                        embed = discord.embeds.Embed(
                            title="User Warnings",
                            description=f"{member} has {count} warnings"
                                        f"```{warns}"
                                        f"+ {remainder} more```",
                            colour=embedcolor()
                        )
                    try:
                        await ctx.reply(embed=embed)
                    except discord.Forbidden:
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
