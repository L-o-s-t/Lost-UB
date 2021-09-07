import discord.ext.commands

from bot import *


class Blacklist(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def blacklist(self, ctx, action: str = None, member=None):
        # if command author is the bot user then...
        if ctx.author == bot.user:

            log(ctx, "BLACKLIST")  # logs to console

            # if action is nothing, it will fetch the blacklisted users
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

            # if action is add, it will add the specified user
            elif action.lower() == "add":
                if member is None:
                    await ctx.reply(f"Command usage {get_prefix()}blacklist add (@member)")
                elif '@' in str(member):
                    member = await bot.fetch_user(int(member[3:21]))
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
                        notfound = False
                        try:
                            member = await bot.fetch_user(member)
                            print('found')
                        except discord.errors.NotFound:
                            print('notfound')
                            notfound = True
                            pass
                        oldfile = open("data/blacklist.txt", "r")
                        oldfile_content = oldfile.read()
                        lines = oldfile_content.split("\n")
                        if f"{member}" in lines:
                            await ctx.reply("That user is already blacklisted.")
                        else:
                            with open("data/blacklist.txt", "a+") as oldfile:
                                if notfound:
                                    oldfile.write(f"{oldfile.read()}"
                                                  f"{member}\n")
                                else:
                                    oldfile.write(f"{oldfile.read()}"
                                                  f"{member.id}\n")
                            embed = discord.embeds.Embed(
                                title="Blacklisted User Added",
                                colour=embedcolor()
                            )
                            if notfound:
                                embed.add_field(
                                    name="User",
                                    value="UNKNOWN",
                                    inline=True
                                )
                                embed.add_field(
                                    name="ID",
                                    value=f"{member}",
                                    inline=True
                                )
                                embed.set_thumbnail(
                                    url=f"https://cdn.drawception.com/drawings/848910/l0ZT9m55a0.png"
                                )
                            else:
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
                                if notfound:
                                    await simple_codeblock(ctx,
                                                           f"[ Blacklisted User Added ]\n\n"
                                                           f"[ User ]\n"
                                                           f"UKNOWN\n\n"
                                                           f"[ ID ]\n"
                                                           f"{member}")
                                else:
                                    await simple_codeblock(ctx,
                                                           f"[ Blacklisted User Added ]\n\n"
                                                           f"[ User ]\n"
                                                           f"{member}\n\n"
                                                           f"[ ID ]\n"
                                                           f"{member.id}")
                    else:
                        await ctx.message.delete()
                        log(ctx, "ERROR", f"Invalid User ID.")

            # if action is remove, it will add the specified user
            elif action.lower() == "remove":
                if member is None:
                    await ctx.reply(f"Command usage {get_prefix()}blacklist remove (@member)")
                elif '@' in str(member):
                    member = await bot.fetch_user(int(member[3:21]))
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
                                        pass
                                    else:
                                        temp += f"{x}\n"
                            with open("data/blacklist.txt", "w") as file:
                                file.write(temp)
                            notfound = False
                            user = None
                            try:
                                user = await bot.fetch_user(member)
                            except discord.errors.NotFound:
                                notfound = True
                            embed = discord.embeds.Embed(
                                title="Blacklisted User Removed",
                                colour=embedcolor()
                            )
                            if notfound:
                                embed.add_field(
                                    name="User",
                                    value=f"UKNOWN",
                                    inline=True
                                )
                                embed.add_field(
                                    name="ID",
                                    value=f"{member}",
                                    inline=True
                                )
                                embed.set_thumbnail(
                                    url=f"https://cdn.drawception.com/drawings/848910/l0ZT9m55a0.png"
                                )
                            else:
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
                                    url=user.avatar_url
                                )
                            embed.set_footer(
                                text=f"Logged in as {bot.user} | Lost-UB",
                                icon_url=bot.user.avatar_url
                            )
                            try:
                                await ctx.reply(embed=embed)
                            except discord.Forbidden:
                                if notfound:
                                    await simple_codeblock(ctx,
                                                           f"[ Blacklisted User Removed ]\n\n"
                                                           f"[ User ]\n"
                                                           f"UNKNOWN\n\n"
                                                           f"[ ID ]\n"
                                                           f"{member}")
                                else:
                                    await simple_codeblock(ctx,
                                                           f"[ Blacklisted User Removed ]\n\n"
                                                           f"[ User ]\n"
                                                           f"{user}\n\n"
                                                           f"[ ID ]\n"
                                                           f"{user.id}")
                        else:
                            await ctx.reply(f"That user isn't blacklisted.")
                    elif count == 3:
                        if str(member).lower() == "all":
                            with open('data/blacklist.txt', 'w+', encoding='utf8') as file:
                                file.write("")
                                try:
                                    await simple_embed(ctx,
                                                       title="Blacklist",
                                                       description="**Successfully removed all users.**")
                                except discord.Forbidden:
                                    await simple_codeblock(ctx,
                                                           "[ Blacklist ]\n"
                                                           "Successfully removed all users.")
                    else:
                        await ctx.message.delete()
                        log(ctx, "ERROR", f"Invalid User ID.")

            # if action is none of the above, it will send an error to console
            else:
                log(ctx, "ERROR", f"{action.lower()} is not an action. "
                                  f"{get_prefix()}blacklist (add/remove) (@member/member_id)")
                await ctx.message.delete()


def setup(userbot):
    userbot.add_cog(Blacklist(userbot))
