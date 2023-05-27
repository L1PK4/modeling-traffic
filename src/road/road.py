from copy import copy
from enum import Enum
from typing import Sequence

import numpy as np

from src.car.car import Car


class Sign:
    speed_limit: float | None
    can_cross: bool

    def __init__(
            self,
            can_cross: bool,
            speed_limit: float | None,
        ) -> None:
        self.speed_limit = speed_limit
        self.can_cross = can_cross


class Coating(Enum):
    asphalt = 0
    concrete = 1
    gravel = 2

class Lines(Enum):
    onelined = 0
    twolined = 1


class Road:
    spread: float
    coating: Coating
    lines: Lines
    cars: list[Car] = []
    signs: dict[float, Sign] = {}

    def __init__(
            self,
            coating: Coating,
            lines: Lines,
            spread: float,
            signs: Sequence[tuple[bool, float | None]] | None = None,
            ) -> None:
        self.coating = coating
        self.lines = lines
        self.spread = spread
        if signs is not None:
            self.parse_signs(signs)

    def parse_signs(
            self,
            signs: Sequence[tuple[bool, float | None]],
    ) -> None:
        self.signs = {}
        for it, si in enumerate(signs):
            self.signs[it * 4] = Sign(*si)

    def __len__(
            self
    ) -> int:
        return len(self.cars)

    def add_car(self, car: Car):
        self.cars.append(car)
        

    def generate_car(
            self,
            cars: list[Car],
    ) -> Car:
        n = len(cars)
        probabilities = [
            car.spawn_chance
            for car
            in cars
        ]
        new_car_idx = np.random.choice(
            n,
            p=probabilities
        )
        new_car = copy(cars[new_car_idx])
        self.add_car(new_car)
        return new_car

            