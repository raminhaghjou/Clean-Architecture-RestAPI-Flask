

class City:
    """
        Definition of the CityProvince entity
    """

    city_id : int
    
    def __init__(self, name, province_id):
        self.name = name
        self.province_id = province_id
