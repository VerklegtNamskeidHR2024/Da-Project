class work_request_logic_manager:

    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def sanity_check_new_work_request_property_id(self, property_id: str) -> bool: 
        """Gets all properties from storage and compares the property ID given by the user and compares it
        to the ones that already exist. """

        all_properties = self.Storage_Layer_Wrapper.get_all_properties_at_location()
        for property in all_properties:
            if property.property_id == property_id:
                return True    
        return False 
    
                
    def sanity_check_boolean_input_work_requests(self, yes_or_no: str) -> bool:
        """Takes the input given by the user and returns True or False based on if the user had entered spefically 
        yes/Yes or no/No. Otherwise it returns None. """

        match yes_or_no:
            case "yes" | "Yes":
                return True
            case "no" | "No":
                return False
            case _:
                return 
            
    def sanity_check_priority_for_request(self, priority: str) -> bool:
        """Takes the input given by the user and returns True if the user had entered spefically low/Low, medium/Medium
        or high/High. Otherwise it returns False. """

        match priority:
            case "high" | "High":
                return True
            case "medium" | "Medium":
                return True
            case "low" | "Low":
                return True
            case _ :
                return False
            
    def sanity_check_location_for_request(self, set_location: str) -> bool:
        """Gets all locations from storage and compares the names input given by the user to the  that already exist. """

        all_locations = self.Storage_Layer_Wrapper.get_all_locations()
        for location in all_locations:
            if location.name == set_location:
                return True
        return False
    
    # def sanity_check_edit_employee_id_request(self, staff_id: str) -> bool:
    
    # def sanity_check_edit_request_status(self, status: str) -> bool:

    def set_new_work_request_id(self, Work_request: object) -> str:
        highest_id = 0
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:
            stripped_id = work_request.work_request_id[2:]
            if int(stripped_id) > highest_id:
                highest_id = int(stripped_id)
        highest_id += 1
        new_work_request_id = "WR" + str(highest_id)
        Work_request.set_work_request_id(new_work_request_id)
        return Work_request
            

    def add_work_request(self, Work_request: object) -> bool:
        Work_request_with_id = self.set_new_work_request_id(Work_request)
        all_works_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        all_works_requests.append(Work_request_with_id)
        self.Storage_Layer_Wrapper.write_to_file_work_requests(all_works_requests) 
        return 


    def edit_work_request(self, Work_request: object) -> bool:
        pass

    def get_work_request_by_id(self, rank: str, location: str, work_request_id: str, status: str, is_accepted: bool) -> object:
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:
            if (work_request.location == location and work_request.work_request_id == work_request_id 
            and work_request.work_request_status == status and work_request.accepted_by_employee == is_accepted):
                return work_request
        return 

    def get_all_work_requests_at_location(self, rank: str, location: str, status: str, is_accepted: bool) -> list:
            """Gets all work requests at specific location. """
            work_request_sorted_list = []

            all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()

            for work_request in all_work_requests:
                if (work_request.location == location and work_request.work_request_status == status 
                    and work_request.accepted_by_employee == is_accepted):
                    work_request_sorted_list.append(work_request)
            
            return work_request_sorted_list 
        
    def get_my_work_request(self, rank: str, location: str, status: str, is_accepted: bool) -> list:
        work_request_sorted_list = []

        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()

        for work_request in all_work_requests:
            if (work_request.location == location and work_request.work_request_status == status 
                and work_request.accepted_by_employee == is_accepted):
                work_request_sorted_list.append(work_request)
        
        return work_request_sorted_list

    def get_all_closed_work_requests_in_storage(self, rank: str, location: str, status: str, is_accepted: bool) -> list:
        work_request_sorted_list = []

        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()

        for work_request in all_work_requests:
            if (work_request.location == location and work_request.work_request_status == status 
                and work_request.accepted_by_employee == is_accepted):
                work_request_sorted_list.append(work_request)
        
        return work_request_sorted_list

    def get_all_pending_work_requests_in_storage(self, rank: str, location: str, status: str, is_accepted: bool) -> list:
        work_request_sorted_list = []

        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()

        for work_request in all_work_requests:
            if (work_request.location == location and work_request.work_request_status == status 
                and work_request.accepted_by_employee == is_accepted):
                work_request_sorted_list.append(work_request)
        
        return work_request_sorted_list

    def get_all_new_work_requests_in_storage(self, rank: str, location: str, status: str, is_accepted: bool) -> list:
        work_request_sorted_list = []

        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()

        for work_request in all_work_requests:
            if (work_request.location == location and work_request.work_request_status == status 
                and work_request.accepted_by_employee == is_accepted):
                work_request_sorted_list.append(work_request)
        
        return work_request_sorted_list
 
