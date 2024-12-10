import json
from Model_Classes.contractor_model import Contractor

class contractor_storage:
    def __init__(self):
        """Constructor for contractor_storage"""
        pass

    def get_all_contractor(self) -> list[Contractor]:
        """Gets all contractors from the file"""
        with open('Data/contractor_storage.json', 'r') as contractor_file:
            contractors_data = json.load(contractor_file)
        contractors_list = [Contractor(**data) for data in contractors_data]
        return contractors_list

    def write_to_file_contractor(self, list_of_contractors: list[Contractor]):
        """Writes the list of contractors to the file"""
        #print('we writing')
        dict_of_contractors = [contractor.to_dict() for contractor in list_of_contractors]
        with open('Data/contractor_storage.json', 'w') as contractor_file:
            json.dump(dict_of_contractors, contractor_file, indent=4)