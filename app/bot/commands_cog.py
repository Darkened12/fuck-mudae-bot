import discord
import random
from discord.ext import commands
from app.services.logging_service import logger
from app.models.waifu_anime_dataset import anime_waifus
from app.views.mudae_embed import get_mudae_embed


class CommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f'"{self.__cog_name__}" is ready.')

    @commands.command()
    async def wa(self, ctx: commands.Context):
        """Waifu Anime"""
        logger.info(f'User "{ctx.author.display_name}" used command "wa".')
        waifu = random.choice(anime_waifus)
        return await ctx.send(embed=get_mudae_embed(waifu))

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

