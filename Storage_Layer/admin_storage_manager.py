import json
from Model_Classes.admin_model import Admin

class admin_storage:
    def __init__(self):
        pass

    def get_all_admin(self) -> list[Admin]:
        with open('Data/admin_storage.json', 'r') as admin_file:
            admin_data = json.load(admin_file)
        admin_list = [Admin(**data) for data in admin_data]
        return admin_list
    
    def write_to_file_admin(self, list_of_admins: list[Admin]):
        dict_of_admins = [admin.to_dict() for admin in list_of_admins]
        with open('Data/admin_storage.json', 'w') as admin_file:
            json.dump(dict_of_admins, admin_file, indent=4)