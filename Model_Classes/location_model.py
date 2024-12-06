class Location:
    def __init__(self, country:str="", location:str="", airport:str="", phone_number:str="", branch_manager:str="", 
                opening_hours:str=""):
        self.country = country
        self.location = location
        self.airport = airport
        self.phone_number = phone_number
        self.opening_hours = opening_hours
        self.branch_manager = branch_manager

    def set_country(self, country):
        self.country = country

    def set_location(self, location):
        self.location = location
    
    def set_airport(self, airport):
        self.airport = airport
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_branch_manager(self, branch_manager):
        self.branch_manager = branch_manager

    def set_opening_hours(self, opening_hours):
        self.opening_hours = opening_hours
    
    def get_country(self):
        return self.country
    
    def get_location(self):
        return self.location
    
    def get_airport(self):
        return self.airport
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_branch_manager(self):
        return self.branch_manager
    
    def get_opening_hours(self):
        return self.opening_hours
    
    def to_dict(self):
        return {
            'country': self.country,
            'location': self.location,
            'airport': self.airport,
            'phone_number': self.phone_number,
            'branch_manager': self.branch_manager,
            'opening_hours': self.opening_hours
        }