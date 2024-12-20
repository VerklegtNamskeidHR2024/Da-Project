class Property:
    def __init__(self, property_id:str="", name:str="", location:str="", condition:str="",total_price_to_fix:float=0.0,property_price:float=0.0):
        self.property_id = property_id
        self.location = location
        self.name = name
        self.condition = condition
        self.total_price_to_fix = total_price_to_fix
        self.property_price = property_price

    # Setters for the Property class
    def set_property_id(self, property_id):
        """Sets the property id"""
        self.property_id = property_id

    def set_name(self, name):
        """Sets the name"""
        self.name = name

    def set_condition(self, condition):
        """Sets the condition"""
        self.condition = condition

    def set_location(self, location):
        """Sets the location"""
        self.location = location

    def set_total_price_to_fix(self, total_price_to_fix):
        """Sets the total price to fix"""
        self.total_price_to_fix = total_price_to_fix

    def set_property_price(self, property_price):
        self.property_price = property_price

    # Getters for the Property class
    def get_property_id(self):
        """Gets the property id"""
        return self.property_id

    def get_name(self):
        """Gets the name"""
        return self.name
    
    def get_condition(self):
        """Gets the condition"""
        return self.condition

    def get_location(self):
        """Gets the location"""
        return self.location

    def get_total_price_to_fix(self):
        """Gets the total price to fix"""
        return self.total_price_to_fix
    
    def get_property_price(self):
        return self.property_price