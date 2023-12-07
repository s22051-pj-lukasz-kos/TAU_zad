"""
Test set checking functionality of web page
URL: https://www.selenium.dev/selenium/web/web-form.html
"""
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from driver_fixture import setup_driver  # pylint: disable=unused-import

URL = "https://www.selenium.dev/selenium/web/web-form.html"


@pytest.fixture(scope="session")
def url():
    """Setup URL for setup_driver fixture"""
    return URL


def test_text_input(driver):
    """Kliknięcie w pole Text Input i wypełnienie go tekstem. Oszacowanie czy tekst się zgadza"""
    text_input_id = "my-text-id"
    text_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.ID, text_input_id))
    )
    text_input.send_keys("cokolwiek")
    assert text_input.get_attribute("value") == "cokolwiek", "Text input value mismatch"


def test_password_input(driver):
    """Kliknięcie w pole Password i wypełnienie go tekstem. Oszacowanie czy tekst się zgadza"""
    password_input_name = "my-password"
    password_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.NAME, password_input_name))
    )
    password_input.send_keys("???")
    assert password_input.get_attribute('value') == "???", "Password input value mismatch"


def test_textarea_input(driver):
    """Kliknięcie w pole Textarea i wypełnienie go tekstem. Oszacowanie czy tekst się zgadza"""
    textarea_input_name = "my-textarea"
    textarea_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.NAME, textarea_input_name))
    )
    textarea_input.send_keys("działa?")
    assert textarea_input.get_attribute('value') == "działa?", "Textarea input value mismatch"


def test_dropdown_select(driver):
    """Kliknięcie w Dropdown (select) i wybranie opcji "Two". Oszacowanie czy wartość się zgadza."""
    dropdown_input_name = "my-select"
    dropdown_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.NAME, dropdown_input_name))
    )
    Select(dropdown_input).select_by_visible_text("Two")
    assert dropdown_input.get_attribute('value') == "2", "Dropdown selection mismatch"


def test_dropdown_datalist(driver):
    """
    Kliknięcie w pole Dropdown (datalist) i wpisanie "Los".
    Oszacowanie czy fropdown zawiera tylko jeden element.
    """
    datalist_input_name = "my-datalist"
    datalist_input_text = "los"
    datalist_id = "my-options"
    datalist_input = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.NAME, datalist_input_name))
    )
    datalist_input.send_keys(datalist_input_text)
    time.sleep(1)
    datalist_select = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, datalist_id))
    )
    options = datalist_select.find_elements(By.TAG_NAME, "option")
    matching_options = [option for option in options if datalist_input_text in
                        option.get_attribute('value').lower()]
    expected_matching_count = 1
    assert len(
        matching_options) == expected_matching_count, \
        f"Expected {expected_matching_count} options, but found {len(matching_options)}"


def test_submit_button(driver):
    """Kliknięcie w przycisk Submit i oszacowanie czy załadowała się kolejna strona"""
    submit_button_css = "button"
    message_id = "message"
    submit_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, submit_button_css))
    )
    submit_button.click()

    # Verify submission message
    message = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, message_id))
    )
    assert message.text == "Received!", "Submission message mismatch"
