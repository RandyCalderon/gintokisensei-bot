import discord


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        print(lines[0].strip())
        return lines[0].strip()


token = read_token()

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")

client.run(token)
