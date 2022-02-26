Feature: Log into application

  Scenario: Log into application using accepted username
    Given user opens saucedemo application
    When user enters 'standard_user' username
    And user enters 'secret_sauce' password
    And user clicks login button
    Then user is logged in


  Scenario: Log into application using locked username
    Given user opens saucedemo application
    When user enters 'locked_out_user' username
    And user enters 'secret_sauce' password
    And user clicks login button
    Then user see error message 'Epic sadface: Sorry, this user has been locked out.'
    



