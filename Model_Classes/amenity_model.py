from property_model import Property

class Amenity(Property):
    def __init__(self, name: str, location: str, total_price_to_fix: float, amenity_id: str):
        super().__init__(name, location, total_price_to_fix)
        self.amenity_id = amenity_id

    def set_amenity_id(self, amenity_id):
        self.amenity_id = amenity_id

    def get_amenity_id(self):
        return self.amenity_id