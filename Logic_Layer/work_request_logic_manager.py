class work_request_logic_manager:

    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def get_all_work_requests(self, location) -> list:
        work_request_list = []

        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()

        for work_request in all_work_requests:
            work_request_list.append(work_request)

        return work_request_list

    def sanity_check_work_request_id(self, work_request_id: str) -> bool:
        work_request_id_list = list(work_request_id)
        if (len(work_request_id_list) == 5 and work_request_id_list[0] == "W" and work_request_id_list[1] == "R") == True:
            return True
        else:
            return False  

    def sanity_check_new_work_request_property_id(self, property_id: str) -> bool:
        property_id_listed = list(property_id)
        if (len(property_id_listed) == 5 and property_id_listed[0] == "P") == True:
            return True
        else:
            return False 
    
    def sanity_check_repititive_work_requests(self, yes_or_no: str) -> bool:
        match yes_or_no:
            case "yes" | "Yes":
                return True
            case "no" | "No":
                return False
            case _:
                return 
    
    def set_new_work_request(self, rank, location, Work_request: object=None) -> str:
        highest_id = 0
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:
            stripped_id = work_request.work_request_id[2:]
            if int(stripped_id) > highest_id:
                highest_id = int(stripped_id)
        highest_id += 1
        new_work_request_id = "WR" + str(highest_id)
        Work_request_with_id = Work_request.set_work_request_id(new_work_request_id)
        return Work_request_with_id
            

    def add_work_request(self, rank, location, Work_request: object=None) -> bool:
        Work_request_with_id = self.set_new_work_request(Work_request)
        all_works_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        all_works_requests.append(Work_request_with_id)
        self.Storage_Layer_Wrapper.write_to_file_work_requests(all_works_requests) 
        return True


    def edit_work_request(self, Work_request: object) -> bool:
        pass

    def fetch_my_work_request(self, employee_id: str="") -> list:
        pass

    def fetch_work_request_by_id(self, rank, location, work_request_id) -> object:
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:
            if work_request.location == location and work_request.work_request_id == work_request_id:
                return work_request
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
 
