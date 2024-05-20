from bot import *


class Mock(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def mock(self, ctx, *, message: str = None):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use MOCK"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use MOCK"))
        else:
            if message is None:
                print(log(ctx, f"ERROR", "You must specify a message to mock!"))
            else:
                print(log(ctx, description="This user used the command HELP"))
                count = 0
                mocked_msg = ""
                for x in message:
                    if count % 2 == 0:
                        mocked_msg += f"{x.upper()}"
                    else:
                        mocked_msg += f"{x.lower()}"
                    count += 1
                if ctx.author == bot.user:
                    await ctx.send(mocked_msg)
            if ctx.author == bot.user:
                await ctx.message.delete()

    @commands.command()
    async def automock(self, ctx, action: str = None, member=None):

        # if command author is bot user:
        if ctx.author == bot.user:

            # if member is none:
            if action is None:
                with open('data/automock.txt', 'r', encoding="utf8") as oldfile:
                    content = oldfile.read()
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
                            await simple_codeblock(ctx, f"[ AutoMock User List ]\n"
                                                        f"These Users will automatically be mocked.\n"
                                                        f"{description} + {remainder} more...\n\n"
                                                        f"[ Total AutoMocked Users ]\n"
                                                        f"{count}")
                    elif count != 0:
                        await simple_codeblock(ctx, f"[ AutoMock User List ]\n"
                                                    f"{description}\n\n"
                                                    f"[ Total AutoMocked Users ]\n"
                                                    f"{count}")
                    else:
                        await simple_codeblock(ctx, f"[ AutoMock User List ]\n"
                                                    f"No automocked users yet...\n\n")

            # else if "#" in member:
            elif action.lower() == "add":
                if member is None:
                    print(log(ctx, "Member not specified."))
                    await ctx.message.delete()

                elif '@' in str(member):
                    member = await bot.fetch_user(int(member[3:21]))
                    with open('data/automock.txt', 'r+') as oldfile:
                        content = oldfile.read()
                        lines = content.split("\n")
                        if f"{member.id}" in lines:
                            print(log(ctx, "User is already automocked."))
                        else:
                            oldfile.write(f"{member.id}\n")
                            await simple_codeblock(ctx, f"[ AutoMock User Added ]\n\n"
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
                        with open('data/automock.txt', 'r+') as oldfile:
                            content = oldfile.read()
                            lines = content.split("\n")
                            if f"{member}" in lines:
                                await ctx.message.delete()
                                print(log(ctx, "User is already automocked."))
                            else:
                                notfound = False

                                # try to find member by id
                                try:
                                    member = await bot.fetch_user(member)
                                except discord.errors.NotFound:
                                    notfound = True
                                if notfound:
                                    oldfile.write(f"{member}\n")
                                else:
                                    oldfile.write(f"{member.id}\n")
                                if notfound:
                                    await simple_codeblock(ctx, f"[ AutoMock User Added ]\n\n"
                                                                f"[ User ]\n"
                                                                f"UNKNOWN\n\n"
                                                                f"[ ID ]\n"
                                                                f"{member}")
                                else:
                                    await simple_codeblock(ctx, f"[ AutoMock User Added ]\n\n"
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
                    oldfile = open("data/automock.txt", "r")
                    content = oldfile.read()
                    lines = content.split("\n")
                    temp = ""
                    if f"{member.id}" in str(lines):
                        for x in lines:
                            if x:
                                if int(x) == member.id:
                                    pass
                                else:
                                    temp += f"{x}\n"
                        with open('data/automock.txt', 'w', encoding='utf8') as file:
                            file.write(temp)
                        await simple_codeblock(ctx, f"[ Automock User Removed ]\n\n"
                                                    f"[ User ]\n"
                                                    f"{member}\n\n"
                                                    f"[ ID ]\n"
                                                    f"{member.id}")
                    else:
                        await ctx.message.delete()
                        print(log(ctx, "That user isn't being automocked."))

                else:
                    count = 0
                    for x in f"{member}":
                        count += 1
                    if count == 18:
                        temp = ""
                        oldfile = open("data/automock.txt", "r")
                        content = oldfile.read()
                        lines = content.split("\n")
                        if f"{member}" in str(lines):
                            for x in lines:
                                if x:
                                    if int(x) == int(member):
                                        pass
                                    else:
                                        temp += f"{x}\n"
                            with open('data/automock.txt', 'w', encoding='utf8') as file:
                                file.write(temp)
                            notfound = False
                            try:
                                member = await bot.fetch_user(member)
                            except discord.errors.NotFound:
                                notfound = True
                            if notfound:
                                await simple_codeblock(ctx, "[ Automock User Removed ]\n\n"
                                                            "[ User ]\n"
                                                            f"UNKNOWN\n\n"
                                                            f"[ ID ]\n"
                                                            f"{member}")
                            else:
                                await simple_codeblock(ctx, "[ Automock User Removed ]\n\n"
                                                            "[ User ]\n"
                                                            f"{member}\n\n"
                                                            f"[ ID ]\n"
                                                            f"{member.id}")
                        else:
                            await ctx.message.delete()
                            print(log(ctx, "That user isn't being automocked."))
                    elif count == 3:
                        if str(member).lower() == "all":
                            with open('data/automock.txt', 'w+', encoding='utf8') as file:
                                file.write("")
                                await simple_codeblock(ctx, f"[ AutoMock User List ]\n"
                                                            f"Successfully removed all users.")
                    else:
                        await ctx.message.delete()
                        print(log(ctx, "Invalid User ID"))

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if config['CONFIGURATION']['automock'] == "True":
            with open('data/automock.txt', 'r', encoding='utf8') as file:
                content = file.read()
                users = content.split("\n")
                if f"{ctx.author.id}" in users:
                    if f"{ctx.content}".startswith(f"{get_prefix()}"):
                        print(log(ctx, "AutoMocked message starts with prefix, skipping..."))
                    else:
                        count = 0
                        mocked_msg = ""
                        for x in ctx.content:
                            if count % 2 == 0:
                                mocked_msg += f"{x.upper()}"
                            else:
                                mocked_msg += f"{x.lower()}"
                            count += 1
                        await ctx.send(mocked_msg + " 🤡")


def setup(userbot):
    userbot.add_cog(Mock(userbot))
