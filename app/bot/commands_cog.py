import discord
from discord.ext import commands
from app.services.logging_service import logger


class CommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def wa(self, ctx: commands.Context):
        """Waifu Anime"""
        logger.info(f'User "{ctx.author.display_name}" used command "wa".')
        return await ctx.send('hello')

    @commands.command()
    async def ha(self, ctx: commands.Context):
        """Husbando Anime"""
        logger.info(f'User "{ctx.author.display_name}" used command "ha".')
        return await ctx.send('hello')

    @commands.command()
    async def wg(self, ctx: commands.Context):
        """Waifu Game"""
        logger.info(f'User "{ctx.author.display_name}" used command "wg".')
        return await ctx.send('hello')

    @commands.command()
    async def hg(self, ctx: commands.Context):
        """Husbando Game"""
        logger.info(f'User "{ctx.author.display_name}" used command "hg".')
        return await ctx.send('hello')

