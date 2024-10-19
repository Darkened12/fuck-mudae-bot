import discord
from typing import Union


class TimeoutLoggingService:
    def __init__(self, target_channel: discord.TextChannel):
        self.timeouts: int = 0
        self.channel_to_log_to = target_channel

    async def new_timeout(self, user: Union[discord.User, discord.Member], log_to_channel: bool = True):
        self.timeouts += 1
        if log_to_channel:
            embed = discord.Embed(
                title='Novo timeout',
                colour=discord.Colour.red()
            )
            embed.add_field(name='Otário(a): ', value=user.mention)
            if user.avatar:
                if user.avatar.url:
                    embed.set_thumbnail(url=user.avatar.url)
            embed.set_footer(text=f'timeouts até agora: {self.timeouts}')
            return await self.channel_to_log_to.send(embed=embed)
