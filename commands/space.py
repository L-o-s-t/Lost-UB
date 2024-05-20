from bot import *


class Space(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def space(self, ctx, *, message):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use SPACE"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use SPACE"))
        else:
            uppercase_spacing = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
            lowercase_spacing = "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    
            if message is None:
                print(log(ctx, description="This user used the command SPACE"))
            else:
                space_message = ""
                for x in message:
                    if x == "A":
                        space_message += uppercase_spacing[0]
                    elif x == "a":
                        space_message += lowercase_spacing[0]
                    elif x == "B":
                        space_message += uppercase_spacing[1]
                    elif x == "b":
                        space_message += lowercase_spacing[1]
                    elif x == "C":
                        space_message += uppercase_spacing[2]
                    elif x == "c":
                        space_message += lowercase_spacing[2]
                    elif x == "D":
                        space_message += uppercase_spacing[3]
                    elif x == "d":
                        space_message += lowercase_spacing[3]
                    elif x == "E":
                        space_message += uppercase_spacing[4]
                    elif x == "e":
                        space_message += lowercase_spacing[4]
                    elif x == "F":
                        space_message += uppercase_spacing[5]
                    elif x == "f":
                        space_message += lowercase_spacing[5]
                    elif x == "G":
                        space_message += uppercase_spacing[6]
                    elif x == "g":
                        space_message += lowercase_spacing[6]
                    elif x == "H":
                        space_message += uppercase_spacing[7]
                    elif x == "h":
                        space_message += lowercase_spacing[7]
                    elif x == "I":
                        space_message += uppercase_spacing[8]
                    elif x == "i":
                        space_message += lowercase_spacing[8]
                    elif x == "J":
                        space_message += uppercase_spacing[9]
                    elif x == "j":
                        space_message += lowercase_spacing[9]
                    elif x == "K":
                        space_message += uppercase_spacing[10]
                    elif x == "k":
                        space_message += lowercase_spacing[10]
                    elif x == "L":
                        space_message += uppercase_spacing[11]
                    elif x == "l":
                        space_message += lowercase_spacing[11]
                    elif x == "M":
                        space_message += uppercase_spacing[12]
                    elif x == "m":
                        space_message += lowercase_spacing[12]
                    elif x == "N":
                        space_message += uppercase_spacing[13]
                    elif x == "n":
                        space_message += lowercase_spacing[13]
                    elif x == "O":
                        space_message += uppercase_spacing[14]
                    elif x == "o":
                        space_message += lowercase_spacing[14]
                    elif x == "P":
                        space_message += uppercase_spacing[15]
                    elif x == "p":
                        space_message += lowercase_spacing[15]
                    elif x == "Q":
                        space_message += uppercase_spacing[16]
                    elif x == "q":
                        space_message += lowercase_spacing[16]
                    elif x == "R":
                        space_message += uppercase_spacing[17]
                    elif x == "r":
                        space_message += lowercase_spacing[17]
                    elif x == "S":
                        space_message += uppercase_spacing[18]
                    elif x == "s":
                        space_message += lowercase_spacing[18]
                    elif x == "T":
                        space_message += uppercase_spacing[19]
                    elif x == "t":
                        space_message += lowercase_spacing[19]
                    elif x == "U":
                        space_message += uppercase_spacing[20]
                    elif x == "u":
                        space_message += lowercase_spacing[20]
                    elif x == "V":
                        space_message += uppercase_spacing[21]
                    elif x == "v":
                        space_message += lowercase_spacing[21]
                    elif x == "W":
                        space_message += uppercase_spacing[22]
                    elif x == "w":
                        space_message += lowercase_spacing[22]
                    elif x == "X":
                        space_message += uppercase_spacing[23]
                    elif x == "x":
                        space_message += lowercase_spacing[23]
                    elif x == "Y":
                        space_message += uppercase_spacing[24]
                    elif x == "y":
                        space_message += lowercase_spacing[24]
                    elif x == "Z":
                        space_message += uppercase_spacing[25]
                    elif x == "z":
                        space_message += lowercase_spacing[25]
                    else:
                        space_message += x
                if ctx.author == bot.user:
                    await ctx.send(space_message)
            if ctx.author == bot.user:
                await ctx.message.delete()
            else:
                pass


def setup(userbot):
    userbot.add_cog(Space(userbot))
