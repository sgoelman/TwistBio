from multiprocessing import Pool
import pandas as pd

from src.DNA_to_amino_acid import DNA_TO_AMINO_ACID
from src.logic import Logic


class FileReader:

    def get_blocks(self, input_dna_seq):
        with open(input_dna_seq) as f:
            for chunk in self.read_in_chunks(f):
                logic = Logic(False, chunk)
                logic()

    def read_in_chunks(self, file_object, chunk_size=99):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k."""
        seek = 0
        while True:
            file_object.seek(seek)
            data = file_object.read(chunk_size)
            if not data:
                break
            line = file_object.readline()
            counter = 0
            for c in range(len(line)):
                line = line.replace("\n", "")
                line = line.replace("\r", "")
                single_DNA = line[c:c + 3]
                counter += len(single_DNA)
                seek = chunk_size + counter
                data = data + single_DNA
                if len(single_DNA) == 3 and DNA_TO_AMINO_ACID[single_DNA] == '*':
                    # exit
                    yield data
                else:
                    # no * or not divided by 3
                    if len(single_DNA) < 3:
                        seek = seek - len(single_DNA)

    def getChunk(self, size):
        pass

    def get_next_stop_codon(self):
        pass


fr = FileReader()
fr.get_blocks('test')

#
# CREATE_TAB_MODE = 0
# DF_INDEX = None
# df_columns = None
# df_list = []
#
# with open(chunk) as f:
#     for line in f:
#         for c in range(len(line)):
#             single_DNA = line[c:c+3]
#             if DNA_TO_AMINO_ACID[single_DNA] == '*':
#
#         # elif line.startswith('END OF DISPLAY'):
#         #     break
#         # elif CREATE_TAB_MODE:
#         #     if df_columns is None:
#         #         df_columns = line.strip().split()
#         #     else:
#         #         df_list.append(line.strip().split())
#
# df = pd.DataFrame(df_list, columns=df_columns)
#
# for index, row in df.iterrows():
#     if int(row['D']) > 30:
#         DF_INDEX = index
#         break
#
# print(df[DF_INDEX:])
