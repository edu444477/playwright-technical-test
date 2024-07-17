from playwright.sync_api import expect

# Use pytest test_evaluation.py to run the test


def test_saucedemo_page(page):
    # 1 - Login with the standard user
    page.goto("https://www.saucedemo.com/")
    page.locator('//input[@id="user-name"]'). fill("standard_user")
    page.locator('//input[@id="password"]').fill("secret_sauce")
    page.locator('//input[@id="login-button"]').click()
    # Checking URL to ensure login redirects to the correct page.
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
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
    # 4 - Add the product “Sauce Labs Bike Light” and “Sauce Labs Fleece Jacket” to the cart
    page.locator('//button[@id="add-to-cart-sauce-labs-bike-light"]').click()
    page.locator('//button[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    # 5 - Delete the product “Sauce Labs Backpack” from the cart
    remove_backpack_button.click()
    # 6 - Verify that the button text changes from "Remove" to "Add to cart"
    expect(add_backpack_button).to_have_text("Add to cart")
    # Extra check to verify that the "Remove" button is not visible
    expect(remove_backpack_button).not_to_be_visible()
    # 7 - Click on the cart
    page.locator('//a[@data-test="shopping-cart-link"]').click()
    # 8 - Verify that the url is: https://www.saucedemo.com/cart.html
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    # 9 - Click on the "Checkout" button.
    page.locator('//button[@id="checkout"]').click()
    # 10 - Click on the "Continue" button
    page.locator('//input[@id="continue"]').click()
    # 11 - Verify that an error message appears with the text First name is required
    expect(page.locator('//h3[@data-test="error"]')).to_have_text("Error: First Name is required")
    # Extra check to verify that the error div is visible
    expect(page.locator('//div[@class="error-message-container error"]')).to_be_visible()
    # 12 - Fill out the entire form with your personal information
    page.locator('//input[@id="first-name"]').fill("Eduardo")
    page.locator('//input[@id="last-name"]').fill("Orellana")
    page.locator('//input[@id="postal-code"]').fill("29660")
    # 13 - Click on the "Continue" button
    page.locator('//input[@id="continue"]').click()
    # 14 - Verify that the "Total" is the sum of "Item total" + "Tax"
    item_total_text = page.locator('div[data-test="subtotal-label"]').text_content()
    tax_text = page.locator('div[data-test="tax-label"]').text_content()
    total_text = page.locator('div[data-test="total-label"]').text_content()
    item_total = float(item_total_text.split('$')[1])
    tax = float(tax_text.split('$')[1])
    total = float(total_text.split('$')[1])
    assert round(item_total + tax, 2) == total, f"Expected total to be {round(item_total + tax, 2)}, but got {total}"
    # 15 - Click on the "Finish" button
    page.locator('//button[@id="finish"]').click()
    # 16 - Verify that the message "Thank you for your order!" appears.
    expect(page.locator('//h2[@data-test="complete-header"]')).to_have_text("Thank you for your order!")
    # 17 - Click on the "Back Home" button
    page.locator('//button[@id="back-to-products"]').click()
    # 18 - Click on the dropdown menu
    page.locator('//button[@id="react-burger-menu-btn"]').click()
    # 19 - Click on "Logout"
    page.locator('//a[@id="logout_sidebar_link"]').click()
    # 20 - Verify that the "Username" and "Password" fields are visible
    expect(page.locator('//input[@id="user-name"]')).to_be_visible()
    expect(page.locator('//input[@id="password"]')).to_be_visible()
