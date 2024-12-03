import json
from Model_Classes.admin_model import Admin

class admin_storage:
    admin_list = []
    def __init__(self):
        pass
    def add_admin(self):
        pass
    def get_all_admin(self):
        with open('Data/admin_storage.json', 'r') as admin_file:
            admin_data = json.load(admin_file)
        admin_list = [Admin(**data) for data in admin_data]
        return admin_list
    def set_id_and_add_to_storage(self):
        pass