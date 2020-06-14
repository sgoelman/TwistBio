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

    def convert_DNA_to_AA(self, input_data, is_input_in_file=True):
        """
    updates member self.amino_acid_output with the correct converted amino acids
        :rtype: void
        """
        data = self.__get_input_seq(input_data, is_input_in_file)
        self.__check_input_divide_by_3(data)
        # todo:check if yield returns 2 val or 1
        for x in self.do_conversion(data):
            self.amino_acid_output = x

    # todo:rename method to update add doc string
    def do_conversion(self, data):
        codon_start = False
        current_aa_sequence = ''
        # todo:create dna in one line
        for i in range(0, len(data), 3):
            single_DNA = data[i:i + 3]
            try:
                codon_start, current_aa_sequence = yield from self.__check_if_start_end_AA(codon_start,
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
#todo: remove wraper method
    def convert_back_to_DNA(self):
        """
        :return: int - total combinations of back-translated from the amino acids sequence to there DNA sequence
        """
        print('All of the back-translated from the amino acids sequence to there DNA sequence:')
        return self.__do_convert_back_to_DNA()

    # todo: rename method fix_input
    def __check_input_divide_by_3(self, data):
        while len(data) % 3 != 0:
            print("Error input DNA does not divide by 3 , will remove final char and try again")
            data = data[:-1]

    # todo: rename method create_legal_codon
    def __check_if_start_end_AA(self, codon_start, current_aa_sequence, single_DNA):
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

    def __do_convert_back_to_DNA(self):
        """
        :rtype: int - total combinations of back-translated from the amino acids sequence to there DNA sequence
        """
        total_combinations = 1
        if self.amino_acid_output:
            for aa in self.amino_acid_output:
                total_combinations = len(self.AMINO_ACID_TO_DNA[aa] * total_combinations)
                self.back_translated_list.append((self.AMINO_ACID_TO_DNA[aa], len(self.AMINO_ACID_TO_DNA[aa])))
            print(self.back_translated_list)
            return total_combinations

    def __get_input_seq(self, input_dna_seq, is_input_in_file=True):
        if is_input_in_file:
            with open(input_dna_seq, 'r') as file:
                data = file.read().replace('\n', '')
            return data
        else:
            return input_dna_seq
