from bot import *


class IQ(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def iq(self, ctx, member: discord.Member):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use IQ"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use IQ"))
        else:
            print(log(ctx, description="This user used the command IQ"))
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
            await simple_codeblock(ctx, f"[ {member.display_name}'s IQ Rating ]\n"
                                        f"{member.display_name}'s IQ is [ {iq_rating} ]\n\n"
                                        f"[ IQ Classification ]\n"
                                        "130 and above: Very Superior\n"
                                        f"120 - 129:     Superior\n"
                                        f"110 - 119:     High Average\n"
                                        f"90 - 109:      Average\n"
                                        f"80 - 89:       Low Average\n"
                                        f"70 - 79:       Borderline\n"
                                        f"69 and below:  Extremely Low\n\n")


def setup(userbot):
    userbot.add_cog(IQ(userbot))
