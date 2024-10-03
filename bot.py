import discord
import random
from bot_func import gen_pass
from bot_func import gen_emodji
from discord.ext import commands
from bot_func import get_duck_image_url
from bot_func import get_dog_image_url
import os


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def bye(ctx):
    await ctx.send("😔")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji)


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def add1(ctx, left: int, right: int):
    """Multiplies two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def add2(ctx, left: int, right: int):
    """Divides two numbers."""
    await ctx.send(left / right)

@bot.command()
async def add3(ctx, left: int, right: int):
    """Subtracts two numbers."""
    await ctx.send(left - right)

@bot.command()
async def ayuda(ctx):
    await ctx.send("Ayuda. Para ejecutar comandos siempre utiliza $ al inicio. Ejemplo: $hello, Comandos: add, add1, add2, add3 (suma, multiplica, divide, resta), hello, bye, etc.")

@bot.command()
async def Help(ctx):
    await ctx.send("Help. Use $ al inicio para ejecutar comandos. Ejemplo: $hello, Comandos: add, add1, add2, add3 (suma, multiplica, divide, resta), hello, bye, etc.")
    
@bot.command()
async def meme(ctx):
    meme_alet = random.choice(os.listdir("images"))
    with open(f'images/{meme_alet}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def gato(ctx):
    meme_alet = random.choice(os.listdir("images_cat"))
    with open(f'images_cat/{meme_alet}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def cat(ctx):
    meme_alet = random.choice(os.listdir("images_gatitos"))
    with open(f'images_gatitos/{meme_alet}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando dog, 
    el programa llama a la función get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)


bot.run("token")
