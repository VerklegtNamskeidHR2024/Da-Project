from Storage_Layer.work_request_storage_manager import work_reques_storage

class work_request_logic_manager:

    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def sanity_check_work_request(Work_request) -> bool:
        pass

    def add_work_request(Work_request) -> None:
        pass

    def edit_work_request(Work_request) -> None:
        pass

    def fetch_my_work_request(Employee_ID) -> list:
        pass

    def fetch_work_request_by_id(self, rank, location, work_request_id) -> object:
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()

        for work_request in all_work_requests:
            if work_request.location == location and work_request.work_request_id == work_request_id:
                return work_request
            else:
                return  
    
    def get_all_work_requests_at_location(self, rank, location) -> list:
            '''Gets all work requests at specific location'''
            work_request_sorted_list = []

            all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()

            for work_request in all_work_requests:
                if work_request.location == location:
                    work_request_sorted_list.append(work_request)
            
            return work_request_sorted_list 

    def fetch_all_open_work_requests_in_storage(self, Work_request_ID) -> list:
        pass

    def fetch_all_closed_work_requests_in_storage(Work_request_ID) -> list:
        pass

    def fetch_all_pending_work_requests_in_storage(Work_request_ID) -> list:
        pass

    def fetch_all_new_work_requests_in_storage(Work_request_ID) -> list:
        pass
 
