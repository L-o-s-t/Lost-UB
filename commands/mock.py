from bot import *


class Mock(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def mock(self, ctx, *, message: str = None):
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
            await ctx.send(mocked_msg)
        await ctx.message.delete()


def setup(userbot):
    userbot.add_cog(Mock(userbot))