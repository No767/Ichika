from discord.commands import slash_command
from discord.ext import commands

class Helper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @slash_command(name="help", description="Displays a list of commands.")
    async def help(self, ctx):
        await ctx.respond("hello")
        
def setup(bot):
    bot.add_cog(Helper(bot))