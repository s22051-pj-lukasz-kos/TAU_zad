Feature: Web form interaction on Selenium Dev Site
  As a user of the Selenium Dev site
  I want to interact with the web form
  So that I can test various form functionalities

  Scenario Outline: Test text input
    Given I am on the Selenium Dev web form page
    When I fill in the input field with "<input_text>"
    Then Text input value should contains "<input_text>"

  Examples:
    | input_text |
    | cos_tam    |
    | cosk faf   |
    | qerqer@adf |

  Scenario Outline: Test password input
    Given I am on the Selenium Dev web form page
    When I fill in the password field with "<input_text>"
    Then Password input value should contains "<input_text>"

  Examples:
    | input_text |
    | cos_tam    |
    | cosk faf   |
    | qerqer@adf |

  Scenario Outline: Test textarea input
    Given I am on the Selenium Dev web form page
    When I fill in the textarea field with "<input_text>"
    Then Textarea input value should contains "<input_text>"

  Examples:
    | input_text |
    | cos_tam    |
    | cosk faf   |
    | qerqer@adf |

  Scenario Outline: Selecting different options in a dropdown
    Given I am on the Selenium Dev web form page
    When I select "<visible_text>" from the dropdown
    Then the dropdown value should be "<value>"

  Examples:
    | visible_text | value |
    | One          | 1     |
    | Two          | 2     |
    | Three        | 3     |

  Scenario: Submitting a form
    Given I am on the Selenium Dev web form page
    When I click Submit button
    Then I get "Received!" message