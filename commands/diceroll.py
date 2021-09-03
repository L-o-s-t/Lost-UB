from bot import *


class DiceRoll(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def diceroll(self, ctx):
        if blacklist_check(ctx):
            log(ctx, "BLACKLIST", f"{ctx.author.display_name} tried to use the command DICEROLL.")
        else:
            log(ctx, "ROLLADICE")
            number = random.randrange(1, 7)
            try:
                embed = discord.embeds.Embed(
                    title="Dice Roll",
                    description=f"You rolled a {number}",
                    colour=embedcolor()
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await simple_codeblock(ctx, f"[ Dice Roll ]\n"
                                            f"You rolled a {number}")


def setup(userbot):
    userbot.add_cog(DiceRoll(userbot))
