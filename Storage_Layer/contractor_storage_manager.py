import json
from Model_Classes.contractor_model import Contractor

class contractor_storage:
    def __init__(self):
        """Constructor for contractor_storage"""
        pass

    def get_all_contractor(self) -> list[Contractor]:
        """Gets all contractors from the file"""
        # Here we are reading the data from the file and creating a list of contractors objects
        # And returning the list so that contractors can be used in the other layers
        with open('Data/contractor_storage.json', 'r') as contractor_file:
            contractors_data = json.load(contractor_file)
        contractors_list = [Contractor(**data) for data in contractors_data]
        return contractors_list

    def write_to_file_contractor(self, list_of_contractors: list[Contractor]):
        """Writes the list of contractors to the file"""
        # Read the current data from the file
        # this to get the data from the file so that it can be write to a temp file
        with open('Data/contractor_storage.json', 'r') as contractor_file:
            current_data = json.load(contractor_file)
        # Write the current data to a temp file
        # This is done to prevent data loss in case of an error
        with open('Data/contractor_storage_temp.json', 'w') as temp_file:
            json.dump(current_data, temp_file, indent=4)
        # Write the new data to the original fil
        # This is done to update the data in the file
        dict_of_contractors = [contractor.to_dict() for contractor in list_of_contractors]
        with open('Data/contractor_storage.json', 'w') as contractor_file:
            json.dump(dict_of_contractors, contractor_file, indent=4)