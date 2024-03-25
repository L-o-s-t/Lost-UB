from bot import *


class Help(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command(aliases=['help'])
    async def info(self, ctx, module: str = None):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use HELP"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use HELP"))
        else:
            print(log(ctx, description="This user used the command HELP"))
            if module is None:
                await simple_codeblock(ctx, f"[ Command Categories ]\n"
                                            f"Choose a category\n"
                                            f"Command usage: {get_prefix()}help [category]\n\n"
                                            f"[ Games ]\n"
                                            f"Total Commands: {games}\n\n"
                                            f"[ Fun ]\n"
                                            f"Total Commands: {fun}\n\n"
                                            f"[ Tools ]\n"
                                            f"Total Commands: {tools}\n\n"
                                            f"[ Admin ]\n"
                                            f"Total Commands: {admin}\n\n")
            elif module.lower() == "games" or module.lower() == "game":
                await simple_codeblock(ctx, f"[ Game Commands ]\n"
                                            f"Your prefix is: {get_prefix()}\n"
                                            f"[] = required, () = optional.\n\n"
                                            f"[ Games ]\n"
                                            f"Rock, Paper, Scissors | {get_prefix()}rps\n"
                                            f"Battle  | {get_prefix()}battle\n"
                                            f"Fight   | {get_prefix()}fight [@member]\n"
                                            f"Hangman | {get_prefix()}hangman\n\n")
            elif module.lower() == "fun":
                await simple_codeblock(ctx, f"[ Fun Commands ]\n"
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
                                            f"Space         | {get_prefix()}space [message]\n\n")
            elif module.lower() == "tools" or module.lower() == "tool":
                await simple_codeblock(ctx, f"[ Tools Commands ]\n"
                                            f"Your prefix is: {get_prefix()}\n"
                                            f"[] = required, () = optional.\n\n"
                                            f"[ Tools ]\n"
                                            f"StealPFP       | {get_prefix()}stealpfp [@member]\n"
                                            f"SavePFP        | {get_prefix()}savepfp [@member]\n"
                                            f"PFP            | {get_prefix()}pfp [@member]\n"
                                            f"AFK            | {get_prefix()}afk\n"
                                            f"ServerInfo     | {get_prefix()}serverinfo\n"
                                            f"ServerIcon     | {get_prefix()}servericon\n"
                                            f"UserInfo       | {get_prefix()}userinfo [@member]\n"
                                            f"Calculate      | {get_prefix()}calculate [number] [operator] [number]\n"
                                            f"Poll           | {get_prefix()}poll\n"
                                            f"Blacklist      | {get_prefix()}blacklist [add/remove] [@member]\n"
                                            f"UserLog        | {get_prefix()}userlog [add/remove] [@member]\n\n")
            elif module.lower() == "admin":
                await simple_codeblock(ctx, f"[ Admin Commands ]\n"
                                            f"Your prefix is: {get_prefix()}\n"
                                            f"[] = required, () = optional.\n\n"
                                            f"[ Admin ]\n"
                                            f"Kick   | {get_prefix()}kick [member] [reason]\n"
                                            f"Ban    | {get_prefix()}ban [member] [reason]\n"
                                            f"Warn        | {get_prefix()}warn [member] [reason]\n"
                                            f"Warnings        | {get_prefix()}warnings [member] [reason]\n\n")
            else:
                await simple_codeblock(ctx, f"[ Category Not Found ]\n"
                                            f"Your prefix is: {get_prefix()}\n\n"
                                            f"[ Categories ]\n"
                                            f"- Games\n"
                                            f"- Fun\n"
                                            f"- Tools\n"
                                            f"- Admin\n\n")


def setup(userbot):
    userbot.add_cog(Help(userbot))
