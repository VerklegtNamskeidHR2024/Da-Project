import json
from Model_Classes.work_request_model import WorkRequest

class work_reques_storage:
    """Class for work_reques_storage"""
    def __init__(self):
        """Constructor for work_reques_storage"""
        pass

    def get_all_work_requests(self) -> list[WorkRequest]:
        """Gets all work requests from the file and stores each instance of the class in a list that is 
        returned back to the storage wrapper. """
        # Here we are reading the data from the file and creating a list of Managers objects
        # And returning the list so that Maintenance Report can be used in the other layers
        with open('Data/work_request_storage.json', 'r') as work_request_file:
            work_request_data = json.load(work_request_file)
        work_request_list = [WorkRequest(**data) for data in work_request_data]
        return work_request_list

    def write_to_file_work_requests(self, list_of_work_requests: list[WorkRequest]):
        """Writes the list of work requests to the file"""
        # Read the current data from the file
        # this to get the data from the file so that it can be write to a temp file
        with open('Data/work_request_storage.json', 'r') as work_request_file:
            current_data = json.load(work_request_file)
        
        # Write the current data to a temp file
        # This is done to prevent data loss in case of an error
        with open('Data/work_request_storage_temp.json', 'w') as temp_file:
            json.dump(current_data, temp_file, indent=4)
        
        # Write the new data to the original fil
        # This is done to update the data in the file
        dict_of_work_requests = [work_request.to_dict() for work_request in list_of_work_requests]
        with open('Data/work_request_storage.json', 'w') as work_request_file:
            json.dump(dict_of_work_requests, work_request_file, indent=4)