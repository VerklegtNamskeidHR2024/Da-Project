class Property:
    def __init__(self, property_id:str="", name:str="", location:str="", condition:str="",total_price_to_fix:float=0.0,property_price:float=0.0):
        self.property_id = property_id
        self.location = location
        self.name = name
        self.condition = condition
        self.total_price_to_fix = total_price_to_fix
        self.property_price = property_price
        
    def set_property_id(self, property_id):
        self.property_id = property_id

    def set_name(self, name):
        self.name = name

    def set_condition(self, condition):
        self.condition = condition

    def set_location(self, location):
        self.location = location

    def set_total_price_to_fix(self, total_price_to_fix):
        self.total_price_to_fix = total_price_to_fix

    def set_property_price(self, property_price):
        self.property_price = property_price

    def get_property_id(self):
        return self.property_id

    def get_name(self):
        return self.name
    
    def get_condition(self):
        return self.condition

    def get_location(self):
        return self.location

    def get_total_price_to_fix(self):
        return self.total_price_to_fix
    
    def get_property_price(self):
        return self.property_price


    """def to_dict(self):
        {
        	"property_id": self.property_id,
            "name": self.name,
            "location": self.location,
            "condition": self.condition,
            "total_price_to_fix": self.total_price_to_fix,
            
        }"""