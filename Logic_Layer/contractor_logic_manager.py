
class contractor_logic_manager:
    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def get_all_contractors(self) -> list:
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
        location_sorted_contractors = self.get_all_contractors_at_location(location)

        for contractor in location_sorted_contractors:
            if contractor.contractor_id == contractor_id:
                return contractor 
            
        return 
    
    def sanity_check_contractor(self, contractor, new):
        """check if all info in a contractor object is correct"""
        # needs to check phone number 
        #print(len(contractor.phone_number))
        if len(str(contractor.phone_number)) == 7:
            return True
        
        return False
    
    def add_new_contractor_to_storage(self, rank, location, contractor):
        print('Adding new contractor to storage')
        list_of_all_contractors = self.get_all_contractors()
        new_property_id = self.set_id_for_contractor()
        contractor.contractor_id = new_property_id
        list_of_all_contractors.append(contractor)
        self.Storage_Layer_Wrapper.write_to_file_contractor(list_of_all_contractors)
    
    def set_id_for_contractor(self):
        highestID = -1
        list_of_all_contractor = self.get_all_contractors()
        for contractor in list_of_all_contractor:
            stripped_ID = contractor.contractor_id[1:]
            if int(stripped_ID) > highestID:
                highestID = int(stripped_ID)
        highestID += 1

        new_property_id = 'C' + str(highestID)
        return new_property_id

    def write_to_file_checker(self, new_list):
        # needs to check if all the same ids are in the new list and the old one
        # then send the new list to storage
        return list
    # make sure list to write is ok
    
    def edit_existing_contractor_in_storage(self, contractor, location, edit_choice, new_value):
        list_of_contractors = self.get_all_contractors()
        for contr in list_of_contractors:
            if contr.contractor_id == contractor.contractor_id:
                if edit_choice == 'contact_name':
                    contr.set_contact_name(new_value)
                elif edit_choice == 'phone_number':
                    contr.set_phone_number(new_value)
                elif edit_choice == 'opening_hours':
                    contr.set_opening_hours(new_value)
        self.Storage_Layer_Wrapper.write_to_file_contractor(list_of_contractors)


    def get_contractor_work_requests(self, location, contractor_id) -> list:
        work_request_list = []
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:
            if work_request.contractor_id == contractor_id:
                work_request_list.append(work_request)
        return work_request_list
    
    def get_contractor_maintenance_reports(self, location, contractor_id):
        maintenance_report_list = []
        all_maintenance_reports = self.Storage_Layer_Wrapper.get_all_maintenance_report()
        for maintenance_report in all_maintenance_reports:
            if maintenance_report.contractor_id == contractor_id:
                maintenance_report_list.append(maintenance_report)
        return maintenance_report_list
