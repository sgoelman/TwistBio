import time
import math
from src.DNA_to_amino_acid import DNA_TO_AMINO_ACID, AMINO_ACID_TO_DNA


class Logic:

    def __init__(self, is_input_from_file=True, input_dna_seq="DNA_input.txt"):
        self.DNAtoAA = DNA_TO_AMINO_ACID
        self.AMINO_ACID_TO_DNA = AMINO_ACID_TO_DNA
        self.amino_acid_list = []
        self.back_translated_list = []
        self.min_seq = None
        self.seq = self.__get_input_seq(is_input_from_file, input_dna_seq)

    def __call__(self):
        self.__convert_DNA_to_AA()
        self.print_aa_list()
        min_seq = 'The shortest sequence with a minimum of 20 DNA letters is :', self.get_shortest_minimum_20()
        convert_to_DNA = 'The total different DNA sequences that can be back-translated from the AA sequence is:', self.convert_back_to_DNA()
        with open('output.txt', 'a') as the_file:
            the_file.truncate(0)
            the_file.write(repr(min_seq) + '\n')
            the_file.write(repr(convert_to_DNA))
            the_file.close()

    def __convert_DNA_to_AA(self):
        self.__check_input_divide_by_3()
        t0 = time.time()
        self.__do_conversion()
        t1 = time.time()
        total = t1 - t0
        print('total translation time:', total)
        return

    def __check_input_divide_by_3(self):
        while len(self.seq) % 3 != 0:
            print("Error input DNA does not divide by 3 , will remove final char and try again")
            self.seq = self.seq[:-1]

    def __do_conversion(self):
        codon_start = False
        current_aa_sequence = ''
        for i in range(0, len(self.seq), 3):
            codon = self.seq[i:i + 3]
            try:
                if self.DNAtoAA[codon] == 'M':
                    # new codon
                    codon_start = True
                elif self.DNAtoAA[codon] == '*':
                    if codon_start:
                        # end codon
                        current_aa_sequence += self.DNAtoAA[codon]
                        self.amino_acid_list.append((current_aa_sequence, len(current_aa_sequence)))
                        codon_start = False
                        current_aa_sequence = ''
                if codon_start:
                    current_aa_sequence += self.DNAtoAA[codon]
            except NameError as ne:
                print(ne)
                print("Sequence:", codon, " doesn't match a known DNA")
                continue
            except Exception as e:
                print(e)

    def get_shortest_minimum_20(self):
        min_seq, min_length = None, math.inf
        if self.amino_acid_list:
            for seq, length in self.amino_acid_list:
                if length >= 7 and length <= min_length:
                    min_seq = seq
                    min_length = length
            self.min_seq = min_seq
            return min_seq, min_length

    def print_aa_list(self):
        print('All of the converted DNA to amino acids:')
        if self.amino_acid_list:
            for seq in self.amino_acid_list:
                print(seq)
            print('//////////////////////////////////////////////////////////////')
        else:
            print('There are no legal amino acids')

    def convert_back_to_DNA(self):
        print('All of the back-translated from the amino acids sequence to there DNA sequence:')
        return self.__do_convert_back_to_DNA()

    def __do_convert_back_to_DNA(self):
        total_combinations = 1
        if self.min_seq:
            for aa in self.min_seq:
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
