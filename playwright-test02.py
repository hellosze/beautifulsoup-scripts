import asyncio
from bs4 import BeautifulSoup
from lxml import etree
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://hondaeastcincy.com/honda-models/")
        print(await page.title())
        # print(await page.content())
        html = await page.content()

        print(html)

        soup = BeautifulSoup(html, 'html.parser')
        print(soup.find_all('h3'))
        for child in soup.select('h3.margin-top-none'):
            print(child.contents)

        await browser.close()

asyncio.run(main())
