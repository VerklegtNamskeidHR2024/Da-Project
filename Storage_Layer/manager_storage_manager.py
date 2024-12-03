import json
from Model_Classes.manager_model import Manager

class manager_storage():
    manager_list = []

    def __init__(self):
        pass
    def add_manager(self):
        pass
    def get_all_managers(self):
        with open('Data/manager_storage.json', 'r') as manager_file:
            manager_data = json.load(manager_file)
        manager_list = [Manager(**data) for data in manager_data]
        return manager_list
    def manager_set_ID_and_to_storage(self):
        pass