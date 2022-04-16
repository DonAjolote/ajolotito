import discord
import random
from discord.ext import commands
import sys
sys.path.append('..')
from list.funlist import *


class Fun(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def meme(self, ctx):
		await ctx.channel.trigger_typing()
		await ctx.send(random.choice(memes))
		await ctx.message.delete()
	
	@commands.command(aliases=['8ball'])
	async def ball(self, ctx):
		await ctx.channel.trigger_typing()
		await ctx.send(random.choice(respuestas))
	@ball.error
	async def ball_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Por favor, inserta una pregunta.")

	@commands.command()
	async def up(self, ctx, *, msg:str):
		await ctx.channel.trigger_typing()
		await ctx.send(" ".join(list(msg.upper())))
		await ctx.message.delete()
	@up.error
	async def up_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Por favor, inserta un texto/palabra.")

	@commands.command()
	async def down(self, ctx, *, msg:str):
		await ctx.channel.trigger_typing()
		await ctx.send(" ".join(list(msg.lower())))
		await ctx.message.delete()
	@down.error
	async def down_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Por favor, inserta un texto/palabra.")

	@commands.command()
	async def reverse(self, ctx, *, msg:str):
		await ctx.channel.trigger_typing()
		await ctx.send(msg[::-1])
		await ctx.message.delete()
	@reverse.error
	async def reverse_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Por favor, inserta un texto/palabra.")


	@commands.command()
	async def intellect(self, ctx, *, msg:str):
		await ctx.channel.trigger_typing()
		intellectify = ""
		for char in msg:
			intellectify += random.choice([char.upper(), char.lower()])
		await ctx.send(intellectify)
		await ctx.message.delete()
	@intellect.error
	async def intellect_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Por favor, inserta un texto/palabra.")

	@commands.command()
	async def avatar(self, ctx, *,  member : discord.Member=None):
	    if not member:
	    	member = ctx.message.author
	    	return
	    avatar = member.avatar_url
	    await ctx.send(avatar)


	    

	@commands.command()
	async def say(self, ctx, *, mensaje):
		await ctx.send(mensaje)
		await ctx.message.delete()

	@commands.command()
	async def p(self, ctx):
		await ctx.send("Prueba")

	@commands.command()
	async def perro(self, ctx):
		await ctx.channel.trigger_typing()
		await ctx.send(random.choice(perros))
	
	@commands.command()
	async def gato(self, ctx):
		await ctx.channel.trigger_typing()
		await ctx.send(random.choice(gatos))

def setup(client):
	client.add_cog(Fun(client))
	print("Fun cargado")