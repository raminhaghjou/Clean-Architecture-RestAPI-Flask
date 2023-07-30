from dataclasses import dataclass

@dataclass
class GetCityDTO:
    city_id : str
    name : str
    province_id : str