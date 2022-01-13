from bot import *


class Poll(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def poll(self, ctx, *, arguments: str = None):
        await log(ctx, description="This user used the command POLL", color=embedcolor())
        if ctx.author == bot.user:
            if arguments is None:
                await ctx.message.delete()
                await log(ctx, "Missing required arguments.", color=embedcolor("red"))
            else:
                title, description = arguments.split('| ')
                await ctx.message.delete()
                embed = discord.embeds.Embed(
                    title=title,
                    description=description,
                    colour=embedcolor()
                )
                footer(embed)
                try:
                    msg = await ctx.send(embed=embed)
                except discord.Forbidden:
                    msg = await simple_codeblock(ctx, f"[ {title} ]\n"
                                                      f"{description}", reply=False)
                await msg.add_reaction('✅')
                await msg.add_reaction('❎')


def setup(userbot):
    userbot.add_cog(Poll(userbot))
