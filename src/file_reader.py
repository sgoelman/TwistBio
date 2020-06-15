import re
import traceback

from src.DNA_to_amino_acid import DNA_TO_AMINO_ACID


class FileReader:
    def __init__(self):
        self.file_position = 0
        self.end_of_file = False

    def convert_by_chunks(self, input_dna_file='DNA_input.txt', block_size=999):
        with open(input_dna_file) as f:
            for block in self.__read_in_chunks(f, block_size):
                yield block

    def __read_in_chunks(self, file_object, block_size):
        """Generator removes /n
         returns blocks that divide by 3 and end with * """

        while not self.end_of_file:
            data = file_object.read(block_size)
            data_before_remove_n = data
            data, removed_backslash_data = self.__remove_backslash(data)
            if removed_backslash_data % 3 != 0:
                # made sure that the chunk is divided by 3  after removed n/:
                # and add remainder to data
                data = data + file_object.read(removed_backslash_data % 3)
            yield from self.check_end_of_file(block_size, data, removed_backslash_data)
            if self.end_of_file:
                break
            yield from self.__get_till_stop_codon(data, file_object)

    def check_end_of_file(self, block_size, data, removed_backslash_data):
        if len(data) < block_size - removed_backslash_data:
            self.end_of_file = True
            if len(data) % 3 != 0:
                # check if we need to remove the last char
                chars_to_remove = len(data) % 3
                data = data[:-chars_to_remove]
            yield data

    def __get_till_stop_codon(self, data, file_object):
        found_end_codon = False
        while not found_end_codon:
            single_DNA = file_object.read(3)
            try:
                if single_DNA.__contains__("\n"):
                    single_DNA = self.deal_with_bs_n(file_object, data, single_DNA)

                if DNA_TO_AMINO_ACID[single_DNA] != '*':
                    data += single_DNA
                else:
                    # found the end of the codon
                    if len(data) % 3 == 0:
                        yield data
                        break
                    else:
                        raise ValueError('Error in data not divided by 3 ')

            except NameError as ne:
                print(ne)
                print("Sequence:", single_DNA, " doesn't match a known DNA")
                continue
            except Exception as e:
                print('Exception: ' + str(e))
                print(traceback.print_tb(e.__traceback__))

    @staticmethod
    def __remove_backslash(data):
        count = 0
        (data, qty) = re.subn("\n", "", data)
        count += qty
        return data, count

    def deal_with_bs_n(self, file_object, data, single_DNA):
        char_to_add = file_object.read(1)
        new_DNA = single_DNA.replace("\n", "") + char_to_add
        data += new_DNA
        return new_DNA
