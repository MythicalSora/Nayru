import aiohttp as ai
import aiofiles as af
import asyncio
import JsonLoader as jl
import pathlib
import os

class ChampionLoader:
    def __init__(self, champion: str, patch: str):
        self.champion = {"name": champion, url: f'https://cdn.communitydragon.org/{patch}/champion/{champion.lower()}'}


    def __parse_champion(self):
        return None

    async def __get_champion(self):
        async with ai.ClientSession() as session:
            async with session.get(f'{self.champion["url"]}/data') as res:
                if not os.path.exists(f'./cache/portaits/{self.champion["name"]}'):
                    await __cache_portrait()
                return await self.__parse_champion(jl.get_obj(await res.read()))


    async def __cache_portrait(self):
        """
        Caches ddragon to a local file to prevent high request rate.
        """
        async with ai.ClientSession() as session:
            async with session.get('https://ddragon.leagueoflegends.com/cdn/10.8.1/data/en_US/champion.json') as res:
                async with af.open(self.cache['characters'], 'wb') as f:
                    await f.write(await res.read())
                    await f.close()


    def get(self):
        """
        Retrieves the requested Champion from the League of Legends Data Dragon (or ddragon)
        """
        data = jl.get_obj(self.cache['characters'])
        print(data['data'][self.champion['name']])

cl = ChampionLoader('Akali', '10.8.1')
cl.get_champion()
        