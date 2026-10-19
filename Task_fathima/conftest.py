
import pytest
import pytest_asyncio

from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright


# Async fixture
@pytest_asyncio.fixture
async def async_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        yield page

        await browser.close()


# Sync fixture for Amazon assignment
@pytest.fixture
def amazon_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.set_default_timeout(10000)
        page.set_default_navigation_timeout(20000)

        page.goto("https://www.amazon.in/")

        yield page

        browser.close()
