from Model_Classes.property_model import Property

class House(Property):
    def __init__(self, property_id:str="", name:str="", location:str="", condition:str="",total_price_to_fix:float=0.0, property_price:float=0.0):
        super().__init__(property_id , name, location, condition, total_price_to_fix)
        self.property_price = property_price
        

    # Setters for the House class
    def set_property_price(self, property_price):
        """Sets the property price"""
        self.property_price = property_price

    # Getters for the House class
    def get_property_price(self):
        """Gets the property price"""
        return self.property_price
    
    def to_dict(self):
        """Converts the House object to a dictionary"""
        # This is done to convert the House object to a dictionary so that it can be written to a json file more easily
        return {
            'property_id': self.property_id,
            'name': self.name,
            'location': self.location,
            'condition': self.condition,
            'total_price_to_fix': self.total_price_to_fix,
            'property_price': self.property_price
        }