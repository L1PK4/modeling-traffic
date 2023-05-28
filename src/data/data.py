import json
from typing import Annotated, Any, Generic, Iterator, Self, Type, TypeVar

from src.utils.singleton import Singleton


class Data(metaclass=Singleton):
    _data: dict[
        str,
        dict[int, list[Any]]
    ] = {}

    def __setattr__(self, __name: str, __value: dict[int, list[Any]]) -> None:
        self._data[__name] = __value

    def __getattr__(self, __name: str) -> dict[int, list[Any]] | dict[str, dict[int, list[Any]]] | None:
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
