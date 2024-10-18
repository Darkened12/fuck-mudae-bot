import os
from app.bot import bot, events_cog, commands_cog, reaction_cog
from dotenv import load_dotenv

load_dotenv()

bot.add_cog(events_cog.EventsCog(bot))
bot.add_cog(commands_cog.CommandsCog(bot))
bot.add_cog(reaction_cog.ReactionCog(bot))
bot.run(os.environ.get('MUDAE_BOT'))

