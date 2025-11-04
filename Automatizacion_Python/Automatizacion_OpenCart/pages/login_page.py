from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def verify_login_success(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Logout"))
        )
        return True