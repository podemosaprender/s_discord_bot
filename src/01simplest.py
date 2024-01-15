# bot.py
import os
TOKEN = os.getenv('DISCORD_TOKEN')

import discord

#VER: https://discordpy.readthedocs.io/en/stable/quickstart.html
intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(f"onmsg {message} {message.content}")
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    else:
        await message.channel.send('Un pesado!')


client.run(TOKEN)
