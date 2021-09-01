from bot import *


class Prefix(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def prefix(self, ctx, x):
        if ctx.author == bot.user:
            log(ctx, "PREFIX")
            config["CONFIGURATION"]["prefix"] = x
            write()
            bot.command_prefix = x
            await ctx.reply(f'Prefix changed to: ``{x}``')


def setup(userbot):
    userbot.add_cog(Prefix(userbot))
