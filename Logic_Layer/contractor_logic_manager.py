class contractor_logic_manager:
    def __init__(self, Storage_Layer_Wrapper):
        """Constructor for contractor logic manager"""
        # Initialize the contractor logic manager with a storage layer wrapper
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def get_all_contractors(self) -> list:
        """Get all contractors"""
        # Initialize an empty list to hold contractors
        contractor_list = []

        # Retrieve all contractors from the storage layer
        all_contractors = self.Storage_Layer_Wrapper.get_all_contractor()

        # Iterate through the list of all contractors and append each to the contractor list
        for contractor in all_contractors:
            contractor_list.append(contractor)

        # Return the list of contractors
        return contractor_list

    def get_all_contractors_at_location(self, location) ->list:
        """Get all contractors at a specific location"""
        contractor_sorted_list = []

        all_contractors = self.Storage_Layer_Wrapper.get_all_contractor()

        for contractor in all_contractors:
            if contractor.location == location:
                contractor_sorted_list.append(contractor)

        return contractor_sorted_list
    
    def get_contractor_by_id(self, location, contractor_id) -> object:
        """Find a contracor by contractor_id"""
        
        # Get all contractors at a specific location
        location_sorted_contractors = self.get_all_contractors_at_location(location)
        # Iterate through the list of contractors and return the contractor with the matching contractor_id
        for contractor in location_sorted_contractors:
            if contractor.contractor_id == contractor_id:
                return contractor 
            
        return 
    
    def sanity_check_contractor(self, contractor):
        """check if all info in a contractor object is correct"""
        # needs to check phone number 
        #print(len(contractor.phone_number))
        if len(str(contractor.phone_number)) != 7:
            return False
        
        return True
    
    def add_new_contractor_to_storage(self, rank, location, contractor):
        """Add a new contractor to the storage"""
        print('Adding new contractor to storage')
        list_of_all_contractors = self.get_all_contractors() # get all contractors
        new_property_id = self.set_id_for_contractor() # get a new id for the contractor
        contractor.contractor_id = new_property_id # set the new id to the contractor
        list_of_all_contractors.append(contractor) # append the contractor to the list of all contractors
        self.Storage_Layer_Wrapper.write_to_file_contractor(list_of_all_contractors) # write the list of all contractors to the storage
    
    def set_id_for_contractor(self):
        """Set a new id for a contractor"""
        highestID = -1 # initialize the highest id to -1
        list_of_all_contractor = self.get_all_contractors()
        for contractor in list_of_all_contractor: # iterate through all contractors
            stripped_ID = contractor.contractor_id[1:] # get the id of the contractor
            if int(stripped_ID) > highestID: # checks if the id is higher than the highest id
                highestID = int(stripped_ID) # set the highest id to the id
        highestID += 1 # increment the highest id by 1

        new_property_id = 'C' + str(highestID) # set the new id to the highest id
        return new_property_id  # return the new id

    def write_to_file_checker(self, new_list: list) -> list:
        # needs to check if all the same ids are in the new list and the old one
        # then send the new list to storage
        return new_list
    # make sure list to write is ok
    
    def edit_existing_contractor_in_storage(self, contractor, location, edit_choice, new_value):
        """Edit an existing contractor in the storage"""
        list_of_contractors = self.get_all_contractors()
        for contr in list_of_contractors: 
            if contr.contractor_id == contractor.contractor_id:  # checks if the contractor id is the same as the contractor id in the list of contractors
                # checks if the choice is equal to the contractor name,phone number or opening hours
                if edit_choice == 'contact_name':
                    contr.set_contact_name(new_value)
                elif edit_choice == 'phone_number':
                    contr.set_phone_number(new_value)
                elif edit_choice == 'opening_hours':
                    contr.set_opening_hours(new_value)
        self.Storage_Layer_Wrapper.write_to_file_contractor(list_of_contractors) # write the list of all contractors to the storage


    def get_contractor_work_requests(self, location, contractor_id) -> list: 
        """Get all work requests for a contractor"""
        work_request_list = []
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests() 
        for work_request in all_work_requests:  # iterate through all work requests	
            if work_request.contractor_id == contractor_id:  # checks if the contractor id is the same as the contractor id in the work request
                work_request_list.append(work_request) # append the work request to the work request list
        return work_request_list 
    
    def get_contractor_maintenance_reports(self, location, contractor_id):
        """Get all maintenance reports for a contractor"""
        maintenance_report_list = [] 
        all_maintenance_reports = self.Storage_Layer_Wrapper.get_all_maintenance_reports() 
        for maintenance_report in all_maintenance_reports: # iterate through all maintenance reports
            if maintenance_report.contractor_id == contractor_id:
                maintenance_report_list.append(maintenance_report)
        return maintenance_report_list  # return the maintenance report list if the contractor id is the same as the contractor id in the maintenance report
