from bot import *
import requests


class Hangman(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def hangman(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                await log(ctx, "BLACKLIST", "This user attempted to use HANGMAN", color=embedcolor("red"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                await log(ctx, "WHITELIST", "This user attempted to use HANGMAN", color=embedcolor("red"))
        else:
            await log(ctx, description="This user used the command HANGMAN", color=embedcolor())
            health = 6
            display = []
            guesses = []
            requested_word = requests.get('https://random-word-form.herokuapp.com/random/noun')
            random_word = f"{requested_word.json()}".replace('[\'', '').replace('\']', '')
            for x in f"{random_word}":
                display.append('-')
            try:
                embed = discord.embeds.Embed(
                    title="Hangman",
                    description=f"{'♥' * health}\n"
                                f"Word: {' '.join(display)}\n"
                                f"Guesses: {', '.join(guesses)}",
                    colour=embedcolor()
                )
                footer(embed)
                message = await ctx.reply(embed=embed)
            except Exception as e:
                message = await simple_codeblock(ctx, f"[ Hangman ]\n"
                                                      f"{'♥' * health}\n"
                                                      f"Word: {' '.join(display)}\n"
                                                      f"Guesses: {', '.join(guesses)}")

            def check(m):
                return m.author == ctx.author

            while True:
                guess = await bot.wait_for("message", check=check)
                letters = 0
                for letter in guess.content:
                    letters += 1
                if letters == 1:
                    if guess.content not in guesses:
                        guesses.append(guess.content)
                        count = 0
                        for x in f"{random_word}":
                            if x == guess.content.lower():
                                display.pop(count)
                                display.insert(count, guess.content.lower())
                                count += 1
                            else:
                                if guess.content.lower() not in f"{random_word}":
                                    health -= 1
                                    break
                                count += 1
                        try:
                            embed = discord.embeds.Embed(
                                title="Hangman",
                                description=f"{'♥' * health}\n"
                                            f"Word: {' '.join(display)}\n"
                                            f"Guesses: {', '.join(guesses)}.",
                                colour=embedcolor()
                            )
                            footer(embed)
                            message = await ctx.reply(embed=embed)
                        except Exception as e:
                            message = await simple_codeblock(ctx, f"[ Hangman ]\n"
                                                                  f"{'♥' * health}\n"
                                                                  f"Word: {' '.join(display)}\n"
                                                                  f"Guesses: {', '.join(guesses)}")
                        if ''.join(display) == random_word:
                            try:
                                embed = discord.embeds.Embed(
                                    title="Hangman | YOU WON.",
                                    description=f"{'♥' * health}\n"
                                                f"Word: {' '.join(display)}\n"
                                                f"Guesses: {', '.join(guesses)}.\n"
                                                f"The word was {random_word}",
                                    colour=embedcolor()
                                )
                                footer(embed)
                                message = await ctx.reply(embed=embed)
                            except Exception as e:
                                await simple_codeblock(ctx, f"[ Hangman | YOU WON. ]\n"
                                                            f"{'♥' * health}\n"
                                                            f"Word: {' '.join(display)}\n"
                                                            f"Guesses: {', '.join(guesses)}.\n"
                                                            f"The word was {random_word}")
                            break
                        elif health == 0:
                            try:
                                embed = discord.embeds.Embed(
                                    title="Hangman | YOU LOST.",
                                    description=f"{'♥' * health}\n"
                                                f"Word: {' '.join(display)}\n"
                                                f"Guesses: {', '.join(guesses)}.\n"
                                                f"The word was {random_word}",
                                    colour=embedcolor("red")
                                )
                                footer(embed)
                                message = await ctx.reply(embed=embed)
                            except Exception as e:
                                await simple_codeblock(ctx, f"[ Hangman | YOU LOST. ]\n"
                                                            f"{'♥' * health}\n"
                                                            f"Word: {' '.join(display)}\n"
                                                            f"Guesses: {', '.join(guesses)}.\n"
                                                            f"The word was {random_word}")
                            break
                        else:
                            continue
                    else:
                        error = discord.embeds.Embed(
                            title="You've already guessed this letter",
                            description=f"Guesses: {', '.join(guesses)}.",
                            colour=embedcolor("red")
                        )
                        footer(error)
                        await ctx.send(embed=error)
                else:
                    error = discord.embeds.Embed(
                        title="You can only guess single letters.",
                        description=f"Guesses: {', '.join(guesses)}.",
                        colour=embedcolor("red")
                    )
                    footer(error)
                    await ctx.send(embed=error)


def setup(userbot):
    userbot.add_cog(Hangman(userbot))
