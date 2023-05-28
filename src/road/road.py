from copy import copy
from enum import Enum
from typing import Sequence

import numpy as np

from src.car import Car
from src.data import Data


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
    signs: dict[int, Sign] = {}

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
            self.signs[it] = Sign(*si)

    def __len__(
            self
    ) -> int:
        return len(self.cars)

    def add_car(self, car: Car):
        self.cars.append(car)
        

    def generate_car(
            self,
            cars: list[Car],
            t: float,
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
        new_car.time = t
        self.add_car(new_car)
        return new_car


    def get_closest_sign(
            self,
            car: Car,
    ) -> Sign:
        return self.signs[int(car.position // 4000) + 1]
    

    def move(
            self,
            dt: float,
            current_idx: int
    ) -> int:
        print(f'Current index {current_idx}')
        current = self.cars[current_idx]
        next_to_current = self.cars[current_idx - 1]
        sign = self.get_closest_sign(current)
        crossed = current.move(
            next_to_current,
            dt,
            sign.speed_limit,
            sign.can_cross,
        )
        if crossed:
            self.cars[current_idx] = next_to_current
            self.cars[current_idx - 1] = current
            return current_idx - 1
        return current_idx
    

    def load_data(
            self,
            exp_idx: int,
    ):
        data = Data()
        cars_data = {}
        for car in self.cars:
            car_data = car.load_data()
            cars_data[car.id] = cars_data
        name = self.data_name()
        if (attr := getattr(data, name)) is not None:
            attr[exp_idx] = cars_data
            setattr(data, name, attr)
            return
        setattr(data, name, cars_data)

    def data_name(self):
        return f'Data_{self.coating.name}_{self.lines.name}'

