from pprint import pprint

from doublestardata import DoubleStarData, read_data_from_file


def calculate_parallax(star_data: DoubleStarData,
                       first_star_mass: float, second_star_mass: float):
    return (star_data.major_semi_axes /
            (star_data.period ** 2 * (first_star_mass + second_star_mass)) ** (1 / 3))


def main() -> None:
    star_number = 0
    star_data = read_data_from_file(star_number)

    pprint(star_data)
    pprint(calculate_parallax(star_data, 1, 1))


if __name__ == "__main__":
    main()
