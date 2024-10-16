import csv
from pathlib import Path

import scipy


def get_corrected_mass(stellar_magnitude: float) -> float:
    path_to_file = (Path(__file__).parent /
                    f'../../data/dependence_luminocity_on_mass.csv').resolve()

    with open(path_to_file, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        header_row = next(csv_reader)

        mass_column = 0
        stellar_magnitude_column = 1

        for i, column_name in enumerate(header_row):
            match column_name.strip().upper():
                case 'LG(M/M☉)':
                    mass_column = i
                case 'MBOL':
                    stellar_magnitude_column = i

        xp: list[float] = []
        fp: list[float] = []
        for row in csv_reader:
            for i, column in enumerate(row):
                if i == mass_column:
                    fp.append(float(column))

                if i == stellar_magnitude_column:
                    xp.append(float(column))

        linear_interpolation = scipy.interpolate.interp1d(xp, fp)

    return float(10 ** linear_interpolation(stellar_magnitude))
