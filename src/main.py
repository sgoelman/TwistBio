from src.file_reader import FileReader
from src.logic import Logic


def main():
    fr=FileReader()
    fr.read_in_chunks('DNA_input.txt')


if __name__ == "__main__":
    main()
