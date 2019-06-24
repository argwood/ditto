import discord
import asyncio
import ditto


'''
ditto: your media squire for Discord

usage: python3 start_ditty.py
'''


client = discord.Client()

token = 'NTkyNzkzOTg5NjgyNDI5OTc1.XREgqw.2EevJ7HjFfeovaDDvzB9Um4FDho'

@client.event
async def on_ready():
    print('Improving your Discord multimedia experience...')

@client.event
async def on_message(message):
    if message.content.startswith('$test'):
        await client.send_message(message.channel, 'Hello!')


if __name__ == "__main__":

    try:
        client.run(token)
    except:
        client.close()
