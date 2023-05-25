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

def mass(
        car_id: int,
        chars: Sequence[Sequence[float]] = brand_chars
) -> float:
    a, sigma = chars[car_id][:2]
    return y2() * sigma + a

def velocity(
        car_id: int,
        mode: int,
        chars: Sequence[Sequence[float]] = brand_chars,
        speeds: Sequence[Sequence[float]] = allowed_speed
) -> float:
    
    m = mass(
        car_id=car_id,
        chars=chars
    )
    sigma = 20 * 3.6
    a = speeds[mode][int(m >= 5.5)]
    return y2() * a + sigma

def main():
    for p in [0, 1]:
        for k in [0, 1, 2]:
            i = 0
            for j in range(N):
                i += 1
