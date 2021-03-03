import discord
import os 
import markov

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        filename = markov.open_and_read_file("green-eggs.txt")
        markov_chains = markov.make_chains(filename)
        makov_text = markov.make_text(markov_chains)
        await message.channel.send(markov_text)

        # open_and_read_file
        # make_chains
        # make_text

client.run(os.environ['DISCORD_TOKEN'])