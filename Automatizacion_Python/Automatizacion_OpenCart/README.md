# 🧪 Automatización OpenCart con Pytest + Selenium

## 📋 Descripción del proyecto

Este proyecto automatiza el flujo completo de registro, inicio de sesión, selección de producto y checkout dentro del sitio de pruebas de **OpenCart** utilizando **Python**, **Pytest** y **Selenium WebDriver**.  

El objetivo es demostrar un flujo funcional end-to-end (E2E) y generar evidencias automáticas (screenshots y reportes HTML) para cada paso del proceso.

---

## ⚙️ Tecnologías utilizadas

| Componente | Descripción |
|-------------|-------------|
| **Python 3.12+** | Lenguaje principal |
| **Pytest** | Framework de pruebas |
| **Selenium WebDriver** | Automatización del navegador |
| **Pytest-HTML** | Generación de reportes HTML |
| **Google Chrome / ChromeDriver** | Navegador de ejecución |

---

## 🏗️ Estructura del proyecto

```
Automatizacion_OpenCart/
│
├── 📁 pages/                  # Clases Page Object (Home, Login, Register, Product, Cart)
│   ├── home_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── 📁 tests/                  # Archivos de pruebas Pytest
│   └── test_flow_opencart.py
│
├── 📁 utils/                  # Utilidades y configuración
│   ├── driver_factory.py
│   └── config.py
│   └── evidencias.py
│
├── 📁 evidencias/             # Capturas automáticas generadas por los tests
│
├── conftest.py                # Hook Pytest para adjuntar evidencias
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Este archivo
```

---

## 📦 Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/GhostNoc99/Automatizacion_OpenCart.git
   cd Automatizacion_OpenCart
   ```

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🧰 Configuración

El archivo `utils/config.py` contiene las variables principales del entorno:

```python
BASE_URL = "https://opencart.abstracta.us/"
TEST_USER = {
    "firstname": "Cesar",
    "lastname": "Vargas",
    "email": "usuario_prueba@example.com",
    "telephone": "3001234567",
    "password": "Password123!"
}
```

Asegúrate de modificar el correo para que sea único en cada ejecución (OpenCart no permite duplicados).

---

## ▶️ Ejecución del test

Para ejecutar **todos los tests**:

```bash
pytest --html=report.html --self-contained-html
```

---

## 📸 Evidencias y reportes

- Durante la ejecución, se generan **screenshots por cada paso** dentro de la carpeta:

  ```
  Automatizacion_OpenCart/evidencias/
  ```

- Si alguna prueba falla, se adjunta automáticamente la imagen en el **reporte HTML**.

- El reporte final (`report.html`) queda en la raíz del proyecto.  
  Puedes abrirlo con doble clic o desde navegador.

---

## 🧱 Ejemplo de salida esperada

En consola:

```
🟦 Iniciando flujo completo OpenCart...
🟢 Navegando al formulario de registro...
✅ Registro exitoso.
🟡 Navegando a login e iniciando sesión...
✅ Inicio de sesión exitoso.
🔵 Volviendo al Home antes de seleccionar producto...
🟣 Seleccionando primer producto y agregándolo al carrito...
✅ Producto agregado correctamente al carrito.
🟠 Abriendo carrito y procediendo al checkout...
✅ Checkout iniciado correctamente.
🎉 FLUJO COMPLETO EJECUTADO SIN ERRORES 🎉
```

En reporte HTML:

✅ 1 test passed  
📸 Screenshots adjuntos  
📄 Metadatos del entorno (Pytest + Selenium)

---

## 🧹 Limpieza

Para limpiar screenshots y reportes antiguos:

```bash
rm -rf evidencias/*
del report.html
```

---

## ✨ Autor

**Cesar Vargas**  
💻 QA Automation | Python | Selenium | Pytest  
📅 2025