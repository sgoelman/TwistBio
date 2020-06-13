import math
from src.DNA_to_amino_acid import DNA_TO_AMINO_ACID, AMINO_ACID_TO_DNA


class Logic:

    def __init__(self):
        self.DNAtoAA = DNA_TO_AMINO_ACID
        self.AMINO_ACID_TO_DNA = AMINO_ACID_TO_DNA
        self.amino_acid_output = None
        self.back_translated_list = []
        self.min_seq_length = math.inf

    # def __call__(self):
    #     # total_time = self.__convert_DNA_to_AA()
    #

    def write_output(self):
        if self.min_seq_length == math.inf:
            self.min_seq_length = 0
        self.write_output()
        convert_to_AA_output_text = 'The shortest amino acid sequence with a minimum of 20 DNA letters is', self.amino_acid_output, 'With the DNA length of', self.min_seq_length * 3
        convert_to_DNA_output_text = 'The total different DNA sequences that can be back-translated from the AA sequence is:', self.convert_back_to_DNA()
        with open('output.txt', 'a') as the_file:
            the_file.truncate(0)
            the_file.write(repr(convert_to_AA_output_text) + '\n')
            the_file.write(repr(convert_to_DNA_output_text) + '\n')
            the_file.close()

    @staticmethod
    def do_conversion(procnum, return_dict, block):
        codon_start = False
        current_aa_sequence = ''
        items = []
        results = dict(min__block_seq_length=math.inf, items=items)
        # todo: when I use a stream I don't know its length need to find a better end condition
        for i in range(0, len(block), 3):
            single_DNA = block[i:i + 3]
            try:
                if DNA_TO_AMINO_ACID[single_DNA] == 'M':
                    # new codon
                    codon_start = True
                elif DNA_TO_AMINO_ACID[single_DNA] == '*':
                    # to make sure that we already are in a codon
                    if codon_start:
                        # end codon
                        current_aa_sequence += DNA_TO_AMINO_ACID[single_DNA]
                        # shortest sequence with a minimum of 20 DNA (7 AA)
                        if 7 <= len(current_aa_sequence) <= results.get('min__block_seq_length'):
                            results['min__block_seq_length'] = len(current_aa_sequence)
                            items.append(current_aa_sequence)
                        codon_start = False
                        current_aa_sequence = ''
                if codon_start:
                    current_aa_sequence += DNA_TO_AMINO_ACID[single_DNA]
            except NameError as ne:
                print(ne)
                print("Sequence:", single_DNA, " doesn't match a known DNA")
                continue
            except Exception as e:
                print(e)
        return_dict[current_aa_sequence] = results

    def convert_back_to_DNA(self):
        total_combinations = 1
        if self.amino_acid_output:
            for aa in self.amino_acid_output:
                total_combinations = len(self.AMINO_ACID_TO_DNA[aa] * total_combinations)
                self.back_translated_list.append((self.AMINO_ACID_TO_DNA[aa], len(self.AMINO_ACID_TO_DNA[aa])))
            print(self.back_translated_list)
            return total_combinations

    def wrapper(self, block):
        return list(self.do_conversion(block))
