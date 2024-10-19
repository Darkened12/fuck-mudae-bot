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
                    if not self.__is_admin(user):
                        await reaction.remove(user)
                        logger.info(f'Removed reaction "{reaction}" from user "{user.display_name}".')
                        return !waawait self.__execute_timeout(user)

                    raise PermissionError('User is an admin.')
                except (commands.MissingPermissions, discord.errors.Forbidden, PermissionError) as err:
                    logger.error(f'Failed to fully execute script due to "{err}".')
                    return await self.__execute_fake_marriage(reaction, user)

    @staticmethod
    async def __execute_timeout(user: Union[discord.User, discord.Member], duration=timedelta(seconds=300)):
        await user.timeout_for(duration=duration, reason='Não use Mudae.')
        await user.send('Seems like there has been an internal error. Please send a ticket to '
                        '[www.mudae.net/support](<https://tinyurl.com/57xa2jwk>) so we can sort this out! 💖')
        return logger.info(f'User "{user.display_name}" has been muted.')

    @staticmethod
    async def __execute_fake_marriage(reaction: discord.Reaction, user: Union[discord.User, discord.Member]):
        embed: discord.Embed = reaction.message.embeds[0]
        embed.colour = discord.Colour.dark_red()
        await reaction.message.edit(embed=embed)
        return await reaction.message.channel.send(f'💖 **{user.name}** and '
                                                   f'**{embed.title}** are now married! 💖')

    @staticmethod
    def __is_admin(user: Union[discord.User, discord.Member]) -> bool:
        return any(role.permissions.administrator for role in user.roles)
