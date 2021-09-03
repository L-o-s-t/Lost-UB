from bot import *


class Mock(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def mock(self, ctx, *, message: str = None):
        if blacklist_check(ctx):
            log(ctx, "BLACKLIST", f"{ctx.author.display_name} tried to use the command MOCK.")
        else:
            if message is None:
                log(ctx, f"ERROR", "You must specify a message to mock!")
            else:
                count = 0
                mocked_msg = ""
                for x in message:
                    if count % 2 == 0:
                        mocked_msg += f"{x.upper()}"
                    else:
                        mocked_msg += f"{x.lower()}"
                    count += 1
                if ctx.author != bot.user:
                    await ctx.reply(f"> {ctx.author}: {ctx.message.content}\n"
                                    f"{mocked_msg}")
                elif ctx.author == bot.user:
                    await ctx.send(mocked_msg)
            if ctx.author == bot.user:
                await ctx.message.delete()
            else:
                pass


def setup(userbot):
    userbot.add_cog(Mock(userbot))