import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

# Constants for element locators
BROWSERS = ["chrome", "firefox"]
URL = "https://www.selenium.dev/selenium/web/web-form.html"

@pytest.fixture(scope="session", params=BROWSERS)
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()


def test_text_input(driver):
    TEXT_INPUT_ID = "my-text-id"
    text_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, TEXT_INPUT_ID))
    )
    text_input.send_keys("cokolwiek")
    assert text_input.get_attribute("value") == "cokolwiek", "Text input value mismatch"


def test_password_input(driver):
    PASSWORD_INPUT_NAME = "my-password"
    password_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.NAME, PASSWORD_INPUT_NAME))
    )
    password_input.send_keys("???")
    assert password_input.get_attribute('value') == "???", "Password input value mismatch"


def test_textarea_input(driver):
    TEXTAREA_INPUT_NAME = "my-textarea"
    textarea_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.NAME, TEXTAREA_INPUT_NAME))
    )
    textarea_input.send_keys("działa?")
    assert textarea_input.get_attribute('value') == "działa?", "Textarea input value mismatch"


def test_dropdown_select(driver):
    DROPDOWN_INPUT_NAME = "my-select"
    dropdown_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.NAME, DROPDOWN_INPUT_NAME))
    )
    Select(dropdown_input).select_by_visible_text("Two")
    assert dropdown_input.get_attribute('value') == "2", "Dropdown selection mismatch"


def test_dropdown_datalist(driver):
    DATALIST_INPUT_NAME = "my-datalist"
    DATALIST_INPUT_TEXT = "los"
    DATALIST_ID = "my-options"
    datalist_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.NAME, DATALIST_INPUT_NAME))
    )
    datalist_input.send_keys(DATALIST_INPUT_TEXT)
    time.sleep(1)
    datalist_select = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, DATALIST_ID))
    )
    options = datalist_select.find_elements(By.TAG_NAME, "option")
    matching_options = [option for option in options if DATALIST_INPUT_TEXT in
                        option.get_attribute('value').lower()]
    expected_matching_count = 1
    assert len(
        matching_options) == expected_matching_count, \
        f"Expected {expected_matching_count} options, but found {len(matching_options)}"


def test_submit_button(driver):
    SUBMIT_BUTTON_CSS = "button"
    MESSAGE_ID = "message"
    submit_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, SUBMIT_BUTTON_CSS))
    )
    submit_button.click()

    # Verify submission message
    message = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, MESSAGE_ID))
    )
    assert message.text == "Received!", "Submission message mismatch"
