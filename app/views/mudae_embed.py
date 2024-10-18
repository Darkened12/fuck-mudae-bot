import discord
from app.models.base_model import MudaeModel


def get_mudae_embed(model: MudaeModel) -> discord.Embed:
    embed = discord.Embed(
        title=model.name,
        description=f'{model.series}\nReact with any emote to claim!',
        colour=discord.Colour.orange()
    )
    embed.set_image(url=model.image_url)
    return embed
