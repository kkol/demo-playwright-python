from playwright.sync_api import Page, BrowserType, Browser, BrowserContext, sync_playwright
import yaml
import os


def read_config(config_option):
    config_file = open(os.getcwd()+'/config.yml')
    parsed_config = yaml.full_load(config_file)
    return parsed_config["config"][config_option]


class Setup:
    setup = sync_playwright()\
        .start()\
        .chromium\
        .launch(headless=read_config("browser_headless"), slow_mo=read_config("slow_mo"), args=['--start-maximized'])\
        .new_page()
