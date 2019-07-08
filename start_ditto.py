import os
import discord
import asyncio
import ditto

'''
Ditto - your media squire for Discord

Provide bot token as environment variable:
    export TOKEN='my_token_here'

Usage:
    python3 start_ditto.py
'''

client = discord.Client()

try:
    token = os.environ['TOKEN']
except KeyError:
    print('Make sure you\'ve provided your bot token as an environment variable. Use: export TOKEN = \'my_token_here\'.')
    client.close()

_ditto = ditto.Ditto(client)
@client.event
async def on_ready():
    print('Improving your Discord media experience...')
    print('Currently running on Discord.py version {}. Ditto runs best on version 0.16.12.'.format(discord.__version__))

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
async def on_reaction_add(reaction, user):
    message = reaction.message
    if _ditto.check_file_type(reaction.message):
        if _ditto.check_for_ditto_react(reaction):
            await _ditto.on_ditto_react(message, user)

if __name__ == "__main__":

    try:
        client.run(token)
    except:
        client.close()
