from features.pages.setup import Setup as driver
import allure

username_input = "#user-name"
password_input = "#password"
login_button = "#login-button"
error_message_locator = "div.error h3"


def error_message():
    return driver.setup.locator(error_message_locator)


def open_browser(url):
    driver.setup.goto(url)


def enter_login(username):
    driver.setup.fill(username_input, username)


def enter_password(password):
    driver.setup.fill(password_input, password)


def log_in():
    driver.setup.click(login_button)
    screen = driver.setup.screenshot()
    allure.attach(screen)
