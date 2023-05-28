import csv
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
        Lines.twolined,
        numbers_of_experiments=100
    )

    ensure_results_folder()

    from datetime import datetime
    start = datetime.now()
    # with open('results/test_exp.json', 'wt', encoding='utf-8') as f:
    #     f.write(str(data))
    load_to_csv()
    print(f"Elapsed 1 {datetime.now() - start}")


def ensure_results_folder():
    import os
    if not os.path.exists('results'):
        os.mkdir('results')

def load_to_csv():
    data = Data()
    ensure_results_folder()
    with open('results/data.csv', 'wt', encoding='utf-8') as file:
        writer =csv.writer(file, delimiter=';')
        for key, datum in data.items():
            writer.writerow(["Данные:", key])
            writer.writerow([
                "Номер машины",
                "Кол-во",
                "Среднее время",
                "Среднее кол-во обгонов",
                "Средняя скорость"
            ])
            for idx, car_datum in datum.items():
                writer.writerow([
                    idx,
                    car_datum["population"], # type: ignore
                    car_datum["mean_time"], # type: ignore
                    car_datum["mean_crossings"], # type: ignore
                    car_datum["mean_vel"], # type: ignore
                ])


if __name__ == '__main__':
    from datetime import datetime
    start = datetime.now()
    main()
    print(f"Elapsed 2 {datetime.now() - start}")