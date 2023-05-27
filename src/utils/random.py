from numpy import log, random

from src.settings import lambda_


def y2(r: int = 6) -> float:
    ans = -float(r)
    for z in range(r * 2):
        ans += random.random()
    return ans


y3 = y2

def ti(l: float = lambda_) -> float:
    return -log(random.random()) / l