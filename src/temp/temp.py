import re

from src.file_reader import FileReader
from src.logic import Logic

# if __name__ == "__main__":
#     file_reader = FileReader()
#     res = []
#     for block in file_reader.convert_by_chunks('DNA_input.txt'):
#         res.append(block)
#         print('Block Div:' + str(len(block) % 3))
#         print('Block size:' + str(len(block)))
#
#     b = ''.join(p for p in res)
#     print('Total L: ' + str(len(b)))
#
# # tests /n
# with open('DNA_input.txt') as f:
#     d = f.read()
#     # 30329 -counts/n as 1
#     print(len(d))
#     count = 0
#     (d, qty) = re.subn("\n", "", d)
#     count += qty
#
#     print('n\_removed:' + str(count))
#     # 30756
#     print(f.tell())
#     # 29902   # 30329 -counts/n as 2
#     print('Total L Should be :' + str(len(d)))

procnum = 1
new_list = []
data = {procnum: {2147483647: None}, 2: {12412: None}, 3: {15: None}}
data[4] = {15: None}
for key in data[procnum]:
    print(int(key))
a=data[procnum].keys()
print(data)