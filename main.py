from city_info import *
from city_formatter import *


def main():
    moscow_namedtuple  = CityInfoNamedTuple(name='Moscow', population=1263546, \
                                        longitude=37.62, latitude=55.75)
    moscow_typedict  = CityInfoTypedDict(name='Moscow', longitude=37.62, \
                                        latitude=55.75, population=12635466)
    moscow_dataclass = CityInfo(population=12635466, name='Moscow', \
                                longitude=37.62, latitude=55.75)
    print(format_city_info(moscow_namedtuple))
    print(format_city_info_typeddict(moscow_typedict))
    print(format_city_info(moscow_dataclass))

if __name__ == "__main__":
    main()
