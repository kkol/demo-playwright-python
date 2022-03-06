from behave import *

import features.pages.cart as cart_page


@when("user removes '{}' from cart")
def remove_item_from_cart(context, label):
    cart_page.cart_list_element_add_remove_button(label).click()


@then("item '{}' is added to cart")
def item_is_added_to_cart(context, label):
    cart_page.cart_list_element_label(label).is_visible()


@then("item '{}' is removed from cart")
def item_is_removed_to_cart(context, label):
    print(cart_page.cart_list_items_labels().count())
    if cart_page.cart_list_items_labels().count() > 0:
        assert label not in cart_page.cart_list_items_labels().text_content()

