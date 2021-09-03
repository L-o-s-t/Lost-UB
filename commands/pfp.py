from bot import *


class PFP(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def stealpfp(self, ctx, member: discord.Member):
        if ctx.author == bot.user:
            log(ctx, "STEALPFP")
            if config['CONFIGURATION']['silentsteal'] == "True":
                await ctx.message.delete()
            elif config['CONFIGURATION']['silentsteal'] == "False":
                try:
                    embed = discord.embeds.Embed(
                        title="Avatar Stolen!",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="User",
                        value=member.display_name
                    )
                    embed.add_field(
                        name="Avatar",
                        value=f"[Link]({member.avatar_url})"
                    )
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await ctx.reply(f"```ini\n"
                                    f"[ Avatar Stolen! ]\n\n"
                                    f"[ User ]\n"
                                    f"{member.display_name}\n\n"
                                    f"[ Avatar ]\n"
                                    f"{member.avatar_url}\n\n"
                                    f"{codeblock_footer()}\n"
                                    f"```")
            if member.is_avatar_animated():
                await member.avatar_url.save(f"data\\avatars\\{member.id}.gif")
                with open(f'data/avatars/{member.id}.gif', 'rb') as image:
                    await bot.user.edit(avatar=image.read())
            else:
                await member.avatar_url.save(f"data\\avatars\\{member.id}.png")
                with open(f'data/avatars/{member.id}.png', 'rb') as image:
                    await bot.user.edit(avatar=image.read())

    @commands.command()
    async def pfp(self, ctx, member: discord.Member):
        if blacklist_check(ctx):
            log(ctx, "BLACKLIST", f"{ctx.author.display_name} tried to use the command PFP.")
        else:
            log(ctx, "PFP")
            try:
                embed = discord.embeds.Embed(
                    title="Profile Picture",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="Link",
                    value=f"[Click Me]({member.avatar_url_as(format='jpg')})"
                )
                embed.add_field(
                    name="User",
                    value=f"{member.display_name}"
                )
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(
                    text=f"Logged in as {bot.user} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                await ctx.reply(f"```ini\n"
                                f"[ Profile Picture ]\n\n"
                                f"[ Link ]\n"
                                f"{member.avatar_url}\n\n"
                                f"[ User ]\n"
                                f"{member.display_name}\n\n"
                                f"{codeblock_footer()}\n"
                                f"```")

    @commands.command()
    async def savepfp(self, ctx, member: discord.Member):
        if ctx.author == bot.user:
            log(ctx, "PFP")
            if config['CONFIGURATION']['silentsave'] == "True":
                await ctx.message.delete()
            elif config['CONFIGURATION']['silentsave'] == "False":
                try:
                    embed = discord.embeds.Embed(
                        title="Avatar Saved!",
                        description=f"{member.display_name}'s avatar was saved.",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="User",
                        value=str(member)
                    )
                    embed.add_field(
                        name="Avatar",
                        value=f"[Link]({member.avatar_url})"
                    )
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await simple_codeblock(ctx, f"[ Avatar Saved! ]\n"
                                                f"{member.display_name}'s avatar was saved.\n\n"
                                                f"[ User ]\n"
                                                f"{member}\n\n"
                                                f"[ Avatar ]\n"
                                                f"{member.avatar_url}")
            if member.is_avatar_animated():
                await member.avatar_url.save(f"data\\avatars\\{member.id}.gif")
            else:
                await member.avatar_url.save(f"data\\avatars\\{member.id}.png")


def setup(userbot):
    userbot.add_cog(PFP(userbot))
