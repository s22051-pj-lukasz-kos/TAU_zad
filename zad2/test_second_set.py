import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

BROWSERS = ["chrome", "firefox"]
URL = 'https://smakliter.pl/'


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


def test_cookie_bar(driver):
    COOKIE_BAR = "div#cookies-message"
    COOKIE_BUTTON = "a[href='javascript:WHCloseCookiesWindow();']"

    cookie_btn = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, COOKIE_BUTTON)))
    cookie_btn.click()

    assert WebDriverWait(driver, 10).until(ec.invisibility_of_element_located((By.CSS_SELECTOR, COOKIE_BAR)))


def test_search_bar(driver):
    SEARCHBAR = "#filter"
    SEARCH_BUTTON = "button.searchButton"
    BOOK_LINK = "a[href='/umowmy-sie-na-polske-anna-wojciuk-maciej-kisilowski,produkt-2016482']"

    search = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, SEARCHBAR))
    )
    search.send_keys("umówmy")
    button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, SEARCH_BUTTON))
    )
    button.click()
    time.sleep(3)
    assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, BOOK_LINK))), "Wrong redirection"


def test_add_to_basket(driver):
    ADD_TO_BASKET = "div.productContainerDataAddToCartButton"
    CONFIRMATION = "div#addedToCartHeader"

    button_add_to_basket = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, ADD_TO_BASKET)))
    button_add_to_basket.click()

    confirmation_msg = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, CONFIRMATION)))

    assert confirmation_msg.text == "Dodano produkt do koszyka", "Don't add element to basket"


def test_go_to_basket(driver):
    BASKET_BUTTON = "div#addedToCartToShoppingCart"
    BASKET_URL = "https://smakliter.pl/koszyk"

    basket = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, BASKET_BUTTON)))
    basket.click()

    assert WebDriverWait(driver, 10).until(ec.url_matches(BASKET_URL)), "Wrong redirection"
