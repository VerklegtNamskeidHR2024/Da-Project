class Location:
    def __init__(self, country:str="", location:str="", airport:str="", phone_number:str="", branch_manager:str="", 
                opening_hours:str=""):
        self.country = country
        self.location = location
        self.airport = airport
        self.phone_number = phone_number
        self.opening_hours = opening_hours
        self.branch_manager = branch_manager
        """Constructor for Location"""
    def set_country(self, country):
        """Sets the country"""
        self.country = country

    def set_location(self, location):
        """Sets the location"""
        self.location = location
    
    def set_airport(self, airport):
        """Sets the airport"""
        self.airport = airport
    
    def set_phone_number(self, phone_number):
        """Sets the phone number"""
        self.phone_number = phone_number

    def set_branch_manager(self, branch_manager):
        """Sets the branch manager"""
        self.branch_manager = branch_manager

    def set_opening_hours(self, opening_hours):
        """Sets the opening hours"""
        self.opening_hours = opening_hours
    
    def get_country(self):
        """Gets the country"""
        return self.country
    
    def get_location(self):
        """Gets the location"""
        return self.location
    
    def get_airport(self):
        """Gets the airport"""
        return self.airport
    
    def get_phone_number(self):
        """Gets the phone number"""
        return self.phone_number
    
    def get_branch_manager(self):
        """Gets the branch manager"""
        return self.branch_manager
    
    def get_opening_hours(self):
        """Gets the opening hours"""
        return self.opening_hours
    
    def to_dict(self):
        """Converts the Location object to a dictionary"""
        return {
            'country': self.country,
            'location': self.location,
            'airport': self.airport,
            'phone_number': self.phone_number,
            'branch_manager': self.branch_manager,
            'opening_hours': self.opening_hours
        }