from playwright.async_api import async_playwright
import asyncio


async def test_diff_browser():
    async with async_playwright() as p:

        # ============================
        # chrome
        # ============================

        chrome_browser = await p.chromium.launch(headless=False)
        user_context = await chrome_browser.new_context()
        page = await user_context.new_page()
        await page.goto("http://google.com")

        admin_context = await chrome_browser.new_context()
        page = await admin_context.new_page()
        await page.goto("https://www.amazon.in/")


        # ============================
        # firefox
        # ============================

        firefox_browser = await p.firefox.launch(headless=False)
        user_context = await firefox_browser.new_context()
        page = await user_context.new_page()
        await page.goto("http://google.com")

        admin_context = await firefox_browser.new_context()
        page = await admin_context.new_page()
        await page.goto("https://www.amazon.in/")


        await asyncio.sleep(5)

        await chrome_browser.close()
        await firefox_browser.close()


asyncio.run(test_diff_browser())
import pytest


@pytest.mark.asyncio
async def test_chrome_browser(chromium_page):
    await chromium_page.goto("https://www.google.com/")


@pytest.mark.asyncio
async def test_firefox_browser(firefox_page):
    await firefox_page.goto("https://www.amazon.in/")