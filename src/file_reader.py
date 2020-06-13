from multiprocessing import Pool
import pandas as pd

from src.DNA_to_amino_acid import DNA_TO_AMINO_ACID


class FileReader:
    def __init__(self):
        self.file_position = 0
        self.end_of_file = False

    def convert_by_chunks(self, logic, input_dna_file='DNA_input.txt', chunk_size=999):
        self.end_of_file = False
        with open(input_dna_file) as f:
            for block in self.__read_in_chunks(f, chunk_size):
                yield block

    def __read_in_chunks(self, file_object, chunk_size):
        """Generator removes /n and /r
         returns blocks that divide by 3 and end with * """
        # seek = 0
        while not self.end_of_file:
            file_object.seek(self.file_position)
            data = file_object.read(chunk_size)
            # if not data:
            #     self.end_of_file = True
            line = file_object.read(100)
            if (len(line) < 99):
                data = file_object.read(chunk_size + len(line))
                self.end_of_file = True
                yield self.__remove_backslash(data)
            counter = 0
            for c in range(len(line) - 1):
                line = self.__remove_backslash(line)
                single_DNA = line[c:c + 3]
                counter += len(single_DNA)
                chunk_position = chunk_size + counter
                data = data + single_DNA
                if len(single_DNA) == 3 and DNA_TO_AMINO_ACID[single_DNA] == '*':
                    # exit
                    self.file_position = self.file_position + chunk_position
                    yield self.__remove_backslash(data)
                    break
                else:
                    # no * or not divided by 3
                    if len(single_DNA) < 3:
                        self.file_position = self.file_position - len(single_DNA)

    @staticmethod
    def __remove_backslash(data):
        data = data.replace("\n", "")
        data = data.replace("\r", "")
        return data
