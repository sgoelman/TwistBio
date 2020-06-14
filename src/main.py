from src.file_reader import FileReader
from src.logic import Logic
import multiprocessing

import time


def worker(procnum, return_dict, block):
    print('PID:' + str(procnum) + " Block data: " + block)
    res = Logic.do_conversion(procnum, return_dict, block)
    # res = Logic.do_conversion(procnum, block)
    print(res)


def main():
    t0 = time.time()
    logic = Logic()
    file_reader = FileReader()
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for threadId, block in enumerate(file_reader.convert_by_chunks()):
        # p = multiprocessing.Process(target=worker, args=(threadId, block))
        p = multiprocessing.Process(target=worker, args=(threadId, return_dict, block))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print(return_dict.values())


if __name__ == "__main__":
    main()

#
#
# def main():
#     try:
#         t0 = time.time()
#         logic = Logic()
#         apply_async_with_callback(logic)
#         logic.convert_back_to_DNA()
#         logic.write_output()
#
#         t1 = time.time()
#         total = t1 - t0
#         print('total translation time:', str(total))
#     except Exception as e:
#         print(e)
#
#
# def collect_results(lst):
#     results.extend(lst)
#
#
# def apply_async_with_callback(logic):
#     file_reader = FileReader()
#     pool = mp.Pool()
#     for block in file_reader.convert_by_chunks(logic):
#         pool.apply_async(logic.wrapper, args=(block),
#                          callback=collect_results)
