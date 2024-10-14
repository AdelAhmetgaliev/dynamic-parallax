from pathlib import Path
from pprint import pprint

from doublestardata import read_data_from_file


def main() -> None:
    star_number = 1

    data_path = (Path(__file__).parent / '../data/init_params_of_double_stars.csv').resolve()
    star_data = read_data_from_file(data_path, star_number)

    pprint(star_data)

if __name__ == "__main__":
    main()
