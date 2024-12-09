import json
from Model_Classes.amenity_model import Amenity

class amenity_storage:
    def __init__(self):
        """Constructor for amenity_storage"""
        pass

    def get_all_amenities(self) -> list[Amenity]:
        """Gets all amenities from the file"""
        with open('Data/amenity_storage.json', 'r') as amenity_file:
            amenity_data = json.load(amenity_file)
        amenity_list = [Amenity(**data) for data in amenity_data]
        return amenity_list

    #Bua til eitt append og eitt edit fall sem kallar a get all og svo write to file og að write to file er ekki i logic layar!

    def write_to_file_amenities(self, list_of_amenities: list[Amenity]):
        """Writes the list of amenities to the file"""

        with open('Data/amenity_storage.json', 'r') as amenity_file:
            current_data = json.load(amenity_file)

        with open('Data/amenity_storage_temp.json', 'w') as temp_file:
            json.dump(current_data, temp_file, indent=4)

        dict_of_amenities = [amenity.to_dict() for amenity in list_of_amenities]
        with open('Data/amenity_storage.json', 'w') as amenity_file:
            json.dump(dict_of_amenities, amenity_file, indent=4)