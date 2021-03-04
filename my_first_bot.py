import discord
import os 
import markov
import sys

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ham me'):
        filename = sys.argv[1:]
        raw_text = markov.open_and_read_file(filename)
        markov_chains = markov.make_chains(raw_text)
        markov_text = markov.make_text(markov_chains)
        await message.channel.send(markov_text)

client.run(os.environ['DISCORD_TOKEN'])