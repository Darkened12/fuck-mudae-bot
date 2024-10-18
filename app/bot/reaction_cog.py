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
        if reaction.message.author == self.bot.user and reaction.message.embeds:
            if reaction.message.embeds[0].colour != discord.Colour.dark_red():
                try:
                    logger.info(f'Detected reaction "{reaction}" from user "{user.display_name}".')
                    await reaction.remove(user)
                    logger.info(f'Removed reaction "{reaction}" from user "{user.display_name}".')
                    await user.timeout_for(duration=timedelta(seconds=300), reason='Não use Mudae.')
                    return logger.info(f'User "{user.display_name}" has been muted.')
                except (commands.MissingPermissions, discord.errors.Forbidden) as err:
                    logger.error(f'Failed to fully execute script due to "{err}".')
                    embed: discord.Embed = reaction.message.embeds[0]
                    embed.colour = discord.Colour.dark_red()
                    await reaction.message.edit(embed=embed)
                    return await reaction.message.channel.send(f'💖 **{user.name}** and '
                                                               f'**{embed.title}** are now married! 💖')


