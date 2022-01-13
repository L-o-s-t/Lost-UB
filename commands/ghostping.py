from bot import *


class GhostPing(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def ghostping(self, ctx, member: discord.Member):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use GHOSTPING", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use GHOSTPING", color=embedcolor("red"))
        else:
            await log(ctx, description="This user used the command GHOSTPING", color=embedcolor())
            msg = await ctx.send(f'{member}')
            await msg.delete()
            await ctx.message.delete()

    @commands.command()
    async def ghostpingall(self, ctx, member: discord.Member = None):
        if ctx.author == bot.user:
            await log(ctx, description="This user used the command GHOSTPINGALL", color=embedcolor())
            await ctx.message.delete()
            if member is None:
                await log(ctx, "Member not found", color=embedcolor("red"))
            else:
                for channels in ctx.guild.channels:
                    try:
                        ghost = await channels.send(member.mention)
                        await ghost.delete()
                    except AttributeError:
                        pass
                    except discord.Forbidden:
                        pass


def setup(userbot):
    userbot.add_cog(GhostPing(userbot))
