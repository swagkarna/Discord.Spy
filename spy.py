import discord
from discord.ext import commands
import asyncio
token = "somerandomtokenblablabla" #insert target token
prefix = ""
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix, self_bot=True)
@bot.event
async def on_message(message):
    print("on:" + " " + message.guild.name + " " + " in ch:" + " " +  message.channel.name + " " + "from:" + " " + message.author.name + ":" + " " + message.content)
asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.new_event_loop()
bot.run(token, bot=False)
