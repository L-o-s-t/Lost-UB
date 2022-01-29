from bot import *


class UserLog(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def userlog(self, ctx, action: str = None, member=None):
        await log(ctx, description="This user used the command USERLOG", color=embedcolor())

        # if command author is bot user:
        if ctx.author == bot.user:

            # if member is none:
            if action is None:
                with open('data/logs/loggedusers.txt', 'r', encoding="utf8") as logfile:
                    content = logfile.read()
                    lines = content.split("\n")
                    description = ""
                    count = 0
                    remainder = 0
                    for x in lines:
                        if x:
                            count += 1
                            if count <= 10:
                                try:
                                    member = await bot.fetch_user(int(x))
                                except discord.NotFound:
                                    member = "UKNOWN USER"
                                description += f"- {member} ({x})\n"
                            elif count > 10:
                                remainder += 1
                    try:
                        if remainder >= 1:
                            embed = discord.embeds.Embed(
                                title="Logged User List",
                                description=f"**These users will automatically be logged.**\n"
                                            f"```{description} + {remainder} more...```\n"
                                            f"Total Logged Users: {count}",
                                colour=embedcolor()
                            )
                        else:
                            if count != 0:
                                embed = discord.embeds.Embed(
                                    title="Logged User List",
                                    description=f"**These users will automatically be logged.**\n"
                                                f"```{description}```"
                                                f"Total Logged Users: {count}",
                                    colour=embedcolor()
                                )
                            else:
                                embed = discord.embeds.Embed(
                                    title="Logged User List",
                                    description=f"**No logged users yet...**",
                                    colour=embedcolor()
                                )
                        footer(embed)
                        await ctx.send(embed=embed)
                    except Exception as e:
                        if count != 0:
                            await simple_codeblock(ctx, f"[ Logged User List ]\n"
                                                        f"{description}\n\n"
                                                        f"[ Total Logged Users ]\n"
                                                        f"{count}")
                        else:
                            await simple_codeblock(ctx, f"[ Logged User List ]\n"
                                                        f"No logged users yet...\n\n")

            # else if "#" in member:
            elif action.lower() == "add":
                if member is None:
                    await log(ctx, "Member not specified.", color=embedcolor("red"))
                    await ctx.message.delete()

                elif '@' in str(member):
                    member = await bot.fetch_user(int(member[3:21]))
                    with open('data/logs/loggedusers.txt', 'r+') as logfile:
                        content = logfile.read()
                        lines = content.split("\n")
                        if f"{member.id}" in lines:
                            await log(ctx, "User is already logged.", color=embedcolor("red"))
                        else:
                            logfile.write(f"{member.id}\n")
                            try:
                                embed = discord.embeds.Embed(
                                    title="Logged User Added",
                                    colour=embedcolor()
                                )
                                embed.add_field(
                                    name="User",
                                    value=f"{member}"
                                )
                                embed.add_field(
                                    name="ID",
                                    value=f"{member.id}"
                                )
                                embed.set_thumbnail(url=member.avatar_url)
                                footer(embed)
                                await ctx.reply(embed=embed)
                            except Exception as e:
                                await simple_codeblock(ctx, f"[ Logged User Added ]\n\n"
                                                            f"[ User ]\n"
                                                            f"{member}\n\n"
                                                            f"[ ID ]\n"
                                                            f"{member.id}")

                else:

                    # counts the amount of numbers in string
                    count = 0
                    for x in str(member):
                        count += 1

                    # if the amount of numbers is 18 then it is a possible user id
                    if count == 18:
                        with open('data/logs/loggedusers.txt', 'r+') as logfile:
                            content = logfile.read()
                            lines = content.split("\n")
                            if f"{member}" in lines:
                                await ctx.message.delete()
                                await log(ctx, "User is already logged.", color=embedcolor())
                            else:
                                notfound = False

                                # try to find member by id
                                try:
                                    member = await bot.fetch_user(member)
                                except discord.errors.NotFound:
                                    notfound = True
                                if notfound:
                                    logfile.write(f"{member}\n")
                                else:
                                    logfile.write(f"{member.id}\n")
                                try:
                                    embed = discord.embeds.Embed(
                                        title="Logged User Added",
                                        colour=embedcolor()
                                    )
                                    if notfound:
                                        embed.add_field(
                                            name="User",
                                            value=f"UKNOWN"
                                        )
                                        embed.add_field(
                                            name="ID",
                                            value=f"{member}"
                                        )
                                        embed.set_thumbnail(url='https://cdn.drawception.com'
                                                                '/drawings/848910/l0ZT9m55a0.png')
                                    else:
                                        embed.add_field(
                                            name="User",
                                            value=f"{member}"
                                        )
                                        embed.add_field(
                                            name="ID",
                                            value=f"{member.id}"
                                        )
                                        embed.set_thumbnail(url=member.avatar_url)
                                    footer(embed)
                                    await ctx.reply(embed=embed)
                                except Exception as e:
                                    if notfound:
                                        await simple_codeblock(ctx, f"[ Logged User Added ]\n\n"
                                                                    f"[ User ]\n"
                                                                    f"UNKNOWN\n\n"
                                                                    f"[ ID ]\n"
                                                                    f"{member}")
                                    else:
                                        await simple_codeblock(ctx, f"[ Logged User Added ]\n\n"
                                                                    f"[ User ]\n"
                                                                    f"{member}\n\n"
                                                                    f"[ ID ]\n"
                                                                    f"{member.id}")
                    else:
                        await log(ctx, "Invalid user ID.", color=embedcolor("red"))

            elif action.lower() == "remove":
                if member is None:
                    await log(ctx, "Member not specified.", color=embedcolor("red"))
                    await ctx.message.delete()

                elif '@' in str(member):
                    member = await bot.fetch_user(int(member[3:21]))
                    logfile = open("data/logs/loggedusers.txt", "r")
                    content = logfile.read()
                    lines = content.split("\n")
                    temp = ""
                    if f"{member.id}" in str(lines):
                        for x in lines:
                            if x:
                                if int(x) == member.id:
                                    pass
                                else:
                                    temp += f"{x}\n"
                        with open('data/logs/loggedusers.txt', 'w', encoding='utf8') as file:
                            file.write(temp)
                        try:
                            embed = discord.embeds.Embed(
                                title="Logged User Removed",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name="User",
                                value=f"{member}"
                            )
                            embed.add_field(
                                name="ID",
                                value=f"{member.id}"
                            )
                            embed.set_thumbnail(url=member.avatar_url)
                            footer(embed)
                            await ctx.reply(embed=embed)
                        except Exception as e:
                            await simple_codeblock(ctx, "[ Logged User Removed ]\n\n"
                                                        "[ User ]\n"
                                                        f"{member}\n\n"
                                                        f"[ ID ]\n"
                                                        f"{member.id}")
                    else:
                        await ctx.message.delete()
                        await log(ctx, "That user isn't being logged.", color=embedcolor("red"))

                else:
                    count = 0
                    for x in f"{member}":
                        count += 1
                    if count == 18:
                        temp = ""
                        logfile = open("data/logs/logfile.txt", "r")
                        content = oldfile.read()
                        lines = content.split("\n")
                        if f"{member}" in str(lines):
                            for x in lines:
                                if x:
                                    if int(x) == member:
                                        pass
                                    else:
                                        temp += f"{x}\n"
                            with open('data/logs/loggedusers.txt', 'w', encoding='utf8') as file:
                                file.write(temp)
                            notfound = False
                            try:
                                member = await bot.fetch_user(member)
                            except discord.errors.NotFound:
                                notfound = True
                            try:
                                embed = discord.embeds.Embed(
                                    title="Logged User Removed",
                                    colour=embedcolor()
                                )
                                if notfound:
                                    embed.add_field(
                                        name="User",
                                        value="UNKNOWN"
                                    )
                                    embed.add_field(
                                        name="ID",
                                        value=f"{member}"
                                    )
                                    embed.set_thumbnail(url='https://cdn.drawception.com'
                                                            '/drawings/848910/l0ZT9m55a0.png')
                                else:
                                    embed.add_field(
                                        name="User",
                                        value=f"{member}"
                                    )
                                    embed.add_field(
                                        name="ID",
                                        value=f"{member}"
                                    )
                                    embed.set_thumbnail(url=member.avatar_url)
                                footer(embed)
                                await ctx.reply(embed=embed)
                            except Exception as e:
                                if notfound:
                                    await simple_codeblock(ctx, "[ Logged User Removed ]\n\n"
                                                                "[ User ]\n"
                                                                f"UNKNOWN\n\n"
                                                                f"[ ID ]\n"
                                                                f"{member}")
                                else:
                                    await simple_codeblock(ctx, "[ Logged User Removed ]\n\n"
                                                                "[ User ]\n"
                                                                f"{member}\n\n"
                                                                f"[ ID ]\n"
                                                                f"{member.id}")
                        else:
                            await ctx.message.delete()
                            await log(ctx, "That user isn't being logged.", color=embedcolor())
                    elif count == 3:
                        if str(member).lower() == "all":
                            with open('data/logs/loggedusers.txt', 'w+', encoding='utf8') as file:
                                file.write("")
                                try:
                                    await simple_embed(ctx,
                                                       title="Logged User List",
                                                       description="**Successfully removed all users.**")
                                except Exception as e:
                                    await simple_codeblock(ctx,
                                                           "[ Logged User List ]\n"
                                                           "Successfully removed all users.")
                    else:
                        await ctx.message.delete()
                        await log(ctx, "Invalid User ID", color=embedcolor())

    @commands.Cog.listener()
    async def on_message(self, ctx):
        logfile = open('data/logs/loggedusers.txt', 'r+')
        content = logfile.read()
        lines = content.split('\n')
        if f'{ctx.author.id}' in lines:
            if not os.path.exists(f'data/logs/users/{ctx.author.id}.txt'):
                open(f'data/logs/users/{ctx.author.id}.txt', 'a+')
            text = f"{ctx.content}".replace('\n', ' ')
            if not ctx.content:
                text = "EMBEDDED MESSAGE"
            with open(f'data/logs/users/{ctx.author.id}.txt', 'a+', encoding='utf8') as logfile:
                logfile.write(f"[{time.localtime().tm_mon}.{time.localtime().tm_mday}.{time.localtime().tm_year} "
                              f"- {time.localtime().tm_hour}:{time.localtime().tm_min}]"
                              f"[{ctx.guild}][{ctx.author}]> {text}\n")


def setup(userbot):
    userbot.add_cog(UserLog(userbot))
