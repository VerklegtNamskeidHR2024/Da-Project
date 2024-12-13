from Model_Classes.human_model import Human

class Manager(Human):
    def __init__(self, name:str="", social_security_number:str='', phone_number:str='', location:str="", system_permissions:str="Manager",
                email:str="", staff_id:str=""):
        super().__init__(name, social_security_number, phone_number, location, system_permissions, email, staff_id)
        
    def to_dict(self):
        """Converts the Manager object to a dictionary"""
        # This is done to convert the Manager object to a dictionary so that it can be written to a json file more easily
        return {
            'name': self.name,
            'social_security_number': self.social_security_number,
            'phone_number': self.phone_number,
            'location': self.location,
            'system_permissions': self.system_permissions,
            'email': self.email,
            'staff_id': self.staff_id
        }