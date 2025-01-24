import discord
from discord.ext import commands
from bot_logic import gen_pass, flip_coin, gen_emodji, numero

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

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

bot.run("Tu token va aqui")
