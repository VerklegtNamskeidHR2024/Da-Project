from property_model import Property

class House(Property):
    def __init__(self, name: str, location: str, total_price_to_fix: float, property_id: str, property_price: float):
        super().__init__(name, location, total_price_to_fix)
        self.property_id = property_id
        self.property_price = property_price

    def set_property_id(self, property_id):
        self.property_id = property_id

    def set_property_price(self, property_price):
        self.property_price = property_price

    def get_property_id(self):
        return self.property_id

    def get_property_price(self):
        return self.property_price