
import os
import re
import pytest
from playwright.sync_api import expect
AMAZON_URL = "https://www.amazon.in/"
SEARCH_KEYWORD = os.getenv("SEARCH_KEYWORD", "wireless mouse")


def search_product(page, keyword):
    search_box = page.locator("#twotabsearchtextbox")
    search_box.fill(keyword)
    search_box.press("Enter")

    page.wait_for_load_state("domcontentloaded")

    product_cards = page.locator(
        "[data-component-type='s-search-result']"
    )

    expect(product_cards.first).to_be_visible()


# Task 1 - End-to-End Product Discovery



# def test_task_1_product_discovery(amazon_page):
#     page = amazon_page
#
#     search_product(page, SEARCH_KEYWORD)
#
#     product_cards = page.locator(
#         "[data-component-type='s-search-result']"
#     )
#
#     matching_card = None
#     product_count = product_cards.count()
#
#     for i in range(product_count):
#         card = product_cards.nth(i)
#         title_locator = card.locator("h2")
#
#         if title_locator.count() == 0:
#             continue
#
#         title = title_locator.first.inner_text().strip()
#
#         if SEARCH_KEYWORD.lower() in title.lower():
#             product_link = card.locator("a:has(h2)").first
#
#             if product_link.count() > 0:
#                 matching_card = card
#                 break
#
#     assert matching_card is not None, (
#         f"No matching product with a clickable link found "
#         f"for: {SEARCH_KEYWORD}"
#     )
#
#     product_title = matching_card.locator(
#         "h2"
#     ).first.inner_text().strip()
#
#     product_link = matching_card.locator("a:has(h2)").first
#     product_url = product_link.get_attribute("href")
#
#     assert product_url, "Product URL was not found"
#
#     price = matching_card.locator(
#         ".a-price .a-offscreen"
#     ).first
#
#     if price.count() > 0:
#         product_price = price.inner_text()
#     else:
#         product_price = "Price not displayed"
#
#     print("Product Title:", product_title)
#     print("Product Price:", product_price)
#     print("Product URL:", product_url)
#
#     product_link.click()
#
#     expect(page.locator("#productTitle")).to_be_visible()
#
#     detail_title = page.locator(
#         "#productTitle"
#     ).inner_text().strip()
#
#     assert detail_title == product_title, (
#         f"Product title mismatch. Search: {product_title}, "
#         f"Details: {detail_title}"
#     )


#
# # Task 2 - Dynamic Product Selection
#
# def test_dynamic_product_selection(amazon_page):
#     page = amazon_page
#     search_product(page, SEARCH_KEYWORD)
#
#     cards = page.locator("[data-component-type='s-search-result']")
#     matching_cards = cards.filter(
#         has=page.get_by_role("heading", name=re.compile("mouse", re.I))
#     )
#
#     if matching_cards.count() == 0:
#         pytest.fail("No product card matching 'mouse' was found.")
#
#     card = matching_cards.first
#     expect(card.locator("h2")).to_be_visible()
#     print("Matched product:", card.locator("h2").inner_text())
#
#
# # Task 3 - Auto-Suggest Dropdown
#
# def test_auto_suggest(amazon_page):
#     page = amazon_page
#     search_box = page.locator("#twotabsearchtextbox")
#     search_box.fill("wireless mou")
#
#     suggestions = page.locator(".s-suggestion")
#
#     try:
#         suggestions.first.wait_for(state="visible", timeout=3000)
#         suggestion = suggestions.filter(
#             has_text=re.compile("wireless mouse", re.I)
#         ).first
#
#         if suggestion.count() > 0:
#             suggestion.click()
#         else:
#             search_box.press("Enter")
#     except PlaywrightTimeoutError:
#         print("Suggestions were not displayed; using the Search button.")
#         page.get_by_role("button", name=re.compile("Search", re.I)).click()
#
#     page.wait_for_load_state("domcontentloaded")
#     print("Current URL:", page.url)
#
#
# # Task 4 - Checkout Journey (Stop Before Purchase)
#

# Task 4 - Cart Journey


# Task 4 - Cart Journey


# Task 4 - Cart Journey


# TASK 4: Add to Cart Journey

# def test_cart_journey(amazon_page):
#     page = amazon_page
#
#     # Step 1: Search for a product
#     search_box = page.locator("#twotabsearchtextbox")
#     search_box.fill(SEARCH_KEYWORD)
#     search_box.press("Enter")
#
#     page.wait_for_load_state("domcontentloaded")
#
#     # Step 2: Find the first product with a valid product link
#     product_cards = page.locator(
#         "[data-component-type='s-search-result']"
#     )
#
#     product_url = None
#
#     for i in range(product_cards.count()):
#         card = product_cards.nth(i)
#         product_link = card.locator("a:has(h2)").first
#
#         if product_link.count() > 0:
#             href = product_link.get_attribute("href")
#
#             if href and "/dp/" in href:
#                 product_url = href
#                 break
#
#     # Step 3: Check whether a product was found
#     assert product_url is not None, "No product link found in search results"
#
#     # Step 4: Open the product details page
#     if product_url.startswith("http"):
#         page.goto(product_url)
#     else:
#         page.goto("https://www.amazon.in" + product_url)
#
#     page.wait_for_load_state("domcontentloaded")
#
#     # Step 5: Verify the product title
#     product_title_element = page.locator("span#productTitle")
#     expect(product_title_element).to_be_visible(timeout=15000)
#
#     product_title = product_title_element.inner_text().strip()
#     print("Product selected:", product_title)
#
#     # Step 6: Check whether Add to Cart is available
#     add_to_cart = page.locator("#add-to-cart-button")
#
#     if add_to_cart.count() == 0 or not add_to_cart.is_visible():
#         pytest.skip("Add to Cart button is unavailable for this product")
#
#     if not add_to_cart.is_enabled():
#         pytest.skip("Add to Cart button is disabled for this product")
#
#     # Step 7: Add the product to the cart
#     add_to_cart.click()
#
#     # Step 8: Open the cart
#     cart_link = page.locator("#nav-cart")
#
#     expect(cart_link).to_be_visible(timeout=15000)
#     cart_link.click()
#
#     page.wait_for_load_state("domcontentloaded")
#
#     # Step 9: Verify the cart page
#     expect(page).to_have_url(re.compile(r"/cart|/gp/cart"))
#
#     print("Cart URL:", page.url)
#



    # Do not place an order or submit payment.
#
#
# # # Task 5 - UI and API Validation
# #
# def test_ui_api_validation():
#     pytest.skip(
#         "Use a trainer-approved API or mock endpoint before implementing "
#         "the API/UI comparison."
#     )
# #
#
# # Task 6 - Managing State Across Pages
#

# TASK 6: Product State Across Pages

# def test_product_state_across_pages(amazon_page):
#     page = amazon_page
#
#     # Step 1: Search for a product
#     search_product(page, SEARCH_KEYWORD)
#
#     # Step 2: Get the first product card
#     product_cards = page.locator(
#         "[data-component-type='s-search-result']"
#     )
#
#     product_url = None
#     title_before = None
#
#     # Step 3: Find a product with a valid URL
#     for i in range(product_cards.count()):
#         card = product_cards.nth(i)
#
#         title_element = card.locator("h2").first
#         product_link = card.locator("a:has(h2)").first
#
#         if title_element.count() > 0 and product_link.count() > 0:
#             href = product_link.get_attribute("href")
#
#             if href and "/dp/" in href:
#                 title_before = title_element.inner_text().strip()
#                 product_url = href
#                 break
#
#     assert product_url is not None, "No valid product URL found"
#     assert title_before, "Product title is empty"
#
#     print("Search result title:", title_before)
#
#     # Step 4: Open the product details page
#     if product_url.startswith("http"):
#         page.goto(product_url)
#     else:
#         page.goto("https://www.amazon.in" + product_url)
#
#     page.wait_for_load_state("domcontentloaded")
#
#     # Step 5: Get the product title from the details page
#     detail_title_element = page.locator("span#productTitle")
#
#     expect(detail_title_element).to_be_visible(timeout=15000)
#
#     title_after = detail_title_element.inner_text().strip()
#     print("Product details title:", title_after)
#
#     # Step 6: Verify that the product title is retained
#     assert title_after, "Product details title is empty"
#
#     # Amazon may truncate titles in search results,
#     # so compare only the common starting text.
#     search_title_clean = " ".join(title_before.split())
#     detail_title_clean = " ".join(title_after.split())
#
#     common_title = search_title_clean[:30].lower()
#
#     assert common_title in detail_title_clean.lower(), (
#         "The product title on the details page does not match "
#         "the search result title"
#     )
#
#     print("Task 6 completed successfully")

#
#
# # Task 7 - Pagination and Infinite Scroll
#
# def test_pagination(amazon_page):
#     page = amazon_page
#     search_product(page, SEARCH_KEYWORD)
#
#     next_page = page.locator("a.s-pagination-next")
#
#     if next_page.count() > 0 and next_page.is_visible():
#         old_url = page.url
#         next_page.click()
#         page.wait_for_load_state("domcontentloaded")
#         assert page.url != old_url
#         print("Moved to next results page:", page.url)
#     else:
#         print("Next-page control is not available in this session.")
# #
#
# # Task 8 - Multi-Step Form and Data Persistence
#
# def test_form_data_persistence(amazon_page):
#     pytest.skip(
#         "Run this task only with a trainer-approved mock form or authorized "
#         "test account and safe test data."
#     )

#
# # Task 9 - Conditional Product Availability
#

# TASK 9: Conditional Product Availability

def test_product_availability(amazon_page):
    page = amazon_page


    search_product(page, SEARCH_KEYWORD)


    product_cards = page.locator(
        "[data-component-type='s-search-result']"
    )

    product_url = None

    for i in range(product_cards.count()):
        card = product_cards.nth(i)
        product_link = card.locator("a:has(h2)").first

        if product_link.count() > 0:
            href = product_link.get_attribute("href")

            if href and "/dp/" in href:
                product_url = href
                break

    assert product_url is not None, "No product URL found"


    if product_url.startswith("http"):
        page.goto(product_url)
    else:
        page.goto("https://www.amazon.in" + product_url)

    page.wait_for_load_state("domcontentloaded")


    product_title = page.locator("span#productTitle")
    expect(product_title).to_be_visible(timeout=15000)

    print("Product:", product_title.inner_text().strip())

    add_to_cart = page.locator("#add-to-cart-button")

    if add_to_cart.count() > 0 and add_to_cart.is_visible():
        if add_to_cart.is_enabled():
            print("Add to Cart button is visible and enabled.")
            print("Product appears available for adding to cart.")
        else:
            print("Add to Cart button is disabled.")
            print("Product may be unavailable.")
    else:
        print("Add to Cart button is not available.")
        print("Product availability could not be confirmed.")

    # Step 6: Check for availability-related messages
    availability_message = page.locator(
        "#availability"
    )

    if availability_message.count() > 0 and availability_message.is_visible():
        message = availability_message.inner_text().strip()
        print("Availability message:", message)
    else:
        print("No visible availability message found.")


