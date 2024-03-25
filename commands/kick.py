from bot import *


class Kick(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        if ctx.author == bot.user:
            print(log(ctx, description="This user used the command KICK"))
            if reason is None:
                await member.kick(reason=f"You have been kicked by {ctx.author}")
                await member.send(f"You have been kicked from {ctx.guild}")
            else:
                await member.kick(reason=f"You have been kicked by {ctx.author} for: {reason}")
                await member.send(f"You have been kicked from {ctx.guild} for: {reason}")
            await simple_codeblock(ctx, f"[ User Kicked ]\n"
                                        f"Command author: {ctx.author}\n\n"
                                        f"[ User ]\n"
                                        f"{member}\n\n"
                                        f"[ Reason ]\n"
                                        f"{reason}")
        else:
            return


def setup(userbot):
    userbot.add_cog(Kick(userbot))
