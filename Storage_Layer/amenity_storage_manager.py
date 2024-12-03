import json
from Model_Classes.amenity_model import Amenity

class amenity_storage:
    amenity_list = []
    def __init__(self):
        pass

    def get_all_amenities(self):
        with open('Data/amenity_storage.json', 'r') as amenity_file:
            amenity_data = json.load(amenity_file)
        amenity_list = [Amenity(**data) for data in amenity_data]
        return amenity_list