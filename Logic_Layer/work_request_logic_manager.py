class work_request_logic_manager:

    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def sanity_check_work_request(Work_request):
        pass

    def add_work_request(Work_request):
        pass

    def edit_work_request(Work_request):
        pass

    def fetch_my_work_request(Employee_ID) -> list:
        pass

    def fetch_all_work_requests_in_storage(self, location) -> list:
        return self.Storage_Layer_Wrapper.get_all_work_requests()
    
    def fetch_all_open_work_requests_in_storage(self, Work_request_ID) -> list:
        pass

    def fetch_all_closed_work_requests_in_storage(Work_request_ID) -> list:
        pass

    def fetch_all_pending_work_requests_in_storage(Work_request_ID) -> list:
        pass

    def fetch_all_new_work_requests_in_storage(Work_request_ID) -> list:
        pass
 
