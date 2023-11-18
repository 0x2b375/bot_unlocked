import discord
import os
import sqlite3
from discord.ext import commands
from dotenv import load_dotenv

conn = sqlite3.connect('unlocked.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mute_timeouts (
        guild_id INTEGER,
        member_id INTEGER,
        unmute_time TEXT,
        reason TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hardmute_timeouts (
        guild_id INTEGER,
        member_id INTEGER,
        unmute_time TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS muted_member_roles (
        member_id INTEGER,
        roles TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS add_restrict (
        guild_id INTEGER,
        member_id INTEGER,
        time INT
    )
''')

load_dotenv()
token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def setup_hook():
    for filename in os.listdir('events'):
        if filename.endswith('.py'):
            await bot.load_extension(f'events.{filename[:-3]}')

    for filename in os.listdir('commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')
            
    for filename in os.listdir('slash_commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'slash_commands.{filename[:-3]}')
    

bot.run(token)
