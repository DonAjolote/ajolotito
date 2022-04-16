import discord
from discord.ext import commands
import sys
sys.path.append('..')
from set import check
from asyncio import sleep
from discord.utils import get

class Admin(commands.Cog):
	def __init__(self, client):
			self.client = client

	#Kickear usuarios 
	@check.can_kick()
	@commands.command()
	async def kick(self, ctx, user : discord.Member):
		if ctx.author == user:
			embed =  discord.Embed(title='Error', color=0x00ff00)
			embed.add_field(name="No puedes autoexpulsarte", value="\u200b")
			embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/777006797424427018/777218859190190080/giphy.gif")
			await ctx.send(embed=embed)
		else:
			await user.kick()
			embed = discord.Embed(title=f'El usuario {user.name} fue expulsado.', color=0x00ff00)
			embed.add_field(name="Adios!", value=":boot:")
			embed.set_thumbnail(url=user.avatar_url)
			await ctx.send(embed=embed)

	#Banear usuarios
	@check.can_ban()
	@commands.command()
	async def ban(self, ctx, user : discord.Member):
		if ctx.author == user:
			embed = discord.Embed(title='Error', color=0x00ff00)
			embed.add_field(name="No puedes autobanearte", value="\u200b")
			embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/777006797424427018/777218859190190080/giphy.gif")
			await ctx.send(embed=embed)
		else:
			await user.ban()
			embed = discord.Embed(title=f'El usuario {user.name} fue baneado.', color=0x00ff00)
			embed.add_field(name="Adios!", value=":hammer:")
			embed.set_thumbnail(url=user.avatar_url)
			await ctx.send(embed=embed)

	#Desbanear usuarios
	@commands.has_permissions(administrator=True)
	@commands.command()
	async def unban(self, ctx, *, member):
		banned_users = await ctx.guild.bans()
		for ban_entry in banned_users:
			user = ban_entry.user
			await ctx.guild.unban(user)
			embed = discord.Embed(title=f'El usuario ````{member}``` ha sido desbaneado.', color=0x00ff00)
			embed.add_field(name="Adios!", value=":hammer:")
			embed.set_thumbnail(url=user.avatar_url)
			await ctx.send(embed=embed)

	#Mutear usuarios


	@check.can_mute()
	@commands.command()
	async def mute(self, ctx, user : discord.Member, time: int):
		if ctx.author == user:
			embed = discord.Embed(title=f'Error', color=0x00ff00)
			embed.add_field(name="No puedes silenciarte a ti mismo", value="<:triste:777217502999478302>")
			embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/777006797424427018/777218859190190080/giphy.gif")
			await ctx.send(embed=embed)
			return
		else:
			rolem = discord.utils.get(ctx.message.guild.roles, name='Muted')
			if rolem is None:
				embed = discord.Embed(title=f'Error.', color=0x00ff00)
				embed.add_field(name="No existe ningún rol llamado `Muted`", value="[Como crear un rol 'Muted'](https://youtu.be/WWQMNgHujwI)", inline=False)
				embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/777006797424427018/777218859190190080/giphy.gif")
				await ctx.send(embed=embed)
				return
			elif rolem not in user.roles:
				embed = discord.Embed(title=f'El usuario {user.name} ha sido muteado por `{time}` minutos.', color=0x00ff00)
				embed.add_field(name="Shhh!", value=":zipper_mouth:")
				embed.set_thumbnail(url=user.avatar_url)
				await ctx.send(embed=embed)
				await user.add_roles(rolem)
				user = await ctx.message.guild.fetch_member(user.id)
				await sleep(time * 60)
				if rolem in user.roles:
					try:
						await user.remove_roles(rolem)
						embed = discord.Embed(title=f'El usuario {user.name} ha sido desmuteado.', color=0x00ff00)
						embed.add_field(name="Ya puedes hablar!", value=":open_mouth:")
						embed.set_thumbnail(url=user.avatar_url)
						await ctx.send(embed=embed)
					except Exception:
						print(f'El usuario {user.name} no ha sido desmuteado!')
			else:
				await ctx.send(f'El usuario {user.mention} ya está muteado.')

	@mute.error
	async def mute_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			embed = discord.Embed(title=f'Error', color=0x00ff00)
			embed.add_field(name="Necesito argumentos para poder silenciar usuario.", value="\u200b")
			embed.add_field(name="Ejemplo: **a.mute @Miembro 20 m**", value="\u200b", inline=False)
			embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/777006797424427018/777218859190190080/giphy.gif")
			await ctx.send(embed=embed)
	


	#Desmutear usuarios
	@check.can_mute()
	@commands.command()
	async def unmute(self, ctx, member: discord.Member = None):
		if not member:
			embed = discord.Embed(title=f'Error', color=0x00ff00)
			embed.add_field(name="No has especificado a ningún usuario", value="<:triste:777217502999478302>")
			embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/777006797424427018/777218859190190080/giphy.gif")
			await ctx.send(embed=embed)
			return	
		rolem = discord.utils.get(ctx.message.guild.roles, name='Muted')
		if rolem in member.roles:
			embed = discord.Embed(title=f'El usuaio {member.name} ha sido desmuteado.', color=0x00ff00)
			embed.add_field(name="Ya puedes hablar!", value=":open_mouth:")
			embed.set_thumbnail(url=member.avatar_url)
			await ctx.send(embed=embed)
			await member.remove_roles(rolem)


	#Borrar mensajes
	# Borrar mensajes del bot
	@check.can_managemsg()
	@commands.command()
	async def clear(self, ctx, amount=10):
		await ctx.channel.purge(limit=amount)
		await ctx.send(f'`{amount}` Mensajes fueron eliminados', delete_after=5)
		await self.client.delete_message(message)
		await self.ctx.message.delete()


	@commands.command()
	async def sugest(self, ctx, *, content: str = None):
		channel = self.client.get_channel(777630433465597982)
		embed = discord.Embed(
			name="Nueva sugerencia!",
		    description=f"    **Sugerencia**\n"
						f"    {content}\n\n"
						f"    **Autor**\n"
						f"    {ctx.author.mention}\n\n",
			color=discord.Color.red())
		message = await channel.send(embed=embed)
		embed.set_footer(text=f'message ID: {message.id}')
		await message.edit(embed=embed)
		await message.add_reaction('✅')
		await message.add_reaction('❎')








def setup(client):
    client.add_cog(Admin(client))
    print("Moderacion cargada")