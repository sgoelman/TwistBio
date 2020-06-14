import re
import traceback

from src.DNA_to_amino_acid import DNA_TO_AMINO_ACID


class FileReader:
    def __init__(self):
        self.file_position = 0
        self.end_of_file = False

    def convert_by_chunks(self, input_dna_file='DNA_input.txt', block_size=5001):
        with open(input_dna_file) as f:
            for block in self.__read_in_chunks(f, block_size):
                yield block

    def __read_in_chunks(self, file_object, block_size):
        """Generator removes /n and /r
         returns blocks that divide by 3 and end with * """
        line_size = 210

        while not self.end_of_file:
            print('Posission:' + str(self.file_position))
            file_object.seek(self.file_position)
            self.file_position = file_object.tell()
            data = file_object.read(block_size)
            if data == '':
                print('Reached EOF')
            data, removed_backslash_data = self.__remove_backslash(data)
            remainder_backslash_data = removed_backslash_data % 3
            # made sure that the chunk is divided by 3  after removed n/:
            # todo: make sure that removed  remainder does't have /n
            data = data + file_object.read(remainder_backslash_data)
            print('data size after read chunk ' + str(len(data)))
            self.file_position = file_object.tell()
            print('Posission after block size:' + str(self.file_position))
            line = file_object.read(line_size)
            self.file_position = file_object.tell()
            print('Posission after read line' + str(self.file_position))
            line, remainder_backslash_line = self.__remove_backslash(line)
            yield from self.check_end_of_file(file_object, line, remainder_backslash_line, block_size, data,
                                              removed_backslash_data, line_size)
            yield from self.__get_till_stop_codon(data, line, remainder_backslash_line, file_object)

    def check_end_of_file(self, file_object, line, remainder_backslash_line, block_size, data, removed_backslash_data,
                          line_size):
        if len(line) + remainder_backslash_line < line_size or len(data) < block_size - removed_backslash_data:
            # end of file:
            if len(line) + remainder_backslash_line < line_size:
                line = file_object.read(len(line))
            else:
                line = 0
            self.file_position = file_object.tell()
            self.end_of_file = True
            print('last Line ' + str(len(line)))
            data = data + line
            if len(data) % 3 != 0:
                # check if we need to remove the last char
                chars_to_remove = len(data) % 3
                data = data[:-chars_to_remove]
            yield data

    def __get_till_stop_codon(self, data, line, remainder_backslash_line, file_object):
        counter = 0
        has_m = False
        for c in range(len(line) + remainder_backslash_line):
            single_DNA = line[c:c + 3]
            counter += 3
            # chunk_position = chunk_size + counter + remainder_backslash_line
            data = data + single_DNA
            try:
                # if len(single_DNA) == 3 and DNA_TO_AMINO_ACID[single_DNA] == '*':
                if DNA_TO_AMINO_ACID[single_DNA] == 'M':
                    has_m = True
                if DNA_TO_AMINO_ACID[single_DNA] == '*' and has_m == True:
                    # found the end of the codon
                    self.file_position = file_object.tell()
                    file_object.seek(self.file_position)
                    print('Counter:' + str(counter))
                    yield data
                    break
                else:
                    # no * or not divided by 3
                    if len(single_DNA) < 3:
                        # reached end of line and a single DNA is less then 3
                        line = file_object.read(99)
                        self.file_position = file_object.tell()
                        print('Posission no * or not divided by 3: ' + str(self.file_position))
                        # self.file_position = self.file_position + chunk_position - len(
                        #     single_DNA) + remainder_backslash_line
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
        print('remainder_remove:' + str(count))
        return data, count
