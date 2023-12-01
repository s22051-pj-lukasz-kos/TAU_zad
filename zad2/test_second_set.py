import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

BROWSERS = ["chrome", "firefox"]
URL = 'https://www.empik.com/'


@pytest.fixture(scope="session", params=BROWSERS)
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    driver.get(URL)
    yield driver
    driver.quit()


def test_accept_cookies(driver):
    COOKIE_ACCEPT = "button.css-18n58r"

    cookie_accept = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, COOKIE_ACCEPT))
    )
    cookie_accept.click()
    assert WebDriverWait(driver, 10).until(ec.invisibility_of_element(cookie_accept)), "Cookie box don't disappear"


def test_search_bar(driver):
    EMPIK_SEARCHBAR = "div.empikHeader__container>input.css-1sobvo3"
    BOOK_LINK = "div.empikHeader__container>a[href='https://www.empik.com/umowmy-sie-na-polske-kisilowski-maciej,p1380134992,ksiazka-p?qa=um%C3%B3wmy&ac=true']"
    BOOK_PAGE = "https://www.empik.com/umowmy-sie-na-polske-kisilowski-maciej"
    search_bar = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, EMPIK_SEARCHBAR))
    )
    search_bar.send_keys("umówmy")
    book_link = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, BOOK_LINK))
    )
    book_link.click()
    assert WebDriverWait(driver, 10).until(ec.url_contains(BOOK_PAGE)), "Wrong redirection"
