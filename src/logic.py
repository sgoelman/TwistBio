import re
import traceback

from src.DNA_to_amino_acid import DNA_TO_AMINO_ACID, AMINO_ACID_TO_DNA


class Logic:

    @staticmethod
    def do_conversion(procnum, return_dict, block):
        codon_start = False
        current_aa_sequence = ''
        max_int = 2147483647
        min_seq = max_int
        result_json = {procnum: {max_int: None}}

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
                        for key in result_json[procnum]:
                            if 7 <= len(current_aa_sequence) < min_seq:
                                min_seq = len(current_aa_sequence)
                                result_json[procnum] = {len(current_aa_sequence): current_aa_sequence}
                            codon_start = False
                            current_aa_sequence = ''
                if codon_start:
                    current_aa_sequence += DNA_TO_AMINO_ACID[single_DNA]
            except NameError as ne:
                print(ne)
                print("Sequence:", single_DNA, " doesn't match a known DNA")
                continue
            except Exception as e:
                print('PID ' + str(procnum) + ' Exception for  single_DNA : ' + str(e))
                print(traceback.print_tb(e.__traceback__))
        return_dict[procnum] = result_json

    @staticmethod
    def get_min_seq(return_dict):
        a = return_dict.values()
        max_int = 2147483647
        new = (max_int, None)
        for p in return_dict.values():
            for key, val in p.items():
                for key, val in val.items():
                    if key < max_int:
                        new = (key, val)
                        max_int = key
        min_seq = new[1]
        return min_seq

    @staticmethod
    def write_output(min_amino_acid, total_combinations):
        min_seq_length = 0
        if min_amino_acid != None:
            min_seq_length = len(min_amino_acid) * 3
        convert_to_AA_output_text = 'The shortest amino acid sequence with a minimum of 20 DNA letters is', min_amino_acid, 'With the DNA length of', min_seq_length
        convert_to_DNA_output_text = 'The total different DNA sequences that can be back-translated from the AA sequence is:', total_combinations
        with open('output.txt', 'a') as the_file:
            the_file.truncate(0)
            the_file.write(repr(convert_to_AA_output_text) + '\n')
            the_file.write(repr(convert_to_DNA_output_text) + '\n')
            the_file.close()

    @staticmethod
    def __remove_backslash(data):
        count = 0
        (data, qty) = re.subn("\n", "", data)
        count += qty
        print('remainder_remove:' + str(count))
        return data, count

    @staticmethod
    def get_total_combinations(min_dna_seq):
        if min_dna_seq != None:
            total_combinations = 1
            back_translated_list = []
            for aa in min_dna_seq:
                total_combinations = len(AMINO_ACID_TO_DNA[aa] * total_combinations)
                back_translated_list.append((AMINO_ACID_TO_DNA[aa], len(AMINO_ACID_TO_DNA[aa])))
            print(back_translated_list)
            return total_combinations
        return None

    def wrapper(self, procnum, return_dict, block):
        return list(self.do_conversion(procnum, return_dict, block))
