import json
from Model_Classes.house_model import House

class property_storage:
    def __init__(self):
        """Constructor for property_storage"""
        pass

    def get_all_properties(self) -> list[House]:
        """Gets all properties from the file"""
        with open('Data/property_storage.json', 'r') as property_file:
            properties_data = json.load(property_file)
        properties_list = [House(**data) for data in properties_data]
        return properties_list

    def write_to_file_property(self, list_of_properties: list[House]):
        """Writes the list of properties to the file"""
        # Read the current data from the file
        with open('Data/property_storage.json', 'r') as property_file:
            current_data = json.load(property_file)
        
        # Write the current data to a temp file
        with open('Data/property_storage_temp.json', 'w') as temp_file:
            json.dump(current_data, temp_file, indent=4)
        
        # Write the new data to the original file
        dict_of_properties = [property.to_dict() for property in list_of_properties]
        with open('Data/property_storage.json', 'w') as property_file:
            json.dump(dict_of_properties, property_file, indent=4)