import discord
from app.services.rickroll_service import RickRollService
from app.services.logging_service import logger


class RickRollView(discord.ui.View):
    def __init__(self, rickroll_service: RickRollService):
        super().__init__()
        self.rickroll_service = rickroll_service

    @discord.ui.button(label='Claim rewards and remove timeout!', style=discord.ButtonStyle.primary)
    async def on_button_press(self, button: discord.Button, interaction: discord.Interaction):
        await interaction.message.edit(content='https://media1.tenor.com/m/h2S2SXQWu30AAAAC/rick-roll.gif', view=None)
        await self.rickroll_service.new_rickroll(interaction.user)
        logger.info(f'User "{interaction.user.display_name}" has been rick rolled. Current count: '
                    f'{self.rickroll_service.rickrolls}')
