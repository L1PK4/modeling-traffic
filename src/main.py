from typing import Sequence

from numpy import log, random

from src.data.data import Data, Datum
from src.road.road import Road
from src.settings import *


def make_experiment(
        road: Road,
        time_limit: int = Tk,
        delta_time: int = dt,
) -> None:
    data = Data()
    new_datum = Datum('')




def main():
    for p in [0, 1]:
        sign = signs[p]
        for k in [0, 1, 2]:
            i = -1
            A = []
            t = []
            for j in range(N):
                i += 1
                Ttec = 0
                Itec = i
                while Ttec <= Tk:
                    Ttec += ti()
                    car = choose_car()
                    mass, velocity = get_mass_velocity(car, k)
                    t.append([car, mass, velocity, 0])
                    while t[i][3] < S:
                        si = sign[int(t[i][3])]
                        if si[1] is not None:
                            t[i][2] = si[1]
                        elif t[i][2] <= t[i - 1][2]:
                            pass
                        elif not si[0]:
                            t[i][2] = t[i - 1][2]
                        else:
                            t[i], t[i - 1] = t[i - 1], t[i]
                            i -= 1
                        t[i][3] += t[i][2] * dt
                        i = Itec + 1
