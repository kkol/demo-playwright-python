from features.pages.setup import Setup as driver

menu_button_locator = "#react-burger-menu-btn"
cart_button_locator = "#shopping_cart_container"
filter_dropdown_locator = ".select_container .product_sort_container"
inventory_locator = ".inventory_list .inventory_item"


def inventory_list():
    return driver.setup.locator(inventory_locator)


def menu_button():
    return driver.setup.locator(menu_button_locator)


def filter_dropdown():
    return driver.setup.locator(filter_dropdown_locator)


def cart_button():
    return driver.setup.locator(cart_button_locator)


def inventory_list_element(label):
    return inventory_list().locator(f'text={label}')
