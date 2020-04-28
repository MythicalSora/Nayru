import aiohttp as ai
import aiofiles as af
import asyncio
import loaders.JsonLoader as jl
import pathlib
import json
import os
import re

class ChampionLoader:
    def __init__(self, champion: str, patch: str):
        champion = re.sub('\W+','', champion)
        self.cache = {'portraits': './cache/portraits/', 'folder': './cache/', 'icons': './cache/icons'}
        self.champion = {"name": champion.lower(), 'url': f'https://cdn.communitydragon.org/{patch}/champion/{champion.lower()}'}


    async def __parse_champion(self, champion):
        return self.champion['portrait']

    async def __get_champion(self):
        async with ai.ClientSession() as session:
            async with session.get(f'{self.champion["url"]}/data') as res:
                if os.path.exists(f'./cache/portraits/{self.champion["name"]}.jpg') == False:
                    if os.path.exists(self.cache['portraits']) == False:
                        pathlib.Path(self.cache['portraits']).mkdir(parents=True, exist_ok=True)
                    await self.__cache_portrait()
                self.champion['portrait'] = os.path.abspath(f'{self.cache["portraits"]}{self.champion["name"]}.jpg')
                return await self.__parse_champion(await res.json())


    async def __cache_portrait(self):
        """
        Caches Champion potrait for future use.
        """
        print('active')
        async with ai.ClientSession() as session:
            async with session.get(f'{self.champion["url"]}/portrait') as res:
                async with af.open(f'{self.cache["portraits"]}{self.champion["name"]}.jpg', 'wb') as f:
                    self.champion['portrait'] = os.path.abspath(f'{self.cache["portraits"]}{self.champion["name"]}.jpg')
                    print(self.champion)
                    await f.write(await res.read())
                    await f.close()


    async def get(self):
        """
        Retrieves the requested Champion from the League of Legends Community Dragon (or cdragon)
        """
        return await self.__get_champion()
        