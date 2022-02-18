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

bot = commands.Bot(command_prefix="?", intents=intents)

example_dict = { # this is the object i need returned
    "code": "CSE114",
    "title": "Introduction to Object-Oriented Programming",
    "description": "An introduction to procedural and object-oriented programming methodology. Topics include program structure, conditional and iterative programming, procedures, arrays and records, object classes, encapsulation, information hiding, inheritance, polymorphism, file I/O, and exceptions. Includes required laboratory. This course has been designated as a High Demand/Controlled Access (HD/CA) course. Students registering for HD/CA courses for the first time will have priority to do so.",
    "prereq": "Level 5 or higher on the math placement exam",
    "SBC": "TECH",
    "credits": "4 credits"
}

def create_embed(query_dict):
    embed = discord.Embed(
        title=query_dict["title"], description=query_dict["description"], colour="#650100")
    embed.add_field(name="Prerequisites",
                    value=query_dict["prereq"], inline=False)
    embed.add_field(name="SBC",
                    value=query_dict["credits"], inline=False)
    embed.add_field(name="Course Code",
                    value=query_dict["code"], inline=False)
    return embed

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    

@bot.command()
async def query(ctx):
    embed = create_embed(example_dict)
    await ctx.send(embed=embed)
