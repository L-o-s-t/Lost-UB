from bot import *


class GhostPing(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def ghostping(self, ctx, member: discord.Member):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use GHOSTPING"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use GHOSTPING"))
        else:
            print(log(ctx, description="This user used the command GHOSTPING"))
            msg = await ctx.send(f'{member}')
            await msg.delete()
            await ctx.message.delete()

    @commands.command()
    async def ghostpingall(self, ctx, member: discord.Member = None):
        if ctx.author == bot.user:
            print(log(ctx, description="This user used the command GHOSTPINGALL"))
            await ctx.message.delete()
            if member is None:
                print(log(ctx, "Member not found"))
            else:
                for channels in ctx.guild.channels:
                    try:
                        ghost = await channels.send(member.mention)
                        await ghost.delete()
                    except AttributeError:
                        pass
                    except Exception as e:
                        pass


def setup(userbot):
    userbot.add_cog(GhostPing(userbot))
