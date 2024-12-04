import json
from Model_Classes.work_request_model import WorkRequest

class work_reques_storage:
    def __init__(self):
        pass

    def get_all_work_requests(self) -> list[WorkRequest]:
        with open('Data/work_request_storage.json', 'r') as work_request_file:
            work_request_data = json.load(work_request_file)
        work_request_list = [WorkRequest(**data) for data in work_request_data]
        return work_request_list
    
    def write_to_file_work_requests(self, list_of_work_requests: list[WorkRequest]):
        dict_of_work_requests = [work_request.to_dict() for work_request in list_of_work_requests]
        with open('Data/work_request_storage.json', 'w') as work_request_file:
            json.dump(dict_of_work_requests, work_request_file, indent=4)