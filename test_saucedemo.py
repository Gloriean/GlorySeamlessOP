import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.confirmation_page import ConfirmationPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_login_positive(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    assert inventory.is_logged_in()

def test_login_negative(driver):
    login = LoginPage(driver)
    login.login("standard_user", "esteem")
    assert "Username and password do not match" in login.get_error_message()

def test_full_checkout_flow(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    assert len(cart.get_cart_items()) == 1
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_checkout_info("John", "Doe", "12345")

    overview = CheckoutOverviewPage(driver)
    overview.click_finish()

    confirm = ConfirmationPage(driver)
    assert confirm.get_confirmation_text() == "Thank you for your order!"
    confirm.click_back_home()

    driver.find_element_by_id("react-burger-menu-btn").click()
    driver.find_element_by_id("logout_sidebar_link").click()
    assert "saucedemo.com" in driver.current_url
