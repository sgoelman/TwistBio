from timeit import default_timer
from src.logic import Logic


def main():
    start = default_timer()
    logic = Logic()
    logic.convert_DNA_to_AA('DNA_input.txt')
    logic.write_output()
    duration = default_timer() - start
    print('Total execution Time is : ' + str(duration))


if __name__ == "__main__":
    main()
