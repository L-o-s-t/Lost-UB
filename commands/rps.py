from bot import *


class RPS(commands.Cog):
    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def rps(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use RPS"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use RPS"))
        else:
            print(log(ctx, description="This user used the command RPS"))
            await ctx.simple_codeblock(ctx, f"[ Rock, Paper, Scissors Game]\n"
                                            f"What is your choice?\n\n"
                                            f"[ Choices ]\n"
                                            f"Rock\n"
                                            f"Paper\n"
                                            f"Scissors\n\n")
                                            

            def check(m):
                return m.author == ctx.author

            try:
                answer = await bot.wait_for("message", check=check, timeout=60.0)
                rps_choice = random.choice(['rock', 'paper', 'scissors'])
                result = ""
                if answer.content.lower() == "rock":
                    if rps_choice == "rock":
                        result = "It's a tie!"
                    elif rps_choice == "paper":
                        result = "You lost!"
                    elif rps_choice == "scissors":
                        result = "You won!"
                elif answer.content.lower() == "paper":
                    if rps_choice == "rock":
                        result = "You won!"
                    elif rps_choice == "paper":
                        result = "It's a tie!"
                    elif rps_choice == "scissors":
                        result = "You lost!"
                elif answer.content.lower() == "scissors":
                    if rps_choice == "rock":
                        result = "You lost!"
                    elif rps_choice == "paper":
                        result = "You won!"
                    elif rps_choice == "scissors":
                        result = "It's a tie!"
                else:
                    await simple_codeblock(ctx, f"[ Rock, Paper, Scissors Game Results! ]\n"
                                                f"Those weren't any of the choices!")
                    return
                await simple_codeblock(ctx, f"[ Rock, Paper, Scissors Game Results! ]\n"
                                            f"{result}\n\n"
                                            f"[ Your Choice ]\n"
                                            f"{answer.content.lower()}\n\n"
                                            f"[ CPU's Choice ]\n"
                                            f"{rps_choice}")
            except asyncio.TimeoutError:
                await simple_codeblock(ctx, f"[ Error ]\n"
                                            f"You took too long to respond!")


def setup(userbot):
    userbot.add_cog(RPS(userbot))
