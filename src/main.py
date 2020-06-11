from Bio.Seq import Seq
import time
t0 = time.time()
stream = open("DNA_data.txt", "r", encoding="utf-8")
my_dna = Seq(squ)
print(my_dna.translate())
t1 = time.time()
total = t1-t0
print('total execution time:',total)


# Codon 'ZZZ' is invalid