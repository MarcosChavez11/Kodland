import discord
from bot_logic import gen_pass
from bot_logic import flip_coin
from bot_logic import gen_emodji
from bot_logic import numero 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("hola"):
        await message.channel.send("Hola")
    elif message.content.startswith("bye"):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("+emoji"):
        await message.channel.send(gen_emodji())
    elif message.content.startswith("+coin"):
        await message.channel.send(flip_coin())
    elif message.content.startswith("+pswd"):
        await message.channel.send(f"Tu contraseña generada es: {gen_pass(10)}")
    else:
        await message.channel.send(message.content)

client.run("Tu token va aqui")
