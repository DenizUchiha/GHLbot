import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='.')
import json
import os
from discord import User
os.chdir(r"C:\Users\asche\Desktop\mhwbot")

class msg:

    
    async def on_message(self, message):
        user_add_xp(message.author.id, 1)

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member, server):
        with open("mhwbot.json", "r") as f:
            users = json.load(f)
        
def setup(bot):
    bot.add_cog(msg(bot))

def user_add_xp(user_id: int, exp: int,):
    if os.path.isfile("mhwbot.json"):
        try:
            with open('mhwbot.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['nachrichten'] += exp
            with open('mhwbot.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('mhwbot.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['nachrichten'] = exp
            with open('mhwbot.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['nachrichten'] = exp
        with open('mhwbot.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=1)

def get_xp(user_id: int):
    try:

        if os.path.isfile('usersmsg.json'):
            with open('usersmsg.json', 'r') as fp:
                users = json.load(fp)
            return users[user_id]['Nachrichten']
        else:
            return 0
    except KeyError:
        return "hat noch nichts gesendet"

def get_zeit(user_id: int):
    try:
        if os.path.isfile('users.json'):
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            return users[user_id]['zulezt online']
        else:
            return 0
    except KeyError:
        return "UNBEKANNT"

def get_voicezeit(user_id: int):
    try:
        if os.path.isfile('users.json'):
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            return users[user_id]['voicezeit']
        else:
            return 0
    except KeyError:
        return "war noch nicht in einem Voicechannel"

def zeit(user_id:int, timestr: int):    
    if os.path.isfile("mhwbot.json"):

        try:
            with open('mhwbot.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['zulezt online'] = timestr
            with open('mhwbot.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('mhwbot.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['zulezt online'] = timestr
            with open('mhwbot.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)


def voicezeit(user_id:int, timestr: int):    
    if os.path.isfile("mhwbot.json"):

        try:
            with open('mhwbot.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['voicezeit'] = timestr
            with open('mhwbot.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('mhwbot.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['voicezeit'] = timestr
            with open('mhwbot.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
