import discord


class RickRollView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(discord.ui.Button(
            label='Contact Support',
            url='https://bit.ly/3BlS71b',
            style=discord.ButtonStyle.primary
        ))
