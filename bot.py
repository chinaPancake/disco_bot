import discord
import requests
from discord.ext import tasks
from config import token_bot, channel_id

class MyClient(discord.Client):
    async def on_ready(self):
        self.my_background_task.start()
        print('We have logged in as {0.user}'.format(self))

    @tasks.loop(seconds=300)  # Runs every 5 minutes
    async def my_background_task(self):
        secik = set()
        url = "https://api.thegraph.com/subgraphs/name/ethprague23pl/fairticket-graph"
        body = {
            "query": """
            {
            ticketBoughts(first: 5) {
                id
                _contractEvent
                _ticketId
                blockNumber
            }
            }
            """
        }

        response = requests.post(url, json=body)
        data = response.json()

        if data['data']['ticketBoughts'][1]['_contractEvent'] not in secik:
            channel = self.get_channel(channel_id)
            await channel.send("***Wallet with address:*** {} \n ***Bought ticket for event:*** {}".format(data['data']['ticketBoughts'][1]['id'],data['data']['ticketBoughts'][1]['_contractEvent']))

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token_bot)
