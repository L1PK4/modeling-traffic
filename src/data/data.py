from typing import Annotated, Generic, Type, TypeVar

from src.utils.singleton import Singleton

T = TypeVar('T')

class Datum(Generic[T]):
    name: str
    ref: Type[T]
    data: T
    def __init__(
            self,
            name: str,
            data: T,
    ):
        self.name = name
        self.ref = type(data)
        self.data = data
    


class Data(metaclass=Singleton):
    _data: dict[
        str, 
        dict[int, list[Datum]]
        ] = {}
    def __setattr__(self, __name: str, __value: dict[int, list[Datum]]) -> None:
        self._data[__name] = __value
        
    def __getattr__(self, __name: str) -> dict[int, list[Datum]] | dict[str, dict[int, list[Datum]]] | None:
        if __name == 'data':
            return self._data
        return self._data.get(__name, None)