import json
from Model_Classes.admin_model import Admin

class admin_storage:
    def __init__(self):
        """Constructor for admin_storage"""
        pass

    def get_all_admins(self) -> list[Admin]:
        """Gets all admins from the file"""
        # Here we open the file and read the data
        with open('Data/admin_storage.json', 'r') as admin_file:
            admin_data = json.load(admin_file)
        # Then we make a list of admin objects from the data
        admin_list = [Admin(**data) for data in admin_data]
        # Finally we return the list
        return admin_list

    def write_to_file_admin(self, list_of_admins: list[Admin]):
        """Writes the list of admins to the file"""
        # Read the current data from the file
        with open('Data/admin_storage.json', 'r') as admin_file:
            current_data = json.load(admin_file)
        
        # Write the current data to a temp file
        with open('Data/admin_storage_temp.json', 'w') as temp_file:
            json.dump(current_data, temp_file, indent=4)
        
        # Write the new data to the original file
        dict_of_admins = [admin.to_dict() for admin in list_of_admins]
        with open('Data/admin_storage.json', 'w') as admin_file:
            json.dump(dict_of_admins, admin_file, indent=4)