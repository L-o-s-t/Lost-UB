from bot import *


class UserInfo(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        if blacklist_check(ctx):
            log(ctx, "BLACKLIST", f"{ctx.author.display_name} tried to use the command USERINFO.")
        else:
            log(ctx, "USERINFO")
            minute = ""
            friends = ""
            guilds = ""
            roles = ""
            gay = random.randint(0, 100)
            if member == bot.user:
                gay = "very straight for using Lost-UB!"
            elif gay >= 50:
                gay = "yes"
            elif gay <= 49:
                gay = "no"
            for role in member.roles:
                roles += f"- {role}\n"
            if member != bot.user:
                list_of_guilds = await member.mutual_guilds()
                for guild in list_of_guilds:
                    guilds += f"- {guild}\n"
            else:
                guilds = "None"
            if member != bot.user and not member.bot:
                friend_count = 0
                list_of_friends = await member.mutual_friends()
                for friend in list_of_friends:
                    friends += f"- {friend}\n"
                    friend_count += 1
                if friend_count == 0:
                    friends = "No Mutual Friends"
            elif member.bot:
                friends = "bots don't have friends"
            else:
                friends = "no one"
            suffix = ""
            hour = ""
            month = ""
            a = member.created_at
            if a.month == 1:
                month = "Janurary"
            elif a.month == 2:
                month = "February"
            elif a.month == 3:
                month = "March"
            elif a.month == 4:
                month = "April"
            elif a.month == 5:
                month = "May"
            elif a.month == 6:
                month = "June"
            elif a.month == 7:
                month = "July"
            elif a.month == 8:
                month = "August"
            elif a.month == 9:
                month = "September"
            elif a.month == 10:
                month = "October"
            elif a.month == 11:
                month = "November"
            elif a.month == 12:
                month = "December"
            if str(a.day).endswith("1"):
                day = f"{a.day}st"
            elif str(a.day).endswith("2"):
                day = f"{a.day}nd"
            elif str(a.day).endswith("3"):
                day = f"{a.day}rd"
            else:
                day = f"{str(a.day)}th"
            if 1 <= a.hour <= 11:
                suffix = "am"
                hour = f"{a.hour}"
            elif 12 <= a.hour <= 23:
                if a.hour == 13:
                    hour = "1"
                elif a.hour == 14:
                    hour = "2"
                elif a.hour == 15:
                    hour = "3"
                elif a.hour == 16:
                    hour = "4"
                elif a.hour == 17:
                    hour = "5"
                elif a.hour == 18:
                    hour = "6"
                elif a.hour == 19:
                    hour = "7"
                elif a.hour == 20:
                    hour = "8"
                elif a.hour == 21:
                    hour = "9"
                elif a.hour == 22:
                    hour = "10"
                elif a.hour == 23:
                    hour = "11"
                elif a.hour == 24:
                    hour = "12"
                suffix = "pm"
            if 0 <= a.minute <= 9:
                minute = f"0{a.minute}"
            try:
                embed = discord.embeds.Embed(
                    title="User Info",
                    colour=embedcolor()
                )
                embed.add_field(
                    name="User",
                    value=str(member),
                    inline=True
                )
                embed.add_field(
                    name="Date Created",
                    value=f"{month} {day}, {a.year}",
                    inline=True
                )
                if 0 <= a.minute <= 9:
                    embed.add_field(
                        name="Time Created",
                        value=f"{hour}:{minute}{suffix}",
                        inline=True
                    )
                else:
                    embed.add_field(
                        name="Time Created",
                        value=f"{hour}:{a.minute}{suffix}",
                        inline=True
                    )
                embed.set_footer(
                    text=f"Logged in as {ctx.author} | Lost-UB",
                    icon_url=bot.user.avatar_url
                )
                if member.is_avatar_animated():
                    embed.add_field(
                        name="Avatar Url",
                        value=f"[Link]({member.avatar_url_as(format='gif')})",
                        inline=True
                    )
                else:
                    embed.add_field(
                        name="Avatar Url",
                        value=f"[Link]({member.avatar_url_as(format='png')})",
                        inline=True
                    )
                embed.add_field(
                    name="Roles",
                    value=f"{roles}",
                    inline=True
                )
                embed.add_field(
                    name="User ID",
                    value=f"{member.id}",
                    inline=True
                )
                embed.add_field(
                    name="Mutual Friends",
                    value=f"{friends}",
                    inline=True
                )
                embed.add_field(
                    name="Mutual Guilds",
                    value=f"{guilds}",
                    inline=True
                )
                embed.add_field(
                    name="Gay?",
                    value=f"{gay}",
                    inline=True
                )
                embed.set_thumbnail(
                    url=member.avatar_url
                )
                await ctx.reply(embed=embed)
            except discord.Forbidden:
                if 0 <= a.minute <= 9:
                    time_created = f"{hour}:{minute}{suffix}"
                else:
                    time_created = f"{hour}:{a.minute}{suffix}"
                if member.is_avatar_animated():
                    avatar = f"{member.avatar_url_as(format='gif')}"
                else:
                    avatar = f"{member.avatar_url_as(format='png')}"
                await simple_codeblock(ctx,
                                       f"[ User Info ]\n\n"
                                       f"[ User ]\n"
                                       f"{member}\n\n"
                                       f"[ Date Created ]\n"
                                       f"{month} {day}, {a.year}\n\n"
                                       f"[ Time Created ]\n"
                                       f"{time_created}\n\n"
                                       f"[ Avatar Url ]\n"
                                       f"{avatar}\n\n"
                                       f"[ Roles ]\n"
                                       f"{roles}\n"
                                       f"[ User ID ]\n"
                                       f"{member.id}\n\n"
                                       f"[ Mutual Friends ]\n"
                                       f"{friends}\n\n"
                                       f"[ Mutual Guilds ]\n"
                                       f"{guilds}\n"
                                       f"[ Gay? ]\n"
                                       f"{gay}")


def setup(userbot):
    userbot.add_cog(UserInfo(userbot))
