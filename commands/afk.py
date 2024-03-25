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
                await ctx.reply("Successfully set! AFK has been turned off.")
            elif config["CONFIGURATION"]["AFK"] == "False":
                config["CONFIGURATION"]["AFK"] = "True"
                write()
                await ctx.reply("Successfully set! AFK has been turned on.")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if config["CONFIGURATION"]["AFK"] == "True":
            if f'<@{bot.user.id}>' in ctx.content or f'<@!{bot.user.id}>' in ctx.content:
                if config['CONFIGURATION']['afk_legit'] == "True":
                    time.sleep(random.randrange(5, 10))
                    async with ctx.channel.typing():
                        await asyncio.sleep(5)
                await ctx.reply(config["CONFIGURATION"]["afk_msg"])


def setup(userbot):
    userbot.add_cog(AFK(userbot))
