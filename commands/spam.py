from bot import *


class Spam(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def spam(self, ctx, delay: str = None, count: str = None, *, message: str = None):
        if bot.user == ctx.author:
            print(log(ctx, description="This user used the command SPAM"))
            await ctx.message.delete()
            if delay is None:
                print(log(ctx, description=f"Missing required arguments.\n"
                                           f"Usage: {get_prefix()}spam [delay] [count] [message]"))
            elif not delay.isnumeric():
                print(log(ctx, description=f"Invalid arguments, '{delay}' is not a number."))
            else:
                if count is None:
                    print(log(ctx, description=f"Missing required arguments.\n"
                                               f"Usage: {get_prefix()}spam [delay] [count] [message]"))
                elif not count.isnumeric():
                    print(log(ctx, description=f"Invalid arguments, '{count}' is not a number."))
                else:
                    if message is None:
                        print(log(ctx, description=f"Missing required arguments. "
                                                   f"{get_prefix()}spam [delay] [count] [message]"))
                    elif message is None:
                        print(log(ctx, description=f"You have to specify what you want to spam!"))
                    else:
                        counter = 0
                        while counter < int(count):
                            await ctx.send(message)
                            time.sleep(int(delay))
                            counter += 1

    @commands.command()
    async def spamall(self, ctx, *, message: str = None):
        if ctx.author == bot.user:
            print(log(ctx, description="This user used the command SPAMALL"))
            await ctx.message.delete()
            if message is None:
                print(log(ctx, description=f"You must specify a message. {get_prefix()}spamall [message]"))
            else:
                for channels in ctx.guild.channels:
                    try:
                        await channels.send(message)
                    except AttributeError:
                        pass
                    except Exception as e:
                        pass


def setup(userbot):
    userbot.add_cog(Spam(userbot))
