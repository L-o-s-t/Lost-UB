from bot import *


class UserLog(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def userlog(self, ctx, action: str = None, member=None):
        print(log(ctx, description="This user used the command USERLOG"))

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
                    if remainder >= 1:
                            await simple_codeblock(ctx, f"These users will automatically be logged.\n"
                                                        f"{description} + {remainder} more...\n"
                                                        f"Total Logged Users: {count}")
                    elif count != 0:
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
                    print(log(ctx, "Member not specified."))
                    await ctx.message.delete()

                elif '@' in str(member):
                    member = await bot.fetch_user(int(member[3:21]))
                    with open('data/logs/loggedusers.txt', 'r+') as logfile:
                        content = logfile.read()
                        lines = content.split("\n")
                        if f"{member.id}" in lines:
                            print(log(ctx, "User is already logged."))
                        else:
                            logfile.write(f"{member.id}\n")
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
                                print(log(ctx, "User is already logged."))
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
                        print(log(ctx, "Invalid user ID."))

            elif action.lower() == "remove":
                if member is None:
                    print(log(ctx, "Member not specified."))
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
                        await simple_codeblock(ctx, f"[ Logged User Removed ]\n\n"
                                                    f"[ User ]\n"
                                                    f"{member}\n\n"
                                                    f"[ ID ]\n"
                                                    f"{member.id}")
                    else:
                        await ctx.message.delete()
                        print(log(ctx, "That user isn't being logged."))

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
                            if notfound:
                                await simple_codeblock(ctx, f"[ Logged User Removed ]\n\n"
                                                            f"[ User ]\n"
                                                            f"UNKNOWN\n\n"
                                                            f"[ ID ]\n"
                                                            f"{member}")
                            else:
                                await simple_codeblock(ctx, f"[ Logged User Removed ]\n\n"
                                                            f"[ User ]\n"
                                                            f"{member}\n\n"
                                                            f"[ ID ]\n"
                                                            f"{member.id}")
                        else:
                            await ctx.message.delete()
                            print(log(ctx, "That user isn't being logged."))
                    elif count == 3:
                        if str(member).lower() == "all":
                            with open('data/logs/loggedusers.txt', 'w+', encoding='utf8') as file:
                                file.write("")
                                await simple_codeblock(ctx, "[ Logged User List ]\n"
                                                            "Successfully removed all users.")
                    else:
                        await ctx.message.delete()
                        print(log(ctx, "Invalid User ID"))

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
