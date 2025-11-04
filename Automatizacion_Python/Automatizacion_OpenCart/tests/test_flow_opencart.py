import pytest
from utils.driver_factory import get_driver
from utils.config import BASE_URL, TEST_USER
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.evidencias import take_screenshot  # 👈 importar helper

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_full_flow(setup):
    driver = setup
    home = HomePage(driver)
    register = RegisterPage(driver)
    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    print("🟦 Iniciando flujo completo OpenCart...")

    # Crear usuario
    print("🟢 Navegando al formulario de registro...")
    home.go_to_register()
    register.fill_registration_form(TEST_USER)
    assert register.verify_success()
    take_screenshot(driver, "01_registro_exitoso")

    # Iniciar sesión
    print("🟡 Navegando a login e iniciando sesión...")
    home.go_to_login()
    login.login(TEST_USER["email"], TEST_USER["password"])
    assert login.verify_login_success()
    take_screenshot(driver, "02_login_exitoso")

    # Volver al home
    print("🔵 Volviendo al Home antes de seleccionar producto...")
    driver.get("https://opencart.abstracta.us/index.php?route=common/home")
    take_screenshot(driver, "03_home")

    # Seleccionar producto
    print("🟣 Seleccionando primer producto y agregándolo al carrito...")
    product.select_first_product()
    product.add_to_cart()
    assert product.verify_added_to_cart()
    take_screenshot(driver, "04_producto_agregado")

    # Ir al carrito y proceder al checkout
    print("🟠 Abriendo carrito y procediendo al checkout...")
    cart.go_to_cart()
    cart.proceed_to_checkout()
    take_screenshot(driver, "05_checkout_iniciado")

    print("🎉 FLUJO COMPLETO EJECUTADO SIN ERRORES 🎉")
    take_screenshot(driver, "06_flujo_final_exitoso")