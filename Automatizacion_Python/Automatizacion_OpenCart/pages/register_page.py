from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_registration_form(self, user):
        self.driver.find_element(By.ID, "input-firstname").send_keys(user["first_name"])
        self.driver.find_element(By.ID, "input-lastname").send_keys(user["last_name"])
        self.driver.find_element(By.ID, "input-email").send_keys(user["email"])
        self.driver.find_element(By.ID, "input-telephone").send_keys(user["telephone"])
        self.driver.find_element(By.ID, "input-password").send_keys(user["password"])
        self.driver.find_element(By.ID, "input-confirm").send_keys(user["password"])
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()

    def verify_success(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, "div#content p"),
                    "Congratulations! Your new account has been successfully created!"
                )
            )
            return True
        except TimeoutException:
            print("⏰ No se encontró el mensaje de confirmación del registro.")
            self.driver.save_screenshot("register_fail.png")
            return False