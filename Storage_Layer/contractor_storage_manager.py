import json
from Model_Classes.contractor_model import Contractor

class contractor_storage:
    contractors_list = []

    def __init__(self):
        pass
    def add_contractor(self):
        pass

    def get_all_contractor():
        with open('Data/contractor_storage.json', 'r') as file:
            contractors_data = json.load(file)
        contractors_list = [Contractor(**data) for data in contractors_data]
        return contractors_list
    
    def get_contractor(self):
        pass

    def contractor_set_ID_and_add_to_storage(self):
        pass