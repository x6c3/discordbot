import discord
import requests
from discord.ext import commands
import random

class UserWelcome(commands.Bot):
    async def on_ready(self):
        print(f'{self.user} connected to Discord')

    async def on_member_join(self, member):
        welcome_channel_id = 1135835966586761279 
        guild = member.guild

        welcome_channel = guild.get_channel(welcome_channel_id)
        if welcome_channel is not None:
            welcome_message = f'Welcome {member.mention} to {guild.name}'
            await welcome_channel.send(welcome_message)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

token = 'MTEzMjk2OTEwNjc3NDE3OTkwMA.GRYuBw.yXqkGj2tEgU-KXc14iTSDeFptiR9HV1_ro2bZE'

bot = UserWelcome(command_prefix=">", intents=intents)

@bot.command()
async def nsfw(ctx):
    keyword = 'memes'
    num_posts = 5 

    url = f'https://www.reddit.com/r/{keyword}/top/.json?limit={num_posts}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    posts = requests.get(url, headers=headers)
    data = posts.json()

    memes = [
        post['data']['url'] 
        for post in data['data']['children'] 
        if 'preview' in post['data'] and 'images' in post['data']['preview']
    ]

    
    random.shuffle(memes)

  
    for memes in memes:
        await ctx.send(memes)

bot.run(token)
