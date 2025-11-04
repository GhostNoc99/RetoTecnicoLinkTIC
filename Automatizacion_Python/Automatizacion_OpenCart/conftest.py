import sys
import os
import pytest
from pytest_html import extras


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Adjunta screenshots en el reporte HTML si el test falla."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup", None)
        if driver:
            # Crear carpeta evidencias
            screenshots_dir = os.path.join(os.getcwd(), "evidencias")
            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_path = os.path.join(screenshots_dir, f"failed_{report.nodeid.replace('::', '_')}.png")
            driver.save_screenshot(screenshot_path)
            if os.path.exists(screenshot_path):
                html = f'<div><img src="{screenshot_path}" alt="screenshot" style="width:400px;height:auto;" onclick="window.open(this.src)" /></div>'
                extra = getattr(report, "extra", [])
                extra.append(extras.html(html))
                report.extra = extra
