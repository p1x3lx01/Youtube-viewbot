import json
import random
import time
import asyncio
from pyppeteer import launch
from fake_useragent import UserAgent

class Viewbot:
    def __init__(self):
        self.config = json.load(open('./data/config.json', 'r+'))
        self.proxies = open('./data/proxies.txt').read().splitlines()
        self.ua = UserAgent()

    async def open_url(self, ua, sleep_time, proxy):
        browser = await launch(headless=True, executablePath="/usr/bin/chromium")
        page = await browser.newPage()
        await page.setUserAgent(ua.random)
        await page.goto(self.config["url"], {"waitUntil": "domcontentloaded"})
        await asyncio.sleep(sleep_time)  # انتظار عدد من الثواني محدد
        await browser.close()

    async def main(self):
        for _ in range(self.config["views"]):
            sleeptime = random.randint(self.config["min_watch"], self.config["max_watch"])
            proxy = random.choice(self.proxies)
            await self.open_url(self.ua, sleeptime, proxy)

if __name__ == "__main__":
    bot = Viewbot()
    asyncio.run(bot.main())
