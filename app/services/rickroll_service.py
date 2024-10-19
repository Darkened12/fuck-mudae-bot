import discord
from typing import Union


class RickRollService:
    def __init__(self, target_channel: discord.TextChannel):
        self.rickrolls: int = 0
        self.channel_to_log_to = target_channel

    async def new_rickroll(self, user: Union[discord.User, discord.Member], log_to_channel: bool = True):
        self.rickrolls += 1
        if log_to_channel:
            embed = discord.Embed(
                title='Novo rickroll',
                colour=discord.Colour.dark_grey()
            )
            embed.add_field(name='Usuário: ', value=user.mention)
            if user.avatar:
                if user.avatar.url:
                    embed.set_thumbnail(url=user.avatar.url)
            embed.set_footer(text=f'rickrolls até agora: {self.rickrolls}')
            return await self.channel_to_log_to.send(embed=embed)
