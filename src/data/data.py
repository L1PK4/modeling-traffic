import json
from typing import Annotated, Generic, Iterator, Type, TypeVar

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


    def __str__(self) -> str:
        return f'{self.name}({self.ref.__name__}): {self.data}'
    def __repr__(self) -> str:
        return self.__str__()


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

    def __str__(self) -> str:
        return json.dumps(
            self._data,
            indent=4,
            ensure_ascii=False,
            default=lambda x: str(x)
        )
