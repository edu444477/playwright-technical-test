import time
from playwright.sync_api import expect


def test_standard_user_login(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('//input[@id="user-name"]'). fill("standard_user")
    page.locator('//input[@id="password"]').fill("secret_sauce")
    page.locator('//input[@id="login-button"]').click()
    # Checking URL to ensure login redirects to the correct page.
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    time.sleep(5)
