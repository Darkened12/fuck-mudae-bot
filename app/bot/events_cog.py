import discord
from discord.ext import commands
from app.services.logging_service import logger


class EventsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name='$help | $search'))
        logger.info(f'"{self.__cog_name__}" is ready.')

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        logger.error(f'User tried command "{ctx.command}". Error was "{error}".')
        return await ctx.send(f'We are currently experiencing too much network usage and some commands are not working. '
                              f'Currently, only `$wa`, `$ha`, `$wg` and `$hg` are available.')
