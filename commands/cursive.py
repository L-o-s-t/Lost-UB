from bot import *


class Cursive(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def cursive(self, ctx, *, message):

        if blacklist_check(ctx):
            log(ctx, "BLACKLIST", f"{ctx.author.display_name} tried to use the command CURSIVE.")
        else:

            uppercase_cursive = "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩"
            lowercase_cursive = "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"

            if message is None:
                log(ctx, "ERROR", "You must specify a message you want in cursive!")
            else:
                cursive_message = ""
                for x in message:
                    if x == "A":
                        cursive_message += uppercase_cursive[0]
                    elif x == "a":
                        cursive_message += lowercase_cursive[0]
                    elif x == "B":
                        cursive_message += uppercase_cursive[1]
                    elif x == "b":
                        cursive_message += lowercase_cursive[1]
                    elif x == "C":
                        cursive_message += uppercase_cursive[2]
                    elif x == "c":
                        cursive_message += lowercase_cursive[2]
                    elif x == "D":
                        cursive_message += uppercase_cursive[3]
                    elif x == "d":
                        cursive_message += lowercase_cursive[3]
                    elif x == "E":
                        cursive_message += uppercase_cursive[4]
                    elif x == "e":
                        cursive_message += lowercase_cursive[4]
                    elif x == "F":
                        cursive_message += uppercase_cursive[5]
                    elif x == "f":
                        cursive_message += lowercase_cursive[5]
                    elif x == "G":
                        cursive_message += uppercase_cursive[6]
                    elif x == "g":
                        cursive_message += lowercase_cursive[6]
                    elif x == "H":
                        cursive_message += uppercase_cursive[7]
                    elif x == "h":
                        cursive_message += lowercase_cursive[7]
                    elif x == "I":
                        cursive_message += uppercase_cursive[8]
                    elif x == "i":
                        cursive_message += lowercase_cursive[8]
                    elif x == "J":
                        cursive_message += uppercase_cursive[9]
                    elif x == "j":
                        cursive_message += lowercase_cursive[9]
                    elif x == "K":
                        cursive_message += uppercase_cursive[10]
                    elif x == "k":
                        cursive_message += lowercase_cursive[10]
                    elif x == "L":
                        cursive_message += uppercase_cursive[11]
                    elif x == "l":
                        cursive_message += lowercase_cursive[11]
                    elif x == "M":
                        cursive_message += uppercase_cursive[12]
                    elif x == "m":
                        cursive_message += lowercase_cursive[12]
                    elif x == "N":
                        cursive_message += uppercase_cursive[13]
                    elif x == "n":
                        cursive_message += lowercase_cursive[13]
                    elif x == "O":
                        cursive_message += uppercase_cursive[14]
                    elif x == "o":
                        cursive_message += lowercase_cursive[14]
                    elif x == "P":
                        cursive_message += uppercase_cursive[15]
                    elif x == "p":
                        cursive_message += lowercase_cursive[15]
                    elif x == "Q":
                        cursive_message += uppercase_cursive[16]
                    elif x == "q":
                        cursive_message += lowercase_cursive[16]
                    elif x == "R":
                        cursive_message += uppercase_cursive[17]
                    elif x == "r":
                        cursive_message += lowercase_cursive[17]
                    elif x == "S":
                        cursive_message += uppercase_cursive[18]
                    elif x == "s":
                        cursive_message += lowercase_cursive[18]
                    elif x == "T":
                        cursive_message += uppercase_cursive[19]
                    elif x == "t":
                        cursive_message += lowercase_cursive[19]
                    elif x == "U":
                        cursive_message += uppercase_cursive[20]
                    elif x == "u":
                        cursive_message += lowercase_cursive[20]
                    elif x == "V":
                        cursive_message += uppercase_cursive[21]
                    elif x == "v":
                        cursive_message += lowercase_cursive[21]
                    elif x == "W":
                        cursive_message += uppercase_cursive[22]
                    elif x == "w":
                        cursive_message += lowercase_cursive[22]
                    elif x == "X":
                        cursive_message += uppercase_cursive[23]
                    elif x == "x":
                        cursive_message += lowercase_cursive[23]
                    elif x == "Y":
                        cursive_message += uppercase_cursive[24]
                    elif x == "y":
                        cursive_message += lowercase_cursive[24]
                    elif x == "Z":
                        cursive_message += uppercase_cursive[25]
                    elif x == "z":
                        cursive_message += lowercase_cursive[25]
                    else:
                        cursive_message += x
                if ctx.author != bot.user:
                    await ctx.reply(f"> {ctx.author}: {ctx.message.content}\n"
                                    f"{cursive_message}")
                elif ctx.author == bot.user:
                    await ctx.send(cursive_message)
            if ctx.author == bot.user:
                await ctx.message.delete()
            else:
                pass


def setup(userbot):
    userbot.add_cog(Cursive(userbot))
