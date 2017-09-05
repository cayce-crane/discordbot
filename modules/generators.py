import discord
from discord.ext import commands
from mazerats import Character
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
    async def random(self, schema : str, arg : str, count=1):
     #   try:
        i = 0
        if schema == 'mazerats':
            ch = Character()
            if arg == 'character':
                result = prefix.choosePrefix()
                while (i < count):
                    ch = Character()
                    result += ch.returnChar() + "\n\n"
                    i += 1
            if arg == 'spell':
                result = prefix.choosePrefix()
                while (i < count):
                    result += ch.randomSpell() + "\n"
                    i += 1
        await self.bot.say(result)
     #   except Exception:
      #      await self.bot.say('Format must be "]random <schema> <argument>".')
      #      return


def setup(bot):
    bot.add_cog(generators(bot))