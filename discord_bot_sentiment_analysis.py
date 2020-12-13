import discord
from discord.ext import commands
import boto3

description="\
Sentiment Analysis Bot\
"

comprehend = boto3.client(service_name='comprehend')

intents=discord.Intents.default()
bot=commands.Bot(command_prefix='.',description=description,intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print(bot.guilds)

@bot.command()
async def sa(ctx, message):
    print(message)

    aws_reply=comprehend.detect_sentiment(Text=message, LanguageCode='en')
    print(aws_reply)
    sentiment=aws_reply['Sentiment']
    print(sentiment)

    if sentiment=='POSITIVE':
        emoji = '\U0001F600'
        await ctx.message.add_reaction(emoji)
    elif sentiment=='NEGATIVE':
        emoji='\U00002639'
        await ctx.message.add_reaction(emoji)
    elif sentiment=='NEUTRAL':
        emoji='\U000026AB'
        await ctx.message.add_reaction(emoji)

@bot.command()
async def safull(ctx, message):
    print(message)

    aws_reply=comprehend.detect_sentiment(Text=message, LanguageCode='en')
    print(aws_reply)
    sentiment=aws_reply['Sentiment']
    print(sentiment)

    if sentiment=='POSITIVE':
        emoji = '\U0001F600'
        await ctx.message.add_reaction(emoji)
    elif sentiment=='NEGATIVE':
        emoji='\U00002639'
        await ctx.message.add_reaction(emoji)
    elif sentiment=='NEUTRAL':
        emoji='\U000026AB'
        await ctx.message.add_reaction(emoji)

    embed=discord.Embed()
    embed.add_field(name='test',value=message)
    await ctx.send(embed=embed)
    await ctx.send(aws_reply['SentimentScore'])


file=open('discord_bot.secret','r')
secret=file.readline()
file.close()

bot.run(secret)
