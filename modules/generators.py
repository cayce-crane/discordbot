import discord
from discord.ext import commands
from os import path
from prefix import prefix
import pypyodbc
import random as rand
import sys

class generators():
def __init__(self, bot):
    self.bot = bot

@commands.command(description="Generate a variety of things. Syntax: ']random <schema> <argument>' \n " \
    "e.g. ']random mazerats character'")
async def random(self, schema : str, arg : str):
    try:
        ### Add the setup to sql server here
        ### connection = 

        try:
            if schema = 'mazerats':
                if arg = 'character':





        except Exception:
            await self.bot.say('Format must be "]random <schema> <argument>".')
            return

    except Exception:
        await self.bot.say('Error connecting to database!')






def setup(bot):
    bot.add_cog(generators(bot))