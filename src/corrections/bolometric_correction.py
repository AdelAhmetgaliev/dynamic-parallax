import csv
from pathlib import Path

import scipy

from doublestardata import DoubleStarData


def get_bolometric_correction(
        star_data: DoubleStarData) -> tuple[float, float]:
    first_star_type = star_data.first_spectral_class[2:]
    first_star_class = star_data.first_spectral_class[:2]

    second_star_type = star_data.second_spectral_class[2:]
    second_star_class = star_data.second_spectral_class[:2]

    first_correction = _get_bolometric_correction_by_type(
        first_star_type, first_star_class)
    second_correction = _get_bolometric_correction_by_type(
        second_star_type, second_star_class)

    return first_correction, second_correction


def _spectral_class_to_num(spectral_class: str) -> int:
    letter_to_num = {'O': 1, 'B': 2, 'A': 3, 'F': 4, 'G': 5, 'K': 6, 'M': 7}
    return letter_to_num[spectral_class[0]] * \
        len(letter_to_num) + int(spectral_class[1])


def _get_bolometric_correction_by_type(
        star_type: str, star_class: str) -> float:
    path_to_file = (Path(__file__).parent /
                    f'../../data/bolometric_corrections_{star_type}.csv').resolve()

    with open(path_to_file, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        header_row = next(csv_reader)

        spectral_class_column = 0
        correction_column = 5

        for i, column_name in enumerate(header_row):
            match column_name.strip().upper():
                case 'SP':
                    spectral_class_column = i
                case 'BC':
                    correction_column = i

        xp: list[int] = []
        fp: list[float] = []
        for row in csv_reader:
            for i, column in enumerate(row):
                if i == spectral_class_column:
                    xp.append(_spectral_class_to_num(column))

                if i == correction_column:
                    fp.append(float(column.replace(',', '.')))

    star_spectral_num = _spectral_class_to_num(star_class)
    linear_interpolation = scipy.interpolate.interp1d(xp, fp)

    return float(linear_interpolation(star_spectral_num))
