from dataclasses import dataclass

@dataclass
class GetProvinceDTO:
    province_id : str
    name : str