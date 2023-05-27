from src.utils.singleton import Singleton


class Datum(list):
    name: str
    def __init__(
            self,
            name: str,
            *args,
            **kwargs
    ):
        self.name = name
        super().__init__(*args, **kwargs)
    

    


class Data(metaclass=Singleton):
    _data: dict[str, Datum] = {}
    def __setattr__(self, __name: str, __value: Datum) -> None:
        self._data[__name] = __value
        
    def __getattr__(self, __name: str) -> Datum | dict[str, Datum] | None:
        if __name == 'data':
            return self._data
        return self._data.get(__name, None)