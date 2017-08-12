
import discord
from discord.ext import commands
from os import path
from prefix import prefix
import random
import sys

class codephrase():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Generate a code phrase.")
    async def codephrase(self):
        coin = random.randint(0,1)
        result = ""
        # get the first list of code words, using system-agnostic path
        # delimiters
        list1 = open(path.join(path.curdir, 'files', 'code1.txt')) \
                    .read().split()

        # pick a random word
        firstword = list1[random.randint(0,48)]

        #lather, rinse, repeat
        list2 = open(path.join(path.curdir, 'files', 'code2.txt')) \
                    .read().split()

        secondword = list2[random.randint(0,52)]

        thirdword = list2[random.randint(0,52)]

        if coin == 0:
            result = firstword + ' ' + secondword
        else:
            result = firstword + ' ' + secondword + ' ' + thirdword
        result = prefix.choosePrefix() + "Your code phrase is " + result + "."
        await self.bot.say(result)

def setup(bot):
    bot.add_cog(codephrase(bot))

