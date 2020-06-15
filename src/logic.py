import math
from src.DNA_to_amino_acid import DNA_TO_AMINO_ACID, AMINO_ACID_TO_DNA


class Logic:

    def __init__(self):
        self.DNAtoAA = DNA_TO_AMINO_ACID
        self.AMINO_ACID_TO_DNA = AMINO_ACID_TO_DNA
        self.amino_acid_output = None
        self.back_translated_list = []
        self.min_seq_length = math.inf

    def write_output(self, total_combinations):
        """
        writes the shortest amino acid sequence with a minimum of 20 DNA letters and the  total different DNA
        sequences that can be back-translated from this sequence :rtype: void
        """
        if self.min_seq_length == math.inf:
            self.min_seq_length = 0
        convert_to_AA_output_text = 'The shortest amino acid sequence with a minimum of 20 DNA letters is', self.amino_acid_output, 'With the DNA length of', self.min_seq_length * 3
        convert_to_DNA_output_text = 'The total different DNA sequences that can be back-translated from the AA sequence is:', total_combinations

        with open('output.txt', 'a') as the_file:
            the_file.truncate(0)
            the_file.write(repr(convert_to_AA_output_text) + '\n')
            the_file.write(repr(convert_to_DNA_output_text) + '\n')
            the_file.close()

    def get_min_aa(self, input_data, is_input_in_file=True):
        """
    updates member self.amino_acid_output with the correct converted amino acids
        :rtype: void
        """
        data = self.__replace_backslash_n(input_data, is_input_in_file)
        data = self.__fix_input(data)
        # gets min amino acid min values final value is the min or equal to the min
        for x in self.get_aa_codon(data):
            self.amino_acid_output = x

    def get_aa_codon(self, data):
        """
        method will get all min amino acid codons - final codons is with min length
        :rtype: str
        """
        codon_start = False
        current_aa_sequence = ''
        # big for loop for all data , jumps by 3
        for i in range(0, len(data), 3):
            single_DNA = data[i:i + 3]
            try:
                codon_start, current_aa_sequence = yield from self.__convert_dna_to_legal_codon(codon_start,
                                                                                                current_aa_sequence,
                                                                                                single_DNA)
                if codon_start:
                    # add AA to codon
                    current_aa_sequence += self.DNAtoAA[single_DNA]
            except NameError as ne:
                print(ne)
                print("Sequence:", single_DNA, " doesn't match a known DNA")
                continue
            except Exception as e:
                print(e)

    def __fix_input(self, data):
        while len(data) % 3 != 0:
            print("Error input DNA does not divide by 3 , will remove final char and try again")
            data = data[:-1]
        return data

    def __convert_dna_to_legal_codon(self, codon_start, current_aa_sequence, single_DNA):
        if self.DNAtoAA[single_DNA] == 'M':
            # new codon
            codon_start = True
        elif self.DNAtoAA[single_DNA] == '*':
            # to make sure that we already are in a codon
            if codon_start:
                # end codon *
                current_aa_sequence += self.DNAtoAA[single_DNA]
                # shortest sequence with a minimum of 20 DNA (7 AA)
                if 7 <= len(current_aa_sequence) <= self.min_seq_length:
                    self.min_seq_length = len(current_aa_sequence)
                    yield current_aa_sequence
                codon_start = False
                current_aa_sequence = ''
        return codon_start, current_aa_sequence

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
