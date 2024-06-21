import os
import random
import discord
import requests
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
animales_img=['https://ibb.co/d4x43N8','https://ibb.co/MGgHyy6','https://ibb.co/SNLFCjv','https://ibb.co/2yXdzWv']
@bot.command('mem')
async def mem(ctx):
    img_mem = random.choice(os.listdir('images'))
    with open(f'images/{img_mem}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
print(os.listdir('images'))

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def duck(ctx):
    '''Una vez que llamamos al comando dog, 
    el programa llama a la función get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command('animales')
async def animales(ctx):
    '''Una vez que llamamos al comando animales, 
    el programa toma una imagen aleatoria de la variable animales_img'''
    image_url = random.choice(animales_img)
    await ctx.send(image_url)

bot.run("tu token")
