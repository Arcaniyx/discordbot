import discord
from discord.ext import commands

TOKEN = "MTMyNTY4OTgzODQ5Nzk1NTkwMQ.Gqosl6.BbVHHiQ3Clypkzmu0f-jS2byC9sd7nK0E1g3aI"

bot = commands.Bot()

@bot.event
async def on_ready():
    print("ready!")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Salut {ctx.author.name} 👋!")

@bot.command()
async def add(ctx, a: int, b: int):
    result = a + b
    await ctx.send(f"La somme de {a} et {b} est {result}.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque des arguments pour cette commande.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Cette commande n'existe pas.")
    else:
        await ctx.send("Une erreur est survenue.")
        raise error  # Lève l'erreur pour la voir dans la console.

bot.run(TOKEN)
