import discord
from charguana import get_charset
import random

token = "NjE2MDk4ODIyNjQwMjM4NjMw.XWifpA.rhbfgIgZRdBOmJ32ND_U0wCbJ-0"

client = discord.Client()

hiragana = list(get_charset('hiragana'))

@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("ビールとおっぱいがだいすきです！")

    if message.content.find("!WOTD") != -1:
        rand_num = random.randint(0, len(hiragana) - 1)
        await message.channel.send(f'Character of the day: {hiragana[rand_num]}')

    if message.content.find("!help") != -1:
        # TODO: implement
        pass

client.run(token)
