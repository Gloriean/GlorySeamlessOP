# Access confirmation_page
from selenium.webdriver.common.by import By

class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_text(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text

    def click_back_home(self):
        self.driver.find_element(By.ID, "back-to-products").click()
