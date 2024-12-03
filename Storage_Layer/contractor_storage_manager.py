import json
from Model_Classes.contractor_model import Contractor

class contractor_storage:
    def __init__(self):
        self.contractors_list = []

    def add_contractor(self):
        pass

    def get_all_contractor(self):
        with open('Data/contractors.json', 'r') as file:
            self.contractors_list = json.load(file)
            

    def get_contractor(self):
        pass

    def contractor_set_ID_and_add_to_storage(self):
        pass