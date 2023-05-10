from math import ceil, log2
from typing import Dict, Sequence


class WrapperInt:
    def __init__(self, options: str | Sequence[str]) -> None:
        self.__options: set[str] = set(options)
        self.__bits: int = ceil(log2(len(self.__options)))
        self.__map: Dict[str, int] = {
            op: n for n, op in enumerate(self.__options)
        }
        self.bit_string: int = 1

    def compress(self, data: str) -> None:
        pass

    def descompress(self) -> str:
        return """"""
