from typing import List

import discord
import random
from discord.ext import commands

from app.models.base_model import MudaeModel
from app.controllers.character_controller import CharacterController
from app.services.logging_service import logger
from app.views.mudae_embed import get_mudae_embed


class CommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.character_controller = CharacterController()

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f'"{self.__cog_name__}" is ready.')

    async def __send_random_mudae_model(self, ctx: commands.Context):
        logger.info(f'User "{ctx.author.display_name}" used command "{ctx.command}".')
        character = self.character_controller.get(ctx.command.name)
        return await ctx.send(embed=get_mudae_embed(character))

    @commands.command()
    async def wa(self, ctx: commands.Context):
        """Waifu Anime"""
        await self.__send_random_mudae_model(ctx)

    @commands.command()
    async def ha(self, ctx: commands.Context):
        """Husbando Anime"""
        await self.__send_random_mudae_model(ctx)

    @commands.command()
    async def wg(self, ctx: commands.Context):
        """Waifu Game"""
        await self.__send_random_mudae_model(ctx)

    @commands.command()
    async def hg(self, ctx: commands.Context):
        """Husbando Game"""
        await self.__send_random_mudae_model(ctx)
