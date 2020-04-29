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
    if not champion:
        embed = discord.Embed(
            title='Not Found!',
            description='The Champion you queried either doesn\'t exist or hasn\'t been added to cdragon yet.',
            color=discord.Colour.red()
        )
        await ctx.send(embed=embed)
        return
    file = discord.File(champion['portrait'], filename="champion.jpg")
    roles = ''

    embed = discord.Embed(
        title=f'{champion["title"]} - {champion["name"]}',
        description=champion['desc'],
        color=discord.Colour.blurple(),
    )
    embed.set_thumbnail(url="attachment://champion.jpg")

    embed.add_field(name='Damage', value=champion['playstyle']['damage'], inline=True)
    embed.add_field(name='Durability', value=champion['playstyle']['durability'], inline=True)
    embed.add_field(name='Crowd Control', value=champion['playstyle']['crowdControl'], inline=True)
    embed.add_field(name='Mobility', value=champion['playstyle']['mobility'], inline=True)
    embed.add_field(name='Utility', value=champion['playstyle']['utility'], inline=True)

    for r in champion['roles']:
        roles += f'{r}, '
    
    embed.add_field(name='Roles', value=roles, inline=True)

    await ctx.send(embed=embed, file=file)

bot.run(config['discord_token'])
