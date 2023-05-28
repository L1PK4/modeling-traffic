import json
from typing import Any

from src.utils.singleton import Singleton


class Data(metaclass=Singleton):
    _data: dict[
        str,
        dict[int, dict[str, Any]]
    ] = {}

    def __setattr__(self, __name: str, __value: dict[int, dict[str, Any]]) -> None:
        self._data[__name] = __value

    def __getattr__(
            self,
            __name: str
    ) -> dict[int, dict[str, Any]] | dict[str, dict[int, dict[str, Any]]] | None:
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

    def items(self):
        return self._data.items()