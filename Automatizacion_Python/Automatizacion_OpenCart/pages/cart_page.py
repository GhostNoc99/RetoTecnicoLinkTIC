from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        self.driver.find_element(By.ID, "cart-total").click()
        self.driver.find_element(By.XPATH, "//strong[text()=' View Cart']").click()

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))
        ).click()