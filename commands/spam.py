from bot import *


class Spam(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def spam(self, ctx, delay: str = None, count: str = None, *, message: str = None):
        if bot.user == ctx.author:
            await log(ctx, description="This user used the command SPAM", color=embedcolor())
            await ctx.message.delete()
            if delay is None:
                await log(ctx, description=f"Missing required arguments.\n"
                                           f"Usage: {get_prefix()}spam [delay] [count] [message]",
                          color=embedcolor("red"))
            elif not delay.isnumeric():
                await log(ctx, description=f"Invalid arguments, '{delay}' is not a number.", color=embedcolor("red"))
            else:
                if count is None:
                    await log(ctx, description=f"Missing required arguments.\n"
                                               f"Usage: {get_prefix()}spam [delay] [count] [message]",
                              color=embedcolor("red"))
                elif not count.isnumeric():
                    await log(ctx, description=f"Invalid arguments, '{count}' is not a number.",
                              color=embedcolor("red"))
                else:
                    if message is None:
                        await log(ctx, description=f"Missing required arguments. "
                                                   f"{get_prefix()}spam [delay] [count] [message]",
                                  color=embedcolor("red"))
                    elif message is None:
                        await log(ctx, description=f"You have to specify what you want to spam!",
                                  color=embedcolor("red"))
                    else:
                        counter = 0
                        while counter < int(count):
                            await ctx.send(message)
                            time.sleep(int(delay))
                            counter += 1

    @commands.command()
    async def spamall(self, ctx, *, message: str = None):
        if ctx.author == bot.user:
            await log(ctx, description="This user used the command SPAMALL", color=embedcolor())
            await ctx.message.delete()
            if message is None:
                await log(ctx, description=f"You must specify a message. {get_prefix()}spamall [message]",
                          color=embedcolor("red"))
            else:
                for channels in ctx.guild.channels:
                    try:
                        await channels.send(message)
                    except AttributeError:
                        pass
                    except discord.Forbidden:
                        pass


def setup(userbot):
    userbot.add_cog(Spam(userbot))
