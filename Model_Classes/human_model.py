class Human:
    def __init__(self,name: str, social_security_number: int, phone_number: int, location: str,
                system_permissions: str, email: str):
        self.name = name
        self.social_security_number = social_security_number
        self.phone_number = phone_number
        self.location = location
        self.system_permissions = system_permissions
        self.email = email

    def set_name(self, name):
        self.name = name
    
    def set_social_security_number(self, social_security_number):
        self.social_security_number = social_security_number
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_location(self, location):
        self.location = location

    def set_system_permissions(self, system_permissions):
        self.system_permissions = system_permissions
    
    def set_email(self, email):
        self.email = email
    
    def get_name(self):
        return self.name
    
    def get_social_security_number(self):
        return self.social_security_number
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_location(self):
        return self.location
    
    def get_system_permissions(self):
        return self.system_permissions
    
    def get_email(self):
        return self.email