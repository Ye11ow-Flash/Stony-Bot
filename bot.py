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
import major_scrapper, courses_scrapper

intents = discord.Intents.all()
load_dotenv()
TOKEN = os.environ.get('TOKEN', 3)

bot = commands.Bot(command_prefix="?", intents=intents)
bot.remove_command('help')

def create_embed(query_dict):
    embed = discord.Embed(
        title=query_dict["title"], description=query_dict["description"], colour=0X650100)
    embed.add_field(name="Prerequisites",
                    value=query_dict["prereq"], inline=False)
    embed.add_field(name="Credits",
                    value=query_dict["credits"], inline=False)
    embed.add_field(name="Course Code",
                    value=query_dict["code"], inline=False)
    return embed

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def courseinfo(ctx, subject, code):
    class_dict = major_scrapper.get_course_data(subject, code)
    embed = create_embed(class_dict)
    await ctx.send(embed=embed)
    
@bot.command()
async def listcourse(ctx):
    string = "```\n"
    for i in courses_scrapper.get_courses():
        string += i
    await ctx.send(i + '\n```')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help", description="Accessing the undergrad bulletin has never been easier! A major code is the 3 digit major classification, such as CSE or CHE", colour=0X650100)
    embed.add_field(name="?help",
                    value="list of all commands", inline=False)
    embed.add_field(name="?courseinfo  <majorcode> <number>",
                    value="information for any course", inline=False)
    embed.add_field(name="?degreeinfo <majorcode>",
                    value="information about degree requirements", inline=False)
    embed.add_field(name="?randomcourse <majorname>",
                    value="random course in that major!", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    await ctx.send("Sorry! I encountered this error: \n```" + f"{error}" + '```')

bot.run(TOKEN)