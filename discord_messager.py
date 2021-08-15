import yaml
import sys
import logging
import discord

''' 
------------------------------------------------------------------------
    DISCORD CLIENT - Init the client
------------------------------------------------------------------------
'''

discord_client = discord.Client()
with open('config.yml', 'rb') as f:
    config = yaml.safe_load(f)

''' 
------------------------------------------------------------------------
    MESSAGE AS WE RECIEVE FROM FORWARDGRAM SCRIPT
------------------------------------------------------------------------
'''

message = sys.argv[1]

''' 
------------------------------------------------------------------------
    DISCORD SERVER START EVENT - We will kill this immaturely
------------------------------------------------------------------------
'''
# when discord is initalized, it will trigger this event. 
# we quickly send messages to our discord channels and quit the script prematurely.
# this gets trigged again when a new message is sent on channel from telegram

@discord_client.event
async def on_ready():

    print('We have logged in as {0.user}'.format(discord_client))
    print('Awaiting Telegram Message')

    # My channels are for RTX card drops and PS5
    channel_1 = discord_client.get_channel(config["discord_1_channel"])
    channel_2 = discord_client.get_channel(config["discord_2_channel"])
    channel_3 = discord_client.get_channel(config["discord_3_channel"])
    channel_4 = discord_client.get_channel(config["discord_4_channel"])

    if 'Mario' in message:
        await channel_1.send(message)
    elif 'Zelda' in message:
        await channel_2.send(message)
    elif 'Minecraft' in message:
        await channel_3.send(message)
    elif 'Valhiem' in message:
        await channel_4.send(message)

    quit()

discord_client.run(config["discord_bot_token"])

    

    

