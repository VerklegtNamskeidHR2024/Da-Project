import json
from Model_Classes.contractor_model import Contractor

class contractor_storage:
    def __init__(self):
        pass

    def add_contractor(self):
        pass

    def get_all_contractor(self):
        pass
        temp_list = []
        with open('Data/contractor_storage.json', 'w') as file:
            temp_list = json.load(file)

    def get_contractor(self):
        pass

    def contractor_set_ID_and_add_to_storage(self):
        pass