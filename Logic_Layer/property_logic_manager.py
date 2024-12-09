#from storage_layer_wrapper import get_all_properties

class property_logic_manager:

    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def sanity_check_properties(self, what_to_check, new_value) -> bool:
        if what_to_check == 'name':
            if len(new_value) > 3:
                return True
            else:
                return False
        elif what_to_check == 'location':
            list_of_all_locations = self.Storage_Layer_Wrapper.get_all_locations()
            for location in list_of_all_locations:
                if location.location == new_value:
                    return True
            return False
        elif what_to_check == 'condition':
            if len(new_value) > 0:
                return True
            else:
                return False
        elif what_to_check == 'price_to_fix':
            try:
                float(new_value)
                return True
            except ValueError:
                return False
        elif what_to_check == 'price':
            try:
                float(new_value)
                return True
            except ValueError:
                return False

    def get_all_properties(self) -> list:
        property_list = []
        all_properties = self.Storage_Layer_Wrapper.get_all_properties_at_location()

        for property in all_properties:
            property_list.append(property)
        return property_list 
     
    def get_highest_ID(self, location):
        highestID = -1
        list_of_all_properties = self.get_all_properties()
        for property in list_of_all_properties:
            stripped_ID = property.property_id[1:]
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
        print('Adding new property to storage')
        list_of_all_properties = self.get_all_properties()
        new_property_id = self.get_highest_ID(location)
        property.property_id = new_property_id
        list_of_all_properties.append(property)
        self.Storage_Layer_Wrapper.write_to_file_property(list_of_all_properties)
        
    def edit_existing_property_in_storage(self, property, location, edit_choice, new_value):
        list_of_properties = self.get_all_properties()
        for prop in list_of_properties:
            if prop.property_id == property.property_id:
                if edit_choice == 'name':
                    prop.set_name(new_value)
                elif edit_choice == 'condition':
                    prop.set_condition(new_value)
                elif edit_choice == 'price to fix':
                    prop.set_total_price_to_fix(new_value)
                elif edit_choice == 'price':
                    prop.set_property_price(new_value)
        self.Storage_Layer_Wrapper.write_to_file_property(list_of_properties)

    def get_property_by_id(self, location, property_id) -> object:
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
