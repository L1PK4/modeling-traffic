
from typing import Sequence

from src.settings import allowed_speed
from src.utils.random import y2


class Car:
    id: int
    name: str
    lifting: float
    lifting_range: float
    spawn_chance: float
    probability: float

    mass: float
    velocity: float

    def _get_mass(
            self
    ) -> float:
        a = self.lifting
        sigma = self.lifting_range
        return y2(r=1) * sigma + a
    
    def _get_initial_velocity(
        self,
        mode: int,
        speeds: Sequence[Sequence[float]] = allowed_speed
    ) -> float:
        sigma = 20 * 3.6
        a = speeds[mode][int(self.mass >= 5.5)]
        return y2(r=1) * a + sigma

    def __init__(
            self,
            *,
            id: int,
            name: str,
            lifting: float,
            lifting_range: float,
            spawn_chance: float,
            probability: float,
            mode: int,
    ):
        self.id = id
        self.name = name
        self.lifting = lifting
        self.lifting_range = lifting_range
        self.spawn_chance = spawn_chance
        self.probability = probability
        self.mass = self._get_mass()
        self.velocity = self._get_initial_velocity(mode)

        
