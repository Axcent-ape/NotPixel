import random
import re
from utils.not_pixels import NotPixel
from data import config
from utils.core import logger
from utils.core.telegram import Accounts
import datetime
import pandas as pd
import asyncio
import os
import time


async def start(thread: int, session_name: str, phone_number: str, proxy: [str, None]):
    pixel = NotPixel(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)
    account = session_name + '.session'

    if not await pixel.login():
        return

    errors = 0
    while True:
        try:
            status = await pixel.status()

            await pixel.tasks(status.get('tasks'))

            await pixel.mining_claim(status.get('fromStart'))

            await pixel.upgrades(status.get('userBalance'), status.get("boosts"))

            status = await pixel.status()
            await pixel.painting(status.get('charges'), status.get('userBalance'))

            status = await pixel.status()
            need_charge = status.get('maxCharges') - status.get('charges')
            sleep = status.get('reChargeTimer')/1000 + need_charge * status.get('reChargeSpeed')/1000 + random.uniform(*config.DELAYS['RECOVERY_CHARGE'])

            logger.info(f"Thread {thread} | {account} | Wait {sleep:.0f} to charge {need_charge} energy")
            await asyncio.sleep(sleep)

            if not await pixel.login():
                return

        except Exception as e:
            if errors == 5:
                errors = 0
                if not await pixel.login(): return
            else:
                errors += 1
                logger.error(f"Thread {thread} | {account} | Error: {e}")
            await asyncio.sleep(10)

    await pixel.logout()


async def stats():
    accounts = await Accounts().get_accounts()

    tasks = []
    for thread, account in enumerate(accounts):
        session_name, phone_number, proxy = account.values()
        tasks.append(asyncio.create_task(NotPixel(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy).stats()))

    data = await asyncio.gather(*tasks)

    path = f"statistics/statistics_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"
    columns = ['Phone number', 'Name', 'Is Beta Tester', 'Balance', 'League', 'Leaderboard', 'Squad name', 'Referrals', 'Referral link', 'Proxy (login:password@ip:port)']

    if not os.path.exists('statistics'): os.mkdir('statistics')
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(path, index=False, encoding='utf-8-sig')

    logger.success(f"Saved statistics to {path}")
