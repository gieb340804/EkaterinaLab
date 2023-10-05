from dataclasses import dataclass
from typing import NamedTuple, TypedDict
from datetime import date

@dataclass(slots=True, frozen=True )
class File:
    name : str
    processor : str
    ram : int
    memoryСapacity : int
    ramGpu : int
    price : int
    quantity : int


class FileInfoNamedTuple(NamedTuple):
    name : str
    processor : str
    ram : int
    memoryСapacity : int
    ramGpu : int
    price : int
    quantity : int


class FileInfoTypedDict(TypedDict):
    name : str
    processor : str
    ram : int
    memoryСapacity : int
    ramGpu : int
    price : int
    quantity : int


