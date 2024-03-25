from bot import *


class DiceRoll(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def diceroll(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use DICEROLL"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use DICEROLL"))
        else:
            print(log(ctx, description="This user used the command DICEROLL"))
            number = random.randrange(1, 7)
            await simple_codeblock(ctx, f"[ Dice Roll ]\n"
                                        f"You rolled a {number}")


def setup(userbot):
    userbot.add_cog(DiceRoll(userbot))
