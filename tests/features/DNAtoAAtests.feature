# Created by sgoel at 12/06/2020
Feature: DNA to AA Converter  tests


#  Scenario Outline: Validate that I will receive correct errors with illegal DNA sequence
#    Given I am logged in to application
#    When I convert DNA:"<DNA>" to amino acid
#    Then I validate that I receive the correct "<Output shortest sequence>"
#    And I validate that I receive the correct "<Output total different combinations>"
#    And I validate that I receive the correct "<Total amino acid sequences>"
#
#    Examples:
#      | DNA | Output shortest sequence | Output total different combinations | Total amino acid sequences |
##'XXXXXMPPPMPPPPP*' seq:MPPPPP*
#      | TGCTTATGCCACCACCAATGCCACCACCACCACCATAG                                                  | is', 'MPPPPP*', 'With the DNA length of', 21        | AA sequence is:', 3072              | 20 DNA letters are:', 2    |
##Random chars:
#      | XCVxszdgvfg2354987                                                                      | is', None, 'With the DNA length of', 0              | AA sequence is:', None              | 20 DNA letters are:', 0    |
##MSAHARBEEBWRK*555:
#      | ATGAGCGCGCACGCCCGAAATGAGGAGGATTGGCGAAAGTAG555                                           | is', 'MSAHARBEEBWRK*', 'With the DNA length of', 42 | AA sequence is:', 2654208           | 20 DNA letters are:', 1    |
##MHISAHAR*****:
#      | ATGCATATCAGCGCGCACGCCCGATGATGATGATGATGA                                                 | is', 'MHISAHAR*', 'With the DNA length of', 27      | AA sequence is:', 20736             | 20 DNA letters are:', 1    |
##Many start codon in a seq,  !!!!!!MMMHISAHAR*M:
#      | !!!!!!ATGATGATGCATATCAGCGCGCACGCCCGATGAATG                                              | is', 'MHISAHAR*', 'With the DNA length of', 27      | AA sequence is:', 20736             | 20 DNA letters are:', 3    |
##legal but with numbers instead of DNA letters , M1234567*:
#      | ATG1234567TGA                                                                           | is', None, 'With the DNA length of', 0              | AA sequence is:', None              | 20 DNA letters are:', 0    |
##shorter then 20, MH*:
#      | ATGCATTGA                                                                               | is', None, 'With the DNA length of', 0              | AA sequence is:', None              | 20 DNA letters are:', 0    |
##check that the shortest seq is being returned, MHISAHAR* MSAHAR*
#      | ATGCATATCAGCGCGCACGCCCGATGAATGAGCGCGCACGCCCGATGA                                        | is', 'MSAHAR*', 'With the DNA length of', 21        | AA sequence is:', 3456              | 20 DNA letters are:', 2    |
##seq:!*MPPPPP****MPPPPP*PP!!MMPPMPPP*!
#      | TAGATGCCACCACCACCACCATAGTAGTAGTAGATGCCACCACCACCACCATAGCCACCAATGATGCCACCACCAATGCCACCATAG | is', 'MPPPPP*', 'With the DNA length of', 21        | AA sequence is:', 3072              | 20 DNA letters are:', 4    |


  Scenario Outline: Validate that I will receive correct errors with illegal DNA sequence
    Given I am logged in to application
    When I convert DNA:"<DNA>" to amino acid
    And I validate that I receive the correct "<Total amino acid sequences>"
    Examples:
      | DNA                                                                                     | Total amino acid sequences |
      | TAGATGCCACCACCACCACCATAGTAGTAGTAGATGCCACCACCACCACCATAGCCACCAATGATGCCACCACCAATGCCACCATAG | 20 DNA letters are:', 9    |
#      | ATGCCACCACCACCACCATAGCCACCAATGATGCCACCACCAATGCCACCATAG                               | 20 DNA letters are:', 54   |
#      | ATGATGCCACCACCAATGCCACCATAG                                                          | 20 DNA letters are:', 27   |
#      | ATGCCACCACCAATGCCACCATAG                                                             | 20 DNA letters are:', 8   |

#  6 +2 +2
#"TAA": "*", "TAG": "*", "TGA": "*"}
#  "ATG": "M",
#  CCA=C



#  MPPPPPP** = MPPPPPP** +MPPPPPP*


#  ATGCCACCACCACCACCATAGTAG,3,24