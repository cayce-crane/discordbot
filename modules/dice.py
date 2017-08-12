import discord
from discord.ext import commands
from os import path
from prefix import prefix
import random
import sys

class dice():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="roll dice in NdN format.")
    async def roll(self, dice : str):
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        result = prefix.choosePrefix() + result
        await self.bot.say(result)

def setup(bot):
    bot.add_cog(dice(bot))