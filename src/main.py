from timeit import default_timer

from src.logic import Logic


def main():
    start = default_timer()
    logic = Logic()
    logic.do_conversion('DNA_input.txt')
    logic.write_output()
    duration = default_timer() - start
    print('Total execution Time is : ' + str(duration))


if __name__ == "__main__":
    main()
