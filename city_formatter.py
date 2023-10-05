from city_info import *



def format_city_info(city: CityInfo | CityInfoNamedTuple) -> str:
    """Formats city info to string"""
    return (f"Название города: {city.name}\n"
            f"Население: {city.population}\n"
            f"Широта: {city.latitude}\n"
            f"Долгота: {city.longitude}\n")

def format_city_info_typeddict(city: CityInfoTypedDict) -> str:
    """Formats city info from TypedDict to string"""
    return (f"Название города: {city['name']}\n"
            f"Население: {city['population']}\n"
            f"Широта: {city['latitude']}\n"
            f"Долгота: {city['longitude']}\n")



if __name__ == "__main__":
    barnaul = CityInfo('Barnaul', 627789, 53.33, 83.75)
    print(format_city_info(barnaul))
    barnaul = CityInfoTypedDict(name='Barnaul', population=627789, latitude=53.33, longitude=83.75)
    print(format_city_info_typeddict(barnaul))

    
    
