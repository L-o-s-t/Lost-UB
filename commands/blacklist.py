from bot import *


class Blacklist(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def blacklist(self, ctx, action: str = None, member=None):
        if ctx.author == bot.user:
            log(ctx, "BLACKLIST")
            if action is None:
                count = 10
                total = 0
                remainder = 0
                black_list = open("data/blacklist.txt", "r")
                temp = ""
                file_content = black_list.read()
                lines = file_content.split("\n")
                for x in lines:
                    if x:
                        if count != 0:
                            try:
                                user = await bot.fetch_user(int(x))
                            except discord.NotFound:
                                user = "UNKNOWN USER"
                            temp += f"- {user} ({x})\n"
                            count -= 1
                            total += 1
                        else:
                            remainder += 1
                            total += 1

                if remainder > 0:
                    embed = discord.embeds.Embed(
                        title="Blacklisted Users",
                        description=f"**These users are not allowed to use any commands.**\n"
                                    f"```{temp}"
                                    f"+ {remainder} more...```"
                                    f"Total Blacklisted Users: {total}",
                        colour=embedcolor()
                    )
                else:
                    if total == 0:
                        embed = discord.embeds.Embed(
                            title="Blacklisted Users",
                            description=f"**No blacklisted users yet...**\n",
                            colour=embedcolor()
                        )
                    else:
                        embed = discord.embeds.Embed(
                            title="Blacklisted Users",
                            description=f"**These users are not allowed to use any commands.**\n"
                                        f"```{temp}\n```"
                                        f"Total Blacklisted Users: {total}",
                            colour=embedcolor()
                        )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                try:
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    if remainder > 0:
                        string = f"These users are not allowed to use any commands.\n" \
                                 f"```{temp}" \
                                 f"+ {remainder} more...```" \
                                 f"Total Blacklisted Users: {total}"
                    else:
                        if total == 0:
                            string = f"No blacklisted users yet...\n"
                        else:
                            string = f"These users are not allowed to use any commands:\n\n" \
                                     f"{temp}\n" \
                                     f"[ Total Blacklisted Users ]\n" \
                                     f"{total}"
                    await simple_codeblock(ctx,
                                           f"[ Blacklisted Users ]\n"
                                           f"{string}")
            elif action.lower() == "add":
                if member is None:
                    await ctx.reply(f"Command usage {get_prefix()}blacklist add (@member)")
                elif member is discord.Member:
                    oldfile = open("data/blacklist.txt", "r")
                    oldfile_content = oldfile.read()
                    lines = oldfile_content.split("\n")
                    if f"{member.id}" in lines:
                        await ctx.reply("That user is already blacklisted.")
                    else:
                        with open("data/blacklist.txt", "a+") as oldfile:
                            oldfile.write(f"{oldfile.read()}"
                                          f"{member.id}\n")
                        embed = discord.embeds.Embed(
                            title="Blacklisted User Added",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="User",
                            value=f"{member}",
                            inline=True
                        )
                        embed.add_field(
                            name="ID",
                            value=f"{member.id}",
                            inline=True
                        )
                        embed.set_thumbnail(
                            url=f"{member.avatar_url}"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        try:
                            await ctx.reply(embed=embed)
                        except discord.Forbidden:
                            await simple_codeblock(ctx,
                                                   f"[ Blacklisted User Added ]\n\n"
                                                   f"[ User ]\n"
                                                   f"{member}\n\n"
                                                   f"[ ID ]\n"
                                                   f"{member.id}")
                else:
                    count = 0
                    for x in str(member):
                        count += 1
                    if count == 18:
                        member = await bot.fetch_user(member)
                        oldfile = open("data/blacklist.txt", "r")
                        oldfile_content = oldfile.read()
                        lines = oldfile_content.split("\n")
                        if f"{member}" in lines:
                            await ctx.reply("That user is already blacklisted.")
                        else:
                            with open("data/blacklist.txt", "a+") as oldfile:
                                oldfile.write(f"{oldfile.read()}"
                                              f"{member.id}\n")
                            embed = discord.embeds.Embed(
                                title="Blacklisted User Added",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name="User",
                                value=f"{member}",
                                inline=True
                            )
                            embed.add_field(
                                name="ID",
                                value=f"{member.id}",
                                inline=True
                            )
                            embed.set_thumbnail(
                                url=f"{member.avatar_url}"
                            )
                            embed.set_footer(
                                text=f"Logged in as {bot.user} | Lost-UB",
                                icon_url=bot.user.avatar_url
                            )
                            try:
                                await ctx.reply(embed=embed)
                            except discord.Forbidden:
                                await simple_codeblock(ctx,
                                                       f"[ Blacklisted User Added ]\n\n"
                                                       f"[ User ]\n"
                                                       f"{member}\n\n"
                                                       f"[ ID ]\n"
                                                       f"{member.id}")
                    else:
                        await ctx.message.delete()
                        log(ctx, "ERROR", "Invalid User ID.")
            elif action.lower() == "remove":
                if member is None:
                    await ctx.reply(f"Command usage {get_prefix()}blacklist remove (@member)")
                elif member is discord.Member:
                    temp = ""
                    black_list = open("data/blacklist.txt", "r")
                    black_list_content = black_list.read()
                    lines = black_list_content.split("\n")
                    if f"{member.id}" in lines:
                        for x in lines:
                            if x:
                                if int(x) == member.id:
                                    pass
                                else:
                                    temp += f"{x}\n"
                        with open("data/blacklist.txt", "w") as file:
                            file.write(temp)
                        embed = discord.embeds.Embed(
                            title="Blacklisted User Removed",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="User",
                            value=f"{member}",
                            inline=True
                        )
                        embed.add_field(
                            name="ID",
                            value=f"{member.id}",
                            inline=True
                        )
                        embed.set_thumbnail(
                            url=f"{member.avatar_url}"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        try:
                            await ctx.reply(embed=embed)
                        except discord.Forbidden:
                            await simple_codeblock(ctx,
                                                   f"[ Blacklisted User Removed ]\n\n"
                                                   f"[ User ]\n"
                                                   f"{member}\n\n"
                                                   f"[ ID ]\n"
                                                   f"{member.id}")
                    else:
                        await ctx.reply("That user isn't blacklisted.")
                else:
                    count = 0
                    for x in f"{member}":
                        count += 1
                    if count == 18:
                        temp = ""
                        black_list = open("data/blacklist.txt", "r")
                        black_list_content = black_list.read()
                        lines = black_list_content.split("\n")
                        if f"{member}" in lines:
                            for x in lines:
                                if x:
                                    if int(x) == int(member):
                                        print(f"{x} is {member}")
                                        pass
                                    else:
                                        print(f"{x} is not {member}")
                                        temp += f"{x}\n"
                            with open("data/blacklist.txt", "w") as file:
                                file.write(temp)
                            user = await bot.fetch_user(member)
                            embed = discord.embeds.Embed(
                                title="Blacklisted User Removed",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name="User",
                                value=f"{user}",
                                inline=True
                            )
                            embed.add_field(
                                name="ID",
                                value=f"{user.id}",
                                inline=True
                            )
                            embed.set_thumbnail(
                                url=f"{user.avatar_url}"
                            )
                            embed.set_footer(
                                text=f"Logged in as {bot.user} | Lost-UB",
                                icon_url=bot.user.avatar_url
                            )
                            try:
                                await ctx.reply(embed=embed)
                            except discord.Forbidden:
                                await simple_codeblock(ctx,
                                                       f"[ Blacklisted User Removed ]\n\n"
                                                       f"[ User ]\n"
                                                       f"{user}\n\n"
                                                       f"[ ID ]\n"
                                                       f"{user.id}")
                        else:
                            await ctx.reply("That user isn't blacklisted.")
                    else:
                        await ctx.message.delete()
                        log(ctx, "ERROR", "Invalid User ID.")


def setup(userbot):
    userbot.add_cog(Blacklist(userbot))
