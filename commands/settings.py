from bot import *


class Settings(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def settings(self, ctx, section: str = None, setting: str = None, *, value: str = None):
        def sections_embed(context):
            section_embed = discord.embeds.Embed(
                title="Settings",
                description=f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                colour=embedcolor()
            )
            section_embed.add_field(
                name="Sections",
                value="- afk\n"
                      "- pfp\n"
                      "- mock\n"
                      "- customization\n"
                      "- configuration"
            )
            footer(section_embed)
            return context.reply(embed=section_embed)

        def codeblock_sections_embed(context):
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

        def settings_embed(context, setting_name, description):
            setting_desc_embed = discord.embeds.Embed(
                title=f"{setting_name} Setting",
                description=f"{description}",
                colour=embedcolor()
            )
            footer(setting_desc_embed)
            return context.reply(embed=setting_desc_embed)

        def codeblock_settings_embed(context, setting_name, description):
            return context.reply(f"```ini\n"
                                 f"[ {setting_name} Setting ]\n"
                                 f"{description}\n\n"
                                 f"{codeblock_footer()}\n"
                                 f"```")

        def confirmation(context, setting_name, setting_value):
            setting_confirmation = discord.embeds.Embed(
                title=f"{setting_name} Setting",
                description=f"This has been turned {setting_value}!",
                colour=embedcolor()
            )
            footer(setting_confirmation)
            return context.reply(embed=setting_confirmation)

        def codeblock_confirmation(context, setting_name, setting_value):
            return context.reply(f"```ini\n"
                                 f"[ {setting_name} Setting ]\n"
                                 f"This has been turned {setting_value}!\n\n"
                                 f"{codeblock_footer()}\n"
                                 f"```")

        def setting_error(context, setting_name, settting_description: str = f"Value has to be ``True`` or ``False``!"):
            setting_error_embed = discord.embeds.Embed(
                title=f"{setting_name} Setting",
                description=settting_description,
                colour=embedcolor()
            )
            footer(setting_error_embed)
            return context.reply(embed=setting_error_embed)

        def codeblock_setting_error(context, setting_name,
                                    settting_description: str = f"Value has to be True or False!"):
            return context.reply(f"```ini\n"
                                 f"[ {setting_name} Setting ]\n"
                                 f"{settting_description}\n\n"
                                 f"{codeblock_footer()}\n"
                                 f"```")

        if ctx.author == bot.user:
            await log(ctx, description="This user used the command SETTINGS", color=embedcolor())
            if section is None:
                try:
                    await sections_embed(ctx)
                except Exception as e:
                    await codeblock_sections_embed(ctx)
            elif section.lower() == "afk":
                if setting is None:
                    try:
                        embed = discord.embeds.Embed(
                            title="AFK Section",
                            description=f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Settings",
                            value=f"- legit | {config['CONFIGURATION']['afk_legit']}\n"
                                  f"- message | {config['CONFIGURATION']['afk_msg']}"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        await ctx.reply(embed=embed)
                    except Exception as e:
                        await ctx.reply(f"```ini\n"
                                        f"[ AFK Section ]\n"
                                        f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                        f"[ Settings ]\n"
                                        f"- legit | {config['CONFIGURATION']['afk_legit']}\n"
                                        f"- message | {config['CONFIGURATION']['afk_msg']}\n\n"
                                        f"{codeblock_footer()}\n"
                                        f"```")
                elif setting.lower() == "legit":
                    if value is None:
                        try:
                            await settings_embed(ctx, "Legit AFK",
                                                 "Legit afk sends a typing indicator to make it seem like "
                                                 "you aren't user-botting.")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "Legit AFK",
                                                           "Legit afk sends a typing indicator to make it seem like "
                                                           "you aren't user-botting.")
                    elif value.lower() == "true":
                        config['CONFIGURATION']['afk_legit'] = "True"
                        write()
                        try:
                            await confirmation(ctx, "Legit AFK", "on")
                        except Exception as e:
                            await codeblock_confirmation(ctx, "Legit AFK", "on")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['afk_legit'] = "False"
                        write()
                        try:
                            await confirmation(ctx, "Legit AFK", "off")
                        except Exception as e:
                            await codeblock_confirmation(ctx, "Legit AFK", "off")
                    else:
                        try:
                            await setting_error(ctx, "Legit AFK")
                        except Exception as e:
                            await codeblock_setting_error(ctx, "Legit AFK")
                elif setting.lower() == "message":
                    if value is None:
                        try:
                            await settings_embed(ctx,
                                                 "AFK Message",
                                                 "Set the message to send to users when AFK is enabled.")
                        except Exception as e:
                            await codeblock_settings_embed(ctx,
                                                           "AFK Message",
                                                           "Set the message to send to users when AFK is enabled.")
                    else:
                        config["CONFIGURATION"]["afk_msg"] = value
                        write()
                        try:
                            await simple_embed(ctx, "AFK Message", f"Your afk message was set to: {value}")
                        except Exception as e:
                            await simple_codeblock(ctx, "[ AFK Message ]\n"
                                                        f"Your afk message was set to: {value}")
                else:
                    try:
                        embed = discord.embeds.Embed(
                            title="AFK Section",
                            description=f"Setting not found.\n"
                                        f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Settings",
                            value=f"- legit | {config['CONFIGURATION']['afk_legit']}\n"
                                  f"- message | {config['CONFIGURATION']['afk_msg']}"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        await ctx.reply(embed=embed)
                    except Exception as e:
                        await simple_codeblock(ctx,
                                               f"[ AFK Section ]\n"
                                               f"Setting not found.\n"
                                               f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                               f"[ Settings ]\n"
                                               f"- legit | {config['CONFIGURATION']['afk_legit']}\n"
                                               f"- message | {config['CONFIGURATION']['afk_msg']}")
            elif section.lower() == "mock":
                if setting is None:
                    try:
                        embed = discord.embeds.Embed(
                            title="Mock Section",
                            description=f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Settings",
                            value=f"- automock | {config['CONFIGURATION']['automock']}\n"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        await ctx.reply(embed=embed)
                    except Exception as e:
                        await ctx.reply(f"```ini\n"
                                        f"[ Mock Section ]\n"
                                        f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                        f"[ Settings ]\n"
                                        f"- automock | {config['CONFIGURATION']['automock']}\n\n"
                                        f"{codeblock_footer()}\n"
                                        f"```")
                elif setting.lower() == "automock":
                    if value is None:
                        try:
                            await settings_embed(ctx, "AutoMock",
                                                 "Automatically mocks a user's message when sent.")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "AutoMock",
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
                    try:
                        embed = discord.embeds.Embed(
                            title="Mock Section",
                            description=f"Setting not found.\n"
                                        f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Settings",
                            value=f"- automock | {config['CONFIGURATION']['automock']}\n"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        await ctx.reply(embed=embed)
                    except Exception as e:
                        await simple_codeblock(ctx,
                                               f"[ Mock Section ]\n"
                                               f"Setting not found.\n"
                                               f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                               f"[ Settings ]\n"
                                               f"- automock | {config['CONFIGURATION']['automock']}")
            elif section.lower() == "pfp":
                if setting is None:
                    try:
                        embed = discord.embeds.Embed(
                            title="PFP Section",
                            description=f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Settings",
                            value=f"- silentsteal | {config['CONFIGURATION']['silentsteal']}\n"
                                  f"- silentsave  | {config['CONFIGURATION']['silentsave']}"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        await ctx.reply(embed=embed)
                    except Exception as e:
                        await simple_codeblock(ctx, f"[ PFP Section ]\n"
                                                    f"Command usage: {get_prefix()}"
                                                    f"settings (section) (setting) (value)\n"
                                                    f"\n"
                                                    f"[ Settings ]\n"
                                                    f"- silentsteal | {config['CONFIGURATION']['silentsteal']}\n"
                                                    f"- silentsave  | {config['CONFIGURATION']['silentsave']}")
                elif setting.lower() == "silentsteal":
                    if value is None:
                        try:
                            await simple_embed(ctx, "SilentSteal", "Doesn't send any messages after cmd and deletes "
                                                                   "command "
                                                                   "message.")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "SilentSteal",
                                                           "Doesn't send any messages after cmd and "
                                                           "deletes command "
                                                           "message.")
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
                        try:
                            await simple_embed(ctx, "SilentSave Setting",
                                               "Doesn't send any messages after cmd and deletes command message.")
                        except Exception as e:
                            await simple_codeblock(ctx, "[ SilentSave Setting ]\n"
                                                        "Doesn't send any messages after "
                                                        "cmd and deletes command message.")
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
                    try:
                        embed = discord.embeds.Embed(
                            title="PFP Section",
                            description=f"Setting not found.\n"
                                        f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Settings",
                            value=f"- silentsteal | {config['CONFIGURATION']['silentsteal']}\n"
                                  f"- silentsave  | {config['CONFIGURATION']['silentsave']}"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        await ctx.reply(embed=embed)
                    except Exception as e:
                        await simple_codeblock(ctx, "[ PFP Section ]\n"
                                                    f"Setting not found.\n"
                                                    f"Command usage: {get_prefix()}settings (section) (setting) (value)"
                                                    f"\n\n"
                                                    f"[ Settings ]\n"
                                                    f"- silentsteal | {config['CONFIGURATION']['silentsteal']}\n"
                                                    f"- silentsave  | {config['CONFIGURATION']['silentsave']}")
            elif section.lower() == "customization":
                if setting is None:
                    try:
                        embed = discord.embeds.Embed(
                            title="Customization Section",
                            description=f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Settings",
                            value=f"- embedcolor | {config['CONFIGURATION']['embedcolor']}"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        await ctx.reply(embed=embed)
                    except Exception as e:
                        await simple_codeblock(ctx,
                                               f"[ Customization Section ]\n"
                                               f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                               f"[ Settings ]\n"
                                               f"- embedcolor | {config['CONFIGURATION']['embedcolor']}")
                elif setting.lower() == "embedcolor":
                    if value is None:
                        try:
                            await settings_embed(ctx, "EmbedColor", "Changes the color of all embed messages sent.\n"
                                                                    "All Available Colors"
                                                                    "- Red\n"
                                                                    "- Light Red\n"
                                                                    "- Orange\n"
                                                                    "- Light Orange\n"
                                                                    "- Yellow\n"
                                                                    "- Green\n"
                                                                    "- Light Green\n"
                                                                    "- Blue\n"
                                                                    "- Light Blue\n"
                                                                    "- Purple\n"
                                                                    "- Light Purple\n"
                                                                    "- Pink\n"
                                                                    "- Light Pink")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "EmbedColor",
                                                           "Changes the color of all embed messages sent.\n"
                                                           "All Available Colors\n"
                                                           "- Red\n"
                                                           "- Light Red\n"
                                                           "- Orange\n"
                                                           "- Light Orange\n"
                                                           "- Yellow\n"
                                                           "- Green\n"
                                                           "- Light Green\n"
                                                           "- Blue\n"
                                                           "- Light Blue\n"
                                                           "- Purple\n"
                                                           "- Light Purple\n"
                                                           "- Pink\n"
                                                           "- Light Pink")
                    elif value.lower() == "red":
                        config['CONFIGURATION']['embedcolor'] = "red"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "light red":
                        config['CONFIGURATION']['embedcolor'] = "light red"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "orange":
                        config['CONFIGURATION']['embedcolor'] = "orange"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "light orange":
                        config['CONFIGURATION']['embedcolor'] = "light orange"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "yellow":
                        config['CONFIGURATION']['embedcolor'] = "yellow"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "green":
                        config['CONFIGURATION']['embedcolor'] = "green"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "light green":
                        config['CONFIGURATION']['embedcolor'] = "light green"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "blue":
                        config['CONFIGURATION']['embedcolor'] = "blue"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "light blue":
                        config['CONFIGURATION']['embedcolor'] = "light blue"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "purple":
                        config['CONFIGURATION']['embedcolor'] = "purple"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "light purple":
                        config['CONFIGURATION']['embedcolor'] = "light purple"
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "pink":
                        config['CONFIGURATION']['embedcolor'] = "pink"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    elif value.lower() == "light pink":
                        config['CONFIGURATION']['embedcolor'] = "light pink"
                        write()
                        try:
                            await simple_embed(ctx,
                                               f"EmbedColor",
                                               f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   f"[ EmbedColor ]\n"
                                                   f"EmbedColor was set to {config['CONFIGURATION']['embedcolor']}!")
                    else:
                        try:
                            embed = discord.embeds.Embed(
                                title="EmbedColor Setting",
                                description="Invalid Color",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name="Colors",
                                value="- Red\n"
                                      "- Light Red\n"
                                      "- Orange\n"
                                      "- Light Orange\n"
                                      "- Yellow\n"
                                      "- Green\n"
                                      "- Light Green\n"
                                      "- Blue\n"
                                      "- Light Blue\n"
                                      "- Purple\n"
                                      "- Light Purple\n"
                                      "- Pink\n"
                                      "- Light Pink"
                            )
                            embed.set_footer(
                                text=f"Logged in as {bot.user} | Lost-UB",
                                icon_url=bot.user.avatar_url
                            )
                            await ctx.reply(embed=embed)
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   "[ EmbedColor Setting ]\n"
                                                   "Invalid Color\n\n"
                                                   "[ Colors ]\n"
                                                   "- Red\n"
                                                   "- Light Red\n"
                                                   "- Orange\n"
                                                   "- Light Orange\n"
                                                   "- Yellow\n"
                                                   "- Green\n"
                                                   "- Light Green\n"
                                                   "- Blue\n"
                                                   "- Light Blue\n"
                                                   "- Purple\n"
                                                   "- Light Purple\n"
                                                   "- Pink\n"
                                                   "- Light Pink"
                                                   )
                else:
                    try:
                        embed = discord.embeds.Embed(
                            title="Customization Section",
                            description=f"Setting not found.\n"
                                        f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Settings",
                            value=f"- embedcolor | {config['CONFIGURATION']['embedcolor']}"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        await ctx.reply(embed=embed)
                    except Exception as e:
                        await simple_codeblock(ctx,
                                               f"[ Customization Section ]\n"
                                               f"Setting not found.\n"
                                               f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                               f"[ Settings ]\n"
                                               f"- embedcolor | {config['CONFIGURATION']['embedcolor']}")
            elif section.lower() == "configuration" or section.lower() == "config":
                if setting is None:
                    try:
                        embed = discord.embeds.Embed(
                            title="Configuration Section",
                            description=f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Settings",
                            value=f"- blacklist | {config['CONFIGURATION']['blacklist']}\n"
                                  f"- whitelist | {config['CONFIGURATION']['whitelist']}\n"
                                  f"- richpresence | {config['CONFIGURATION']['rich_presence']}\n"
                                  f"- autoupdate | {config['CONFIGURATION']['autoupdate']}"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        await ctx.reply(embed=embed)
                    except Exception as e:
                        await simple_codeblock(ctx,
                                               f"[ Configuration Section ]\n"
                                               f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                               f"[ Settings ]\n"
                                               f"- blacklist | {config['CONFIGURATION']['blacklist']}\n"
                                               f"- whitelist | {config['CONFIGURATION']['whitelist']}\n"
                                               f"- richpresence | {config['CONFIGURATION']['rich_presence']}\n"
                                               f"- autoupdate | {config['CONFIGURATION']['autoupdate']}")
                elif setting.lower() == "blacklist":
                    if value is None:
                        try:
                            await simple_embed(ctx, "Blacklist", "Prevent users from using the bot.")
                        except Exception as e:
                            await simple_codeblock(ctx, "[ Blacklist ]\n"
                                                        "Prevent users from using the bot.")
                    elif value.lower() == "true":
                        if config['CONFIGURATION']['whitelist'] == "True":
                            config['CONFIGURATION']['whitelist'] = "False"
                        config['CONFIGURATION']['blacklist'] = "True"
                        write()
                        try:
                            await simple_embed(ctx, "Blacklist", "Blacklist has been turned on")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   "[ Blacklist ]\n"
                                                   "Blacklist has been turned on")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['blacklist'] = "False"
                        write()
                        try:
                            await simple_embed(ctx, "Blacklist", "Blacklist has been turned off")
                        except Exception as e:
                            await simple_codeblock(ctx, "[ Blacklist ]\n"
                                                        "Blacklist has been turned off")
                    else:
                        try:
                            await simple_embed(ctx, "Blacklist", "Invalid value, must be ``true`` or ``false``")
                        except Exception as e:
                            await simple_codeblock(ctx, "[ Blacklist ]\n"
                                                        "Invalid value, must be \"true\" or \"false\".")
                elif setting.lower() == "whitelist":
                    if value is None:
                        try:
                            await simple_embed(ctx, "Whitelist", "Allow users to use the bot.")
                        except Exception as e:
                            await simple_codeblock(ctx, "[ Whitelist ]\n"
                                                        "Allow users to use the bot.")
                    elif value.lower() == "true":
                        if config['CONFIGURATION']['blacklist'] == "True":
                            config['CONFIGURATION']['blacklist'] = "False"
                        config['CONFIGURATION']['whitelist'] = "True"
                        write()
                        try:
                            await simple_embed(ctx, "Whitelist", "Whitelist has been turned on")
                        except Exception as e:
                            await simple_codeblock(ctx,
                                                   "[ Whitelist ]\n"
                                                   "Whitelist has been turned on")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['whitelist'] = "False"
                        write()
                        try:
                            await simple_embed(ctx, "Whitelist", "Whitelist has been turned off")
                        except Exception as e:
                            await simple_codeblock(ctx, "[ Whitelist ]\n"
                                                        "Whitelist has been turned off")
                    else:
                        try:
                            await simple_embed(ctx, "Whitelist", "Invalid value, must be ``true`` or ``false``")
                        except Exception as e:
                            await simple_codeblock(ctx, "[ Whitelist ]\n"
                                                        "Invalid value, must be \"true\" or \"false\".")
                elif setting.lower() == "richpresence":
                    if value is None:
                        try:
                            await settings_embed(ctx, "Discord Rich Presence",
                                                 "Enables Lost-UB's status in your profile.")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "Discord Rich Presence",
                                                           "Enables Lost-UB's status in your profile.")
                    elif value.lower() == "true":
                        config['CONFIGURATION']['rich_presence'] = "True"
                        write()
                        try:
                            await settings_embed(ctx, "Discord Rich Presence",
                                                 "Rich Presence is now enabled. You will need to restart Lost-UB")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "Discord Rich Presence",
                                                           "Rich Presence is now enabled. "
                                                           "You will need to restart Lost-UB")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['rich_presence'] = "False"
                        write()
                        try:
                            await settings_embed(ctx, "Discord Rich Presence",
                                                 "Rich Presence is now disabled. You will need to restart Lost-UB")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "Discord Rich Presence",
                                                           "Rich Presence is now disabled. "
                                                           "You will need to restart Lost-UB")
                    else:
                        try:
                            await settings_embed(ctx, "Discord Rich Presence",
                                                 "Invalid value, must be true or false")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "Discord Rich Presence",
                                                           "Invalid value, must be true or false")
                elif setting.lower() == "autoupdate":
                    if value is None:
                        try:
                            await settings_embed(ctx, "AutoUpdate",
                                                 "Lost-UB will check for updates as soon as you open the program.")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "AutoUpdate",
                                                           "Lost-UB will check for updates "
                                                           "as soon as you open the program.")
                    elif value.lower() == "true":
                        config['CONFIGURATION']['autoupdate'] = "True"
                        write()
                        try:
                            await settings_embed(ctx, "AutoUpdate",
                                                 "AutoUpdate is now enabled, Lost-UB will now check for updates every"
                                                 "time you open the program.")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "AutoUpdate",
                                                           "AutoUpdate is now enabled, Lost-UB will now check for "
                                                           "updates every time you open the program.")
                    elif value.lower() == "false":
                        config['CONFIGURATION']['autoupdate'] = "False"
                        write()
                        try:
                            await settings_embed(ctx, "AutoUpdate",
                                                 "AutoUpdate is now disabled. Lost-UB will now check for updates every"
                                                 "time you open the program.")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "AutoUpdate",
                                                           "AutoUpdate is now disabled. Lost-UB will now check for up"
                                                           "dates every time you open the program.")
                    else:
                        try:
                            await settings_embed(ctx, "AutoUpdate",
                                                 "Invalid value, must be true or false")
                        except Exception as e:
                            await codeblock_settings_embed(ctx, "AutoUpdate",
                                                           "Invalid value, must be true or false")
                else:
                    try:
                        embed = discord.embeds.Embed(
                            title="Configuration Section",
                            description=f"Setting not found.\n"
                                        f"Command usage: {get_prefix()}settings (section) (setting) (value)",
                            colour=embedcolor()
                        )
                        embed.add_field(
                            name="Settings",
                            value=f"- blacklist | {config['CONFIGURATION']['blacklist']}\n"
                                  f"- richpresence | {config['CONFIGURATION']['rich_presence']}\n"
                                  f"- autoupdate | {config['CONFIGURATION']['autoupdate']}"
                        )
                        embed.set_footer(
                            text=f"Logged in as {bot.user} | Lost-UB",
                            icon_url=bot.user.avatar_url
                        )
                        await ctx.reply(embed=embed)
                    except Exception as e:
                        await simple_codeblock(ctx,
                                               f"[ Configuration Section ]\n"
                                               f"Setting not found.\n"
                                               f"Command usage: {get_prefix()}settings (section) (setting) (value)\n\n"
                                               f"[ Settings ]\n"
                                               f"- blacklist | {config['CONFIGURATION']['blacklist']}\n"
                                               f"- richpresence | {config['CONFIGURATION']['rich_presence']}\n"
                                               f"- autoupdate | {config['CONFIGURATION']['autoupdate']}")

            else:
                try:
                    await sections_embed(ctx)
                except Exception as e:
                    await codeblock_sections_embed(ctx)


def setup(userbot):
    userbot.add_cog(Settings(userbot))
