from .dicsordgram2 import Discordgram2

def setup(bot):
    cog = Discordgram2(bot)
    bot.add_cog(cog)
