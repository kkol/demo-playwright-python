Feature: Verify cart operation in inventory page

  Scenario: Verify button status after adding item to cart
    Given user log into saucedemo application
    When user adds item "Sauce Labs Bike Light" to cart
    Then button label for 'Sauce Labs Bike Light' has value 'Remove'


  Scenario: Verify button status after removing item from cart
    Given user log into saucedemo application
    When user removes item "Sauce Labs Backpack" from cart
    Then button label for 'Sauce Labs Backpack' has value 'Remove'
