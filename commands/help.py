from bot import *


class Help(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command(aliases=['help'])
    async def info(self, ctx, module: str = None):
        if blacklist_check(ctx):
            log(ctx, "BLACKLIST", f"{ctx.author.display_name} tried to use the command HELP.")
        else:
            log(ctx, "HELP")
            if module is None:
                try:
                    embed = discord.embeds.Embed(
                        title="Command Categories\n",
                        description=f"Choose a category\n"
                                    f"Command usage: {get_prefix()}help [category]",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="Games",
                        value=f"Total Commands: {games}",
                        inline=True
                    )
                    embed.add_field(
                        name="Fun",
                        value=f"Total Commands: {fun}",
                        inline=True
                    )
                    embed.add_field(
                        name="Tools",
                        value=f"Total Commands: {tools}",
                        inline=True
                    )
                    embed.add_field(
                        name="Admin",
                        value=f"Total Commands: {admin}",
                        inline=True
                    )
                    embed.set_thumbnail(
                        url="https://i.ibb.co/6PGdDFg/Logo2.png"
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await ctx.reply(f"```ini\n"
                                    f"[Command Categories]\n"
                                    f"Choose a category\n"
                                    f"Command usage: {get_prefix()}help [category]\n\n"
                                    f"[ Games ]\n"
                                    f"Total Commands: {games}\n\n"
                                    f"[ Fun ]\n"
                                    f"Total Commands: {fun}\n\n"
                                    f"[ Tools ]\n"
                                    f"Total Commands: {tools}\n\n"
                                    f"[ Admin ]\n"
                                    f"Total Commands: {admin}\n\n"
                                    f"{codeblock_footer()}"
                                    f"```")
            elif module.lower() == "games" or module.lower() == "game":
                try:
                    embed = discord.embeds.Embed(
                        title="Game Commands",
                        description=f"Your prefix is: ``{get_prefix()}``\n"
                                    f"**[]** = required, **()** = optional.",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="Games",
                        value=f"**Rock, Paper, Scissors** | {get_prefix()}rps\n"
                              f"**Battle** | {get_prefix()}battle\n"
                              f"**Fight**  | {get_prefix()}fight [@member]",
                        inline=True
                    )
                    embed.set_thumbnail(
                        url="https://i.ibb.co/6PGdDFg/Logo2.png"
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await ctx.reply(f"```ini\n"
                                    f"[ Game Commands ]\n"
                                    f"Your prefix is: {get_prefix()}\n"
                                    f"[] = required, () = optional.\n\n"
                                    f"[ Games ]\n"
                                    f"Rock, Paper, Scissors | {get_prefix()}rps\n"
                                    f"Battle | {get_prefix()}battle\n"
                                    f"Fight  | {get_prefix()}fight [@member]\n\n"
                                    f"{codeblock_footer()}"
                                    f"```")
            elif module.lower() == "fun":
                try:
                    embed = discord.embeds.Embed(
                        title="Fun Commands",
                        description=f"Your prefix is: ``{get_prefix()}``\n"
                                    f"**[]** = required, **()** = optional.",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="Fun",
                        value=f"**DickSize**      | {get_prefix()}dicksize [@member]\n"
                              f"**FlipCoin**      | {get_prefix()}flipcoin\n"
                              f"**8Ball**         | {get_prefix()}8ball [question]\n"
                              f"**GhostPing**     | {get_prefix()}ghostping [@member]\n"
                              f"**GhostPingAll**  | {get_prefix()}ghostpingall [@member]\n"
                              f"**IQ Rating**     | {get_prefix()}iq [@member]\n"
                              f"**Dice Roll**     | {get_prefix()}rolladice\n"
                              f"**Spam**          | {get_prefix()}spam [delay] [count] [message]\n"
                              f"**SpamAll**       | {get_prefix()}spamall [message]\n"
                              f"**Mock**          | {get_prefix()}mock [message]\n"
                              f"**Cursive**       | {get_prefix()}cursive [message]\n"
                              f"**Monospace**     | {get_prefix()}monospace [message]\n"
                              f"**Space**         | {get_prefix()}space [message]",
                        inline=True

                    )
                    embed.set_thumbnail(
                        url="https://i.ibb.co/6PGdDFg/Logo2.png"
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await ctx.reply(f"```ini\n"
                                    f"[ Fun Commands ]\n"
                                    f"Your prefix is: {get_prefix()}\n"
                                    f"[] = required, () = optional.\n\n"
                                    f"[ Fun ]\n"
                                    f"DickSize      | {get_prefix()}dicksize [@member]\n"
                                    f"FlipCoin      | {get_prefix()}flipcoin\n"
                                    f"8Ball         | {get_prefix()}8ball [question]\n"
                                    f"GhostPing     | {get_prefix()}ghostping [@member]\n"
                                    f"GhostPingAll  | {get_prefix()}ghostpingall [@member]\n"
                                    f"IQ Rating     | {get_prefix()}iq [@member]\n"
                                    f"Dice Roll     | {get_prefix()}rolladice\n"
                                    f"Spam          | {get_prefix()}spam [delay] [count] [message]\n"
                                    f"SpamAll       | {get_prefix()}spamall [message]\n"
                                    f"Mock          | {get_prefix()}mock [message]\n"
                                    f"Cursive       | {get_prefix()}cursive [message]\n"
                                    f"Monospace     | {get_prefix()}monospace [message]\n"
                                    f"Space         | {get_prefix()}space [message]\n\n"
                                    f"{codeblock_footer()}"
                                    f"```")
            elif module.lower() == "tools" or module.lower() == "tool":
                try:
                    embed = discord.embeds.Embed(
                        title="Tools Commands",
                        description=f"Your prefix is: ``{get_prefix()}``\n"
                                    f"**[]** = required, **()** = optional.",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="Tools",
                        value=f"**StealPFP**   | {get_prefix()}stealpfp [@member]\n"
                              f"**SavePFP**    | {get_prefix()}savepfp [@member]\n"
                              f"**PFP**        | {get_prefix()}pfp [@member]\n"
                              f"**AFK**        | {get_prefix()}afk\n"
                              f"**ServerInfo** | {get_prefix()}serverinfo\n"
                              f"**ServerIcon** | {get_prefix()}servericon\n"
                              f"**UserInfo**   | {get_prefix()}userinfo [@member]\n"
                              f"**Calculate**  | {get_prefix()}calculate [number] [operator] [number]\n"
                              f"**SendEmbed**  | {get_prefix()}sendembed [title] | [description]\n"
                              f"**Poll**       | {get_prefix()}poll\n"
                              f"**Blacklist**  | {get_prefix()}blacklist (add/remove) (@member)\n",
                        inline=True
                    )
                    embed.set_thumbnail(
                        url="https://i.ibb.co/6PGdDFg/Logo2.png"
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await ctx.reply(f"```ini\n"
                                    f"[ Tools Commands ]\n"
                                    f"Your prefix is: {get_prefix()}\n"
                                    f"[] = required, () = optional.\n\n"
                                    f"[ Tools ]\n"
                                    f"StealPFP   | {get_prefix()}stealpfp [@member]\n"
                                    f"SavePFP    | {get_prefix()}savepfp [@member]\n"
                                    f"PFP        | {get_prefix()}pfp [@member]\n"
                                    f"AFK        | {get_prefix()}afk\n"
                                    f"ServerInfo | {get_prefix()}serverinfo\n"
                                    f"ServerIcon | {get_prefix()}servericon\n"
                                    f"UserInfo   | {get_prefix()}userinfo [@member]\n"
                                    f"Calculate  | {get_prefix()}calculate [number] [operator] [number]\n\n"
                                    f"{codeblock_footer()}"
                                    f"```")
            elif module.lower() == "admin":
                try:
                    embed = discord.embeds.Embed(
                        title="Admin Commands",
                        description=f"Your prefix is: ``{get_prefix()}``\n"
                                    f"**[]** = required, **()** = optional.",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="Admin",
                        value=f"**Kick**   | {get_prefix()}kick [member] [reason]\n"
                              f"**Ban**    | {get_prefix()}ban [member] [reason]\n"
                              f"**Warn**        | {get_prefix()}warn [member] [reason]\n"
                              f"**Warnings**        | {get_prefix()}warnings [member] [reason]",
                        inline=True
                    )
                    embed.set_thumbnail(
                        url="https://i.ibb.co/6PGdDFg/Logo2.png"
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await ctx.reply(f"```ini\n"
                                    f"[ Admin Commands ]\n"
                                    f"Your prefix is: {get_prefix()}\n"
                                    f"[] = required, () = optional.\n\n"
                                    f"[ Admin ]\n"
                                    f"Kick   | {get_prefix()}kick [member] [reason]\n"
                                    f"Ban    | {get_prefix()}ban [member] [reason]\n"
                                    f"Warn        | {get_prefix()}warn [member] [reason]\n"
                                    f"Warnings        | {get_prefix()}warnings [member] [reason]\n\n"
                                    f"{codeblock_footer()}"
                                    f"```")
            else:
                try:
                    embed = discord.embeds.Embed(
                        title="Category Not Found",
                        description=f"Your prefix is: ``{get_prefix()}``\n",
                        colour=embedcolor()
                    )
                    embed.add_field(
                        name="Categories",
                        value=f"- Games\n"
                              f"- Fun\n"
                              f"- Tools\n"
                              f"- Admin",
                        inline=True
                    )
                    embed.set_thumbnail(
                        url="https://i.ibb.co/6PGdDFg/Logo2.png"
                    )
                    embed.set_footer(
                        text=f"Logged in as {bot.user} | Lost-UB | Server Code: CFNKjPPUbW",
                        icon_url=bot.user.avatar_url
                    )
                    await ctx.reply(embed=embed)
                except discord.Forbidden:
                    await ctx.reply(f"```ini\n"
                                    f"[ Category Not Found ]\n"
                                    f"Your prefix is: {get_prefix()}\n\n"
                                    f"[ Categories ]\n"
                                    f"- Games\n"
                                    f"- Fun\n"
                                    f"- Tools\n"
                                    f"- Admin\n\n"
                                    f"{codeblock_footer()} | Server Code: CFNKjPPUbW\n"
                                    f"```")


def setup(userbot):
    userbot.add_cog(Help(userbot))
