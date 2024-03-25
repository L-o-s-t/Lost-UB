from bot import *
import requests


class Hangman(commands.Cog):

    def __init__(self, userbot):
        self.bot = userbot

    @commands.command()
    async def hangman(self, ctx):
        if permission_check(ctx):
            if config["CONFIGURATION"]["blacklist"] == "True":
                print(log(ctx, "BLACKLIST", "This user attempted to use HANGMAN"))
            elif config["CONFIGURATION"]["whitelist"] == "True":
                print(log(ctx, "WHITELIST", "This user attempted to use HANGMAN"))
        else:
            print(log(ctx, description="This user used the command HANGMAN"))
            health = 6
            display = []
            guesses = []
            requested_word = requests.get('https://random-word-form.herokuapp.com/random/noun')
            random_word = f"{requested_word.json()}".replace('[\'', '').replace('\']', '')
            for x in f"{random_word}":
                display.append('-')
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
                        message = await simple_codeblock(ctx, f"[ Hangman ]\n"
                                                                f"{'♥' * health}\n"
                                                                f"Word: {' '.join(display)}\n"
                                                                f"Guesses: {', '.join(guesses)}")
                        if ''.join(display) == random_word:
                            await simple_codeblock(ctx, f"[ Hangman | YOU WON. ]\n"
                                                        f"{'♥' * health}\n"
                                                        f"Word: {' '.join(display)}\n"
                                                        f"Guesses: {', '.join(guesses)}.\n"
                                                        f"The word was {random_word}")
                            break
                        elif health == 0:
                            await simple_codeblock(ctx, f"[ Hangman | YOU LOST. ]\n"
                                                        f"{'♥' * health}\n"
                                                        f"Word: {' '.join(display)}\n"
                                                        f"Guesses: {', '.join(guesses)}.\n"
                                                        f"The word was {random_word}")
                            break
                        else:
                            continue
                    else:
                        await simple_codeblock(ctx, f"[ Hangman ]\n"
                                                    f"You've already guessed this letter!\n\n"
                                                    f"[ Guesses ]\n"
                                                    f"{', '.join(guesses)}.")
                else:
                    await simple_codeblock(ctx, f"[ Hangman ]\n"
                                                f"You can only guess single letters.\n\n"
                                                f"[ Guesses ]\n"
                                                f"{', '.join(guesses)}.")


def setup(userbot):
    userbot.add_cog(Hangman(userbot))
