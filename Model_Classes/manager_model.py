from human_model import Human

class Manager(Human):
    def __init__(self, name: str, social_security_number: int, phone_number: int, location: str, system_permissions: str,
                email: str, staff_id: str):
        super().__init__(name, social_security_number, phone_number, location, system_permissions, email)
        self.staff_id = staff_id

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id
    
    def get_staff_id(self):
        return self.staff_id