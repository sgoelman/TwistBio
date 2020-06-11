# Created by sgoel at 11/06/2020
Feature: DNA to AA Converter  tests




  Scenario Outline: Validate that I will receive correct errors with illegal DNA sequence
    Given I am logged in to application
    When I run DNA to amino acid translation on "<DNA>" I should receive the "<Output>"
    Then I validate that project "[Automation] Context Menu Permissions" context menu has "<Enabled Actions>" and "<Disabled Actions>"

    Examples:
      | DNA   | Output                                 | Disabled Actions      |
      | | Open, Rename, Share, Duplicate, Delete | Stop sharing          |
      | View  | Open, Stop sharing, Duplicate          | Rename, Share, Delete |
      | Edit  | Open, Stop sharing, Duplicate          | Rename, Share, Delete |

  Scenario:  non-DNA sequence
    Given a non-DNA sequence'asdazsdasd'
  When