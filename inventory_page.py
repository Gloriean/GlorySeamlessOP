# Access Inventory page
from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name="Sauce Labs Backpack"):
        self.driver.find_element(By.XPATH, f"//div[text()='{item_name}']/../../..//button").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def is_logged_in(self):
        return "inventory" in self.driver.current_url

