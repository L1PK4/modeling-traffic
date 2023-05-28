from typing import Sequence

from numpy import log, random

from src.car import Car
from src.data import Data
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
        # idx += 1
        car = road.generate_car(cars, t=t)
        # print(f'Cars currently {len(road.cars)}')
        car.start(road.coating.value)
        while not car.reached():
            idx = road.move(delta_time, current_idx=idx)
            car = road.cars[idx]
        road.load_car_data(idx)
        idx += 1
    road.load_data(exp_index)


def make_experiments(
        coating: Coating,
        lines: Lines,
        spread: float = 30_000,
        numbers_of_experiments: int = N
        ) ->None:
    for idx in range(numbers_of_experiments):
        # print(f'Statrting expetiment num {idx}')
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
        numbers_of_experiments=100
    )
    from datetime import datetime
    start = datetime.now()
    with open('results/test_exp.json', 'wt', encoding='utf-8') as f:
        f.write(str(data))
    print(f"Elapsed 1 {datetime.now() - start}")


if __name__ == '__main__':
    from datetime import datetime
    start = datetime.now()
    main()
    print(f"Elapsed 2 {datetime.now() - start}")