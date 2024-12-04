from Model_Classes.human_model import Human

class Employee(Human):
    def __init__(self, name:str="", social_security_number:int=0, phone_number:int=0, location:str="", system_permissions:str="Employee",
                email:str="", staff_id:str=""):
        super().__init__(name, social_security_number, phone_number, location, system_permissions, email, staff_id)
    
    def to_dict(self):
        return {
            'name': self.name,
            'social_security_number': self.social_security_number,
            'phone_number': self.phone_number,
            'location': self.location,
            'system_permissions': self.system_permissions,
            'email': self.email,
            'staff_id': self.staff_id
        }