from bot import *


class DickSize(commands.Cog):

    @commands.command()
    async def dicksize(self, ctx, member: discord.Member):

        if blacklist_check(ctx):
            await ctx.reply("You are blacklisted!")
        else:
            desc = ''
            log(ctx, "DICKSIZE")
            size = random.randrange(0, 12)
            if size >= 6:
                desc = "That's a schlong dong!"
            elif size < 6:
                desc = "so smol! 🥺"
            try:
                embed = discord.embeds.Embed(
                    title=f"{member.display_name}'s Dick Size",
                    description=desc,
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Size",
                    value=f"{size} inches"
                )
                embed.add_field(
                    name="Demonstration",
                    value=f"8{size * '='}D"
                )
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await ctx.reply(f"```ini\n"
                                f"[ {member.display_name}'s Dick Size ]\n"
                                f"{desc}\n\n"
                                f"[ Size ]\n"
                                f"{size} inches\n\n"
                                f"[ Demonstration ]\n"
                                f"8{size * '='}D\n\n"
                                f"{codeblock_footer()}"
                                f"```")


def setup(userbot):
    userbot.add_cog(DickSize(userbot))
