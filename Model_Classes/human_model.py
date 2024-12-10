class Human:
    def __init__(self,name:str="", social_security_number:str='', phone_number:str='', location:str="",
                system_permissions:str="", email:str="", staff_id:str=""):
        self.name = name
        self.social_security_number = social_security_number
        self.phone_number = phone_number
        self.location = location
        self.system_permissions = system_permissions
        self.email = email
        self.staff_id = staff_id
        """Constructor for Human"""

    def set_name(self, name):
        """Sets the name"""
        self.name = name
    
    def set_social_security_number(self, social_security_number):
        """Sets the social security number"""
        self.social_security_number = social_security_number
    
    def set_phone_number(self, phone_number):
        """Sets the phone number"""
        self.phone_number = phone_number

    def set_location(self, location):
        """Sets the location"""
        self.location = location

    def set_system_permissions(self, system_permissions):
        """Sets the system permissions"""
        self.system_permissions = system_permissions
    
    def set_email(self, email):
        """Sets the email"""
        self.email = email

    def set_staff_id(self, staff_id):
        """Sets the staff id"""
        self.staff_id = staff_id
    
    def get_name(self):
        """Gets the name"""
        return self.name
    
    def get_social_security_number(self):
        """Gets the social security number"""
        return self.social_security_number
    
    def get_phone_number(self):
        """Gets the phone number"""
        return self.phone_number
    
    def get_location(self):
        """Gets the location"""
        return self.location
    
    def get_system_permissions(self):
        """Gets the system permissions"""
        return self.system_permissions
    
    def get_email(self):
        """Gets the email"""
        return self.email
    
    def get_staff_id(self):
        """Gets the staff id"""
        return self.staff_id