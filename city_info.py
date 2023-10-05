from dataclasses import dataclass
from typing import NamedTuple, TypedDict


class CityInfoNamedTuple(NamedTuple):
    name : str
    population : int
    latitude: float
    longitude: float


class CityInfoTypedDict(TypedDict):
    name : int
    population : int
    latitude: float
    longitude: float


@dataclass(slots=True, frozen=True)
class CityInfo:
    name : str
    population : int
    latitude: float
    longitude: float




if __name__ == "__main__":
    barnaul_namedtuple = CityInfoNamedTuple('Barnaul', 627789, 53.33, 83.75)
    barnaul_typeddict = CityInfoTypedDict(name='Barnaul', population=627789, latitude=53.33, longitude=83.75)
    barnaul_dataclass = CityInfo('Barnaul', 627789, 53.33, 83.75)
    print(barnaul_namedtuple)
    print(barnaul_typeddict)
    print(barnaul_dataclass)
