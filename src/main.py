import traceback

from src.file_reader import FileReader
from src.logic import Logic
import multiprocessing

import time


def worker(procnum, return_dict, block):
    # print('PID:' + str(procnum) + " Block data: " + block)
    return Logic.do_conversion(procnum, return_dict, block)


def main(file_name):
    try:
        start_time = time.time()
        file_reader = FileReader()
        min_dns_dict = run_multiprocess_conversion(file_reader, file_name)
        min_dna_seq = Logic.get_min_seq(min_dns_dict)
        aa_combinations = Logic.get_total_combinations(min_dna_seq)
        Logic.write_output(min_dna_seq, aa_combinations)
        print("--- %s seconds ---" % (time.time() - start_time))
    except Exception as e:
        print('Exception in main: ' + str(e))
        print(traceback.print_tb(e.__traceback__))


def run_multiprocess_conversion(file_reader, file_name):
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for threadId, block in enumerate(file_reader.convert_by_chunks(file_name)):
        p = multiprocessing.Process(target=worker, args=(threadId, return_dict, block))
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()
    return return_dict


if __name__ == "__main__":
    main('DNA_input.txt')
