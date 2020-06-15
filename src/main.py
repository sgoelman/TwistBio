from timeit import default_timer
from src.logic import Logic


def main():
    start = default_timer()
    logic = Logic()
    logic.get_min_aa('l_data')
    total_combinations = logic.convert_back_to_DNA()
    logic.write_output(total_combinations)
    duration = default_timer() - start
    print('Total execution Time is : ' + str(duration))


if __name__ == "__main__":
    main()
