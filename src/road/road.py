from typing import Sequence

from src.car import Car


class Sign:
    speed_limit: float | None
    can_cross: bool

    def __init__(
            self,
            can_cross: bool,
            speed_limit: float | None,
        ) -> None:
        self.speed_limit = speed_limit
        self.can_cross = can_cross




class Road:
    spread: float
    cars: list[Car] = []
    signs: dict[float, Sign] = {}

    def __init__(
            self,
            spread: float,
            signs: Sequence[tuple[bool, float | None]] | None = None,
            ) -> None:
        self.spread = spread
        if signs is not None:
            self.parse_signs(signs)

    def parse_signs(
            self,
            signs: Sequence[tuple[bool, float | None]],
    ) -> None:
        self.signs = {}
        for it, si in enumerate(signs):
            self.signs[it * 4] = Sign(*si)

        
            