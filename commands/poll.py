from bot import *


class Poll(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def poll(self, ctx, *, arguments: str = None):
        print(log(ctx, description="This user used the command POLL"))
        if ctx.author == bot.user:
            if arguments is None:
                await ctx.message.delete()
                print(log(ctx, "Missing required arguments."))
            else:
                title, description = arguments.split('| ')
                await ctx.message.delete()
                msg = await simple_codeblock(ctx, f"[ {title} ]\n"
                                                  f"{description}")
                await msg.add_reaction('✅')
                await msg.add_reaction('❎')


def setup(userbot):
    userbot.add_cog(Poll(userbot))
