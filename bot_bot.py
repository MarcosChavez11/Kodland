import discord
import random, os, requests
from discord.ext import commands
from bot_logic import gen_pass, flip_coin, gen_emodji, numero

print(os.listdir('imageprogramacion'))
print(os.listdir('imagepov'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="+", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command(name="hola")
async def hola(ctx):
    await ctx.send("Hola")

@bot.command(name="bye")
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command(name="emoji")
async def emoji(ctx):
    await ctx.send(gen_emodji())

@bot.command(name="coin")
async def coin(ctx):
    await ctx.send(flip_coin())
import random

@bot.command(name="azar")
async def azar(ctx):
    numero = random.randint(1, 100)
    await ctx.send(f"Tu número aleatorio es: {numero}")

@bot.command(name="repite")
async def repite(ctx, veces: int, *, contenido: str = "repitiendo..."):
    for _ in range(veces):
        await ctx.send(contenido)

@bot.command(name="joined")
async def joined(ctx, member: discord.Member):
    if member.joined_at:
        joined_date = discord.utils.format_dt(member.joined_at, style="F")
        await ctx.send(f'{member.name} se unió el {joined_date}')
    else:
        await ctx.send(f"No se pudo determinar cuándo {member.name} se unió.")

@bot.command(name="pswd")
async def pswd(ctx):
    await ctx.send(f"Tu contraseña generada es: {gen_pass(10)}")

@bot.command(name="suma")
async def suma(ctx, a: int = None, b: int = None):  # Hacemos los argumentos opcionales
    if a is None or b is None:  
        await ctx.send("Error: Debes ingresar dos números. Ejemplo: `+suma 5 10`")
        return
    await ctx.send(f"La suma de {a} + {b} es {a + b}")

@bot.command(name="dado")
async def dado(ctx):
    resultado = random.randint(1, 6)
    await ctx.send(f"🎲 Has sacado un {resultado}")

@bot.command()
async def memeprogramacion(ctx):
    x= os.listdir("imageprogramacion")
    y= random.choice(x)
    with open(f'imageprogramacion/{y}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def memepov(ctx):
    x= os.listdir("imagepov")
    y= random.choice(x)
    with open(f'imagepov/{y}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data.get('url', None)
    return None  

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data.get('url', None)
    return None  

def get_pokemon_image_url():
    pokemon_id = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data["sprites"]["front_default"]
    return None  

def get_anime_by_keyword(keyword):
    url = f"https://kitsu.io/api/edge/anime?filter[text]={keyword}"
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data.get('image', None)
    return None  

@bot.command(name="duck")
async def duck(ctx):
    image_url = get_duck_image_url()
    if image_url:
        await ctx.send("🦆 ¡Aquí tienes un pato! 🦆")
        await ctx.send(image_url)
    else:
        await ctx.send("No se pudo obtener la imagen del pato. Intenta de nuevo.")

@bot.command(name="dog")
async def dog(ctx):
    image_url = get_dog_image_url()
    if image_url:
        await ctx.send("🐶 ¡Aquí tienes un perrito! 🐶")
        await ctx.send(image_url)
    else:
        await ctx.send("No se pudo obtener la imagen del perro. Intenta de nuevo.")

@bot.command(name="pokemon")
async def pokemon(ctx):
    '''Envía la imagen de un Pokémon aleatorio desde la PokeAPI'''
    pokemon_id = random.randint(1, 1017)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    res = requests.get(url)
    if res.status_code != 200:
        await ctx.send("No se pudo obtener la imagen del Pokémon. Intenta de nuevo.")
        return
    data = res.json()
    nombre = data['name'].capitalize()
    imagen_url = data['sprites']['other']['official-artwork']['front_default']
    await ctx.send(f"¡Aquí tienes un Pokémon aleatorio! 🐉\n**{nombre}**")
    await ctx.send(imagen_url)

@bot.command(name="anime")
async def anime(ctx, *, keyword: str):
    '''Busca animes relacionados con cualquier palabra clave que el usuario proporcione.'''
    animes = get_anime_by_keyword(keyword)
    if animes:
        # Enviar todos los resultados
        for anime in animes:
            title = anime['attributes']['canonicalTitle']
            description = anime['attributes'].get('description', 'No description available')
            await ctx.send(f"**{title}**\n{description}\n")
    else:
        await ctx.send(f"No se encontraron animes con la palabra '{keyword}'. Intenta de nuevo.")

@bot.command(name="fox")
async def fox(ctx):
    image_url = get_fox_image_url()
    if image_url:
        await ctx.send("🦊 ¡Aquí tienes un zorro! 🦊")
        await ctx.send(image_url)
    else:
        await ctx.send("No se pudo obtener la imagen del zorro. Intenta de nuevo.")


@bot.command(name="chiste")
async def chiste(ctx):
    chistes = [
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas.",
        "¿Cómo se dice pañuelo en chino? Saka-moko.",
    ]
    await ctx.send(random.choice(chistes))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

bot.run("Tu token va aqui")
