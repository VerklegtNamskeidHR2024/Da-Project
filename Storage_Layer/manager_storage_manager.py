import json
from Model_Classes.manager_model import Manager

class manager_storage():
    def __init__(self):
        pass

    def get_all_managers(self) -> list[Manager]:
        with open('Data/manager_storage.json', 'r') as manager_file:
            manager_data = json.load(manager_file)
        manager_list = [Manager(**data) for data in manager_data]
        return manager_list
    
    def write_to_file_managers(self, list_of_managers: list[Manager]):
        dict_of_managers = [manager.to_dict() for manager in list_of_managers]
        with open('Data/manager_storage.json', 'w') as manager_file:
            json.dump(dict_of_managers, manager_file, indent=4)