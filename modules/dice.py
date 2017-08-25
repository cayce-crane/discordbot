import discord
from discord.ext import commands
from os import path
from prefix import prefix
import random
import sys

class dice():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="roll dice in NdN+X format.")
    async def roll(self, dice : str):
        mod = -1
        try:
            if '+' in dice:
                mod = dice[dice.index('+') + 1:]
                dice = dice[0:dice.index('+')]
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN+x!')
            return
        resultsum = 0
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        for r in (result.split(', ')):
            resultsum += int(r)
        if mod != -1:
            result += ' = ' + str(resultsum)
            result += ' + ' + str(mod)
            resultsum += int(mod)
        result += ' = ' + str(resultsum)
        result = prefix.choosePrefix() + result
        await self.bot.say(result)

def setup(bot):
    bot.add_cog(dice(bot))