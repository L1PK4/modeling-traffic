from dataclasses import dataclass

from src.utils.singleton import Singleton


@dataclass
class Data(metaclass=Singleton):
    pass
