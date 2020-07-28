import discord
from discord.ext import commands
import asyncio
token = "" #insert target token
prefix = ""
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix, self_bot=True)
@bot.event
async def on_message(message):
    print(message.author.name + ":" + " " + message.content)
asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.new_event_loop()
bot.run(token, bot=False)
