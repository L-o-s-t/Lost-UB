from bot import *


class Prefix(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def prefix(self, ctx, new_prefix: str = None):
        if ctx.author == bot.user:
            if new_prefix is None:
                await simple_codeblock(ctx, f"[ Prefix ]\n"
                                            f"Current prefix: {bot.command_prefix}")
            else:
                print(log(ctx, description="This user used the command PREFIX"))
                config["CONFIGURATION"]["prefix"] = new_prefix
                write()
                bot.command_prefix = new_prefix
                await simple_codeblock(ctx, f"[ Prefix ]\n"
                                            f"Prefix changed to: {new_prefix}")


def setup(userbot):
    userbot.add_cog(Prefix(userbot))
