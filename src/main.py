from typing import Sequence
from numpy import log, random
from src.settings import *


def y2(r: int = 6) -> float:
    ans = -float(r)
    for z in range(r * 2):
        ans += random.random()
    return ans


y3 = y2


def ti(l: float = lambda_) -> float:
    return -log(random.random()) / l


def choose_car(
        chars: Sequence[Sequence[float]] = brand_chars,
) -> int:
    return random.choice(
        10,
        p=np.array(brand_chars)[:, 2]
    )


def get_mass(
        car_id: int,
        chars: Sequence[Sequence[float]] = brand_chars
) -> float:
    a, sigma = chars[car_id][:2]
    return y2() * sigma + a


def get_mass_velocity(
        car_id: int,
        mode: int,
        chars: Sequence[Sequence[float]] = brand_chars,
        speeds: Sequence[Sequence[float]] = allowed_speed
) -> tuple[float, float]:
    m = get_mass(
        car_id=car_id,
        chars=chars
    )
    sigma = 20 * 3.6
    a = speeds[mode][int(m >= 5.5)]
    return m, y2() * a + sigma


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
