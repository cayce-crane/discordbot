import discord
from discord.ext import commands
from os import path
from prefix import prefix
import sys

class fun():
    def __init__(self, bot):
        self.bot = bot

    # Simply throws out a lot of trumpets. dootdoot thnkx mr skeltal
    @commands.command(description="Knee deep in the doot.")
    async def doot(self):
        await self.bot.say(":trumpet:" * 200)

    #translate text to full width
    @commands.command(description='As wide as text will get.')
    async def ominous(self, text : str):
        ominous_text = ""
        for c in text:
            if c == ' ':
                ominous_text += "  "
            else:
                # Get the full-width unicode text equivalent of the character
                ominous_text += chr(0xFEE0 + ord(c))
        ominous_text = prefix.choosePrefix() + ominous_text
        await self.bot.say(ominous_text)


def setup(bot):
    bot.add_cog(fun(bot))