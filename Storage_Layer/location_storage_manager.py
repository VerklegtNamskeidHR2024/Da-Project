import json
from Model_Classes.location_model import Location


class location_storage:
    def __init__(self):
        """Constructor for location_storage"""
        pass
    
    def get_all_locations(self) -> list[Location]:
        """Gets all locations from the file"""
        with open('Data/location_storage.json', 'r') as location_file:
            location_data = json.load(location_file)
        location_list = [Location(**data) for data in location_data]
        return location_list
    
    def write_to_file_location(self, list_of_locations: list[Location]):
        """Writes the list of locations to the file"""
        dict_of_locations = [location.to_dict() for location in list_of_locations]
        with open('Data/location_storage.json', 'w') as location_file:
            json.dump(dict_of_locations, location_file, indent=4)