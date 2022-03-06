from behave import *

import features.pages.inventory as inventory_page


@when("user click on '{}' element")
def use_clicks_element(context, inventory_element):
    inventory_page.inventory_list_element_label(inventory_element).click()


@when("user opens cart view")
def open_cart_view(context):
    inventory_page.cart_button().click()


@then("cart icon is displayed")
def cart_icon_is_displayed(context):
    inventory_page.cart_button().is_visible()


@then("menu icon is displayed")
def menu_icon_is_displayed(context):
    inventory_page.menu_button().is_visible()


@then("filter dropdown is displayed")
def filter_dropdown_is_displayed(context):
    inventory_page.filter_dropdown().is_visible()


@then("inventory list is displayed")
def inventory_list_is_displayed(context):
    assert inventory_page.inventory_list().count() > 0


@then("user is logged in")
def user_in_logged_in(context):
    inventory_page.inventory_list().is_visible()


@then("button label for '{}' has value '{}'")
def button_label(context, inventory_element, label_value):
    assert inventory_page.inventory_list_element_add_remove_button(inventory_element).text_content() == label_value
