import time
import math
from src.DNA_to_amino_acid import DNA_TO_AMINO_ACID


class Logic:

    def __init__(self, input_file="DNA_input.txt"):
        f = open(input_file, "r")
        self.seq = f.read()
        self.seq = self.seq.replace("\n", "")
        self.seq = self.seq.replace("\r", "")
        self.DNAtoAA = DNA_TO_AMINO_ACID
        self.amino_acid_list = []
        self.back_translated_list = []
        self.min_seq = None

    def convert_DNA_to_AA(self):
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
        for seq, length in self.amino_acid_list:
            if length >= 7 and length <= min_length:
                min_seq = seq
                min_length = length
        self.min_seq = min_seq
        return min_seq, min_length

    def print_aa_list(self):
        print('All of the converted DNA to amino acids:')
        for seq in self.amino_acid_list:
            print(seq)
        print('//////////////////////////////////////////////////////////////')

    def convert_back_to_DNA(self):
        print('All of the back-translated from the amino acids sequence to there DNA sequence:')
        self.__do_convert_back_to_DNA()
        print('//////////////////////////////////////////////////////////////')

    def __do_convert_back_to_DNA(self):
        for aa in self.min_seq:
            self.back_translated_list += self.DNAtoAA[aa]
        print(self.back_translated_list)

x = Logic()
x.convert_DNA_to_AA()
x.print_aa_list()
print('The shortest sequence with a minimum of 20 DNA letters is :', x.get_shortest_minimum_20())
x.convert_back_to_DNA()
