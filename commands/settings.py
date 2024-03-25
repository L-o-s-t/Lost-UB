from bot import *


class Settings(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def settings(self, ctx, section: str = None, setting: str = None, *, value: str = None):
        def codeblock_sections(context):
            return context.reply(f"```ini\n"
                                 f"[ Settings ]\n"
                                 f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                 f"[ Sections ]\n"
                                 f"- afk\n"
                                 f"- pfp\n"
                                 f"- mock\n"
                                 f"- customization\n"
                                 f"- configuration\n\n"
                                 f"{codeblock_footer()}\n"
                                 f"```")

        def codeblock_settings(context, setting_name, description):
            return context.reply(f"```ini\n"
                                 f"[ {setting_name} Setting ]\n"
                                 f"{description}\n\n"
                                 f"{codeblock_footer()}\n"
                                 f"```")

        def codeblock_confirmation(context, setting_name, setting_value):
            return context.reply(f"```ini\n"
                                 f"[ {setting_name} Setting ]\n"
                                 f"This has been turned {setting_value}!\n\n"
                                 f"{codeblock_footer()}\n"
                                 f"```")

        def codeblock_setting_error(context, setting_name, settting_description: str = f"Value has to be True or False!"):
            return simple_codeblock(context, f"[ {setting_name} Setting ]\n"
                                             f"{settting_description}\n\n")

        if ctx.author == bot.user:
            print(log(ctx, description="This user used the command SETTINGS"))
            if section is None:
                await codeblock_sections(ctx)
            elif section.lower() == "afk":
                if setting is None:
                    await simple_codeblock(ctx, f"[ AFK Section ]\n"
                                                f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                                f"[ Settings ]\n"
                                                f"- legit | {config['CONFIGURATION']['afk_legit']}\n"
                                                f"- message | {config['CONFIGURATION']['afk_msg']}\n\n")
                elif setting.lower() == "legit":
                    if value is None:
                        await simple_codeblock(ctx, f"[ Legit AFK ]\n"
                                                    f"Legit afk sends a typing indicator to make it seem like you aren't user-botting.")
                    elif value.lower() == "true":
                        config['CONFIGURATION']['afk_legit'] = "True"
                        write()
                        await codeblock_confirmation(ctx, "Legit AFK", "on")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['afk_legit'] = "False"
                        write()
                        await codeblock_confirmation(ctx, "Legit AFK", "off")
                    else:
                        await codeblock_setting_error(ctx, "Legit AFK")
                elif setting.lower() == "message":
                    if value is None:
                        await codeblock_settings(ctx, "AFK Message", "Set the message to send to users when AFK is enabled.")
                    else:
                        config["CONFIGURATION"]["afk_msg"] = value
                        write()
                        await simple_codeblock(ctx, f"[ AFK Message ]\n"
                                                    f"Your afk message was set to: {value}")
                else:
                    await simple_codeblock(ctx, f"[ AFK Section ]\n"
                                                f"Setting not found.\n"
                                                f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                                f"[ Settings ]\n"
                                                f"- legit | {config['CONFIGURATION']['afk_legit']}\n"
                                                f"- message | {config['CONFIGURATION']['afk_msg']}")
            elif section.lower() == "mock":
                if setting is None:
                    await simple_codeblock(ctx, f"[ Mock Section ]\n"
                                                f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                                f"[ Settings ]\n"
                                                f"- automock | {config['CONFIGURATION']['automock']}\n\n")
                elif setting.lower() == "automock":
                    if value is None:
                        await codeblock_settings(ctx, "AutoMock",
                                                            "Automatically mocks a user's message when sent.")
                    elif value.lower() == "true":
                        config['CONFIGURATION']['automock'] = "True"
                        write()
                        try:
                            await confirmation(ctx, "AutoMock", "on")
                        except Exception as e:
                            await codeblock_confirmation(ctx, "AutoMock", "on")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['automock'] = "False"
                        write()
                        try:
                            await confirmation(ctx, "AutoMock", "off")
                        except Exception as e:
                            await codeblock_confirmation(ctx, "AutoMock", "off")
                    else:
                        try:
                            await setting_error(ctx, "AutoMock")
                        except Exception as e:
                            await codeblock_setting_error(ctx, "AutoMock")
                else:
                    await simple_codeblock(ctx, f"[ Mock Section ]\n"
                                                f"Setting not found.\n"
                                                f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                                f"[ Settings ]\n"
                                                f"- automock | {config['CONFIGURATION']['automock']}")
            elif section.lower() == "pfp":
                if setting is None:
                    await simple_codeblock(ctx, f"[ PFP Section ]\n"
                                                f"Command usage: {get_prefix()}"
                                                f"settings (section) (setting) (value)\n"
                                                f"\n"
                                                f"[ Settings ]\n"
                                                f"- silentsteal | {config['CONFIGURATION']['silentsteal']}\n"
                                                f"- silentsave  | {config['CONFIGURATION']['silentsave']}")
                elif setting.lower() == "silentsteal":
                    if value is None:
                        await codeblock_settings(ctx, "SilentSteal", "Doesn't send any messages after cmd and deletes command message.")
                    elif value.lower() == "true":
                        config['CONFIGURATION']['silentsteal'] = "True"
                        write()
                        try:
                            await confirmation(ctx, "SilentSteal", "on")
                        except Exception as e:
                            await codeblock_confirmation(ctx, "SilentSteal", "on")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['silentsteal'] = "False"
                        write()
                        try:
                            await confirmation(ctx, "SilentSteal", "off")
                        except Exception as e:
                            await codeblock_confirmation(ctx, "SilentSteal", "off")
                    else:
                        try:
                            await setting_error(ctx, "SilentSteal")
                        except Exception as e:
                            await codeblock_setting_error(ctx, "SilentSteal")
                elif setting.lower() == "silentsave":
                    if value is None:
                        await simple_codeblock(ctx, f"[ SilentSave Setting ]\n"
                                                    f"Doesn't send any messages after "
                                                    f"cmd and deletes command message.")
                    elif value.lower() == "true":
                        try:
                            await confirmation(ctx, "SilentSave", "on")
                        except Exception as e:
                            await codeblock_confirmation(ctx, "SilentSave", "on")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['silentsave'] = "False"
                        write()
                        try:
                            await confirmation(ctx, "SilentSave", "off")
                        except Exception as e:
                            await codeblock_confirmation(ctx, "SilentSave", "off")
                    else:
                        try:
                            await setting_error(ctx, "SilentSave")
                        except Exception as e:
                            await codeblock_setting_error(ctx, "SilentSave")
                else:
                    await simple_codeblock(ctx, f"[ PFP Section ]\n"
                                                f"Setting not found.\n"
                                                f"Command usage: {get_prefix()}settings (section) (setting) (value)"
                                                f"\n\n"
                                                f"[ Settings ]\n"
                                                f"- silentsteal | {config['CONFIGURATION']['silentsteal']}\n"
                                                f"- silentsave  | {config['CONFIGURATION']['silentsave']}")
            elif section.lower() == "customization":
                if setting is None:
                    await simple_codeblock(ctx, f"[ Customization Section ]\n"
                                                f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                                f"[ Settings ]\n"
                                                f"No customization for now :(")
                else:
                    await simple_codeblock(ctx, f"[ Customization Section ]\n"
                                                f"Setting not found.\n"
                                                f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                                f"[ Settings ]\n"
                                                f"No customization for now :(")
            elif section.lower() == "configuration" or section.lower() == "config":
                if setting is None:
                    await simple_codeblock(ctx, f"[ Configuration Section ]\n"
                                                f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                                f"[ Settings ]\n"
                                                f"- blacklist | {config['CONFIGURATION']['blacklist']}\n"
                                                f"- whitelist | {config['CONFIGURATION']['whitelist']}\n"
                                                f"- autoupdate | {config['CONFIGURATION']['autoupdate']}")
                elif setting.lower() == "blacklist":
                    if value is None:
                        await simple_codeblock(ctx, f"[ Blacklist ]\n"
                                                    f"Prevent users from using the bot.")
                    elif value.lower() == "true":
                        if config['CONFIGURATION']['whitelist'] == "True":
                            config['CONFIGURATION']['whitelist'] = "False"
                        config['CONFIGURATION']['blacklist'] = "True"
                        write()
                        await simple_codeblock(ctx, f"[ Blacklist ]\n"
                                                    f"Blacklist has been turned on")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['blacklist'] = "False"
                        write()
                        await simple_codeblock(ctx, f"[ Blacklist ]\n"
                                                    f"Blacklist has been turned off")
                    else:
                        await simple_codeblock(ctx, f"[ Blacklist ]\n"
                                                    f"Invalid value, must be \"true\" or \"false\".")
                elif setting.lower() == "whitelist":
                    if value is None:
                        await simple_codeblock(ctx, f"[ Whitelist ]\n"
                                                    f"Allow users to use the bot.")
                    elif value.lower() == "true":
                        if config['CONFIGURATION']['blacklist'] == "True":
                            config['CONFIGURATION']['blacklist'] = "False"
                        config['CONFIGURATION']['whitelist'] = "True"
                        write()
                        await simple_codeblock(ctx, f"[ Whitelist ]\n"
                                                    f"Whitelist has been turned on")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['whitelist'] = "False"
                        write()
                        await simple_codeblock(ctx, f"[ Whitelist ]\n"
                                                    f"Whitelist has been turned off")
                    else:
                        await simple_codeblock(ctx, f"[ Whitelist ]\n"
                                                    f"Invalid value, must be \"true\" or \"false\".")
                elif setting.lower() == "autoupdate":
                    if value is None:
                        await codeblock_settings(ctx, "AutoUpdate", "Lost-UB will check for updates as soon as you open the program.")
                    elif value.lower() == "true":
                        config['CONFIGURATION']['autoupdate'] = "True"
                        write()
                        await codeblock_settings(ctx, "AutoUpdate", "AutoUpdate is now enabled, Lost-UB will now check for updates every time you open the program.")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['autoupdate'] = "False"
                        write()
                        await codeblock_settings(ctx, "AutoUpdate", "AutoUpdate is now disabled. Lost-UB will now check for up"
                                                                    "dates every time you open the program.")
                    else:
                        await codeblock_settings(ctx, "AutoUpdate", "Invalid value, must be true or false")
                else:
                    await simple_codeblock(ctx, f"[ Configuration Section ]\n"
                                                f"Setting not found.\n"
                                                f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                                f"[ Settings ]\n"
                                                f"- blacklist | {config['CONFIGURATION']['blacklist']}\n"
                                                f"- autoupdate | {config['CONFIGURATION']['autoupdate']}")

            else:
                await codeblock_sections(ctx)


def setup(userbot):
    userbot.add_cog(Settings(userbot))
