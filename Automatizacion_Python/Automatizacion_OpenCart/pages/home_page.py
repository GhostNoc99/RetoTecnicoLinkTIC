from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.my_account_menu = (By.XPATH, "//span[text()='My Account']")
        self.register_option = (By.LINK_TEXT, "Register")
        self.login_option = (By.LINK_TEXT, "Login")
        self.logout_option = (By.LINK_TEXT, "Logout")

    def go_to_register(self):
        self.driver.find_element(*self.my_account_menu).click()
        self.driver.find_element(*self.register_option).click()

    def go_to_login(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            # Abre el menú "My Account"
            wait.until(EC.element_to_be_clickable(self.my_account_menu)).click()

            # Si está el botón de Logout, primero cerrar sesión
            if self._element_exists(self.logout_option):
                wait.until(EC.element_to_be_clickable(self.logout_option)).click()
                print("🔒 Sesión cerrada correctamente.")
                
                # Volver a abrir el menú My Account
                wait.until(EC.element_to_be_clickable(self.my_account_menu)).click()

            # Ahora sí, ir a Login
            wait.until(EC.element_to_be_clickable(self.login_option)).click()
            print("✅ Navegación a la página de login exitosa.")

        except TimeoutException:
                        print("❌ No se pudo abrir el enlace de login o logout. Verifica el texto o XPATH.")

    def _element_exists(self, locator):
        """Verifica si un elemento está presente sin lanzar excepción."""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False