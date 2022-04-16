import discord 
import random
from discord.ext import commands, tasks
from itertools import cycle
from discord.utils import get

class HelpCog(commands.Cog):

	def __init__(self, client):
		self.client = client
		
# Prueba

	@commands.group()
	async def help(self, ctx):
		if ctx.invoked_subcommand is None:

			embed = discord.Embed(
				colour=discord.Colour.green(),
				title="Ajolotito Bot Help",
				description="Ayuda sobre el Ajolotito Bot"
			)
			embed.add_field(name="***help mod***", value="Muestra los comandos de moderacion", inline=False)
			embed.add_field(name="***help gifs***", value="Muestra los comandos sobre gifs", inline=False)
			embed.add_field(name="***help rank***", value="Muestra los comandos de niveles `(No disponible)`", inline=False)
			embed.add_field(name="***help fun***", value="Muestra todos los comandos entretenidos", inline=False)
			embed.add_field(name="***help logs***", value="Muestra los comandos sobre logs")
			embed.add_field(name="***soporte***", value="Invitacion para el servidor de soporte", inline=False)
			await ctx.send(embed=embed)


	@help.group()
	async def mod(self, ctx):

		embed = discord.Embed(
			colour=discord.Colour.green(),
			title="Ajolotito Bot Help",
			description="Ayuda sobre la moderacion"
		)

		embed.add_field(name="***ban***", value="Banear un usuario", inline=False)
		embed.add_field(name="***unban***", value="Desbanear un usuario", inline=False)
		embed.add_field(name="***kick***", value="Kickear un usuario", inline=False)
		embed.add_field(name="***mute***", value="Mutear un usuario", inline=False)
		embed.add_field(name="***unmute***", value="Desmutear un usuario", inline=False)
		embed.add_field(name="clear", value="Borra cierta cantidad de mensajes", inline=False)
		embed.add_field(name="***ping***", value="Tiempo de respuesta del bot", inline=False)

		await ctx.send(embed=embed)

		

	@help.command()
	async def gifs(self, ctx):
		
		embed = discord.Embed(
			colour=discord.Colour.green(),
			title="Ajolotito Bot Help",
			description="Ayuda sobre los gifs"
		)

		embed.add_field(name="***perro***", value="Manda el gif de un perro aleatorio", inline=False)
		embed.add_field(name="***gato***", value="Manda el gif de un gato aleatorio", inline=False)
		await ctx.send(embed=embed)


	@help.command()
	async def fun(self, ctx):

		embed = discord.Embed(
			colour=discord.Colour.green(),
			title="Ajolotito Bot Help",
			description="Ayuda sobre los comandos divertidos"
			)

		embed.add_field(name="***Comandos***", value="`meme`, `ball`, `up`, `down`, `reverse`, `intellect`, `say`, `perro`, `gato`", inline=False)
		embed.set_footer(text="Descubre que es lo que hacen")

		await ctx.send(embed=embed)

	@help.command()
	async def logs(self, ctx):

		embed = discord.Embed(
			colour=discord.Colour.green(),
			title="Ajolotito Bot Help",
			description="Ayuda para configurar los logs"
			)
		embed.add_field(name="***welcome***", value="Configurar el canal para las bienvenidas. \n Ejemplo: ```a.welcome #canal```", inline=False)
		embed.add_field(name="***farewell***", value="Configurar el canal para las despedidas. \n Ejemplo: ```a.farewell #canal```", inline=False)
		embed.add_field(name="***wel_text***", value="Configurar el texto de bienvenidas. Este comando tiene varios parametros posibles: \n {user} = Nombre del usuario \n {mention} = Mencionar al usuario \n {guild} = Nombre del servidor \n {members} = Numero de usuarios \n Ejemplo: ```Bienvenido {user} :hand_splayed:, esperemos la pases bien en {guild}, contigo ya somos {members} usuarios. Pasate por #canal para leer las reglas```", inline=False)
		embed.add_field(name="***bye_text***", value="Configurar el texto de despedidas. Este comando tiene varios parametros posibles: \n {user} = Nombre del usuario \n {guild} = Nombre del servidor \n {members} = Numero de usuarios \n Ejemplo: ```Adios {user} :hand_splayed:, esperamos volverte a ver en {guild}, ahora somos {members} usuarios ```", inline=False)
		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(HelpCog(client))
	print("Ayuda cargada")
