import discord
from charguana import get_charset
import random

def read_token():
    with open("token.txt", "r") as token_file:
        lines = token_file.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

hiragana = list(get_charset('hiragana'))

@client.event
async def on_message(message):
    if message.content.startswith("!hello") == True:
        await message.channel.send("ビールとおっぱいがだいすきです！")

    if message.content.startswith("!COTD") == True:
        rand_num = random.randint(0, len(hiragana) - 1)
        await message.channel.send(f'Character of the day: {hiragana[rand_num]}')

    if message.content.startswith("!WOTD") == True:
        pass

    if message.content.startswith("!POTD") != True:
        pass

    if message.content.startswith("!help") == True:

        e = discord.Embed(description='''

        Commands
        -------------
        ***!hello*** - Say hi to Gintoki Sensei

        ***!COTD***   (Character of the day!) - Get the character of the day

        ***!WOTD***   (Word of the day!) - Get the word of the day and link to the word pronounciation

        ***!POTD***   (Phrase of the day!) - Get the phrase of the day''', colour=discord.Colour.teal())

        await message.channel.send(embed=e)


client.run(token)
