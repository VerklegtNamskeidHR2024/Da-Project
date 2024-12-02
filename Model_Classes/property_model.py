class Property:
    def __init__(self, name: str, location: str, total_price_to_fix: float):
        self.name = name
        self.location = location
        self.total_price_to_fix = total_price_to_fix

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def set_total_price_to_fix(self, total_price_to_fix):
        self.total_price_to_fix = total_price_to_fix

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_total_price_to_fix(self):
        return self.total_price_to_fix