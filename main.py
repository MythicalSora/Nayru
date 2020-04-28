import discord
import asyncio
import pathlib

from loaders.JsonLoader import get_obj
from loaders.ChampionLoader import ChampionLoader
from discord.ext import commands

config = get_obj('./config.json')
bot = commands.Bot(command_prefix=config['prefix'])

@bot.command()
async def test(ctx: commands.Context, champ: str):
    cl = ChampionLoader(champ, config['current_patch'])
    champion = await cl.get()
    file = discord.File(champion, filename="champion.jpg")

    embed = discord.Embed(
        title=champ,
        color=discord.Colour.blurple()
    )
    embed.set_image(url="attachment://champion.jpg")

    await ctx.send(embed=embed, file=file)

bot.run(config['discord_token'])
