"""Fixture that sets browser driver for Selenium functional tests"""
import pytest
from selenium import webdriver

BROWSERS = ["chrome", "firefox"]


@pytest.fixture(name="driver", scope="session", params=BROWSERS)
def setup_driver(request, url):
    """Setup browser driver for specific URL"""
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
