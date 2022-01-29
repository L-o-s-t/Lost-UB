from bot import *


class Ban(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        if ctx.author == bot.user:
            await log(ctx, description="This user used the command BAN", color=embedcolor())
            embed = discord.embeds.Embed(
                title="User Banned",
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
                await member.ban(reason=f"You have been banned by {ctx.author}")
                await member.send(f"You have been banned from {ctx.guild}")
            else:
                await member.ban(reason=f"You have been banned by {ctx.author} for: {reason}")
                await member.send(f"You have been banned from {ctx.guild} for: {reason}")
            try:
                await ctx.reply(embed=embed)
            except Exception as e:
                await simple_codeblock(ctx,
                                       f"[ User Banned ]\n"
                                       f"Command author: {ctx.author}\n\n"
                                       f"[ User ]\n"
                                       f"{member}\n\n"
                                       f"[ Reason ]\n"
                                       f"{reason}")
        else:
            return


def setup(userbot):
    userbot.add_cog(Ban(userbot))
