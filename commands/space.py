from bot import *


class Space(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def spacing(self, ctx, *, message):

        uppercase_spacing = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
        lowercase_spacing = "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"

        if message is None:
            log(ctx, "ERROR", "You must specify a message you want monospaced!")
        else:
            cursive_message = ""
            for x in message:
                if x == "A":
                    cursive_message += uppercase_spacing[0]
                elif x == "a":
                    cursive_message += lowercase_spacing[0]
                elif x == "B":
                    cursive_message += uppercase_spacing[1]
                elif x == "b":
                    cursive_message += lowercase_spacing[1]
                elif x == "C":
                    cursive_message += uppercase_spacing[2]
                elif x == "c":
                    cursive_message += lowercase_spacing[2]
                elif x == "D":
                    cursive_message += uppercase_spacing[3]
                elif x == "d":
                    cursive_message += lowercase_spacing[3]
                elif x == "E":
                    cursive_message += uppercase_spacing[4]
                elif x == "e":
                    cursive_message += lowercase_spacing[4]
                elif x == "F":
                    cursive_message += uppercase_spacing[5]
                elif x == "f":
                    cursive_message += lowercase_spacing[5]
                elif x == "G":
                    cursive_message += uppercase_spacing[6]
                elif x == "g":
                    cursive_message += lowercase_spacing[6]
                elif x == "H":
                    cursive_message += uppercase_spacing[7]
                elif x == "h":
                    cursive_message += lowercase_spacing[7]
                elif x == "I":
                    cursive_message += uppercase_spacing[8]
                elif x == "i":
                    cursive_message += lowercase_spacing[8]
                elif x == "J":
                    cursive_message += uppercase_spacing[9]
                elif x == "j":
                    cursive_message += lowercase_spacing[9]
                elif x == "K":
                    cursive_message += uppercase_spacing[10]
                elif x == "k":
                    cursive_message += lowercase_spacing[10]
                elif x == "L":
                    cursive_message += uppercase_spacing[11]
                elif x == "l":
                    cursive_message += lowercase_spacing[11]
                elif x == "M":
                    cursive_message += uppercase_spacing[12]
                elif x == "m":
                    cursive_message += lowercase_spacing[12]
                elif x == "N":
                    cursive_message += uppercase_spacing[13]
                elif x == "n":
                    cursive_message += lowercase_spacing[13]
                elif x == "O":
                    cursive_message += uppercase_spacing[14]
                elif x == "o":
                    cursive_message += lowercase_spacing[14]
                elif x == "P":
                    cursive_message += uppercase_spacing[15]
                elif x == "p":
                    cursive_message += lowercase_spacing[15]
                elif x == "Q":
                    cursive_message += uppercase_spacing[16]
                elif x == "q":
                    cursive_message += lowercase_spacing[16]
                elif x == "R":
                    cursive_message += uppercase_spacing[17]
                elif x == "r":
                    cursive_message += lowercase_spacing[17]
                elif x == "S":
                    cursive_message += uppercase_spacing[18]
                elif x == "s":
                    cursive_message += lowercase_spacing[18]
                elif x == "T":
                    cursive_message += uppercase_spacing[19]
                elif x == "t":
                    cursive_message += lowercase_spacing[19]
                elif x == "U":
                    cursive_message += uppercase_spacing[20]
                elif x == "u":
                    cursive_message += lowercase_spacing[20]
                elif x == "V":
                    cursive_message += uppercase_spacing[21]
                elif x == "v":
                    cursive_message += lowercase_spacing[21]
                elif x == "W":
                    cursive_message += uppercase_spacing[22]
                elif x == "w":
                    cursive_message += lowercase_spacing[22]
                elif x == "X":
                    cursive_message += uppercase_spacing[23]
                elif x == "x":
                    cursive_message += lowercase_spacing[23]
                elif x == "Y":
                    cursive_message += uppercase_spacing[24]
                elif x == "y":
                    cursive_message += lowercase_spacing[24]
                elif x == "Z":
                    cursive_message += uppercase_spacing[25]
                elif x == "z":
                    cursive_message += lowercase_spacing[25]
                else:
                    cursive_message += x
            await ctx.send(cursive_message)
        await ctx.message.delete()


def setup(userbot):
    userbot.add_cog(Space(userbot))
