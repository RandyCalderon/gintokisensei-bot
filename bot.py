import discord
from charguana import get_charset
import random
import jaconv


def read_token():
    with open("token.txt", "r") as token_file:
        lines = token_file.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()

hiragana = list(get_charset('hiragana'))


@client.event
async def on_message(message):

    message.content = message.content.lower()

    if message.content.startswith("!hello"):
        await message.channel.send("ビールとおっぱいがだいすきです！")

    if message.content.startswith("!cotd"):
        rand_num = random.randint(0, len(hiragana) - 1)
        rand_hiragana_char = hiragana[rand_num]

        translated_char = jaconv.kana2alphabet(rand_hiragana_char)

        # TODO Let's try to make this look nicer!
        await message.channel.send(f'Character of the day: {rand_hiragana_char}\nTranslation: {translated_char}')

    if message.content.startswith("!wotd"):
        pass

    if message.content.startswith("!potd"):
        pass

    if message.content.startswith("!help"):

        e = discord.Embed(description='''
        Commands
        -------------
        ***!hello*** - Say hi to Gintoki Sensei
        ***!COTD***   (Character of the day!) - Get the character of the day
        ***!WOTD***   (Word of the day!) - Get the word of the day and link to the word pronounciation
        ***!POTD***   (Phrase of the day!) - Get the phrase of the day''', colour=discord.Colour.teal())

        await message.channel.send(embed=e)


client.run(token)
