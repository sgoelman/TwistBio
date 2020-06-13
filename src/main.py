from src.logic import Logic


def main():
    logic = Logic(is_input_from_file=True, input_dna_seq='DNA_input.txt')
    logic()


if __name__ == "__main__":
    main()
