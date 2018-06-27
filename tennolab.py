import discord
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
client =discord.Client( )

BOT_PREFIX = ("-", "-")
TOKEN ="NDU3OTk1MDY4NDk0NzA4NzQ2.DgsVhw.ZRLmIdTWTydelWOuHfbXPSaIHSk"

client = Bot(command_prefix=BOT_PREFIX)





@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Bine ai venit {0.mention} pe {1.name}!'
    await client.send_message(server, fmt.format(member, server))

    
    

@client.command(name='globu',
                description="raspunde cu da sau nu la intrebari.",
                brief="Raspunde la tot!.",
                aliases=['globule'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Ai 3 de nu!',
        'Am luat foc!',
        'Mint, dar voi spune...',
        'De sigur ca NU!',
        'Absolut!',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)




@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Warframe"))
    print("Logged in as " + client.user.name)




client.run(TOKEN)
