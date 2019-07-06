
import discord
from discord.ext import commands
from discord import user
from discord.ext.commands import Bot
import asyncio
import chalk
from datetime import datetime
import json
import os
from discord import User
from discord import activity
import datetime
from datetime import datetime
import random
from random import randint 
import time
from time import strftime
import mhwbotmsg
from mhwbotmsg import get_xp
from mhwbotmsg import zeit
from mhwbotmsg import get_zeit
from mhwbotmsg import voicezeit
from mhwbotmsg import get_voicezeit
import math



bot = commands.Bot(command_prefix='.')

print (discord.__version__)

async def _shutdown_bot():
    await bot.logout()

extensions = ["mhwbotmsg"]

os.chdir(r"C:\Users\asche\Desktop\mhwbot")



@bot.command()
@commands.has_role("Admin")
async def unload(extension):
    try:
        bot.unload_extension(extension)
        print("{} wurde entfernt".format(extension))
    except Exception as error:
        print("{} konnte nicht entfernt werden. [{}]".format(extension, error))





@bot.event
async def on_ready():
    print ("Bin jetzt bereit")
    print ("Mein Name: " + bot.user.name)
    print ("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="Bot by Deniz Uchiha"))
    

@bot.command(hidden=True)
@commands.has_role("Admin")
async def fuckoff():
    embed = discord.Embed(title="Wird Ausgeschalten...", color=0x00ff00)
    await bot.say(embed=embed)
    await _shutdown_bot()


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    if str(user.status) == "offline":
        statuss = f"Offline seit {get_zeit(user.id)}"
    else:
        statuss = "Online"
    embed = discord.Embed(title="{}'s info".format(user.name), description="Hier ist, was ich herausfinden konnte.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=statuss, inline=True)
    embed.add_field(name="Höchste Rolle", value=user.top_role)
    embed.add_field(name="Beigetreten", value=user.joined_at)
    embed.add_field(name="Nachrichten", value=get_xp(user.id))
    embed.add_field(name="Letzte mal im Voicechannel", value=get_voicezeit(user.id))
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)




@bot.event
async def on_member_update(before, after):
    if str(before.status) == "online":
        if str(after.status) == "offline":
            timestr = time.strftime("%d.%m.%Y-%H:%M:%S")
            zeit(after.id, timestr)



@bot.event
async def on_voice_state_update(before, after):
    if after.voice.voice_channel:
        timestrr = time.strftime("%d.%m.%Y-%H:%M:%S")
        voicezeit(after.id, timestrr)



            
            
#print("{} has gone {} at date-time {}.".format(after.name,after.status,timestr))




if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print("{} konnte nicht geladen werden. [{}]".format(extension, error))






bot.run("NTk2OTU4NTE2NzY2NTcyNTU0.XSBG-Q.0ZDFkozLvnghH_xWcewd5-cvw3g")
