from bot import *


class Kick(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        if ctx.author == bot.user:
            log(ctx, "KICK")
            embed = discord.embeds.Embed(
                title="User Kicked",
                description=f"Command Author: {ctx.author}",
                colour=embedcolor()
            )
            embed.add_field(
                name="User",
                value=f"{member}"
            )
            embed.add_field(
                name="Reason",
                value=reason
            )
            embed.set_thumbnail(
                url=member.avatar_url
            )
            if reason is None:
                await member.kick(reason=f"You have been kicked by {ctx.author}")
                await member.send(f"You have been kicked from {ctx.guild}")
            else:
                await member.kick(reason=f"You have been kicked by {ctx.author} for: {reason}")
                await member.send(f"You have been kicked from {ctx.guild} for: {reason}")
            try:
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await simple_codeblock(ctx,
                                       f"[ User Kicked ]\n"
                                       f"Command author: {ctx.author}\n\n"
                                       f"[ User ]\n"
                                       f"{member}\n\n"
                                       f"[ Reason ]\n"
                                       f"{reason}")
        else:
            return


def setup(userbot):
    userbot.add_cog(Kick(userbot))
