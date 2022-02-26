Feature: Verify content of inventory page

  Scenario: Check if inventory page contains all needed elements
    Given user log into saucedemo application
    Then menu icon is displayed
    And cart icon is displayed
    And filter dropdown is displayed
    And inventory list is displayed
    When user click on 'Sauce Labs Bike Light' element


