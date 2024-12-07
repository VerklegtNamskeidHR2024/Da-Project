#from storage_layer_wrapper import get_all_properties

class property_logic_manager:

    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def sanity_check_properties(property):
        pass

    def get_all_properties(self) -> list:
        property_list = []

        all_properties = self.Storage_Layer_Wrapper.get_all_properties_at_location()

        for property in all_properties:
            property_list.append(property)

        return property_list  
    def get_highest_ID(self, location):
        highestID = -1
        list_of_all_properties = self.get_all_properties(location)
        for property in list_of_all_properties:
            stripped_ID = property.property_id[2:]
            if int(stripped_ID) > highestID:
                highestID = int(stripped_ID)
        highestID += 1

        new_property_id = 'P' + str(highestID)
        return new_property_id

    def get_all_properties_at_location(self, location) -> list:
        '''Gets all properties at specific location'''
        properties_sorted_list = []

        all_properties = self.Storage_Layer_Wrapper.get_all_properties_at_location()

        for property in all_properties:
            if property.location == location:
                properties_sorted_list.append(property)

        return properties_sorted_list
    
    def get_property_by_id(self, location, property_id) -> object:
        property_list = self.get_all_properties_at_location(location)
        for property in property_list:
            if property.property_id == property_id:
                return property

    def add_new_property_to_storage(self, rank, location, property):
        highestID = -1
        list_of_all_properties = self.get_all_properties_at_location(location)
        for property in list_of_all_properties:
            stripped_ID = property.property_id[2:]
            if int(stripped_ID) > highestID:
                highestID = int(stripped_ID)

    def edit_existing_property_in_storage(property):
        pass

    def fetch_property_from_storage(self, property_ID):
        '''property ID = input, if the property ID is in the property list it returns that property'''
        for prop in "get_all_properties":
            if property_ID in prop:
                return prop
            
    def get_property_work_requests(self, location, property_id) -> list:
        work_request_list = []
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:
            if work_request.property_id == property_id:
                work_request_list.append(work_request)
        return work_request_list
    
    def get_property_maintenance_reports(self, location, property_id):
        maintenance_report_list = []
        all_maintenance_reports = self.Storage_Layer_Wrapper.get_all_maintenance_report()
        for maintenance_report in all_maintenance_reports:
            if maintenance_report.property_id == property_id:
                maintenance_report_list.append(maintenance_report)
        return maintenance_report_list

    def fetch_all_work_request_in_storage(work_request_ID):
        pass

    def fetch_all_maintenance_reports_in_storage(maintenance_report_ID) -> list:
        pass

    def fetch_all_employees_in_storage(employee_ID) -> list:
        pass

    def fetch_all_contractors_in_stoarge(contractor_ID) -> list:
        pass
