import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_typing(async_page):

    await async_page.goto(
        "https://parabank.parasoft.com/parabank/index.htm"
    )

    register = async_page.get_by_text("Register")
    await register.click()

    # First Name - fill()
    fn = async_page.locator("//input[@id='customer.firstName']")
    await fn.fill("Mahi")

    await async_page.wait_for_timeout(5000)

    # Last Name - type()
    ln = async_page.locator("//input[@id='customer.lastName']")
    await ln.type("H")

    # Address - fill()
    add = async_page.locator("//input[@id='customer.address.street']")
    await add.fill("SriNagar")

    # City - type()
    city = async_page.locator("//input[@id='customer.address.city']")
    await city.type("Mysore")

    # State - type()
    state = async_page.locator("//input[@id='customer.address.state']")
    await state.type("Karnataka")

    # Zip Code - type()
    zipcode = async_page.locator(
        "//input[@id='customer.address.zipCode']"
    )
    await zipcode.type("12345")

    # Phone Number - type()
    ph_num = async_page.locator(
        "//input[@id='customer.phoneNumber']"
    )
    await ph_num.type("12345678999")

    # SSN - type()
    ssn = async_page.locator("//input[@id='customer.ssn']")
    await ssn.type("123456789")

    # Username - type()
    un = async_page.locator("//input[@id='customer.username']")
    await un.type("Mahi@123")

    # Password - fill()
    pwd = async_page.locator("//input[@id='customer.password']")
    await pwd.fill("123456789")

    # Confirm Password - fill()
    cpwd = async_page.locator("//input[@id='repeatedPassword']")
    await cpwd.fill("123456789")

    # Register button
    submit = async_page.locator("(//input[@type='submit'])[2]")
    await submit.click()

    await async_page.wait_for_timeout(5000)

    # Verify success message
    msg = async_page.get_by_text(
        "Your account was created successfully. You are now logged in."
    )

    await expect(msg).to_be_visible()

    print(await msg.inner_text())

    # Get page title heading
    title = async_page.locator("//h1[@class='title']")

    print(await title.inner_text())