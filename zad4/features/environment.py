from selenium import webdriver

def before_all(context):
    # You can add logic to choose between browsers here
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit()
