from pprint import pprint

from doublestardata import read_data_from_file


def main() -> None:
    star_number = 1
    star_data = read_data_from_file(star_number)

    pprint(star_data)


if __name__ == "__main__":
    main()
