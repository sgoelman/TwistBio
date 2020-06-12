# Created by sgoel at 12/06/2020
Feature: DNA to AA Converter  tests


  Scenario Outline: Validate that I will receive correct errors with illegal DNA sequence
    Given I am logged in to application
    When I convert DNA to amino acid translation on "<DNA>" I should
    Then I validate that receive the correct "<Output shortest sequence>"
    And I validate that receive the correct "<Output total different combinations>"

    Examples:
      | DNA                                                          | Output shortest sequence                  | Output total different combinations |
#None legal AA seq:
      | TGCTTATGAAAATTTTAATCTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGA | DNA letters is :', None                   | AA sequence is:', None              |
#Random chars:
      | XCVxszdgvfg2354987                                           | DNA letters is :', None                   | AA sequence is:', None              |
#MSAHARBEEBWRK*555:
      | ATGAGCGCGCACGCCCGAAATGAGGAGGATTGGCGAAAGTAG555                | DNA letters is :', ('MSAHARBEEBWRK*', 14) | AA sequence is:', 2654208           |
#MHISAHAR*****:
      | ATGCATATCAGCGCGCACGCCCGATGATGATGATGATGA                      | DNA letters is :', ('MHISAHAR*', 9)       | AA sequence is:', 20736)            |
#Many start codon in a seq,  !!!!!!MMMHISAHAR*M:
      | !!!!!!ATGATGATGCATATCAGCGCGCACGCCCGATGAATG                   | DNA letters is :', ('MMMHISAHAR*', 11)    | AA sequence is:', 20736)            |
#legal but with numbers instead of DNA letters , M1234567*:
      | ATG1234567TGA                                                | DNA letters is :', None                   | AA sequence is:', None              |
#shorter then 20, MH*:
      | ATGCATTGA                                                    | DNA letters is :', (None, inf)            | AA sequence is:', None           |

