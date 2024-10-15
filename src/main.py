from math import log10

from corrections import get_bolometric_correction, get_corrected_mass
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
    star_number = 1
    iteration_count = 5

    star_data = read_data_from_file(star_number)

    first_star_mass = 1
    second_star_mass = 1

    parallax = calculate_parallax(star_data, first_star_mass, second_star_mass)

    print('Значения перед обработкой:')
    print(
        f'\tПервая звезда: {
            first_star_mass:.3f} M☉, '
        f'Вторая звезда: {
            second_star_mass:.3f} M☉')
    print(f'\tПараллакс: {parallax:.3f}"')

    for i in range(iteration_count):
        absolute_stellar_magnitude = calculate_absolute_stellar_magnitude(
            star_data, parallax)
        bolometric_correction = get_bolometric_correction(star_data)

        first_absolute_stellar_magnitude, second_absolue_stellar_magnitude = absolute_stellar_magnitude
        first_bolometric_correction, second_bolometric_correction = bolometric_correction

        first_stellar_magnitude = first_absolute_stellar_magnitude + \
            first_bolometric_correction
        second_stellar_magnitude = second_absolue_stellar_magnitude + \
            second_bolometric_correction

        first_star_mass = get_corrected_mass(first_stellar_magnitude)
        second_star_mass = get_corrected_mass(second_stellar_magnitude)
        parallax = calculate_parallax(
            star_data, first_star_mass, second_star_mass)

        print(f'Итерация №{i + 1}:')
        print(
            f'\tПервая звезда: {
                first_star_mass:.3f} M☉, '
            f'Вторая звезда: {
                second_star_mass:.3f} M☉')
        print(f'\tПараллакс: {parallax:.3f}"')


if __name__ == "__main__":
    main()
