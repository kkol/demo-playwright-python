from behave import fixture, use_fixture
from playwright.sync_api import Page, BrowserType, Browser, BrowserContext, sync_playwright
import yaml
from allure_behave.hooks import allure_report
from features.pages.setup import Setup as driver

# @fixture()
# def setup_chrome(context):
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         page = browser.new_page()
#         page.goto("https://www.saucedemo.com")
#         page.fill("#user-name", "standard_user")
#         page.fill("#password", "secret_sauce")
#         page.click("#login-button")
#         browser.contexts[0].storage_state(path="state.json")
#     yield p
#
#
# def before_all(context):
#     use_fixture(setup_chrome, context)


# def before_scenario(context, scenario):
#     return sync_playwright().start().chromium.launch(headless=read_config("browser_headless")).new_page()
#
#
# def read_config(config_option):
#     config_file = open('features/config.yml')
#     parsed_config = yaml.full_load(config_file)
#     return parsed_config["config"][config_option]

def after_all(context):
    driver.setup.close()




