from bot import *


class PFP(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def stealpfp(self, ctx, member: discord.Member):
        if ctx.author == bot.user:
            print(log(ctx, description="This user used the command STEALPFP"))
            if config['CONFIGURATION']['silentsteal'] == "True":
                await ctx.message.delete()
            elif config['CONFIGURATION']['silentsteal'] == "False":
                await simple_codeblock(ctx, f"[ Avatar Stolen! ]\n\n"
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
    async def pfp(self, ctx, member: discord.Member = None):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use PFP"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use PFP"))
        else:
            print(log(ctx, description="This user used the command PFP"))
            if member is None:
                await ctx.reply(f"```ini\n"
                                f"[ Profile Picture ]\n\n"
                                f"[ Link ]\n"
                                f"{ctx.author.avatar_url}\n\n"
                                f"[ User ]\n"
                                f"{ctx.author.display_name}\n\n"
                                f"{codeblock_footer()}\n"
                                f"```")
            else:
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
            print(log(ctx, description="This user used the command SAVEPFP"))
            if config['CONFIGURATION']['silentsave'] == "True":
                await ctx.message.delete()
            elif config['CONFIGURATION']['silentsave'] == "False":
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
