from typing import Sequence

from numpy import log, random

from src.car import Car
from src.data import Data, Datum
from src.road import Coating, Lines, Road
from src.settings import N, Tk, cars, dt, signs
from src.utils import ti


def make_experiment(
        road: Road,
        exp_index: int,
        cars: list[Car],
        time_limit: int = Tk,
        delta_time: int = dt,
) -> None:
    car = road.generate_car(cars, t=0)
    car.start(road.coating.value)
    t = 0
    idx = 0
    while t < time_limit:
        t += ti()
        car = road.generate_car(cars, t=t)
        print(f'Cars currently {len(road.cars)}')
        car.start(road.coating.value)
        while not car.reached():
            idx = road.move(delta_time, current_idx=idx)
        idx += 1
    road.load_data(exp_index)


def make_experiments(
        coating: Coating,
        lines: Lines,
        spread: float = 30 * 3.6,
        N: int = N
        ) ->None:
    for idx in range(N):
        print(f'Statrting expetiment num {idx}')
        signs_ = signs[lines.value]
        road = Road(
            coating,
            lines,
            spread,
            signs_,
        )
        make_experiment(
            road,
            idx,
            list(map(lambda x: Car(*x), cars)),
        )



def main():
    data = Data()
    make_experiments(
        Coating.asphalt,
        Lines.onelined,
    )


if __name__ == '__main__':
    main()