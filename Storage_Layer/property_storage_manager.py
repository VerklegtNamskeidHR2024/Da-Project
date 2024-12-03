import json
from Model_Classes.house_model import House

class property_storage:
    property_list = []

    def __init__(self):
        pass
    def add_property(self):
        pass
    def get_all_properties(self):
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

        with open('Data/property_storage.json','r') as property_file:
            properties_data = json.load(property_file)
        properties_list = [House(**data) for data in properties_data]
        return properties_list
    
    def property_set_ID_and_add_to_storage(self):
        pass
    