Feature: Verify content of cart

  Scenario: Check if item is added to cart
    Given user log into saucedemo application
    When user adds item "Sauce Labs Bolt T-Shirt" to cart
    And user opens cart view
    Then item 'Sauce Labs Bolt T-Shirt' is added to cart


  Scenario: Check if item is removed from cart
    Given user log into saucedemo application
    When user adds item "Sauce Labs Fleece Jacket" to cart
    And user opens cart view
    And user removes 'Sauce Labs Fleece Jacket' from cart
    Then item 'Sauce Labs Fleece Jacket' is removed from cart

