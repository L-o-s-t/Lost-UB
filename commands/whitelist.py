import discord.ext.commands

from bot import *


class Whitelist(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def whitelist(self, ctx, action: str = None, member=None):
        # if command author is the bot user then...
        if ctx.author == bot.user:

            print(log(ctx, description="This user used the command WHITELIST"))  # logs to console

            # if action is nothing, it will fetch the whitelisted users
            if action is None:
                count = 10
                total = 0
                remainder = 0
                black_list = open("data/whitelist.txt", "r")
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
                    string = f"These users are allowed to use any command.\n" \
                                f"```{temp}" \
                                f"+ {remainder} more...```" \
                                f"Total Whitelisted Users: {total}"
                elif total == 0:
                        string = f"No whitelisted users yet...\n"
                else:
                    string = f"These users are allowed to use any command:\n\n" \
                                f"{temp}\n" \
                                f"[ Total Whitelisted Users ]\n" \
                                f"{total}"
                await simple_codeblock(ctx,
                                        f"[ Whitelisted Users ]\n"
                                        f"{string}")

            # if action is add, it will add the specified user
            elif action.lower() == "add":
                if member is None:
                    await ctx.reply(f"Command usage {get_prefix()}whitelist add (@member)")
                elif '@' in str(member):
                    member = await bot.fetch_user(int(member[3:21]))
                    old_file = open("data/whitelist.txt", "r")
                    oldfile_content = old_file.read()
                    lines = oldfile_content.split("\n")
                    if f"{member.id}" in lines:
                        await ctx.reply("That user is already whitelisted.")
                    else:
                        with open("data/whitelist.txt", "a+") as old_file:
                            old_file.write(f"{old_file.read()}"
                                           f"{member.id}\n")
                        await simple_codeblock(ctx, f"[ Whitelisted User Added ]\n\n"
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
                        old_file = open("data/whitelist.txt", "r")
                        oldfile_content = old_file.read()
                        lines = oldfile_content.split("\n")
                        if f"{member}" in lines:
                            await ctx.reply("That user is already whitelisted.")
                        else:
                            with open("data/whitelist.txt", "a+") as old_file:
                                if notfound:
                                    oldfile.write(f"{oldfile.read()}"
                                                  f"{member}\n")
                                else:
                                    oldfile.write(f"{oldfile.read()}"
                                                  f"{member.id}\n")
                            if notfound:
                                await simple_codeblock(ctx,
                                                        f"[ Whitelisted User Added ]\n\n"
                                                        f"[ User ]\n"
                                                        f"UKNOWN\n\n"
                                                        f"[ ID ]\n"
                                                        f"{member}")
                            else:
                                await simple_codeblock(ctx,
                                                        f"[ Whitelisted User Added ]\n\n"
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
                    await ctx.reply(f"Command usage {get_prefix()}whitelist remove (@member)")
                elif '@' in str(member):
                    member = await bot.fetch_user(int(member[3:21]))
                    temp = ""
                    black_list = open("data/whitelist.txt", "r")
                    black_list_content = black_list.read()
                    lines = black_list_content.split("\n")
                    if f"{member.id}" in lines:
                        for x in lines:
                            if x:
                                if int(x) == member.id:
                                    pass
                                else:
                                    temp += f"{x}\n"
                        with open("data/whitelist.txt", "w") as file:
                            file.write(temp)
                        await simple_codeblock(ctx, f"[ Whitelisted User Removed ]\n\n"
                                                    f"[ User ]\n"
                                                    f"{member}\n\n"
                                                    f"[ ID ]\n"
                                                    f"{member.id}")
                    else:
                        await ctx.reply("That user isn't whitelisted.")
                else:
                    count = 0
                    for x in f"{member}":
                        count += 1
                    if count == 18:
                        temp = ""
                        black_list = open("data/whitelist.txt", "r")
                        black_list_content = black_list.read()
                        lines = black_list_content.split("\n")
                        if f"{member}" in lines:
                            for x in lines:
                                if x:
                                    if int(x) == int(member):
                                        pass
                                    else:
                                        temp += f"{x}\n"
                            with open("data/whitelist.txt", "w") as file:
                                file.write(temp)
                            notfound = False
                            user = None
                            try:
                                user = await bot.fetch_user(member)
                            except discord.errors.NotFound:
                                notfound = True
                            if notfound:
                                await simple_codeblock(ctx,
                                                        f"[ Whitelisted User Removed ]\n\n"
                                                        f"[ User ]\n"
                                                        f"UNKNOWN\n\n"
                                                        f"[ ID ]\n"
                                                        f"{member}")
                            else:
                                await simple_codeblock(ctx,
                                                        f"[ Whitelisted User Removed ]\n\n"
                                                        f"[ User ]\n"
                                                        f"{user}\n\n"
                                                        f"[ ID ]\n"
                                                        f"{user.id}")
                        else:
                            await ctx.reply(f"That user isn't whitelisted.")
                    elif count == 3:
                        if str(member).lower() == "all":
                            with open('data/whitelist.txt', 'w+', encoding='utf8') as file:
                                file.write("")
                                await simple_codeblock(ctx, f"[ Whitelist ]\n"
                                                            f"Successfully removed all users.")
                    else:
                        await ctx.message.delete()
                        log(ctx, "ERROR", f"Invalid User ID.")

            # if action is none of the above, it will send an error to console
            else:
                log(ctx, "ERROR", f"{action.lower()} is not an action. "
                                  f"{get_prefix()}whitelist (add/remove) (@member/member_id)")
                await ctx.message.delete()


def setup(userbot):
    userbot.add_cog(Whitelist(userbot))
