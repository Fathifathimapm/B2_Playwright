
import os
import re
import pytest
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
USERNAME = os.getenv("TEST_USERNAME", "standard_user")
PASSWORD = os.getenv("TEST_PASSWORD", "secret_sauce")


def login(page):
    page.goto(BASE_URL)
    page.locator("#user-name").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()
    expect(page).to_have_url(re.compile(r".*/inventory\.html$"))


# Task 1: Open website and verify the title
def test_open_website(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("Swag Labs")
    expect(page).to_have_url(BASE_URL)


# Task 2: Verify login page elements
def test_login_page_elements(page: Page):
    page.goto(BASE_URL)
    expect(page.locator("#user-name")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("#login-button")).to_be_visible()


# Task 3: Login and verify navigation
@pytest.mark.smoke
def test_login_and_navigation(page: Page):
    login(page)
    expect(page.locator(".title")).to_have_text("Products")
    expect(page.locator(".inventory_list")).to_be_visible()


# Task 4: Back, forward and reload
def test_browser_navigation(page: Page):
    page.goto(BASE_URL)
    login(page)

    page.go_back()
    expect(page.locator("#login-button")).to_be_visible()

    page.go_forward()
    expect(page.locator(".inventory_list")).to_be_visible()

    page.reload()
    expect(page.locator(".inventory_list")).to_be_visible()


# Task 5: Different locator strategies
def test_locator_strategies(page: Page):
    page.goto(BASE_URL)

    # CSS locator
    page.locator("#user-name").fill(USERNAME)
    expect(page.locator("#user-name")).to_have_value(USERNAME)

    # XPath locator
    page.locator('xpath=//*[@id="password"]').fill(PASSWORD)
    expect(page.locator("#password")).to_have_value(PASSWORD)

    # Role locator
    expect(page.get_by_role("button", name="Login")).to_be_visible()

    # Text locator
    expect(page.get_by_text("Swag Labs")).to_be_visible()


# Task 6: Fill, clear, replace and keyboard actions
def test_keyboard_actions(page: Page):
    page.goto(BASE_URL)

    username = page.locator("#user-name")
    username.fill("wrong_user")
    expect(username).to_have_value("wrong_user")

    username.press("Control+A")
    username.fill(USERNAME)
    username.press("Tab")

    expect(username).to_have_value(USERNAME)


# Task 7: Extract text and attributes
def test_extract_text_and_attributes(page: Page):
    page.goto(BASE_URL)

    heading = page.locator(".login_logo").inner_text()
    username_value = page.locator("#user-name").input_value()
    username_id = page.locator("#user-name").get_attribute("id")
    button_type = page.locator("#login-button").get_attribute("type")

    print("Heading:", heading)
    print("Username value:", username_value)
    print("Username ID:", username_id)
    print("Button type:", button_type)

    assert heading == "Swag Labs"
    assert username_value == ""
    assert username_id == "user-name"
    assert button_type == "submit"


# Task 8: Playwright and pytest assertions
def test_assertions(page: Page):
    page.goto(BASE_URL)

    expect(page).to_have_title("Swag Labs")
    expect(page.locator("#login-button")).to_be_visible()
    expect(page.locator("#login-button")).to_be_enabled()
    expect(page.locator("#user-name")).to_have_value("")

    assert "saucedemo.com" in page.url


# Task 9: Soft assertions
def test_soft_assertions(page: Page):
    page.goto(BASE_URL)
    failures = []

    checks = [
        ("Page title",
         lambda: expect(page).to_have_title("Swag Labs")),
        ("Username field",
         lambda: expect(page.locator("#user-name")).to_be_visible()),
        ("Password field",
         lambda: expect(page.locator("#password")).to_be_visible()),
        ("Login button",
         lambda: expect(page.locator("#login-button")).to_be_visible()),
    ]

    for name, check in checks:
        try:
            check()
        except AssertionError as error:
            failures.append(f"{name}: {error}")

    assert not failures, "Failed checks:\n" + "\n".join(failures)


# Task 10: Multiple locators
def test_multiple_locators(page: Page):
    login(page)

    products = page.locator(".inventory_item")
    count = products.count()

    print("Product count:", count)
    assert count == 6

    expect(products.first).to_be_visible()
    expect(products.last).to_be_visible()
    expect(products.nth(1)).to_be_visible()

    names = page.locator(".inventory_item_name")

    for index in range(names.count()):
        print(names.nth(index).inner_text())


# Task 11: Built-in waits and page load states
def test_builtin_waits(page: Page):
    page.goto(BASE_URL, wait_until="domcontentloaded")

    page.locator("#login-button").wait_for(state="visible")
    page.wait_for_load_state("load")

    expect(page.locator("#login-button")).to_be_enabled()


# Task 12: Dynamic waits
def test_dynamic_waits(page: Page):
    page.goto(BASE_URL)

    page.locator("#user-name").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()

    page.wait_for_url(re.compile(r".*/inventory\.html$"))
    page.locator(".inventory_list").wait_for(state="visible")

    expect(page.locator(".title")).to_have_text("Products")


# Task 13: Timeout handling
def test_timeout_handling(page: Page):
    page.goto(BASE_URL)
    page.set_default_timeout(1500)

    try:
        page.locator("#missing-element").wait_for(state="visible")
        pytest.fail("The missing element unexpectedly appeared.")
    except PlaywrightTimeoutError:
        print("Expected timeout handled successfully.")

    expect(page.locator("#login-button")).to_be_visible()


# Task 14: Custom wait condition
def test_custom_wait(page: Page):
    page.goto(BASE_URL)

    page.locator("#user-name").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()

    try:
        page.wait_for_url(
            re.compile(r".*/inventory\.html$"),
            timeout=5000
        )
        page.locator(".inventory_item").first.wait_for(
            state="visible",
            timeout=5000
        )
    except PlaywrightTimeoutError as error:
        pytest.fail(f"Login did not complete: {error}")

    expect(page.locator(".inventory_list")).to_be_visible()
    assert page.url.endswith("/inventory.html")


# Task 15: Browser matrix test
@pytest.mark.parametrize("browser_name", ["chromium", "firefox"])
def test_browser_matrix(browser_name, browser_type):
    browser = browser_type.launch()
    page = browser.new_page()

    try:
        page.goto(BASE_URL)
        expect(page).to_have_title("Swag Labs")
        expect(page.locator("#login-button")).to_be_visible()
    finally:
        browser.close()


# Task 16: Environment configuration check
def test_environment_url(page: Page):
    page.goto(BASE_URL)

    print("Selected BASE_URL:", BASE_URL)
    expect(page).to_have_title("Swag Labs")


# Task 17: Product sorting
@pytest.mark.regression
@pytest.mark.parametrize("sort_option", ["az", "za"])
def test_product_sorting(page: Page, sort_option):
    login(page)

    page.locator(".product_sort_container").select_option(sort_option)
    names = page.locator(".inventory_item_name").all_inner_texts()

    if sort_option == "az":
        assert names == sorted(names)
    else:
        assert names == sorted(names, reverse=True)


# Task 18: Integrated mini-project
@pytest.mark.smoke
def test_integrated_project(page: Page):
    page.goto(BASE_URL, wait_until="domcontentloaded")
    expect(page).to_have_title("Swag Labs")

    # CSS and XPath locators
    page.locator("#user-name").fill(USERNAME)
    page.locator('xpath=//*[@id="password"]').fill(PASSWORD)

    # Role locator
    page.get_by_role("button", name="Login").click()

    try:
        page.wait_for_url(
            re.compile(r".*/inventory\.html$"),
            timeout=5000
        )
        page.locator(".inventory_item").first.wait_for(
            state="visible",
            timeout=5000
        )
    except PlaywrightTimeoutError as error:
        pytest.fail(f"Login failed: {error}")

    expect(page.locator(".title")).to_have_text("Products")

    products = page.locator(".inventory_item")
    assert products.count() == 6

    print(
        "First product:",
        products.first.locator(".inventory_item_name").inner_text()
    )
    print(
        "Last product:",
        products.last.locator(".inventory_item_name").inner_text()
    )
    print(
        "Second product:",
        products.nth(1).locator(".inventory_item_name").inner_text()
    )
