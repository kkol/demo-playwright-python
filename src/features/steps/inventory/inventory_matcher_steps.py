from behave import *
use_step_matcher("re")

import features.pages.inventory as inventory_page


@when(u'I try to match .*')
def step_when_I_try_to_match_foo(context):
    print("DONE")


@when(u'user .* item "(?P<anything>.*)" .*')
def user_adds_removes_item(context, anything):
    inventory_page.inventory_list_element_add_remove_button(anything).click()
