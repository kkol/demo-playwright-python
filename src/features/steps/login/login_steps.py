from behave import *
from features.pages.setup import read_config

import features.pages.login as login_page
import features.pages.inventory as inventory_page

@given('user log into saucedemo application')
def log_into_application(context):
    login_page.open_browser(read_config("base_url"))
    login_page.enter_login(read_config("user"))
    login_page.enter_password(read_config("password"))
    login_page.log_in()
    assert inventory_page.inventory_list().count() > 0

@given('user opens saucedemo application')
def step_impl(context):
    login_page.open_browser(read_config("base_url"))


@when("user enters '{}' username")
def step_impl(context, username):
    login_page.enter_login(username)


@when("user enters '{}' password")
def step_impl(context, password):
    login_page.enter_password(password)


@when("user clicks login button")
def step_impl(context):
    login_page.log_in()


@then("user see error message '{}'")
def user_see_error(context, error):
    assert login_page.error_message().text_content() == error
