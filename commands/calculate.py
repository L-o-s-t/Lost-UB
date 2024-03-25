from bot import *


class Calculate(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command(aliases=['calc'])
    async def calculate(self, ctx, first_number: str = None, operator: str = None, second_number: str = None):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use CALCULATE"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use CALCULATE"))
        else:
            print(log(ctx, description="This user used the command CALCULATE"))
            operators = ['*', '/', '+', '-']
            result = ""
            if not first_number.isnumeric():
                await ctx.message.delete()
                await ctx.reply(f"Invalid argument(s). {first_number} is not a number.")
            else:
                if operator not in operators:
                    await ctx.message.delete()
                    await ctx.reply(f"Invalid argument(s). {operator} is not an operator.")
                else:
                    if not second_number.isnumeric():
                        await ctx.message.delete()
                        await ctx.reply(f"Invalid argument(s). {first_number} is not a number.")
                    else:
                        if operator == "*":
                            result = int(first_number) * int(second_number)
                        elif operator == "/":
                            result = int(first_number) / int(second_number)
                        elif operator == "+":
                            result = int(first_number) + int(second_number)
                        elif operator == "-":
                            result = int(first_number) - int(second_number)
                        await simple_codeblock(ctx,
                                                f"[ Calculator ]\n"
                                                f"Equation: {first_number} {operator} {second_number}\n"
                                                f"Result: {result}")


def setup(userbot):
    userbot.add_cog(Calculate(userbot))
