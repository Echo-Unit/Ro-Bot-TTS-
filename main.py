import discord
import os
import random
import asyncio
from gtts import gTTS
from discord.ext import commands
from keep_alive import keep_alive
from discord.ext.commands import Bot
from discord import FFmpegPCMAudio
from discord.utils import get

bot = commands.Bot(command_prefix=['T','t',''])

client = discord.Client()

##auto send message##
#if voice.play == playing and message.content != MessageFinal
#  await tts.save('MSGbackfill.mp3')

@bot.event
async def on_message(message):
  if message.channel.id == 919700301466959913:
    channel = message.author.voice.channel
    userMessage = message.content
    print(userMessage)
    userName = message.author.display_name
    said = ("said")
    MessageFinal = userName + said + str(userMessage)
    tts = gTTS(MessageFinal)
    tts.save('MSG.mp3', lang='en', tld='com.au')
    if not channel:
      await message.send("You are not connected to a voice channel")
      return
    voice = get(bot.voice_clients, guild=message.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('MSG.mp3')
    player = voice.play(source) 
#Disconnect

@bot.command(alias=["tsstop","TSstop"])
async def tsStop (ctx):
  voice = get(bot.voice_clients, guild=ctx.guild)
  await voice.disconnect()
  await ctx.send("Channel Left")

keep_alive()
bot.run(os.getenv("Token"))
