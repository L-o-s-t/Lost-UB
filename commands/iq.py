from bot import *


class IQ(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def iq(self, ctx, member: discord.Member):
        if blacklist_check(ctx):
            await ctx.reply("You are blacklisted!")
        else:
            log(ctx, "IQ")
            result = ""
            iq_rating = random.randrange(0, 199)
            if iq_rating <= 69:
                result = "Extremely Low"
            elif 70 <= iq_rating <= 79:
                result = "Borderline"
            elif 80 <= iq_rating <= 89:
                result = "Low Average"
            elif 90 <= iq_rating <= 109:
                result = "Average"
            elif 110 <= iq_rating <= 119:
                result = "High Average"
            elif 120 <= iq_rating <= 129:
                result = "Superior"
            elif iq_rating >= 130:
                result = "Very Superior"
            try:
                embed = discord.embeds.Embed(
                    title=f"{member.display_name}'s IQ Rating",
                    description=f"{member}'s IQ is {iq_rating}",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Rating",
                    value=f"{result}"
                )
                embed.add_field(
                    name="IQ Classification",
                    value="130 and above: Very Superior\n"
                          "120 - 129:     Superior\n"
                          "110 - 119:     High Average\n"
                          "90 - 109:      Average\n"
                          "80 - 89:       Low Average\n"
                          "70 - 79:       Borderline\n"
                          "69 and below:  Extremely Low"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await ctx.reply(f"```ini\n"
                                f"[ {member.display_name}'s IQ Rating ]\n"
                                f"{member.display_name}'s IQ is [ {iq_rating} ]\n\n"
                                f"[ IQ Classification ]\n"
                                "130 and above: Very Superior\n"
                                f"120 - 129:     Superior\n"
                                f"110 - 119:     High Average\n"
                                f"90 - 109:      Average\n"
                                f"80 - 89:       Low Average\n"
                                f"70 - 79:       Borderline\n"
                                f"69 and below:  Extremely Low\n\n"
                                f"{codeblock_footer()}"
                                f"```")


def setup(userbot):
    userbot.add_cog(IQ(userbot))
