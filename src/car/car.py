
from typing import Any, Self, Sequence

import numpy as np

from src.utils import y2

# from src.settings import allowed_speed

allowed_speed = (
    (110 / 3.6, 90 / 3.6),
    (90 / 3.6, 70 / 3.6),
    (85 / 3.6, 60 / 3.6)
)

class Car:
    id: int
    name: str
    lifting: float
    lifting_range: float
    spawn_chance: float
    probability: float

    mass: float
    velocity: float
    position: float

    time: float = 0.


    def _get_mass(
            self
    ) -> float:
        a = self.lifting
        sigma = self.lifting_range
        return y2(r=1) * sigma + a
    
    def _get_initial_velocity(
        self,
        coating: int,
        speeds: Sequence[Sequence[float]] = allowed_speed
    ) -> float:
        sigma = 20 / 3.6
        a = speeds[coating][int(self.mass >= 5.5)]
        return y2(r=1) * sigma + a

    def __init__(
            self,
            id: int,
            name: str,
            lifting: float,
            lifting_range: float,
            spawn_chance: float,
            probability: float,
    ):
        self.id = id
        self.name = name
        self.lifting = lifting
        self.lifting_range = lifting_range
        self.spawn_chance = spawn_chance
        self.probability = probability
        self.position = 0
        self.crossing = 0
        self.velocity_sum: float = 0.
        self.steps = 0
    
    def start(
            self,
            coating: int
    ):
        self.mass = self._get_mass()
        self.velocity = self._get_initial_velocity(coating)
        self.velocity_sum += self.velocity
        self.steps += 1

    def move_solo(self, dt: float) -> float:
        self.position += self.velocity * dt
        self.time += dt
        self.velocity_sum += self.velocity
        self.steps += 1
        return self.position
    
    def reached(
            self,
            s: float = 30_000
    ) -> bool:
        return self.position >= s
    
    def move(
            self,
            other: Self,
            dt: float,
            limit: float | None,
            can_cross: bool,
            # s: float = 30 / 3.6,
    ) -> bool:
        crossed = False
        self.time += dt
        if limit is not None and self.velocity > limit:
            self.velocity = limit
        if self.velocity > other.velocity:
            if can_cross:
                # print(f'{self.id} crossed')
                self.crossing += 1
                crossed = True 
            else:
                self.velocity = other.velocity
        self.move_solo(dt)
        # # print(self.position)
        return crossed
    

    def load_data(self) -> list[Any]:
        ans = [
            1,
            self.time,
            self.crossing,
            self.velocity_sum / self.steps,
        ]
        return ans
    
    def cumulate(
            self,
            other: list[Any],
    ) -> list[Any]:
        other = [
            other[0] + 1,
            other[1] + self.time,
            other[2] + self.crossing,
            other[3] + self.velocity_sum / self.steps,
        ]
        return other
        
    


