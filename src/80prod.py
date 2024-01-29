#INFO: los comandos que queremos en la version productiva
#XXX: generalizar/hacer extensible

from util.cfg import cfg_init, cfg_for
cfg_init()
TOKEN = cfg_for('DISCORD_TOKEN')

from typing import Optional

import discord
from discord import app_commands

from dolar import priceAsText
from util.db_cx_async import db_init, save_instance
from charlas_app.models import Recorte


#OjO! los canales NO EXISTEN hasta que tienen su primer mensaje (get_channel devuelve NONE)
REPORT_CH_URL= cfg_for('DISCORD_REPORT_CHANNEL_URL') #U: copie mirando canal de reporte #XXX:MULTISERVIDOR?
GUILD_ID= REPORT_CH_URL.split('/')[-2]
REPORT_CH_ID= int(REPORT_CH_URL.split('/')[-1])
print(f"GUILD {GUILD_ID} REPORT_CH={REPORT_CH_ID}")

MY_GUILD = discord.Object(id=GUILD_ID)  # replace with your guild id

class MyClient(discord.Client):
	def __init__(self, *, intents: discord.Intents):
		super().__init__(intents=intents)
		self.tree = app_commands.CommandTree(self)

	async def setup_hook(self):
		# This copies the global commands over to your guild.
		await db_init() #XXX:replace with alembic?
		self.tree.copy_global_to(guild=MY_GUILD)
		await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
	print(f'Logged in as {client.user} (ID: {client.user.id})')
	print('------')

@client.tree.command()
async def dolar(interaction: discord.Interaction):
	"""dolar price"""
	await interaction.response.send_message(priceAsText())

# This context menu command only works on messages
@client.tree.context_menu(name='Coleccionar', guild= MY_GUILD)
async def testimonio(interaction: discord.Interaction, message: discord.Message):
	"""XXX: DOC save data"""
	result= "ERROR: message was not saved" #DFLT
	try:
		d= {
			'txt': message.content, 
			'author_id': str(message.author.id), 
			'author_name': message.author.name, 
			'msg_dt': message.created_at, 
			'msg_id': str(message.id), 
			'saved_by_id': str(interaction.user.id),
			'saved_by_name': interaction.user.name,
		}
		print(f"RECORTE {d}") 
		recorte= Recorte.model_validate(d);
		await save_instance(recorte)
		result="Recorte guardado!" #XXX: link?
	except Exception as ex:
		print("ERROR recorte",d,ex)

	await interaction.response.send_message( result, ephemeral=True)

@client.tree.command()
async def xtest(interaction: discord.Interaction):
	"""just reply, test"""
	await interaction.response.send_message("test ok")

client.run(TOKEN)
