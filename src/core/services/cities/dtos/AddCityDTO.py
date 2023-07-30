from dataclasses import dataclass

@dataclass
class AddCityDTO:
    province_id : str
    name : str