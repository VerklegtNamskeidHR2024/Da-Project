import json
from Model_Classes.location_model import Location


class location_storage:
    def __init__(self):
        """Constructor for location_storage"""
        pass
    
    def get_all_locations(self) -> list[Location]:
        """Gets all locations from the file"""
        # Here we are reading the data from the file and creating a list of Locations objects
        # And returning the list so that Contractors can be used in the other layers
        with open('Data/location_storage.json', 'r') as location_file:
            location_data = json.load(location_file)
        location_list = [Location(**data) for data in location_data]
        return location_list
    
    def write_to_file_location(self, list_of_locations: list[Location]):
        """Writes the list of locations to the file"""
        # Read the current data from the file
        # this to get the data from the file so that it can be write to a temp file
        with open('Data/location_storage.json', 'r') as location_file:
            current_data = json.load(location_file)
        # Write the current data to a temp file
        # This is done to prevent data loss in case of an error
        with open('Data/location_storage_temp.json', 'w') as temp_file:
            json.dump(current_data, temp_file, indent=4)
        # Write the new data to the original fil
        # This is done to update the data in the file
        dict_of_locations = [location.to_dict() for location in list_of_locations]
        with open('Data/location_storage.json', 'w') as location_file:
            json.dump(dict_of_locations, location_file, indent=4)

    