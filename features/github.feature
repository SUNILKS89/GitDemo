# Created by sunil-k-s at 2/22/26
Feature: GitHub API validation
  # Enter feature description here

  Scenario: session management check
    Given I have GitHub auth credentials
    When I hit getRepo API of GitHub
    Then status code of response should be 200