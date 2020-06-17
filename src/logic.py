import math
from src.DNA_to_amino_acid import DNA_TO_AMINO_ACID, AMINO_ACID_TO_DNA


class Logic:

    def __init__(self):
        self.all_aa_over_20 = []
        self.DNAtoAA = DNA_TO_AMINO_ACID
        self.AMINO_ACID_TO_DNA = AMINO_ACID_TO_DNA
        self.back_translated_list = []
        self.amino_acid_output = None

    def write_output(self, total_combinations):
        """
        writes the shortest amino acid sequence with a minimum of 20 DNA letters and the  total different DNA
        sequences that can be back-translated from this sequence :rtype: void
        """
        min_aa_length = 0
        aa_count = 0
        if self.amino_acid_output:
            min_aa_length = len(self.amino_acid_output) * 3
            aa_count = len(self.all_aa_over_20)
        convert_to_AA_output_text = 'The shortest amino acid sequence with a minimum of 20 DNA letters is', self.amino_acid_output, 'With the DNA length of', min_aa_length
        convert_to_DNA_output_text = 'The total different DNA sequences that can be back-translated from the AA sequence is:', total_combinations
        total_AA_over_20 = 'The total number of amino acid sequences that  are over 20 DNA letters are:', aa_count
        with open('output.txt', 'a') as the_file:
            the_file.truncate(0)
            the_file.write(repr(convert_to_AA_output_text) + '\n')
            the_file.write(repr(convert_to_DNA_output_text) + '\n')
            the_file.write(repr(total_AA_over_20) + '\n')
            the_file.close()

    def get_min_aa(self, input_data, is_input_in_file=True):
        """
    updates member self.amino_acid_output with the correct converted amino acids
        :rtype: void
        """
        data = self.__replace_backslash_n(input_data, is_input_in_file)
        self.get_aa_codons(data)
        print("all amino acid over 20:" + str(self.all_aa_over_20))
        print("Count all amino acid over twenty:" + str(len(self.all_aa_over_20)))
        if self.all_aa_over_20:
            self.amino_acid_output = min(self.all_aa_over_20, key=len)

        # gets min amino acid min values final value is the min or equal to the min

    def get_aa_codons(self, data):
        """
        method will get all min amino acid codons - final codons is with min length
        :rtype: str
        """
        # big whlie loop for all data ,
        i = 0
        while i < len(data):
            #  jumps by 1
            three_chars = data[i:i + 3]
            try:
                if self.DNAtoAA[three_chars] == 'M':
                    # inside a codon
                    k = self.__find_codons(data, i)
                    if k:
                        i = k
                    else:
                        # Reached end of file
                        break
                else:
                   i += 1
            except NameError as ne:
                i = i + 1
                print(ne)
                print("Sequence:", three_chars, " doesn't match a known DNA")
                continue
            except Exception as e:
                print(e)
                i = i + 1
                continue

    def __find_codons(self, data, i):
        """
        need to call method when inside a codon
        :param data: all input data
        :param i: global while iterator
        :return: void
        """
        current_aa_sequence = ''
        k = i
        for k in range(k, len(data), 3):
            #  jumps by 3
            single_DNA = data[k:k + 3]
            if len(single_DNA) == 3:
                current_aa_sequence += self.DNAtoAA[single_DNA]
                if self.DNAtoAA[single_DNA] == '*':
                    # end codon *
                    if 7 <= len(current_aa_sequence):
                        self.update_all_codons_in_aa_seq(current_aa_sequence)
                    return k
            else:
                print('End of file')

    def convert_back_to_DNA(self):
        """
        :rtype: int - total combinations of back-translated from the amino acids sequence to there DNA sequence
        also prints all possible aa values
        """
        print('All of the back-translated from the amino acids sequence to there DNA sequence:')
        total_combinations = 1
        if self.amino_acid_output:
            for aa in self.amino_acid_output:
                total_combinations = len(self.AMINO_ACID_TO_DNA[aa] * total_combinations)
                self.back_translated_list.append((self.AMINO_ACID_TO_DNA[aa], len(self.AMINO_ACID_TO_DNA[aa])))
            print(self.back_translated_list)
            return total_combinations

    def __replace_backslash_n(self, input_dna_seq, is_input_in_file=True):
        if is_input_in_file:
            with open(input_dna_seq, 'r') as file:
                data = file.read().replace('\n', '')
            return data
        else:
            return input_dna_seq

    def update_all_codons_in_aa_seq(self, current_aa_sequence):
        # reveres the string and then gets the position of all Ms
        m_position = [pos for pos, char in enumerate(current_aa_sequence[::-1]) if char == 'M']
        for j in m_position:
            if j >= 6:
                self.all_aa_over_20.append(current_aa_sequence[-j - 1:])



