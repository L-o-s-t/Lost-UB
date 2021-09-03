from bot import *


class Calculate(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command(aliases=['calc'])
    async def calculate(self, ctx, first_number: str = None, operator: str = None, second_number: str = None):
        if blacklist_check(ctx):
            log(ctx, "BLACKLIST", f"{ctx.author.display_name} tried to use the command CALCULATOR.")
        else:
            log(ctx, "CALCULATE")
            operators = ['*', '/', '+', '-']
            result = ""
            if not first_number.isnumeric():
                await ctx.message.delete()
                log(ctx, "ERROR", f"Invalid argument(s). {first_number} is not a number.")
            else:
                if operator not in operators:
                    await ctx.message.delete()
                    log(ctx, "ERROR", f"Invalid argument(s). {operator} is not an operator.")
                else:
                    if not second_number.isnumeric():
                        await ctx.message.delete()
                        log(ctx, "ERROR", f"Invalid argument(s). {first_number} is not a number.")
                    else:
                        if operator == "*":
                            result = int(first_number) * int(second_number)
                        elif operator == "/":
                            result = int(first_number) / int(second_number)
                        elif operator == "+":
                            result = int(first_number) + int(second_number)
                        elif operator == "-":
                            result = int(first_number) - int(second_number)
                        try:
                            embed = discord.embeds.Embed(
                                title="Calculator",
                                description=f"Equation: {first_number} {operator} {second_number}\n"
                                            f"```{result}```",
                                colour=embedcolor()
                            )
                            await ctx.reply(embed=embed)
                        except discord.Forbidden:
                            await simple_codeblock(ctx,
                                                   f"[ Calculator ]\n"
                                                   f"Equation: {first_number} {operator} {second_number}\n"
                                                   f"Result: {result}")


def setup(userbot):
    userbot.add_cog(Calculate(userbot))
