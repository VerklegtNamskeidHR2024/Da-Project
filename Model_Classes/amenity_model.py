from Model_Classes.property_model import Property

class Amenity(Property):
    def __init__(self, property_id:str="", name:str="", location:str="", condition:str="", total_price_to_fix:float=0.0, amenity_description:str=""):
        super().__init__(property_id ,name, location, condition, total_price_to_fix)
        self.amenity_description = amenity_description

    # Setters for the Amenity class
    def set_amenity_description(self, amenity_description):
        """Sets the amenity description"""
        self.amenity_description = amenity_description
        
    # Getters for the Amenity class
    def get_amenity_description(self):
        """Gets the amenity description"""
        return self.amenity_description
        
    
    def to_dict(self):
        """Converts the Amenity object to a dictionary"""
        # This is done to convert the Amenity object to a dictionary so that it can be written to a json file more easily
        return {
            'property_id': self.property_id,
            'name': self.name,
            'location': self.location,
            'condition': self.condition,
            'total_price_to_fix': self.total_price_to_fix,
            'amenity_description': self.amenity_description
        }