import discord
import requests
import os
from dotenv import load_dotenv
from discord.ext import commands
from capital import WeeklyActivity


def main():
    load_dotenv("../.env")
    TOKEN_DISCORD = os.getenv('TOKEN_DISCORD')
    TOKEN_COC = os.getenv('TOKEN_COC')
    ID_CLAN = os.getenv('ID_CLAN')

    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix="!", intents=intents)

    session = requests.Session()
    session.headers.update({'Authorization': 'Bearer ' + TOKEN_COC})

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.command()
    async def getWeeklyActifs(ctx):
        await WeeklyActivity(ctx, session, ID_CLAN)

    client.run(TOKEN_DISCORD)


main()
