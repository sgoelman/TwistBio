import time
import math
from src.DNA_to_amino_acid import DNA_TO_AMINO_ACID, AMINO_ACID_TO_DNA


class Logic:

    def __init__(self, is_input_from_file=True, input_dna_seq="DNA_input.txt"):
        self.DNAtoAA = DNA_TO_AMINO_ACID
        self.AMINO_ACID_TO_DNA = AMINO_ACID_TO_DNA
        self.amino_acid_output = None
        self.back_translated_list = []
        self.min_seq_length = math.inf
        self.seq = self.__get_input_seq(is_input_from_file, input_dna_seq)

    # def __call__(self):
    #     total_time = self.__convert_DNA_to_AA()
    #     if self.min_seq_length == math.inf:
    #         self.min_seq_length = 0
    #     self.write_output(total_time)

    def write_output(self):
        convert_to_AA_output_text = 'The shortest amino acid sequence with a minimum of 20 DNA letters is', self.amino_acid_output, 'With the DNA length of', self.min_seq_length * 3
        convert_to_DNA_output_text = 'The total different DNA sequences that can be back-translated from the AA sequence is:', self.convert_back_to_DNA()

        with open('output.txt', 'a') as the_file:
            the_file.truncate(0)
            the_file.write(repr(convert_to_AA_output_text) + '\n')
            the_file.write(repr(convert_to_DNA_output_text) + '\n')
            the_file.close()

    # def __convert_DNA_to_AA(self):
    #     self.__check_input_divide_by_3()
    #     for x in self.do_conversion(self.seq):
    #         self.amino_acid_output = x
    #
    #     t1 = time.time()
    #     total = t1 - t0
    #
    #     return total

    def __check_input_divide_by_3(self):
        while len(self.seq) % 3 != 0:
            print("Error input DNA does not divide by 3 , will remove final char and try again")
            self.seq = self.seq[:-1]

    def do_conversion(self, sequence):
        codon_start = False
        current_aa_sequence = ''
        for i in range(0, len(sequence), 3):
            single_DNA = sequence[i:i + 3]
            try:
                if self.DNAtoAA[single_DNA] == 'M':
                    # new codon
                    codon_start = True
                elif self.DNAtoAA[single_DNA] == '*':
                    # to make sure that we already are in a codon
                    if codon_start:
                        # end codon
                        current_aa_sequence += self.DNAtoAA[single_DNA]
                        # shortest sequence with a minimum of 20 DNA (7 AA)
                        if 7 <= len(current_aa_sequence) <= self.min_seq_length:
                            self.min_seq_length = len(current_aa_sequence)
                            yield current_aa_sequence
                        codon_start = False
                        current_aa_sequence = ''
                if codon_start:
                    current_aa_sequence += self.DNAtoAA[single_DNA]
            except NameError as ne:
                print(ne)
                print("Sequence:", single_DNA, " doesn't match a known DNA")
                continue
            except Exception as e:
                print(e)

    def convert_back_to_DNA(self):
        print('All of the back-translated from the amino acids sequence to there DNA sequence:')
        return self.__do_convert_back_to_DNA()

    def __do_convert_back_to_DNA(self):
        total_combinations = 1
        if self.amino_acid_output:
            for aa in self.amino_acid_output:
                total_combinations = len(self.AMINO_ACID_TO_DNA[aa] * total_combinations)
                self.back_translated_list.append((self.AMINO_ACID_TO_DNA[aa], len(self.AMINO_ACID_TO_DNA[aa])))
            print(self.back_translated_list)
            return total_combinations

    def __get_input_seq(self, is_input_from_file, input_dna_seq):
        if is_input_from_file:
            f = open(input_dna_seq, "r")
            seq = f.read()
            seq = seq.replace("\n", "")
            seq = seq.replace("\r", "")
            return seq
        else:
            return input_dna_seq
