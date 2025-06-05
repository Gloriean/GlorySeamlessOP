# Access Checkout_overview_page
from selenium.webdriver.common.by import By

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def click_finish(self):
        self.driver.find_element(By.ID, "finish").click()
