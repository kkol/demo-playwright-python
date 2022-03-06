from features.pages.setup import Setup as driver

cart_locator = ".cart_list"
remove_from_cart_button_locator = ".item_pricebar button"
cart_item_label_locator = ".inventory_item_name"


def cart_list():
    return driver.setup.locator(cart_locator)


def cart_list_element(label):
    return cart_list().locator(f".cart_item:has-text('{label}')")


def cart_list_element_label(label):
    return cart_list_element(label).locator(cart_item_label_locator)


def cart_list_element_add_remove_button(label):
    return cart_list_element(label).locator(remove_from_cart_button_locator)


def cart_list_items_labels():
    return driver.setup.locator(cart_item_label_locator)
