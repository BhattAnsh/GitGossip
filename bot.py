from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import api

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
token = os.getenv('BOT_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)



async def get_response(user_input: str) -> str:
    a = api.Gossip()
    reply = a.gettingRes(user_input)
    return reply
# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        async with message.channel.typing():
            response: str = await get_response(user_message)
            await message.reply(response)
    except Exception as e:
        print(e)


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


client.run(str(token))


