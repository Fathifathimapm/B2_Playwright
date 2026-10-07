import asyncio
from playwright.async_api import async_playwright

# from playwright.sync_api import sync_playwright, expect
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#
#     user_context = browser.new_context()
#     page = user_context.new_page()
#
#     page.goto("https://www.facebook.com/")
#     print(page.title())
#     expect(page).to_have_title("Facebook")
#
#     page.goto("https://www.amazon.in/")
#
#     page.go_back()
#     page.go_forward()
#
#     page.reload()

async def test_async():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.google.com/")

        print(await page.title())

        input("Press Enter to close...")

        await browser.close()


asyncio.run(test_async())

