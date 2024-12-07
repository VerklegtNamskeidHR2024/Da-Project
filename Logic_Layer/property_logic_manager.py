#from storage_layer_wrapper import get_all_properties

class property_logic_manager:

    def __init__(self, Storage_Layer_Wrapper, location):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper
        self.location = location

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
    
    def sanity_check_properties(property):
        pass

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
            
        return #error message property ID is not in the system 
    def fetch_all_work_request_in_storage(work_request_ID):
        pass

    def fetch_all_maintenance_reports_in_storage(maintenance_report_ID) -> list:
        pass

    def fetch_all_employees_in_storage(employee_ID) -> list:
        pass

    def fetch_all_contractors_in_stoarge(contractor_ID) -> list:
        pass
