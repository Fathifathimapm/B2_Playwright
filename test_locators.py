
import pytest
from playwright.async_api import expect


# @pytest.mark.asyncio
# async def test_getbyrole(async_page):#role is the link
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     reg_link = async_page.get_by_role("link",name= "Register")
#     await expect(reg_link).to_be_visible()
#     await reg_link.click()
#     await expect(async_page).to_have_title("Demo Web Shop. Register")
#
#
#     #get by role radio button
#     @pytest.mark.asyncio
#     async def test_getByText(async_page):
#         await async_page.goto("https://demowebshop.tricentis.com/")
#         excellent =async_page.get_by_text("Excellent")
#         await expect(excellent).not_to_be_checked()
#         await excellent.click()
#         await expect(excellent).to_be_checked()
#         async_page.wait_for_timeout(10000)
#         vb = async_page.get_by_role("radio", name="Very bad")
#         await expect(vb).to_be_visible()
#         await vb.click()

        #Get by label
import pytest
from playwright.async_api import expect


import pytest
from playwright.async_api import expect


# @pytest.mark.asyncio
# async def test_getBylabel(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#
#     reg_link = async_page.get_by_text("Register")
#     await expect(reg_link).to_be_visible()
#     await reg_link.click()
#
#     g = async_page.get_by_text("Female")
#     await expect(g).to_be_visible()
#     await g.click()
#import pytest
#     fn = async_page.get_by_label("First name:", exact=True)
#     await expect(fn).to_be_visible()
#     await fn.fill("ABC")
#
#     email = async_page.get_by_label("Email:", exact=True)
#     await expect(email).to_be_visible()
#     await email.fill("fathi@gmail.com")
#
#     pwd = async_page.get_by_label("Password:", exact=True)
#     await expect(pwd).to_be_visible()
#     await pwd.fill("Abc@123")
#
#     cpwd = async_page.get_by_label("Confirm password:", exact=True)
#     await expect(cpwd).to_be_visible()
#     await cpwd.fill("Abc@123")


# page.getByPlaceholder() to locate an input by placeholder.
# @pytest.mark.asyncio
# async def test_getByPlaceholder(async_page):
#     await async_page.goto("https://www.amazon.in/")
#
#     search_tb = async_page.get_by_placeholder("Search Amazon.in")
#
#     await expect(search_tb).to_be_visible()
#
#     await search_tb.fill("Books")
#
#     print(await search_tb.input_value())
#
#     await async_page.wait_for_timeout(50000)

               #page.getBytext() to locate an element
# @pytest.mark.asyncio
# async def test_getByalt_text(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    img = async_page.get_by_alt_text("Picture of 14.1-inch Laptop")
#    await expect(img).to_be_visible()
#    await img.click()
#    await expect(async_page).to_have_url("https://demowebshop.tricentis.com/141-inch-laptop")
#    await async_page.wait_for_timeout(50000)


                                            #####locators
import os
import pytest_asyncio
# import pytest
#
# from utils.config import BASE_URL, USERNAME, PASSWORD
# @pytest.mark.asyncio
# async def test_demo(async_page):
#     await async_page.goto(BASE_URL)

#page.getByTitle() to locate an element by its title attribute
import pytest
from playwright.async_api import expect


# @pytest.mark.asyncio
# async def test_getByTitle(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#
#     img = async_page.get_by_title("Show details for 14.1-inch Laptop").first
#
#     await expect(img).to_be_visible()
#
#     await img.click()
#     await async_page.wait_for_timeout(50000)

