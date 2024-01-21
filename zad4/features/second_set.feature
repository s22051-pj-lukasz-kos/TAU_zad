Feature: Adding a book to a basket
  As a user of smakliter.pl
  I want to find and add a book to basket
  So that I could buy it later

  Scenario: Test cookie bar
    Given I am on the smakliter.pl site
    When I click on accept cookie
    Then The cookie bar will disappear

  Scenario: Search for "Umówmy się na Polskę"
    Given I am on the smakliter.pl site
    When I search for "Umówmy"
    Then I should see "Umówmy się na Polskę"

  Scenario: See book page and add to basket
    Given I am on the smakliter.pl site
    And I find a book
    When I click on a book
    Then I should see book page
    And Add it to basket

  Scenario: Check if book is in the basket
    Given I am on the smakliter.pl site
    When I click on basket
    Then I will be redirected to basket
    And I will see book in basket

