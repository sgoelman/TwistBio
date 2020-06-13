from src.file_reader import FileReader
from src.logic import Logic
import multiprocessing as mp

import time

results = []


def main():
    try:
        t0 = time.time()
        logic = Logic()
        apply_async_with_callback(logic)
        logic.convert_back_to_DNA()
        logic.write_output()

        t1 = time.time()
        total = t1 - t0
        print('total translation time:', str(total))
    except Exception as e:
        print(e)


def collect_results(lst):
    results.extend(lst)


def apply_async_with_callback(logic):
    file_reader = FileReader()
    pool = mp.Pool()
    for block in file_reader.convert_by_chunks(logic):
        pool.apply_async(logic.wrapper, args=(block),
                         callback=collect_results)


if __name__ == "__main__":
    main()
