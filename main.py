import discord
import os

TOKEN = "MTQ3MzQ4NDQ0MzU4NjAwMzEwNw.Gre56g.dJVJZc3wWdm4SYWCHXoYc_BdTYeozB6fc-lCKw"

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
