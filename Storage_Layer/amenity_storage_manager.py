import json
from Model_Classes.amenity_model import Amenity

class amenity_storage:
    def __init__(self):
        """Constructor for amenity_storage"""
        pass

    def get_all_amenities(self) -> list[Amenity]:
        """Gets all amenities from the file"""
        # Here we are reading the data from the file and creating a list of Amenity objects
        # And returning the list so that amenities can be used in the other layers
        with open('Data/amenity_storage.json', 'r') as amenity_file:
            amenity_data = json.load(amenity_file)
        amenity_list = [Amenity(**data) for data in amenity_data]
        return amenity_list


    def write_to_file_amenities(self, list_of_amenities: list[Amenity]):
        """Writes the list of amenities to the file"""
        # Read the current data from the file
        # this to get the data from the file so that it can be write to a temp file
        with open('Data/amenity_storage.json', 'r') as amenity_file:
            current_data = json.load(amenity_file)

        # Write the current data to a temp file
        # This is done to prevent data loss in case of an error
        with open('Data/amenity_storage_temp.json', 'w') as temp_file:
            json.dump(current_data, temp_file, indent=4)

        # Write the new data to the original fil
        # This is done to update the data in the file
        dict_of_amenities = [amenity.to_dict() for amenity in list_of_amenities]
        with open('Data/amenity_storage.json', 'w') as amenity_file:
            json.dump(dict_of_amenities, amenity_file, indent=4)