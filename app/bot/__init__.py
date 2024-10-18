import discord
from discord.ext import commands
from app.services.logging_service import logger

__intents = discord.Intents.default()
__intents.messages = True
__intents.message_content = True
__intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=__intents)
