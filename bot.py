import configparser
import os
import discord

config = configparser.ConfigParser()


def write():
    config.write(open('config.ini', 'w'))


# Checks to see if "config.ini" exists, if not then it will create one.
if not os.path.exists('config.ini'):
    config['CONFIGURATION'] = {
        "token": f"{input('Welcome, please enter in your token: ')}"
    }
    write()
else:
    config.read('config.ini')


class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully Logged In.")

    async def on_message(self, message):
        if message.author == client.user:
            if message.content == ">greet":
                await message.reply("Hello :)")


client = MyClient()
client.run(config['CONFIGURATION']['token'])
# for safety purposes and ease of access, your token will be stored in
# config.ini. if for whatever reason you mess up the token, just go to
# config.ini and edit the token value.