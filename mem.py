import discord
import os
from discord.ext import commands 
import random

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='/',intents=intents)

@bot.command()
async def mempr(ctx):
    img = random.choice(os.listdir('images'))
    with open(f'images/{img}','rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def memgm(ctx):
    img = random.choice(os.listdir('images1'))
    with open(f'images1/{img}','rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def meman(ctx):
    img = random.choice(os.listdir('images2'))
    with open(f'images2/{img}','rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
    
        


bot.run ("MTEzMjI3NzgyMzEyNjYzNDQ5Nw.G-k-_6.CB5Feh07ZEBZLdRcD7yzXC9DWUS0FtDdZ8aGIQ")
