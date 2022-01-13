import datetime
import time

from bot import *

keywords = ['.com', 'nitro']


class Security(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.Cog.listener()
    async def on_message_delete(self, ctx):
        if f"<@!{bot.user.id}>" in ctx.content:
            # time_since = time.localtime().tm_sec - ctx.created_at.second
            # if time_since < 0:
            #     time_since += 60
            if f"{ctx.content}".replace(f"<@!{bot.user.id}>", "") == "":
                await log(ctx, title="GhostPing Detection",
                          description="Nothing was included in the message apart from the ping.",
                          color=embedcolor("red"))
            else:
                await log(ctx, title="GhostPing Detection",
                          description=f"{ctx.content}".replace(f"<@!{bot.user.id}>", ""),
                          color=embedcolor("red"))

    # @commands.Cog.listener()
    # async def on_message(self, ctx):


def setup(userbot):
    userbot.add_cog(Security(userbot))
