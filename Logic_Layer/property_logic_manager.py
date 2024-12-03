#from storage_layer_wrapper import get_all_properties

class property_logic_manager:
    def __init__(self, property, property_ID, work_request_ID, maintenance_report_ID, employee_ID, contractor_ID):
        self.property = property
        self.property_ID = property_ID
        

    def fetch_all_properties_in_storage(self, property_ID) -> list:
        '''Returns the property list'''
        return "get_all_properties"
    def sanity_check_properties(property):
        pass
    def add_new_property_to_storage(property): 
        pass
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