
import os
import pytest
from playwright.sync_api import expect, TimeoutError as PlaywrightTimeoutError


# Task 1 - Open website and check title

def test_open_website(page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")


# Task 2 - Browser, context and page fixtures

@pytest.fixture
def my_context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def my_page(my_context):
    page = my_context.new_page()
    return page


def test_using_my_page(my_page):
    my_page.goto("https://www.saucedemo.com/")
    expect(my_page).to_have_title("Swag Labs")


def test_first_context(my_page):
    my_page.goto("https://www.saucedemo.com/")
    my_page.evaluate("localStorage.setItem('name', 'Fathima')")
    assert my_page.evaluate("localStorage.getItem('name')") == "Fathima"


def test_second_context(my_page):
    my_page.goto("https://www.saucedemo.com/")
    assert my_page.evaluate("localStorage.getItem('name')") is None


# Task 3 - Pytest configuration and markers

@pytest.mark.smoke
def test_smoke(page):
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("#login-button")).to_be_visible()


@pytest.mark.regression
def test_regression(page):
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("#user-name")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()


# Task 4 - Browser configuration and timeouts

def test_page_timeout(page):
    page.set_default_timeout(5000)
    page.set_default_navigation_timeout(15000)
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")


# Task 5 - Browser matrix

def test_browser_matrix(page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    expect(page.locator("#login-button")).to_be_enabled()


# Task 6 - Environment variables

def test_environment(page):
    environment = os.getenv("ENV", "DEV").upper()

    urls = {
        "DEV": "https://www.saucedemo.com/",
        "QA": "https://www.saucedemo.com/",
        "STAGING": "https://www.saucedemo.com/"
    }

    base_url = urls.get(environment)
    assert base_url is not None, "Invalid environment"

    print("Environment:", environment)
    print("URL:", base_url)

    page.goto(base_url)
    expect(page).to_have_url(base_url)
    expect(page).to_have_title("Swag Labs")


# Task 7 - Read credentials from environment variables

def test_login_using_environment_credentials(page):
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")

    if not username or not password:
        pytest.skip("Set TEST_USERNAME and TEST_PASSWORD first")

    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


# Task 8 - Navigation and login

def test_login_and_navigation(page):
    page.goto("https://www.saucedemo.com/")

    expect(page).to_have_title("Swag Labs")
    expect(page).to_have_url("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page.locator(".title")).to_have_text("Products")

    page.go_back()
    expect(page).to_have_url("https://www.saucedemo.com/")

    page.go_forward()
    expect(page.locator(".title")).to_have_text("Products")

    page.reload()
    expect(page.locator(".title")).to_have_text("Products")


# Task 9 - Locator strategies

def test_locator_strategies(page):
    page.goto("https://www.saucedemo.com/")

    # CSS selector
    page.locator("#user-name").fill("standard_user")
    expect(page.locator("#user-name")).to_have_value("standard_user")

    # XPath
    page.locator("//input[@id='password']").fill("secret_sauce")
    expect(page.locator("#password")).to_have_value("secret_sauce")

    # Visible text
    expect(page.get_by_text("Swag Labs")).to_be_visible()

    # Role locator
    page.get_by_role("button", name="Login").click()
    expect(page.locator(".title")).to_have_text("Products")


# Task 10 - Typing and keyboard actions

def test_typing_and_keyboard(page):
    page.goto("https://www.saucedemo.com/")

    username = page.locator("#user-name")
    username.fill("wrong_user")
    expect(username).to_have_value("wrong_user")

    username.fill("")
    username.fill("standard_user")
    expect(username).to_have_value("standard_user")

    username.press("Tab")
    expect(page.locator("#password")).to_be_focused()

    username.focus()
    username.press("Control+A")
    username.fill("standard_user")
    expect(username).to_have_value("standard_user")


# Task 11 - Extract text and attributes

def test_extract_details(page):
    page.goto("https://www.saucedemo.com/")

    heading = page.locator(".login_logo").inner_text()
    print("Heading:", heading)

    container_text = page.locator("#login_button_container").inner_text()
    print("Container text:", container_text)

    username = page.locator("#user-name")
    username.fill("standard_user")

    print("Input value:", username.input_value())
    print("Input type:", username.get_attribute("type"))
    print("Input class:", username.get_attribute("class"))

    assert heading == "Swag Labs"
    assert username.input_value() == "standard_user"


# Task 12 - Playwright and pytest assertions

def test_assertions(page):
    page.goto("https://www.saucedemo.com/")

    expect(page).to_have_title("Swag Labs")
    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator("#user-name")).to_be_visible()
    expect(page.locator(".login_logo")).to_have_text("Swag Labs")

    username = page.locator("#user-name")
    username.fill("standard_user")
    expect(username).to_have_value("standard_user")

    expect(page.locator("#login-button")).to_be_enabled()

    element_id = username.get_attribute("id")
    assert element_id == "user-name"


# Task 13 - Soft assertions

def test_soft_assertions(page):
    page.goto("https://www.saucedemo.com/")
    errors = []

    try:
        expect(page).to_have_title("Swag Labs", timeout=1000)
    except AssertionError:
        errors.append("Page title check failed")

    try:
        expect(page.locator("#user-name")).to_be_visible(timeout=1000)
    except AssertionError:
        errors.append("Username field is not visible")

    try:
        expect(page.locator("#login-button")).to_be_enabled(timeout=1000)
    except AssertionError:
        errors.append("Login button is not enabled")

    assert not errors, "\n".join(errors)


# Task 14 - Multiple locators

def test_multiple_locators(page):
    page.goto("https://www.saucedemo.com/")

    inputs = page.locator("input")
    count = inputs.count()

    print("Input count:", count)
    assert count == 3

    inputs.first.fill("standard_user")
    expect(inputs.first).to_have_value("standard_user")

    print("Last input type:", inputs.last.get_attribute("type"))

    inputs.nth(0).fill("standard_user")
    expect(inputs.nth(0)).to_have_value("standard_user")

    for i in range(count):
        print("Input", i, "type:", inputs.nth(i).get_attribute("type"))


# Task 15 - Built-in waits

def test_builtin_waits(page):
    page.goto(
        "https://www.saucedemo.com/",
        wait_until="domcontentloaded"
    )

    username = page.locator("#user-name")
    username.wait_for(state="visible")
    username.fill("standard_user")

    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    page.wait_for_url("**/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


# Task 16 - Dynamic content waits

def test_dynamic_content(page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page.locator(".title")).to_have_text("Products")

    products = page.locator(".inventory_item")
    expect(products.first).to_be_visible()

    assert products.count() > 0


# Task 17 - Timeout handling and custom wait

def test_timeout_handling(page):
    page.set_default_timeout(3000)
    page.set_default_navigation_timeout(10000)

    page.goto("https://www.saucedemo.com/")

    try:
        page.locator("#missing-element").wait_for(
            state="visible",
            timeout=2000
        )
    except PlaywrightTimeoutError:
        print("Expected timeout: element was not found")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    try:
        page.locator(".title").wait_for(
            state="visible",
            timeout=5000
        )
        expect(page.locator(".title")).to_have_text("Products")
    except PlaywrightTimeoutError:
        pytest.fail("Products page did not load in time")


# Task 18 - Integrated mini project

@pytest.mark.regression
def test_complete_login(page):
    page.set_default_timeout(5000)
    page.set_default_navigation_timeout(15000)

    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")

    page.locator("#user-name").fill("standard_user")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    page.wait_for_url("**/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

    products = page.locator(".inventory_item")
    products.first.wait_for(state="visible")

    count = products.count()
    assert count > 0

    print("Product count:", count)
    print("First product:", products.first.inner_text())
    print("Last product:", products.last.inner_text())

    if count > 1:
        print("Second product:", products.nth(1).inner_text())
