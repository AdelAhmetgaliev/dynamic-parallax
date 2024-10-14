import csv

from dataclasses import dataclass
from pathlib import Path


@dataclass
class DoubleStarData:
    name: str
    period: float
    major_semi_axes: float

    first_stellar_magnitude: float
    second_stellar_magnitude: float

    first_spectral_class: str
    second_spectral_class: str


def read_data_from_file(star_number: int) -> DoubleStarData:
    path_to_file = (Path(__file__).parent / '../../data/init_params_of_double_stars.csv').resolve()
    with open(path_to_file, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        header_row = next(csv_reader)

        for i, column_name in enumerate(header_row):
            match column_name.strip().upper():
                case 'N':
                    star_number_column = i
                case 'ЗВЕЗДА':
                    star_name_column = i
                case 'P (ЛЕТ)':
                    star_period_column = i
                case 'MV1':
                    first_stellar_magnitude_column = i
                case 'MV2':
                    second_stellar_magnitude_column = i
                case 'SP1':
                    first_spectral_class_column = i
                case 'SP2':
                    second_spectral_class_column = i
                case 'А"':
                    major_semi_axes_column = i

        for row in csv_reader:
            if int(row[star_number_column]) != star_number:
                continue

            for i, column in enumerate(row):
                if i == star_name_column:
                    star_name = column
                elif i == star_period_column:
                    star_period = float(column)
                elif i == first_stellar_magnitude_column:
                    first_stellar_magnitude = float(column)
                elif i == second_stellar_magnitude_column:
                    second_stellar_magnitude = float(column)
                elif i == first_spectral_class_column:
                    first_spectral_class = column
                elif i == second_spectral_class_column:
                    second_spectral_class = column
                elif i == major_semi_axes_column:
                    major_semi_axes = float(column)

        return DoubleStarData(star_name, star_period, major_semi_axes,
                              first_stellar_magnitude, second_stellar_magnitude,
                              first_spectral_class, second_spectral_class)
