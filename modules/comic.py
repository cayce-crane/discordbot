import discord
from discord.ext import commands
import lxml.html
from os import path
from prefix import prefix
import random
import sys
import urllib.request
from urllib.parse import quote

class comic():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description = "Get an achewood")
    async def achewood(self, *arg):
        result = ""
        # If no search argument is supplied, grab a random strip using urllib and lxml
        if len(arg) == 0:
            page = urllib.request.urlopen('http://www.ohnorobot.com/random.pl?comic=636')
            doc = lxml.html.parse(page)
            imgurl = doc.xpath('//img/@src')
            result =  'http://www.achewood.com' + imgurl[1]
        else:
            # if there's a search term, first turn it into a searchable string
            search = ' '.join(arg)
            search = search.replace('"', '')
            search = quote(search)
            # run the search with ohnorobot
            searchpage = urllib.request.urlopen('http://www.ohnorobot.com/index.php?s=' \
            	+ search + '&Search=Search&comic=636')
            doc = lxml.html.parse(searchpage).getroot()
            # get the links from the results page
            links = doc.xpath('//a/@href')
            # if there're no results, say so
            if 'letsbefriends.php' in links[2]:
                result = "No strip containing that dialog was found, sir. My apologies."
            else:
                # otherwise return the best result
                best_result = links[2]
                page = urllib.request.urlopen(best_result)
                doc = lxml.html.parse(page)
                imgurl = doc.xpath('//img/@src')
                result = 'http://www.achewood.com' + imgurl[1]
        result = prefix.choosePrefix() + result
        await self.bot.say(result)

def setup(bot):
    bot.add_cog(comic(bot))