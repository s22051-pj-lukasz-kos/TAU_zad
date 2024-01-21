from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

@given('I am on the smakliter.pl site')
def step_impl(context):
    context.driver.get("https://smakliter.pl/")

@when('I click on accept cookie')
def step_impl(context):
    cookie_button = "a[href='javascript:WHCloseCookiesWindow();']"
    cookie_btn = (WebDriverWait(context.driver, 10)
                  .until(ec.element_to_be_clickable((By.CSS_SELECTOR, cookie_button))))
    cookie_btn.click()

@then('The cookie bar will disappear')
def step_impl(context):
    cookie_bar = "div#cookies-message"
    assert (WebDriverWait(context.driver, 10)
            .until(ec.invisibility_of_element_located((By.CSS_SELECTOR, cookie_bar))))


@when('I search for "Umówmy"')
def step_impl(context):
    searchbar = "#filter"
    search_button = "button.searchButton"

    search = WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, searchbar))
    )
    search.send_keys("umówmy")
    button = WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, search_button))
    )
    button.click()


@then('I should see "Umówmy się na Polskę"')
def step_impl(context):
    book_link = "a[href='/umowmy-sie-na-polske-anna-wojciuk-maciej-kisilowski,produkt-2016482']"
    time.sleep(3)
    assert (WebDriverWait(context.driver, 10)
            .until(ec.visibility_of_element_located((By.CSS_SELECTOR, book_link))))


@given('I find a book')
def step_impl(context):
    searchbar = "#filter"
    search_button = "button.searchButton"

    search = WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, searchbar))
    )
    search.send_keys("umówmy")
    button = WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, search_button))
    )
    button.click()

@when('I click on a book')
def step_impl(context):
    book_link = "a[href='/umowmy-sie-na-polske-anna-wojciuk-maciej-kisilowski,produkt-2016482']"
    book = WebDriverWait(context.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, book_link)))
    book.click()


@then('I should see book page')
def step_impl(context):
    book_url = "https://smakliter.pl/umowmy-sie-na-polske-anna-wojciuk-maciej-kisilowski,produkt-2016482"
    assert WebDriverWait(context.driver, 10).until(ec.url_matches(book_url)), "Wrong redirection"


@then('Add it to basket')
def step_impl(context):
    add_to_basket = "div#productContainer div.productAddToCartButton"
    button_add_to_basket = (WebDriverWait(context.driver, 10)
                            .until(ec.element_to_be_clickable((By.CSS_SELECTOR, add_to_basket))))
    button_add_to_basket.click()


@when('I click on basket')
def step_impl(context):
    basket = "a[href='/koszyk']"
    basket_button = WebDriverWait(context.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, basket)))
    basket_button.click()


@then('I will be redirected to basket')
def step_impl(context):
    basket_url = "https://smakliter.pl/koszyk"
    assert WebDriverWait(context.driver, 10).until(ec.url_matches(basket_url)), "Wrong redirection"


@then('I will see book in basket')
def step_impl(context):
    product_selector = "div#shoppingCartItemsContainer div.productName"
    product = WebDriverWait(context.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, product_selector)))
    assert product.text == "Umówmy się na Polskę"
