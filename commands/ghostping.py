from bot import *


class GhostPing(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def ghostping(self, ctx, member: discord.Member):
        if blacklist_check(ctx):
            await ctx.reply("You are blacklisted!")
        else:
            log(ctx, "GHOSTPING")
            msg = await ctx.send(f'{member}')
            await msg.delete()
            await ctx.message.delete()

    @commands.command()
    async def ghostpingall(self, ctx, member: discord.Member = None):
        if ctx.author == bot.user:
            log(ctx, "GHOSTPINGALL")
            await ctx.message.delete()
            if member is None:
                log(ctx, "ERROR", "Member not found")
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
