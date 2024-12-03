import json
from Model_Classes.house_model import House

class property_storage:
    property_list = []

    def __init__(self):
        pass
    def add_property(self):
        pass
    def get_all_properties(self):
        with open('Data/property_storage.json','r') as property_file:
            properties_data = json.load(property_file)
        properties_list = [House(**data) for data in properties_data]
        return properties_list
    def property_set_ID_and_add_to_storage(self):
        pass
    