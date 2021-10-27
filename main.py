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

bot = commands.Bot(command_prefix=['+'])

client = discord.Client()


@bot.command()
async def tts (ctx,*, arg):
  channel=bot.get_channel(798662468086923274)
  await channel.send(arg)
  userMessage = arg
  tts = gTTS(userMessage)
  tts.save('MSG.mp3')

@bot.command()
async def bb(ctx):
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
