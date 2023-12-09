"""
Test set checking functionality of web page
URL: https://smakliter.pl/
"""
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from driver_fixture import setup_driver  # pylint: disable=unused-import

URL = 'https://smakliter.pl/'


@pytest.fixture(scope="session")
def url():
    """Setup URL for setup_driver fixture"""
    return URL


def test_cookie_bar(driver):
    """Kliknięcie w przycisk "Rozumiem" w banerze informującym o cookies"""
    cookie_bar = "div#cookies-message"
    cookie_button = "a[href='javascript:WHCloseCookiesWindow();']"

    cookie_btn = (WebDriverWait(driver, 10)
                  .until(ec.element_to_be_clickable((By.CSS_SELECTOR, cookie_button))))
    cookie_btn.click()

    assert (WebDriverWait(driver, 10)
            .until(ec.invisibility_of_element_located((By.CSS_SELECTOR, cookie_bar))))


def test_search_bar(driver):
    """
    Wpisanie w wyszukiwarkę "umówmy" i kliknięcie przycisku szukania
    Strona powinna zwrócić książkę "Umówmy się na Polskę"
    """
    searchbar = "#filter"
    search_button = "button.searchButton"
    book_link = "a[href='/umowmy-sie-na-polske-anna-wojciuk-maciej-kisilowski,produkt-2016482']"

    search = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, searchbar))
    )
    search.send_keys("umówmy")
    button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, search_button))
    )
    button.click()
    time.sleep(3)
    assert (WebDriverWait(driver, 10)
            .until(ec.visibility_of_element_located((By.CSS_SELECTOR, book_link)))), \
        "Wrong redirection"


def test_add_to_basket(driver):
    """Dodanie książki do koszyka'"""
    add_to_basket = "div.productContainerDataAddToCartButton"
    confirmation = "div#addedToCartHeader"

    button_add_to_basket = (WebDriverWait(driver, 10)
                            .until(ec.element_to_be_clickable((By.CSS_SELECTOR, add_to_basket))))
    button_add_to_basket.click()

    confirmation_msg = (WebDriverWait(driver, 10)
                        .until(ec.visibility_of_element_located((By.CSS_SELECTOR, confirmation))))

    assert confirmation_msg.text == "Dodano produkt do koszyka", "Don't add element to basket"


def test_go_to_basket(driver):
    """
    Kliknięcie przycisku "Przejdź do koszyka".
    Upewnienie się, że jesteś na odpowiedniej podstronie (/koszyk).
    """
    basket_button = "div#addedToCartToShoppingCart"
    basket_url = "https://smakliter.pl/koszyk"

    basket = (WebDriverWait(driver, 10)
              .until(ec.element_to_be_clickable((By.CSS_SELECTOR, basket_button))))
    basket.click()

    assert WebDriverWait(driver, 10).until(ec.url_matches(basket_url)), "Wrong redirection"
