import discord 
import random
import datetime
import time
import mysql
import mysql.connector
from discord.ext import commands, tasks
from itertools import cycle
from discord.utils import get


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="ajolotito",
	auth_plugin="mysql_native_password"
)

cursor = mydb.cursor()

class Wels(commands.Cog):
	def __init__(self, client):
			self.client = client


	
	@commands.command()
	async def prueba(self, ctx, *, nombre: str = None):
		sql = 'INSERT INTO users (name) VALUES (%s)'
		cursor.execute(sql, (nombre,))
		mydb.commit()
		await ctx.send(f"Insertado {nombre}")
		
	
	
	@commands.Cog.listener()
	async def on_member_join(self, member):
		cursor.execute("SELECT channel_id FROM `welcome` WHERE guild_id = " + str(member.guild.id))
		result = cursor.fetchone()
		if result is None:
			return
		else:
			cursor.execute("SELECT wel_text FROM `welcome` WHERE guild_id = " + str(member.guild.id))
			result1 = cursor.fetchone()
			members = len(list(member.guild.members))
			mention = member.mention
			user = member.name
			guild = member.guild
			embed = discord.Embed(colour=0x95efcc, description=str(result1[0]).format(members=members, mention=mention, user=user, guild=guild))
			embed.set_thumbnail(url=f"{member.avatar_url}")
			embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
			embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
			embed.timestamp = datetime.datetime.utcnow()
			channel = self.client.get_channel(id=int(result[0]))
			await channel.send(embed=embed)
			mydb.commit()
			print("Test")
	
	
	@commands.Cog.listener()
	async def on_member_remove(self, member):
		cursor.execute("SELECT channel_id FROM farewell WHERE guild_id = " + str(member.guild.id))
		result = cursor.fetchone()
		if result is None:
			return
		else:
			cursor.execute("SELECT bye_text FROM farewell WHERE guild_id = " + str(member.guild.id))
			result1 = cursor.fetchone()
			members = len(list(member.guild.members))
			user = member.name
			guild = member.guild
			embed = discord.Embed(colour=0x95efcc, description=str(result1[0]).format(user=user, guild=guild, members=members))
			embed.set_thumbnail(url=f"{member.avatar_url}")
			embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
			embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
			channel = self.client.get_channel(id=int(result[0]))
			await channel.send(embed=embed)
			mydb.commit()
			print("Test")
	
	@commands.command()
	async def welcome(self, ctx, channel:discord.TextChannel):
		if ctx.message.author.guild_permissions.manage_messages:
			cursor.execute(f"SELECT channel_id FROM welcome WHERE guild_id = {ctx.guild.id}")
			result = cursor.fetchone()
			if result is None:
				sql = ("INSERT INTO  welcome(guild_id, channel_id) VALUES (%s, %s)")
				val = (ctx.guild.id, channel.id)
				await ctx.send(f"El canal de Bienvenidas fue configurado a {channel.mention}")
			elif result is not None:
				sql = ("UPDATE welcome SET channel_id = %s WHERE guild_id = %s")
				val = (channel.id, ctx.guild.id)
				await ctx.send(f"El canal de Bienvenidas fue actualizado a {channel.mention}")
			cursor.execute(sql, val)
			mydb.commit()
			print("Completado")
	

	@commands.command()
	async def farewell(self, ctx, channel:discord.TextChannel):
		if ctx.message.author.guild_permissions.manage_messages:
			cursor.execute(f"SELECT channel_id FROM farewell WHERE guild_id = {ctx.guild.id}")
			result = cursor.fetchone()
			if result is None:
				sql = ("INSERT INTO  farewell(guild_id, channel_id) VALUES (%s, %s)")
				val = (ctx.guild.id, channel.id)
				await ctx.send(f"El canal de Despedidas fue configurado a {channel.mention}")
			elif result is not None:
				sql = ("UPDATE farewell SET channel_id = %s WHERE guild_id = %s")
				val = (channel.id, ctx.guild.id)
				await ctx.send(f"El canal de Despedidas fue actualizado a {channel.mention}")
			cursor.execute(sql, val)
			mydb.commit()
			print("Completado")


	@commands.command()
	async def wel_text(self, ctx, *, text):
		if ctx.message.author.guild_permissions.manage_messages:
			cursor.execute(f"SELECT wel_text FROM welcome WHERE guild_id = {ctx.guild.id}")
			result = cursor.fetchone()
			if result is None:
				sql = ("INSERT INTO  welcome(guild_id, wel_text) VALUES (%s, %s)")
				val = (ctx.guild.id, text)
				await ctx.send(f"El mensaje fue cambiado a `{text}`")
			elif result is not None:
				sql = ("UPDATE welcome SET wel_text = %s WHERE guild_id = %s")
				val = (text, ctx.guild.id)
				await ctx.send(f"El mensaje fue actualiado a `{text}`")
			cursor.execute(sql, val)
			mydb.commit()
			print("Completado")
	
	
	
	@commands.command()
	async def bye_text(self, ctx, *, text):
		if ctx.message.author.guild_permissions.manage_messages:
			cursor.execute(f"SELECT bye_text FROM farewell WHERE guild_id = {ctx.guild.id}")
			result = cursor.fetchone()
			if result is None:
				sql = ("INSERT INTO  farewell(guild_id, bye_text) VALUES (%s, %s)")
				val = (ctx.guild.id, text)
				await ctx.send(f"El mensaje de despedida fue cambiado a `{text}`")
			elif result is not None:
				sql = ("UPDATE farewell SET bye_text = %s WHERE guild_id = %s")
				val = (text, ctx.guild.id)
				await ctx.send(f"El mensaje de despedida fue actualizado a `{text}`")
			cursor.execute(sql, val)
			mydb.commit()
			print("Completado")

#@commands.command()
#async def setprefix(ctx, *, text):
#	if ctx.message.author.guild_permissions.manage_messages:
#		cursor.execute(f"SELECT prefixes FROM prefix WHERE server_id = {ctx.guild.id}")
#		result = cursor.fetchone()
#		if result is not None:
#			sql = ("UPDATE prefix SET prefixes = %s WHERE server_id = %s")
#			val = (text, ctx.guild.id)
#			await ctx.send(f"El prefix fue actualiado a `{text}`")
#		cursor.execute(sql, val)
#		mydb.commit()
#		print("Completado")

def setup(client):
    client.add_cog(Wels(client))
    print("Bienvenidas cargadas")
    print(mydb)
    cursor.execute("show tables")
    for tabla in cursor:
        print(tabla) 
