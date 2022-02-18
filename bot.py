# bot.py
# 02.18.2022

from discord.ext import commands
from dotenv import load_dotenv
import discord
import os
import json
import random
import requests
import asyncio

intents = discord.Intents.all()
load_dotenv()
TOKEN = os.environ.get('TOKEN', 3)

bot = commands.Bot(command_prefix=">", intents=intents)

