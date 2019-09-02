import discord
from charguana import get_charset
import random

token = "NjE2MDk4ODIyNjQwMjM4NjMw.XWyyTg.fJH5WYSaA3ODZLixARQ2mdoGpCQ"

client = discord.Client()

hiragana = list(get_charset('hiragana'))

@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("ビールとおっぱいがだいすきです！")

    if message.content.find("!COTD") != -1:
        rand_num = random.randint(0, len(hiragana) - 1)
        await message.channel.send(f'Character of the day: {hiragana[rand_num]}')


    if message.content.find("!WOTD") != -1:
        pass

    if message.content.find("!POTD") != -1:
        pass

    if message.content.find("!help") != -1:
        await message.channel.send(f'''
        Commands
    --------
    !hello - Say hi to Gintoki Sensei

    !COTD (Character of the day) - Get the character of the day

    !WOTD (Word of the day!) - Get the word of the day and link to the word pronounciation

    !POTD (Phrase) - Get the phrase of the day

        ''')

client.run(token)
