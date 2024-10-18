import discord
from discord.ext import commands
from app.services.logging_service import logger


class CommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def wa(self, ctx: commands.Context):
        logger.info(f'User "{ctx.author.display_name}" used command "wa".')
        return await ctx.send('hello')
