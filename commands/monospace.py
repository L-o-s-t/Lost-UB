from bot import *


class Monospace(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def monospace(self, ctx, *, message):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use MONOSPACE", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use MONOSPACE", color=embedcolor("red"))
        else:
            uppercase_monocase = "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
            lowercase_monocase = "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"

            if message is None:
                await log(ctx, "ERROR", "You must specify a message you want monospaced!")
            else:
                await log(ctx, description="This user used the command MONOSPACE", color=embedcolor())
                monospace_message = ""
                for x in message:
                    if x == "A":
                        monospace_message += uppercase_monocase[0]
                    elif x == "a":
                        monospace_message += lowercase_monocase[0]
                    elif x == "B":
                        monospace_message += uppercase_monocase[1]
                    elif x == "b":
                        monospace_message += lowercase_monocase[1]
                    elif x == "C":
                        monospace_message += uppercase_monocase[2]
                    elif x == "c":
                        monospace_message += lowercase_monocase[2]
                    elif x == "D":
                        monospace_message += uppercase_monocase[3]
                    elif x == "d":
                        monospace_message += lowercase_monocase[3]
                    elif x == "E":
                        monospace_message += uppercase_monocase[4]
                    elif x == "e":
                        monospace_message += lowercase_monocase[4]
                    elif x == "F":
                        monospace_message += uppercase_monocase[5]
                    elif x == "f":
                        monospace_message += lowercase_monocase[5]
                    elif x == "G":
                        monospace_message += uppercase_monocase[6]
                    elif x == "g":
                        monospace_message += lowercase_monocase[6]
                    elif x == "H":
                        monospace_message += uppercase_monocase[7]
                    elif x == "h":
                        monospace_message += lowercase_monocase[7]
                    elif x == "I":
                        monospace_message += uppercase_monocase[8]
                    elif x == "i":
                        monospace_message += lowercase_monocase[8]
                    elif x == "J":
                        monospace_message += uppercase_monocase[9]
                    elif x == "j":
                        monospace_message += lowercase_monocase[9]
                    elif x == "K":
                        monospace_message += uppercase_monocase[10]
                    elif x == "k":
                        monospace_message += lowercase_monocase[10]
                    elif x == "L":
                        monospace_message += uppercase_monocase[11]
                    elif x == "l":
                        monospace_message += lowercase_monocase[11]
                    elif x == "M":
                        monospace_message += uppercase_monocase[12]
                    elif x == "m":
                        monospace_message += lowercase_monocase[12]
                    elif x == "N":
                        monospace_message += uppercase_monocase[13]
                    elif x == "n":
                        monospace_message += lowercase_monocase[13]
                    elif x == "O":
                        monospace_message += uppercase_monocase[14]
                    elif x == "o":
                        monospace_message += lowercase_monocase[14]
                    elif x == "P":
                        monospace_message += uppercase_monocase[15]
                    elif x == "p":
                        monospace_message += lowercase_monocase[15]
                    elif x == "Q":
                        monospace_message += uppercase_monocase[16]
                    elif x == "q":
                        monospace_message += lowercase_monocase[16]
                    elif x == "R":
                        monospace_message += uppercase_monocase[17]
                    elif x == "r":
                        monospace_message += lowercase_monocase[17]
                    elif x == "S":
                        monospace_message += uppercase_monocase[18]
                    elif x == "s":
                        monospace_message += lowercase_monocase[18]
                    elif x == "T":
                        monospace_message += uppercase_monocase[19]
                    elif x == "t":
                        monospace_message += lowercase_monocase[19]
                    elif x == "U":
                        monospace_message += uppercase_monocase[20]
                    elif x == "u":
                        monospace_message += lowercase_monocase[20]
                    elif x == "V":
                        monospace_message += uppercase_monocase[21]
                    elif x == "v":
                        monospace_message += lowercase_monocase[21]
                    elif x == "W":
                        monospace_message += uppercase_monocase[22]
                    elif x == "w":
                        monospace_message += lowercase_monocase[22]
                    elif x == "X":
                        monospace_message += uppercase_monocase[23]
                    elif x == "x":
                        monospace_message += lowercase_monocase[23]
                    elif x == "Y":
                        monospace_message += uppercase_monocase[24]
                    elif x == "y":
                        monospace_message += lowercase_monocase[24]
                    elif x == "Z":
                        monospace_message += uppercase_monocase[25]
                    elif x == "z":
                        monospace_message += lowercase_monocase[25]
                    else:
                        monospace_message += x
                if ctx.author != bot.user:
                    await ctx.reply(f"> {ctx.author}: {ctx.message.content}\n"
                                    f"{monospace_message}")
                elif ctx.author == bot.user:
                    await ctx.send(monospace_message)
            if ctx.author == bot.user:
                await ctx.message.delete()
            else:
                pass


def setup(userbot):
    userbot.add_cog(Monospace(userbot))
