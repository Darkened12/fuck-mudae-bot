from datetime import timedelta
from typing import Union

import discord
from discord.ext import commands
from app.services.logging_service import logger


class ReactionCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: Union[discord.User, discord.Member]):
        if reaction.message.author == self.bot.user:
            try:
                logger.info(f'Detected reaction "{reaction}"')
                await reaction.remove(user)
                logger.info(f'Removed reaction "{reaction}"')
                await user.timeout_for(duration=timedelta(seconds=300), reason='Não use Mudae.')
                return logger.info(f'User "{user.display_name}" has been muted.')
            except commands.MissingPermissions:
                return await reaction.message.delete()


