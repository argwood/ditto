import discord
import asyncio
import ditto


'''
ditto: your media squire for Discord

usage: python3 start_ditty.py
'''


client = discord.Client()

token = 'NTkyNzkzOTg5NjgyNDI5OTc1.XREgqw.2EevJ7HjFfeovaDDvzB9Um4FDho' # don't forget to move token to a config file

_ditto = ditto.Ditto(client)

@client.event
async def on_ready():
    print('Improving your Discord multimedia experience...') # maybe Kevin can come up with a clever message to print when the bot wakes up

@client.event
async def on_message(message):
    if message.content.startswith('$test'): # just a basic test to be used to see if bot is on
        await client.send_message(message.channel, 'Hello!')

## below should be moved to a new file; all message responses are temporary for testing

@client.event
async def on_reaction_add(reaction, user): # it's probably smarter to wait_for(ditto_react) instead of check any time someone reacts on an image - TBD but this works for now
    message = reaction.message
    if _ditto.check_file_type(reaction.message):
        await client.send_message(message.channel, 'Great, that\'s a supported file type!')
        if _ditto.check_for_ditto_react(reaction):
            await client.send_message(message.channel, 'You even used the right reaction!') # passed the reaction tests; here you would actually call library functions
        else: await client.send_message(message.channel, 'Okay but that\'s not a ditto')
    else: await client.send_message(message.channel, 'You\'ve just reacted to a message...cool I guess')

if __name__ == "__main__":

    try:
        client.run(token)
    except:
        client.close()
