# Created by sgoel at 12/06/2020
Feature: DNA to AA Converter  tests


  Scenario Outline: Validate that I will receive correct errors with illegal DNA sequence
    Given I create a test file "test.txt" with the"<DNA>".
    When I convert DNA to amino acid translation from "test.txt" file
    Then I validate that receive the correct "<Output shortest sequence>" in "output.txt" file
    And I validate that receive the correct "<Output total different combinations>" in "output.txt" file

    Examples:
      | DNA                                                          | Output shortest sequence                            | Output total different combinations |
#None legal AA seq:
      | TGCTTATGAAAATTTTAATCTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGA | is', None, 'With the DNA length of', 0              | AA sequence is:', None              |
#Random chars:
      | XCVxszdgvfg2354987                                           | is', None, 'With the DNA length of', 0              | AA sequence is:', None              |
#MSAHARBEEBWRK*555:
      | ATGAGCGCGCACGCCCGAAATGAGGAGGATTGGCGAAAGTAG555                | is', 'MSAHARBEEBWRK*', 'With the DNA length of', 42 | AA sequence is:', 2654208           |
#MHISAHAR*****:
      | ATGCATATCAGCGCGCACGCCCGATGATGATGATGATGA                      | is', 'MHISAHAR*', 'With the DNA length of', 27      | AA sequence is:', 20736             |
#Many start codon in a seq,  !!!!!!MMMHISAHAR*M:
      | !!!!!!ATGATGATGCATATCAGCGCGCACGCCCGATGAATG                   | is', 'MMMHISAHAR*', 'With the DNA length of', 33    | AA sequence is:', 20736             |
#legal but with numbers instead of DNA letters , M1234567*:
      | ATG1234567TGA                                                | is', None, 'With the DNA length of', 0              | AA sequence is:', None              |
#shorter then 20, MH*:
      | ATGCATTGA                                                    | is', None, 'With the DNA length of', 0              | AA sequence is:', None              |
#check that the shortest seq is being returned, MHISAHAR* MSAHAR*
      | ATGCATATCAGCGCGCACGCCCGATGAATGAGCGCGCACGCCCGATGA             | is', 'MSAHAR*', 'With the DNA length of', 21        | AA sequence is:', 3456              |


