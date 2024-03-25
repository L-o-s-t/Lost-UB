from bot import *


class EightBall(commands.Cog):
    def __init__(self, userbot):
        self.bot = userbot

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question: str = None):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use EIGHTBALL"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use EIGHTBALL"))
        else:
            print(log(ctx, description="This user used the command EIGHTBALL"))
            if question is None:
                await ctx.reply(f'Incorrect arguments | {config["CONFIGURATION"]["prefix"]}8ball (question)')
            else:
                answers = random.choice(['It is Certain.',
                                         'It is decidedly so.',
                                         'Without a doubt.',
                                         'Yes definitely.',
                                         'You may rely on it.',
                                         'As I see it, yes.',
                                         'Most likely.',
                                         'Outlook good.',
                                         'Yes.',
                                         'Signs point to yes.',
                                         'Reply hazy, try again.',
                                         'Ask again later.',
                                         'Better not tell you now.',
                                         'Cannot predict now.',
                                         'Concentrate and ask again.',
                                         'Don\'t count on it.',
                                         'My reply is no.',
                                         'My sources say no.',
                                         'Outlook not so good.',
                                         'Very doubtful.'])
                ctx.reply(f"```ini\n"
                        f"[ Eight Ball ]\n"
                        f"{question}\n\n"
                        f"[ Answer ]\n"
                        f"{answers}\n\n"
                        f"{codeblock_footer()}"
                        f"```")


def setup(userbot):
    userbot.add_cog(EightBall(userbot))
