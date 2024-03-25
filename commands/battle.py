from bot import *


class Battle(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def battle(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use BATTLE"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use BATTLE"))
        else:
            await log(ctx)
            player_hp = 100
            enemy_hp = 100
            await simple_codeblock(ctx,
                                    f"[ Battle ]\n"
                                    f"You started a battle! What would you like to do?\n\n"
                                    f"[ Choices ]\n"
                                    f"- Attack\n"
                                    f"- Defend\n"
                                    f"- Run")

            def check(m):
                return m.author == ctx.author

            while True:
                if enemy_hp > 0 and player_hp > 0:
                    action = await bot.wait_for('message', check=check, timeout=60.0)
                    if action.content.lower() == "attack":
                        enemy_action = random.randint(0, 100)
                        player_damage = random.randint(0, 30)
                        if enemy_action >= 50:  # Enemy will attack
                            enemy_damage = random.randint(0, 30)
                            enemy_hp -= player_damage
                            player_hp -= enemy_damage
                            await simple_codeblock(ctx,
                                                    f"[ Battle ]\n"
                                                    f"You dealt {player_damage} damage to the enemy!\n"
                                                    f"The enemy also dealt {enemy_damage} damage to you!\n"
                                                    f"What would you like to do next?\n\n"
                                                    f"[ Your Health ]\n"
                                                    f"{player_hp}\n\n"
                                                    f"[ Enemy Health ]\n"
                                                    f"{enemy_hp}")
                        elif enemy_action <= 49:  # Enemy will defend
                            enemy_shield_effectiveness = random.choice([0.25, 0.50, 0.75, 1.0])
                            player_damage = player_damage * enemy_shield_effectiveness
                            enemy_hp -= player_damage
                            await simple_codeblock(ctx,
                                                    f"[ Battle ]\n"
                                                    f"The enemy blocked your attack, "
                                                    f"so your attack only dealt {player_damage} "
                                                    f"damage!\n"
                                                    f"What would you like to do next?\n\n"
                                                    f"[ Your Health ]\n"
                                                    f"{player_hp}\n\n"
                                                    f"[ Enemy Health ]\n"
                                                    f"{enemy_hp}")
                    elif action.content.lower() == "defend":
                        enemy_action = random.randint(0, 100)
                        enemy_damage = random.randint(0, 30)
                        if enemy_action >= 50:  # Enemy will attack
                            player_shield_effectiveness = random.choice([0.25, 0.50, 0.75, 1.0])
                            enemy_damage = enemy_damage * player_shield_effectiveness
                            player_hp -= enemy_damage
                            await simple_codeblock(ctx,
                                                    f"[ Battle ]\n"
                                                    f"You blocked the enemy's attack, "
                                                    f"so their attack only dealt {enemy_damage} "
                                                    f"damage!\n"
                                                    f"What would you like to do next?\n\n"
                                                    f"[ Your Health ]\n"
                                                    f"{player_hp}\n\n"
                                                    f"[ Enemy Health ]\n"
                                                    f"{enemy_hp}")
                        elif enemy_action <= 49:  # Enemy will defend
                            await simple_codeblock(ctx,
                                                    f" [ Battle ]\n"
                                                    f"You both defended each other, "
                                                    f"blocking each other like idiots!\n"
                                                    f"What would you like to do next?\n\n"
                                                    f"[ Your Health ]\n"
                                                    f"{player_hp}\n\n"
                                                    f"[ Enemy Health ]\n"
                                                    f"{enemy_hp}")
                    elif action.content.lower() == "run":
                        await simple_codeblock(ctx,
                                                f"[ Battle ]\n"
                                                f"You forfeit! The enemy wins!\n\n"
                                                f"[ Your Health ]\n"
                                                f"{player_hp}\n\n"
                                                f"[ Enemy Health ]\n"
                                                f"{enemy_hp}")
                        break
                    else:
                        await simple_codeblock(ctx,
                                                f"[ Battle ]\n"
                                                f"Invalid action!\n\n"
                                                f"[ Choices ]\n"
                                                f"- Attack\n"
                                                f"- Defend\n"
                                                f"- Run")
                elif enemy_hp > 0 and player_hp <= 0:
                    await simple_codeblock(ctx,
                                            f"[ Battle ]\n"
                                            f"The enemy wins! You lose!\n\n"
                                            f"[ Your Health ]\n"
                                            f"{player_hp}\n\n"
                                            f"[ Enemy Health ]\n"
                                            f"{enemy_hp}")
                    break
                elif enemy_hp <= 0 and player_hp > 0:
                    await simple_codeblock(ctx,
                                            f"[ Battle ]\n"
                                            f"You won! The enemy loses!\n\n"
                                            f"[ Your Health ]\n"
                                            f"{player_hp}\n\n"
                                            f"[ Enemy Health ]\n"
                                            f"{enemy_hp}")
                    break
                elif enemy_hp <= 0 and player_hp <= 0:
                    await simple_codeblock(ctx,
                                            f"[ Battle ]\n"
                                            f"It's a tie!\n\n"
                                            f"[ Your Health ]\n"
                                            f"{player_hp}\n\n"
                                            f"[ Enemy Health ]\n"
                                            f"{enemy_hp}")
                    break


def setup(userbot):
    userbot.add_cog(Battle(userbot))
