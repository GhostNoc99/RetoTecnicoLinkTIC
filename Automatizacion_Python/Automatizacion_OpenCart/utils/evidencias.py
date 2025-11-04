# utils/evidencias.py
import os
from datetime import datetime

def take_screenshot(driver, step_name):
    """Guarda un screenshot con nombre basado en el paso y la hora."""
    folder = os.path.join(os.getcwd(), "evidencias")
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = step_name.replace(" ", "_").replace(":", "_")
    file_path = os.path.join(folder, f"{timestamp}_{safe_name}.png")

    driver.save_screenshot(file_path)
    print(f"📸 Screenshot guardado: {file_path}")
    return file_path
