from bot import *


class AFK(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def afk(self, ctx):
        if ctx.author == bot.user:
            print(log(ctx, description="This user used the command AFK"))
            if config["CONFIGURATION"]["AFK"] == "True":
                config["CONFIGURATION"]["AFK"] = "False"
                write()
                await simple_codeblock(ctx, f"[ AFK ]\n"
                                            f"Successfully set! AFK has been turned off.")
            elif config["CONFIGURATION"]["AFK"] == "False":
                config["CONFIGURATION"]["AFK"] = "True"
                write()
                await simple_codeblock(ctx, f"[ AFK ]\n"
                                            f"Successfully set! AFK has been turned on.")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if config["CONFIGURATION"]["AFK"] == "True":
            if f'<@{bot.user.id}>' in ctx.content or f'<@!{bot.user.id}>' in ctx.content:
                if config['CONFIGURATION']['afk_legit'] == "True":
                    time.sleep(random.randrange(5, 10))
                    async with ctx.channel.typing():
                        await asyncio.sleep(5)
                await ctx.reply(config["CONFIGURATION"]["afk_msg"])
            elif ctx.guild is None and ctx.author != bot.user:
                if config['CONFIGURATION']['afk_legit'] == "True":
                    time.sleep(random.randrange(5, 10))
                    async with ctx.channel.typing():
                        await asyncio.sleep(5)
                await ctx.reply(config["CONFIGURATION"]["afk_msg"])
            config['CONFIGURATION']['AFK'] = "False"
            write()
            await asyncio.sleep(30)
            config['CONFIGURATION']['AFK'] = "True"
            write()


def setup(userbot):
    userbot.add_cog(AFK(userbot))
