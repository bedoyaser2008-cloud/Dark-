import discord
import google.generativeai as genai
from flask import Flask
from threading import Thread

# 1. منبه عشان السيرفر يفضل شغال
app = Flask('')
@app.route('/')
def home(): return "OK"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. إعداد الذكاء الاصطناعي بمفتاحك
genai.configure(api_key="C17jtSXT4V2jaDESa2YXwXQTBnL0XllTBF2-aCPQCZ8")
model = genai.GenerativeModel('gemini-pro')

# 3. التوكن الجديد بتاعك
TOKEN = "MTQ3MzQ4NDQ0MzU4NjAwMzEwNw.G_kdI3._A9XGX4NcVR-eMFAbA36dWRVaRmFbaUmPq7c5s"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is online and ready!')

@client.event
async def on_message(message):
    if message.author == client.user: return
    try:
        # "مخ" دارك اللي بيخليه يرد بذكاء gemini
        prompt = f"أنت دارك، عمرك 17 سنة، صانعك المهندس عبد الرحمن، تحب فيفا وروبلوكس. رد بلهجة شبابية: {message.content}"
        response = model.generate_content(prompt)
        await message.channel.send(response.text)
    except:
        await message.channel.send("في مشكلة في الاتصال يا وحش، جرب تاني!")

keep_alive()
client.run(TOKEN)
