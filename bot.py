import discord
from discord.ext import commands
import secret
import logging
import sys
import os


#mr handy's framework is built on Brown bot by @wethegreenpeople
sys.path.append(os.path.join(sys.path[0],'modules'))
#sys.path.insert(0, r'./modules')


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



description = '''Good to be back, sir.'''
bot = commands.Bot(command_prefix=']', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    await bot.change_status(discord.Game(name="]help for commands."))

    bot.load_extension("fun")
    bot.load_extension("dice")
    bot.load_extension("codephrase")


@bot.event
async def on_message(message):
	if message.channel.is_private and message.content.startswith('http') and message.author != bot.user:
		try:
			invite = await bot.get_invite(message.content)
			if isinstance(invite.server, discord.Object):
				await bot.accept_invite(invite)
				await bot.send_message(message.channel, 'Joined the server.')
				log.info('Joined server {0.server.name} via {1.author.name}'.format(invite, message))
			else:
				log.info('Attempted to rejoin {0.server.name} via {1.author.name}'.format(invite, message))
				await bot.send_message(message.channel, 'Already in that server.')
		except:
			log.info('Failed to join a server invited by {0.author.name}'.format(message))
			await bot.send_message(message.channel, 'Could not join server.')
		finally:
			return

	await bot.process_commands(message)
    
# Loads modules manually for testing and whatnot
@bot.command(pass_context=True, hidden="True")
async def load(ctx, extension_name:str):
	if ctx.message.author.id == "87250476927549440" or "97525736696455168":
	    try:
	        bot.load_extension(extension_name)
	    except (AttributeError, ImportError) as e:
	        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
	        return
	    await bot.say("{} loaded.".format(extension_name))
	else:
		await bot.say("You do not have permission to load/unload cogs")

# Unloads for whatever reason
@bot.command(pass_context=True, hidden=True)
async def unload(ctx, extension_name:str):
	if ctx.message.author.id == "87250476927549440" or "97525736696455168":
	    bot.unload_extension(extension_name)
	    await bot.say("{} unloaded.".format(extension_name))
	else:
		await bot.say("You do not have permission to load/unload cogs")

# Refreshes modules because unloading and then loading is work for peasents.
@bot.command(pass_context=True, hidden=True)
async def refresh(ctx, extension_name:str):
	if ctx.message.author.id:
		bot.unload_extension(extension_name)
		bot.load_extension(extension_name)
		await bot.say("Module refreshed")
	else:
		await bot.say("You don't have permission to refresh this module")


bot.loop.set_debug(True)
bot.run(secret.botToken)