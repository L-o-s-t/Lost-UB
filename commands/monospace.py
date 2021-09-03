from bot import *


class Monospace(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def monospace(self, ctx, *, message):

        uppercase_monocase = "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
        lowercase_monocase = "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"

        if message is None:
            log(ctx, "ERROR", "You must specify a message you want monospaced!")
        else:
            cursive_message = ""
            for x in message:
                if x == "A":
                    cursive_message += uppercase_monocase[0]
                elif x == "a":
                    cursive_message += lowercase_monocase[0]
                elif x == "B":
                    cursive_message += uppercase_monocase[1]
                elif x == "b":
                    cursive_message += lowercase_monocase[1]
                elif x == "C":
                    cursive_message += uppercase_monocase[2]
                elif x == "c":
                    cursive_message += lowercase_monocase[2]
                elif x == "D":
                    cursive_message += uppercase_monocase[3]
                elif x == "d":
                    cursive_message += lowercase_monocase[3]
                elif x == "E":
                    cursive_message += uppercase_monocase[4]
                elif x == "e":
                    cursive_message += lowercase_monocase[4]
                elif x == "F":
                    cursive_message += uppercase_monocase[5]
                elif x == "f":
                    cursive_message += lowercase_monocase[5]
                elif x == "G":
                    cursive_message += uppercase_monocase[6]
                elif x == "g":
                    cursive_message += lowercase_monocase[6]
                elif x == "H":
                    cursive_message += uppercase_monocase[7]
                elif x == "h":
                    cursive_message += lowercase_monocase[7]
                elif x == "I":
                    cursive_message += uppercase_monocase[8]
                elif x == "i":
                    cursive_message += lowercase_monocase[8]
                elif x == "J":
                    cursive_message += uppercase_monocase[9]
                elif x == "j":
                    cursive_message += lowercase_monocase[9]
                elif x == "K":
                    cursive_message += uppercase_monocase[10]
                elif x == "k":
                    cursive_message += lowercase_monocase[10]
                elif x == "L":
                    cursive_message += uppercase_monocase[11]
                elif x == "l":
                    cursive_message += lowercase_monocase[11]
                elif x == "M":
                    cursive_message += uppercase_monocase[12]
                elif x == "m":
                    cursive_message += lowercase_monocase[12]
                elif x == "N":
                    cursive_message += uppercase_monocase[13]
                elif x == "n":
                    cursive_message += lowercase_monocase[13]
                elif x == "O":
                    cursive_message += uppercase_monocase[14]
                elif x == "o":
                    cursive_message += lowercase_monocase[14]
                elif x == "P":
                    cursive_message += uppercase_monocase[15]
                elif x == "p":
                    cursive_message += lowercase_monocase[15]
                elif x == "Q":
                    cursive_message += uppercase_monocase[16]
                elif x == "q":
                    cursive_message += lowercase_monocase[16]
                elif x == "R":
                    cursive_message += uppercase_monocase[17]
                elif x == "r":
                    cursive_message += lowercase_monocase[17]
                elif x == "S":
                    cursive_message += uppercase_monocase[18]
                elif x == "s":
                    cursive_message += lowercase_monocase[18]
                elif x == "T":
                    cursive_message += uppercase_monocase[19]
                elif x == "t":
                    cursive_message += lowercase_monocase[19]
                elif x == "U":
                    cursive_message += uppercase_monocase[20]
                elif x == "u":
                    cursive_message += lowercase_monocase[20]
                elif x == "V":
                    cursive_message += uppercase_monocase[21]
                elif x == "v":
                    cursive_message += lowercase_monocase[21]
                elif x == "W":
                    cursive_message += uppercase_monocase[22]
                elif x == "w":
                    cursive_message += lowercase_monocase[22]
                elif x == "X":
                    cursive_message += uppercase_monocase[23]
                elif x == "x":
                    cursive_message += lowercase_monocase[23]
                elif x == "Y":
                    cursive_message += uppercase_monocase[24]
                elif x == "y":
                    cursive_message += lowercase_monocase[24]
                elif x == "Z":
                    cursive_message += uppercase_monocase[25]
                elif x == "z":
                    cursive_message += lowercase_monocase[25]
                else:
                    cursive_message += x
            await ctx.send(cursive_message)
        await ctx.message.delete()


def setup(userbot):
    userbot.add_cog(Monospace(userbot))
