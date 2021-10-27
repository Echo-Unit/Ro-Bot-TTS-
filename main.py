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

bot = commands.Bot(command_prefix=[''])

client = discord.Client()

##auto send message##

@bot.command(alias=['tts','TTS'])
async def tts (ctx,*, arg):
  channel = ctx.message.author.voice.channel
  userMessage = arg
  tts = gTTS(userMessage)
  tts.save('MSG.mp3')
  if not channel:
      await ctx.send("You are not connected to a voice channel")
      return
  voice = get(bot.voice_clients, guild=ctx.guild)
  if voice and voice.is_connected():
        await voice.move_to(channel)
  else:
        voice = await channel.connect()
  source = FFmpegPCMAudio('MSG.mp3')
  player = voice.play(source)

##Repeat Message##

@bot.command(alias=['tts','tts Repeat','tts repeat','tts rep'])
async def botspeak(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('MSG.mp3')
    player = voice.play(source)


keep_alive()
bot.run(os.getenv("Token"))
