from math import log10
from pprint import pprint

from bolometric_correction import get_bolometric_correction
from doublestardata import DoubleStarData, read_data_from_file


def calculate_parallax(star_data: DoubleStarData,
                       first_star_mass: float, second_star_mass: float) -> float:
    return (star_data.major_semi_axes /
            (star_data.period ** 2 * (first_star_mass + second_star_mass)) ** (1 / 3))


def calculate_absolute_stellar_magnitude(
        star_data: DoubleStarData, parallax: float) -> tuple[float, float]:
    first_absolute_stellar_magnitude = star_data.first_stellar_magnitude + \
                                       5 + 5 * log10(parallax)
    second_absolute_stellar_magnitude = star_data.second_stellar_magnitude + \
                                        5 + 5 * log10(parallax)

    return first_absolute_stellar_magnitude, second_absolute_stellar_magnitude


def main() -> None:
    star_number = 0

    star_data = read_data_from_file(star_number)
    first_star_mass = 1
    second_star_mass = 1

    parallax = calculate_parallax(star_data, first_star_mass, second_star_mass)
    absolute_stellar_magnitude = calculate_absolute_stellar_magnitude(
        star_data, parallax)
    bolometric_correction = get_bolometric_correction(star_data)

    pprint(parallax)
    pprint(absolute_stellar_magnitude)
    pprint(bolometric_correction)


if __name__ == "__main__":
    main()
