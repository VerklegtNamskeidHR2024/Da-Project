import json
from Model_Classes.location_model import Location

class location_storage:
    location_list = []

    def __init__(self):
        pass
    def add_location(self):
        pass
    def get_all_locations(self):
        with open('Data/location_storage.json', 'r') as location_file:
            location_data = json.load(location_file)
        location_list = [Location(**data) for data in location_data]
        return location_list
    def location_set_ID_and_add_to_storage(self):
        pass