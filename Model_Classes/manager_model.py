from human_model import Human

class Manager(Human):
    def __init__(self, name:str="", social_security_number:int=0, phone_number:int=0, location:str="", system_permissions:str="",
                email:str="", staff_id:str=""):
        super().__init__(name, social_security_number, phone_number, location, system_permissions, email)
        self.staff_id = staff_id

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id
    
    def get_staff_id(self):
        return self.staff_id
    
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