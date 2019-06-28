import os
import discord
import asyncio
import ditto



'''
ditto: your media squire for Discord

usage: python3 start_ditto.py
'''


client = discord.Client()

token = os.environ['TOKEN']

_ditto = ditto.Ditto(client)
print(discord.__version__)
@client.event
async def on_ready():
    print('Improving your Discord multimedia experience...') # maybe Kevin can come up with a clever message to print when the bot wakes up

@client.event
async def on_message(message):
    if message.content.startswith('$Library'):
        await _ditto.share_library(message)
    elif message.content.startswith('$deleteLibrary'):
        await _ditto.delete_library(message)
    elif message.content.startswith('$myLibraries'):
        await _ditto.list_libraries(message)
    elif message.content.startswith('$surpriseMe'):
        await _ditto.surprise(message)
    elif message.content.startswith('$help'):
        await _ditto.help_msg(message)


@client.event
async def on_reaction_add(reaction, user): # it's probably smarter to wait_for(ditto_react) instead of check any time someone reacts on an image - TBD but this works for now
    message = reaction.message
    if _ditto.check_file_type(reaction.message):
        if _ditto.check_for_ditto_react(reaction):
            await _ditto.on_ditto_react(message)

if __name__ == "__main__":

    try:
        client.run(token)
    except:
        client.close()
