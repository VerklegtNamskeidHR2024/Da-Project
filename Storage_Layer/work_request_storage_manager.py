import json
from Model_Classes.work_request_model import WorkRequest

class work_reques_storage:
    work_reques_list = []

    def __init__(self):
        pass
    def add_work_request(self):
        pass
    def get_all_work_requests(self):
        with open('Data/work_request_storage.json', 'r') as work_request_file:
            work_request_data = json.load(work_request_file)
        work_request_list = [WorkRequest(**data) for data in work_request_data]
        return work_request_list
    def work_request_set_ID_and_add_to_storage():
        pass