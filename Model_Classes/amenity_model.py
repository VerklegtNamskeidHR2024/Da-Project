from property_model import Property

class Amenity(Property):
    def __init__(self, property_id:str="", name:str="", location:str="", total_price_to_fix:float=0.0, amenity_description:str=""):
        super().__init__(property_id ,name, location, total_price_to_fix)
        self.amenity_description = amenity_description

    def set_amenity_description(self, amenity_description):
        self.amenity_description = amenity_description

    def get_amenity_description(self):
        return self.amenity_description