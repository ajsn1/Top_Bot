import discord
from discord.ext import commands
from bot_logic import gen_pass, gen_anime_quote, get_anime_image_url, get_waste_type, get_reduce_waste_tips
# from nama_file import nama_variabel
from settings import settings
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pass_gen(ctx,pass_length:int):
    await ctx.send(gen_pass(pass_length))

@bot.command(description="Anime Quote Generator for Jujutsu Kaisen, Kimetsu no Yaiba, Sakamoto Days")
async def quote_gen(ctx, anime:str):
    await ctx.send(gen_anime_quote(anime))

@bot.command()
async def meme(ctx):
    # nama_folder/nama_file.extension
    # with open('images/mem1.jpeg', 'rb') as f:
    #     # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
    #     picture = discord.File(f)

    #menyimpan nama nama file di suatu folder dalam variabel lsit
    all_local_images = os.listdir('images')
    img_name = random.choice(all_local_images)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command('anime_img')
async def anime_img(ctx, keyword:str):
    '''Setelah kita memanggil perintah anime, program akan memanggil fungsi get_anime_image_url'''
    anime_url = get_anime_image_url(keyword)
    await ctx.send(anime_url)

@bot.command()
async def type(ctx, *, waste:str):
    '''Setelah kita memanggil perintah type, program akan memanggil fungsi get_waste_type'''
    waste_type = get_waste_type(waste)
    await ctx.send(waste_type)

#dicoba di dc
# $type plastic cup

@bot.command()
async def tips(ctx, how_many:int):
    '''Setelah kita memanggil perintah tips, program akan memanggil fungsi get_reduce_waste_tips'''
    tips_list = get_reduce_waste_tips(how_many)
    tips_msg = "\n".join(tips_list)
    await ctx.send(tips_msg)

bot.run(settings["TOKEN"])
