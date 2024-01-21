from behave import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given('I am on the Selenium Dev web form page')
def step_impl(context):
    context.driver.get("https://www.selenium.dev/selenium/web/web-form.html")


@when('I fill in the input field with "{input_text}"')
def step_impl(context, input_text):
    text_input_id = "my-text-id"
    text_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, text_input_id))
    )
    text_input.send_keys(input_text)


@then('Text input value should contains "{expected_value}"')
def step_impl(context, expected_value):
    text_input_id = "my-text-id"
    text_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, text_input_id))
    )
    assert expected_value in text_input.get_attribute("value")


@when('I fill in the password field with "{input_text}"')
def step_impl(context, input_text):
    password_input_name = "my-password"
    password_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, password_input_name))
    )
    password_input.send_keys(input_text)


@then('Password input value should contains "{expected_value}"')
def step_impl(context, expected_value):
    password_input_name = "my-password"
    password_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, password_input_name))
    )
    assert expected_value in password_input.get_attribute("value")


@when('I fill in the textarea field with "{input_text}"')
def step_impl(context, input_text):
    textarea_input_name = "my-textarea"
    textarea_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, textarea_input_name))
    )
    textarea_input.send_keys(input_text)


@then('Textarea input value should contains "{expected_value}"')
def step_impl(context, expected_value):
    textarea_input_name = "my-textarea"
    textarea_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, textarea_input_name))
    )
    assert expected_value in textarea_input.get_attribute("value")


@when('I select "{visible_text}" from the dropdown')
def step_impl(context, visible_text):
    dropdown_input_name = "my-select"
    dropdown_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, dropdown_input_name))
    )
    Select(dropdown_input).select_by_visible_text(visible_text)


@then('the dropdown value should be "{value}"')
def step_impl(context, value):
    dropdown_input_name = "my-select"
    dropdown_input = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, dropdown_input_name))
    )
    selected_option = Select(dropdown_input).first_selected_option
    assert selected_option.get_attribute('value') == value


@when("I click Submit button")
def step_impl(context):
    submit_button_css = "button"
    submit_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, submit_button_css))
    )
    submit_button.click()


@then('I get "{text}" message')
def step_impl(context, text):
    message_id = "message"

    message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, message_id))
    )
    assert message.text == text
