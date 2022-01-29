from bot import *


class Fight(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def fight(self, ctx, member: discord.Member):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use FIGHT", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use FIGHT", color=embedcolor("red"))
        else:
            await log(ctx, description="This user used the command FIGHT", color=embedcolor())
            if member != ctx.author:
                member = await bot.fetch_user(member.id)
                player_health = 100
                player2_health = 100
                player_shield_effectiveness = 0
                player2_shield_effectiveness = 0
                match = 0

                def check(m):
                    return m.author == ctx.author

                def check2(m):
                    return m.author == member

                embed = discord.embeds.Embed(
                    title="Fight",
                    description=f"{ctx.author.display_name} started a fight with {member.display_name}!\n"
                                f"It is {ctx.author.display_name}'s turn.",
                    colour=embedcolor()
                )
                embed.add_field(
                    name=f"{ctx.author.display_name}'s Health",
                    value=f"{player_health}",
                    inline=True
                )
                embed.add_field(
                    name=f"{member.display_name}'s Health",
                    value=f"{player2_health}",
                    inline=True
                )
                embed.add_field(
                    name="Choices",
                    value="- Attack\n"
                          "- Defend\n"
                          "- Run",
                    inline=True
                )
                footer(embed)
                try:
                    await ctx.reply(embed=embed)
                except Exception as e:
                    await simple_codeblock(ctx,
                                           f"[ Fight ]\n"
                                           f"{ctx.author.display_name} started a fight with {member.display_name}!\n"
                                           f"It is {ctx.author.display_name}'s turn.\n\n"
                                           f"[ {ctx.author.display_name}'s Health ]\n"
                                           f"{player_health}\n\n"
                                           f"[ {member.display_name}'s Health ]\n"
                                           f"{player2_health}\n\n"
                                           f"[ Choices ]\n"
                                           f"- Attack\n"
                                           f"- Defend\n"
                                           f"- Run")

                while True:
                    if match % 2 == 0:  # Player 1's Turn
                        if player_health > 0 and player2_health > 0:
                            action = await bot.wait_for('message', check=check, timeout=60.0)
                            if action.content.lower() == "attack":
                                if player2_shield_effectiveness != 0.0:
                                    player_damage = player2_shield_effectiveness * random.randint(0, 30)
                                    player2_health -= player_damage
                                    player2_shield_effectiveness = 0
                                else:
                                    player_damage = random.randint(0, 30)
                                    player2_health -= player_damage

                                embed = discord.embeds.Embed(
                                    title="Fight",
                                    description=f"{ctx.author.display_name} dealt {player_damage} to"
                                                f" {member.display_name}!\n"
                                                f"It is now {member.display_name}'s turn.",
                                    colour=embedcolor()
                                )
                                embed.add_field(
                                    name=f"{ctx.author.display_name}'s Health",
                                    value=f"{player_health}",
                                    inline=True
                                )
                                embed.add_field(
                                    name=f"{member.display_name}'s Health",
                                    value=f"{player2_health}",
                                    inline=True
                                )
                                embed.add_field(
                                    name="Choices",
                                    value="- Attack\n"
                                          "- Defend\n"
                                          "- Run",
                                    inline=True
                                )
                                footer(embed)
                                try:
                                    await action.reply(embed=embed)
                                except Exception as e:
                                    await simple_codeblock(ctx,
                                                           f"[ Fight ]\n"
                                                           f"{ctx.author.display_name} dealt {player_damage} to"
                                                           f" {member.display_name}!\n"
                                                           f"It is now {member.display_name}'s turn.\n\n"
                                                           f"[ {ctx.author.display_name}'s Health ]\n"
                                                           f"{player_health}\n\n"
                                                           f"[ {member.display_name}'s Health ]\n"
                                                           f"{player2_health}\n\n"
                                                           f"[ Choices ]\n"
                                                           f"- Attack\n"
                                                           f"- Defend\n"
                                                           f"- Run")

                            elif action.content.lower() == "defend":
                                player_shield_effectiveness = random.choice([0.0, 1.0])

                                embed = discord.embeds.Embed(
                                    title="Fight",
                                    description=f"{ctx.author.display_name} decided to defend themselves.\n"
                                                f"It is now {member.display_name}'s turn.",
                                    colour=embedcolor()
                                )
                                embed.add_field(
                                    name=f"{ctx.author.display_name}'s Health",
                                    value=f"{player_health}",
                                    inline=True
                                )
                                embed.add_field(
                                    name=f"{member.display_name}'s Health",
                                    value=f"{player2_health}",
                                    inline=True
                                )
                                embed.add_field(
                                    name="Choices",
                                    value="- Attack\n"
                                          "- Defend\n"
                                          "- Run",
                                    inline=True
                                )
                                footer(embed)
                                try:
                                    await action.reply(embed=embed)
                                except Exception as e:
                                    await simple_codeblock(ctx,
                                                           f"[ Fight ]\n"
                                                           f"{ctx.author.display_name} decided to defend themselves.\n"
                                                           f"It is now {member.display_name}'s turn.\n\n"
                                                           f"[ {ctx.author.display_name}'s Health ]\n"
                                                           f"{player_health}\n\n"
                                                           f"[ {member.display_name}'s Health ]\n"
                                                           f"{player2_health}\n\n"
                                                           f"[ Choices ]\n"
                                                           f"- Attack\n"
                                                           f"- Defend\n"
                                                           f"- Run")

                            elif action.content.lower() == "run":

                                embed = discord.embeds.Embed(
                                    title="Fight",
                                    description=f"{ctx.author.display_name} forfeits! "
                                                f"{member.display_name} wins the fight!",
                                    colour=embedcolor()
                                )
                                embed.add_field(
                                    name=f"{ctx.author.display_name}'s Health",
                                    value=f"{player_health}",
                                    inline=True
                                )
                                embed.add_field(
                                    name=f"{member.display_name}'s Health",
                                    value=f"{player2_health}",
                                    inline=True
                                )
                                footer(embed)
                                try:
                                    await action.reply(embed=embed)
                                except Exception as e:
                                    await simple_codeblock(ctx,
                                                           f"[ Fight ]\n"
                                                           f"{ctx.author.display_name} forfeits! "
                                                           f"{member.display_name} wins the fight!\n\n"
                                                           f"[ {ctx.author.display_name}'s Health ]\n"
                                                           f"{player_health}\n\n"
                                                           f"[ {member.display_name}'s Health ]\n"
                                                           f"{player2_health}")

                                break
                        elif player_health > 0 and player2_health < 0:
                            embed = discord.embeds.Embed(
                                title="Fight",
                                description=f"{ctx.author.display_name} wins the fight!",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name=f"{ctx.author.display_name}'s Health",
                                value=f"{player_health}",
                                inline=True
                            )
                            embed.add_field(
                                name=f"{member.display_name}'s Health",
                                value=f"{player2_health}",
                                inline=True
                            )
                            footer(embed)
                            try:
                                await ctx.send(embed=embed)
                            except Exception as e:
                                await simple_codeblock(ctx,
                                                       f"[ Fight ]\n"
                                                       f"{ctx.author.display_name} wins the fight!\n\n"
                                                       f"[ {ctx.author.display_name}'s Health ]\n"
                                                       f"{player_health}\n\n"
                                                       f"[ {member.display_name}'s Health ]\n"
                                                       f"{player2_health}")
                            break
                        elif player_health < 0 and player2_health > 0:
                            embed = discord.embeds.Embed(
                                title="Fight",
                                description=f"{member.display_name} wins the fight!",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name=f"{ctx.author.display_name}'s Health",
                                value=f"{player_health}",
                                inline=True
                            )
                            embed.add_field(
                                name=f"{member.display_name}'s Health",
                                value=f"{player2_health}",
                                inline=True
                            )
                            footer(embed)
                            try:
                                await ctx.send(embed=embed)
                            except Exception as e:
                                await simple_codeblock(ctx,
                                                       f"[ Fight ]\n"
                                                       f"{member.display_name} wins the fight!\n\n"
                                                       f"[ {ctx.author.display_name}'s Health ]\n"
                                                       f"{player_health}\n\n"
                                                       f"[ {member.display_name}'s Health ]\n"
                                                       f"{player2_health}")
                            break
                        match += 1
                    elif match % 2 == 1:  # Player 2's Turn
                        if player_health > 0 and player2_health > 0:
                            action = await bot.wait_for('message', check=check2, timeout=60.0)
                            if action.content.lower() == "attack":
                                if player_shield_effectiveness != 0.0:
                                    player2_damage = player_shield_effectiveness * random.randint(0, 30)
                                    player_health -= player2_damage
                                    player_shield_effectiveness = 0
                                else:
                                    player2_damage = random.randint(0, 30)
                                    player_health -= player2_damage

                                embed = discord.embeds.Embed(
                                    title="Fight",
                                    description=f"{member.display_name} dealt {player2_damage} to "
                                                f"{ctx.author.display_name}!\n"
                                                f"It is now {ctx.author.display_name}'s turn.",
                                    colour=embedcolor()
                                )
                                embed.add_field(
                                    name=f"{ctx.author.display_name}'s Health",
                                    value=f"{player_health}",
                                    inline=True
                                )
                                embed.add_field(
                                    name=f"{member.display_name}'s Health",
                                    value=f"{player2_health}",
                                    inline=True
                                )
                                embed.add_field(
                                    name="Choices",
                                    value="- Attack\n"
                                          "- Defend\n"
                                          "- Run",
                                    inline=True
                                )
                                footer(embed)
                                try:
                                    await action.reply(embed=embed)
                                except Exception as e:
                                    await simple_codeblock(ctx,
                                                           f"[ Fight ]\n"
                                                           f"{member.display_name} dealt {player2_damage} to"
                                                           f" {ctx.author.display_name}!\n"
                                                           f"It is now {ctx.author.display_name}'s turn.\n\n"
                                                           f"[ {ctx.author.display_name}'s Health ]\n"
                                                           f"{player_health}\n\n"
                                                           f"[ {member.display_name}'s Health ]\n"
                                                           f"{player2_health}\n\n"
                                                           f"[ Choices ]\n"
                                                           f"- Attack\n"
                                                           f"- Defend\n"
                                                           f"- Run")

                            elif action.content.lower() == "defend":
                                player2_shield_effectiveness = random.choice([0.0, 1.0])

                                embed = discord.embeds.Embed(
                                    title="Fight",
                                    description=f"{member.display_name} decided to defend themselves.\n"
                                                f"It is now {ctx.author.display_name}'s turn.",
                                    colour=embedcolor()
                                )
                                embed.add_field(
                                    name=f"{ctx.author.display_name}'s Health",
                                    value=f"{player_health}",
                                    inline=True
                                )
                                embed.add_field(
                                    name=f"{member.display_name}'s Health",
                                    value=f"{player2_health}",
                                    inline=True
                                )
                                embed.add_field(
                                    name="Choices",
                                    value="- Attack\n"
                                          "- Defend\n"
                                          "- Run",
                                    inline=True
                                )
                                footer(embed)
                                try:
                                    await action.reply(embed=embed)
                                except Exception as e:
                                    await simple_codeblock(ctx,
                                                           f"[ Fight ]\n"
                                                           f"{member.display_name} decided to defend themselves.\n"
                                                           f"It is now {ctx.author.display_name}'s turn.\n\n"
                                                           f"[ {ctx.author.display_name}'s Health ]\n"
                                                           f"{player_health}\n\n"
                                                           f"[ {member.display_name}'s Health ]\n"
                                                           f"{player2_health}\n\n"
                                                           f"[ Choices ]\n"
                                                           f"- Attack\n"
                                                           f"- Defend\n"
                                                           f"- Run")

                            elif action.content.lower() == "run":

                                embed = discord.embeds.Embed(
                                    title="Fight",
                                    description=f"{member.display_name} forfeits! "
                                                f"{ctx.author.display_name} wins the fight!",
                                    colour=embedcolor()
                                )
                                embed.add_field(
                                    name=f"{ctx.author.display_name}'s Health",
                                    value=f"{player_health}",
                                    inline=True
                                )
                                embed.add_field(
                                    name=f"{member.display_name}'s Health",
                                    value=f"{player2_health}",
                                    inline=True
                                )
                                embed.add_field(
                                    name="Choices",
                                    value="- Attack\n"
                                          "- Defend\n"
                                          "- Run",
                                    inline=True
                                )
                                footer(embed)
                                try:
                                    await action.reply(embed=embed)
                                except Exception as e:
                                    await simple_codeblock(ctx,
                                                           f"[ Fight ]\n"
                                                           f"{member.display_name} forfeits! "
                                                           f"{ctx.author.display_name} wins the fight!\n\n"
                                                           f"[ {ctx.author.display_name}'s Health ]\n"
                                                           f"{player_health}\n\n"
                                                           f"[ {member.display_name}'s Health ]\n"
                                                           f"{player2_health}")

                                break
                        elif player_health > 0 and player2_health < 0:
                            embed = discord.embeds.Embed(
                                title="Fight",
                                description=f"{ctx.author.display_name} wins the fight!",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name=f"{ctx.author.display_name}'s Health",
                                value=f"{player_health}",
                                inline=True
                            )
                            embed.add_field(
                                name=f"{member.display_name}'s Health",
                                value=f"{player2_health}",
                                inline=True
                            )
                            embed.add_field(
                                name="Choices",
                                value="- Attack\n"
                                      "- Defend\n"
                                      "- Run",
                                inline=True
                            )
                            footer(embed)
                            try:
                                await ctx.send(embed=embed)
                            except Exception as e:
                                await simple_codeblock(ctx,
                                                       f"[ Fight ]\n"
                                                       f"{member.display_name} wins the fight!\n\n"
                                                       f"[ {ctx.author.display_name}'s Health ]\n"
                                                       f"{player_health}\n\n"
                                                       f"[ {member.display_name}'s Health ]\n"
                                                       f"{player2_health}")
                            break
                        elif player_health < 0 and player2_health > 0:
                            embed = discord.embeds.Embed(
                                title="Fight",
                                description=f"{ctx.author.display_name} wins the fight!",
                                colour=embedcolor()
                            )
                            embed.add_field(
                                name=f"{ctx.author.display_name}'s Health",
                                value=f"{player_health}",
                                inline=True
                            )
                            embed.add_field(
                                name=f"{member.display_name}'s Health",
                                value=f"{player2_health}",
                                inline=True
                            )
                            embed.add_field(
                                name="Choices",
                                value="- Attack\n"
                                      "- Defend\n"
                                      "- Run",
                                inline=True
                            )
                            footer(embed)
                            try:
                                await ctx.send(embed=embed)
                            except Exception as e:
                                await simple_codeblock(ctx,
                                                       f"[ Fight ]\n"
                                                       f"{ctx.author.display_name} wins the fight!\n\n"
                                                       f"[ {ctx.author.display_name}'s Health ]\n"
                                                       f"{player_health}\n\n"
                                                       f"[ {member.display_name}'s Health ]\n"
                                                       f"{player2_health}")
                            break
                        match += 1
            else:
                await ctx.reply("You can't fight yourself.")


def setup(userbot):
    userbot.add_cog(Fight(userbot))
