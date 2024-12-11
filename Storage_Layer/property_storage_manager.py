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
        dict_of_properties = [property.to_dict() for property in list_of_properties]
        with open('Data/property_storage.json', 'w') as property_file:
            json.dump(dict_of_properties, property_file, indent=4)

# virkar held eg ekki utaf hvering þu ert með property data stored, dæmi
        # held það veit ekki hvað það a að gera utaf það er Reykjavik svo property
        # ætla breyta þvi i json en er með copy a discord dw dw hremmi baby
        """ "Reykjavik": [
        {
            "property_id": "h001",
            "name": "suite",
            "location": "Reykjavik",
            "condition": "excellent",
            "total_price_to_fix": 1500.0,
            "property_price": 30230000000
        },
        {
            "property_id": "h002",
            "name": "suite",
            "location": "Reykjavik",
            "condition": "fair",
            "total_price_to_fix": 1200.0,
            "property_price": 300000000
        }, """