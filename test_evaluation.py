# import time
from playwright.sync_api import expect

# Use pytest test_evaluation.py to run the test
# Uncomment sleeps and time import to debug


def test_saucedemo_page(page):
    # 1 - Login with the standard user
    page.goto("https://www.saucedemo.com/")
    page.locator('//input[@id="user-name"]'). fill("standard_user")
    page.locator('//input[@id="password"]').fill("secret_sauce")
    page.locator('//input[@id="login-button"]').click()
    # Checking URL to ensure login redirects to the correct page.
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    # time.sleep(2)
    # 2 - Add the Sauce Labs Backpack product to the cart
    add_backpack_button = page.locator('//button[@id="add-to-cart-sauce-labs-backpack"]')
    add_backpack_button.click()
    # 3 - Verify that the button changes the text from "Add to cart" to "Remove"
    remove_backpack_button = page.locator('//button[@id="remove-sauce-labs-backpack"]')
    expect(remove_backpack_button).to_have_text("Remove")
    # Extra check to verify that the "Add to cart" button is not visible
    expect(add_backpack_button).not_to_be_visible()
    # Extra check to verify correct cart behavior after adding the product
    expect(page.locator('//span[@class="shopping_cart_badge"]')).to_be_visible()
    # time.sleep(2)
    # 4 - Add the product “Sauce Labs Bike Light” and “Sauce Labs Fleece Jacket” to the cart
    page.locator('//button[@id="add-to-cart-sauce-labs-bike-light"]').click()
    page.locator('//button[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    # time.sleep(2)
    # 5 - Delete the product “Sauce Labs Backpack” from the cart
    remove_backpack_button.click()
    # 6 - Verify that the button text changes from "Remove" to "Add to cart"
    expect(add_backpack_button).to_have_text("Add to cart")
    # Extra check to verify that the "Remove" button is not visible
    expect(remove_backpack_button).not_to_be_visible()
    # time.sleep(2)
    # 7 - Click on the cart
    page.locator('//a[@data-test="shopping-cart-link"]').click()
    # Extra check to verify that the page is as expected
    page.title = "Your Cart"
    # time.sleep(5)
