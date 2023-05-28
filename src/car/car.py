
from typing import Self, Sequence

import numpy as np

from src.data import Datum
from src.utils import y2

# from src.settings import allowed_speed

allowed_speed = (
    (110 * 3.6, 90 * 3.6),
    (90 * 3.6, 70 * 3.6),
    (85 * 3.6, 60 * 3.6)
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
    velocities: list[float] = []
    crossing: int = 0

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
        sigma = 20 * 3.6
        a = speeds[coating][int(self.mass >= 5.5)]
        return y2(r=1) * a + sigma

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
        self.mass = self._get_mass()
        self.position = 0
    
    def start(
            self,
            coating: int
    ):
        self.velocity = self._get_initial_velocity(coating)
        self.velocities.append(self.velocity)

    def move_solo(self, dt: float) -> float:
        self.position = self.velocity * dt
        self.time += dt
        self.velocities.append(self.velocity)
        return self.position
    
    def reached(
            self,
            s: float = 30 * 3.6
    ) -> bool:
        return self.position >= s
    
    def move(
            self,
            other: Self,
            dt: float,
            limit: float | None,
            can_cross: bool,
            # s: float = 30 * 3.6,
    ) -> bool:
        crossed = False
        self.time += dt
        if limit is not None and self.velocity > limit:
            self.velocity = limit
        if self.velocity > other.velocity:
            if can_cross:
                self.crossing += 1
                crossed = True 
            else:
                self.velocity = other.velocity
        self.move_solo(dt)
        return crossed
    

    def load_data(self) -> list[Datum]:
        ans = [
            Datum('Номер', self.id),
            Datum('Время', self.time),
            Datum('Обгоны', self.crossing),
            Datum('Скорости', self.velocities),
            Datum('Средняя скорость', np.mean(self.velocities))
        ]
        return ans
    


