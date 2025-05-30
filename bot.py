import discord
from discord.ext import commands
from modelo import get_class
intencions = discord.Intents.default()
intencions.message_content = True

bot=commands.Bot(command_prefix='!', intents=intencions)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for img in ctx.message.attachments:
            nombre_img = img.filename
            await img.save(f"Imagenes/{nombre_img}")
            await ctx.send("Imagen guardada")

            resultado = get_class(
                model_path= "./keras_model.h5",
                labels_path = "./labels.txt",
                image_path= f"Imagenes/{nombre_img}"
            )

            await ctx.send(f"Resulrado: {resultado}")

token = "COLOCA TU TOKEN AQUÍ"
bot.run(token)
