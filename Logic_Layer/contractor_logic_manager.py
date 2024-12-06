
class contractor_logic_manager:
    def __init__(self, Storage_Layer_Wrapper, location):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper
        self.location = location

    def get_all_contractors(self, location) -> list:
        contractor_lsit = []

        all_contractors = self.Storage_Layer_Wrapper.get_all_contractor()

        for contractor in all_contractors:
            contractor_lsit.append(contractor)

        return contractor_lsit

    def get_all_contractors_at_location(self, location) ->list:
        contractor_sorted_list = []

        all_contractors = self.Storage_Layer_Wrapper.get_all_contractor()

        for contractor in all_contractors:
            if contractor.location == location:
                contractor_sorted_list.append(contractor)

        return contractor_sorted_list
    
    def get_contractor_by_id(self, location, contractor_id) -> object:
        """Find a contracor by contractor_id"""
        
        # reuse get_all_contractors
        location_sorted_contractors = self.get_all_contractors(location)

        for contractor in location_sorted_contractors:
            if contractor.contractor_id == contractor_id:
                return contractor 
            
        return 
    
    def sanity_check_contractor(self, contractor):
        """check if all info in a contractor object is correct"""
        # needs to check phone number 
        if len(contractor.phone_number) != 9:
            return False
        
        return True
        # maybe make sure opening hours are real?
        # maybe add so names cant be longer than 30?
        # maybe make sure location is valid?
        return
    

    # this needs to be done 
    
    def add_new_contractor(self, contractor):
        if self.sanity_check_contractor(contractor) == True:
            
            all_contractors = self.Storage_Layer_Wrapper.get_all_contractor()
            all_contractors.append(contractor, all_contractors)
        return False
    
    def set_id_for_contractor(self, contractor, all_contractors):
        
        highest_id = 0
        for contractor in all_contractors:
            pass

    def write_to_file_checker(self, new_list):
        # needs to check if all the same ids are in the new list and the old one
        # then send the new list to storage
        return list
    # make sure list to write is ok
    

""" def __init__(self, contractor_id:str="", company_name:str="", contact_name:str="", 
                opening_hours:str="",phone_number:int=0,location:str="", previous_job_reports:list=[]):
        self.contractor_id = contractor_id
        self.company_name = company_name
        self.contact_name = contact_name
        self.opening_hours = opening_hours
        self.phone_number = phone_number
        self.location = location
        self.previous_job_reports = previous_job_reports """