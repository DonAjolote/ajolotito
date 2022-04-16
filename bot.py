import discord 
import random
from discord.ext import commands, tasks
from itertools import cycle
from discord.utils import get
import sys
import datetime
import traceback

client = commands.Bot(command_prefix = '-')
client.remove_command("help")

# Token

token = "ODEyMTMxNDUyMjAzMzAyOTcz.YC8SWg.QEuSbdlK3gPfTZ1p57OiSMkCnUU"

status = cycle([
    'Recuerda usar a.help', 
    'Nada', 
    'Prueba todos mis comandos'
])

@client.event 
async def on_ready():
	change_status.start()
	print('Listo jefe')
	
	
@tasks.loop(minutes=10)
async def change_status():
		await client.change_presence(activity=discord.Game(next(status)))

# LOAD COGS

initial_extensions = ['cogs.mod', 'cogs.fun', 'cogs.ayuda']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Error al cargar {extension}', file=sys.stderr)
            traceback.print_exc() 


#ERRORES
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('Este comando no existe. Utiliza a.help.')


# iNFO BOT
@client.command()
async def info(ctx):

    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="Ajolotito Bot Info",
        description="Informacion sobre el Ajolotito Bot"
    )
    embed.set_author(name="Hecho por DonAjolote#4322", icon_url="https://cdn.discordapp.com/attachments/756297115277328438/772287148199116800/img14_2.jpg")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/756297115277328438/772287603273498645/IMG_20201001_183230.jpg")
    embed.add_field(name="Prefijo", value="a.", inline=False)    
    embed.add_field(name="Función", value="La única funcion de este bot es entretener, divertir y moderar.", inline=False)
    embed.add_field(name="Lenguaje", value="Esta programado en Python - Discord.py", inline=False)
    embed.add_field(name="Version", value="Alpha 3.1", inline=False)
    embed.add_field(name="Ayudantes", value="Chapi, Konk, Lil MARCROCK22")
    embed.set_footer(text="Aqui iria un corazon, si tan solo supiera ponerlo")


    await ctx.send(embed=embed)

# Ayuda

@client.command()
async def soporte(ctx):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="Ajolotito Bot Support",
        description="Servidor de soporte del Ajolotito Bot"
        )
    embed.add_field(name="¡Unete!",value="[Haz click en mi para unirte](https://discord.gg/NvfbBbw3G2)")

    await ctx.send(embed=embed)


@client.command()
async def ping(ctx,):
    embed = discord.Embed(
        colour=discord.Colour.green(),
        title="Latencia Ajolotito Bot",
        description="Latencia del Ajolotito Bot"
        )
    embed.add_field(name="El ping es de:", value=f":desktop: {round(client.latency * 1000)}ms.")

    await ctx.send(embed=embed)


client.run(token)
