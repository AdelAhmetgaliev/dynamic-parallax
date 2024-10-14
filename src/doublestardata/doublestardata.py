from dataclasses import dataclass


@dataclass
class DoubleStarData:
    name: str
    period: float
    major_semi_axes: float

    first_stellar_magnitude: float
    second_stellar_magnitude: float

    first_spectral_class: str
    second_spectral_class: str
