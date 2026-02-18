import discord
import os

TOKEN = "MTQ3MzQ4NDQ0MzU4NjAwMzEwNw.GkUQ40.lQdrtfef_SzeAPLoiTLscP1aRuifkn8pXEBenU"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Done! {client.user} is online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'يا دارك':
        await message.channel.send('عيون دارك! أنا شغال يا وحش ⚽🎮')

client.run(TOKEN)
