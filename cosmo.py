import aiohttp
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import random
import asyncio
import logging
import json
import ssl 


scheduler = AsyncIOScheduler()
logging.basicConfig(level=logging.INFO)
logging.getLogger('apscheduler.executors.default').propagate = False
logger = logging.getLogger(__name__)
policy = asyncio.WindowsSelectorEventLoopPolicy()
asyncio.set_event_loop_policy(policy)
 
async def nerf():
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ru,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        'Connection': 'keep-alive',
        'Host': 'api.tonverse.app',
        "Origin": "https://app.tonverse.app",
        "Referer": "https://app.tonverse.app/",
        'Remote-Address': '188.166.16.205:443',
        "Referrer-Policy": "strict-origin-when-cross-origin",
        'X-Application-Version': '0.7.18',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    payload1 = {
        "session": 'rsTcRR0x9wKrPolW0yqRDQInirZ3eqxGrCCEtnTTI6btU0eRTXvC8XBylA_MHOEqHwAJ_gIF6x8OwAK3tcLPnI_DEdP6_5XKQQ69N8rkFNuWKsUDb_QJ5VHSa8JsHNk3wA3j0kL9nAAkdH0g7AALDg',
        "id": 'undefined'
    }
    payload2 = {
        "session": 'rsTcRR0x9wKrPolW0yqRDQInirZ3eqxGrCCEtnTTI6btU0eRTXvC8XBylA_MHOEqHwAJ_gIF6x8OwAK3tcLPnI_DEdP6_5XKQQ69N8rkFNuWKsUDb_QJ5VHSa8JsHNk3wA3j0kL9nAAkdH0g7AALDg'
    }
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.post(f'https://api.tonverse.app/user/info', headers=headers, data=payload1, ssl=ssl_context) as response1:
            text = await response1.text()
            text = json.loads(text)
            if int(text['response']['dust_progress']*100) >= random.randint(17,18):
                async with session.post(f'https://api.tonverse.app/galaxy/collect', headers=headers, data=payload2, ssl=ssl_context) as response2:
                    text = await response1.text()
                    text = json.loads(text)
                    logging.info(text)


async def schedule():
    scheduler.add_job(nerf, 'interval', seconds=5)
    scheduler.start()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(schedule())

