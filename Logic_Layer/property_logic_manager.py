# from storage_layer_wrapper import get_all_properties


class property_logic_manager:

    def __init__(self, Storage_Layer_Wrapper):
        """Constructor for property logic manager"""
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def sanity_check_properties(self, what_to_check, new_value) -> bool:
        """Sanity check for properties"""
        # Check if the new value is valid
        # checks if the name is longer than 3 characters
        if what_to_check == "name":
            if len(new_value) > 3:
                return True
            else:
                return False
        # checks if the location is in the list of locations
        elif what_to_check == 'property id':
            list_of_all_properties = self.Storage_Layer_Wrapper.get_all_properties()
            for property in list_of_all_properties:
                if property.property_id == new_value:
                    return True
            return False

        elif what_to_check == 'location':
            list_of_all_locations = self.Storage_Layer_Wrapper.get_all_locations()
            for location in list_of_all_locations:
                if location.location == new_value:
                    return True
            return False
        # checks if the condition is not empty
        elif what_to_check == "condition":
            if len(new_value) > 0:
                return True
            else:
                return False
        # checks if the price to fix is a float
        elif what_to_check == "price_to_fix":
            try:
                float(new_value)
                return True
            except ValueError:
                return False
        # checks if the price is a float
        elif what_to_check == "price":
            try:
                float(new_value)
                return True
            except ValueError:
                return False

        elif what_to_check == "description":
            if len(new_value) < 10:
                return False
            return True

    def get_all_properties(self) -> list:
        """Gets all properties"""
        property_list = []  # initialize an empty list to hold properties
        all_properties = (
            self.Storage_Layer_Wrapper.get_all_properties_at_location()
        )  # get all properties

        for property in all_properties:  # iterate through all properties
            property_list.append(
                property
            )  # append each property to the properties list
        return property_list  # return the list of properties

    def get_highest_ID(self, p_or_a: str):
        """Get the highest ID for a property"""
        highestID = -1  # initialize the highest ID to -1
        list_of_all_properties = self.get_all_properties()  # get all properties
        for property in list_of_all_properties:  # iterate through all properties
            stripped_ID = property.property_id[1:]  # get the ID without the P
            if (
                int(stripped_ID) > highestID
            ):  # check if the ID is higher than the highest ID
                highestID = int(stripped_ID)  # set the highest ID to the ID
        highestID += 1  # increment the highest ID by 1

        new_property_id = p_or_a + str(
            highestID
        )  # set the new ID to P + the highest ID
        return new_property_id

    def get_all_properties_at_location(self, location: str) -> list:
        """Gets all properties at specific location"""
        properties_sorted_list = []

        all_properties = self.Storage_Layer_Wrapper.get_all_properties_at_location()

        for property in all_properties:
            if property.location == location:
                properties_sorted_list.append(property)

        return properties_sorted_list

    def get_property_by_id(self, location, property_id) -> object:
        """Find a property by property_id"""
        property_list = self.get_all_properties_at_location(location)
        for property in property_list:
            if property.property_id == property_id:
                return property

    def add_new_property_to_storage(self, str_display: str, new_property: object):
        """Add a new property to the storage"""

        print(f"Adding New {str_display} To Storage")
        # checks if the property id is the highest id then appends to the property to the list of all properties
        if str_display == "Property":
            list_of_all_properties = self.get_all_properties()
            new_property_id = self.get_highest_ID("P")
            new_property.property_id = new_property_id
            list_of_all_properties.append(new_property)
            self.Storage_Layer_Wrapper.write_to_file_property(list_of_all_properties)

        if str_display == "Amenity":
            list_of_all_amenities = self.Storage_Layer_Wrapper.get_all_amenities()
            new_amenity_id = self.get_highest_ID("A")
            new_property.property_id = new_amenity_id
            list_of_all_amenities.append(new_property)
            self.Storage_Layer_Wrapper.write_to_file_amenities(list_of_all_amenities)

    def edit_existing_property_in_storage(
        self, property, location, edit_choice, new_value
    ):
        """Edit an existing property in the storage"""
        list_of_properties = self.get_all_properties()
        # checks if the property id is in the list of properties then edits the property
        for prop in list_of_properties:
            if prop.property_id == property.property_id:
                # checks if the edit choice is name, condition, price to fix or price
                if edit_choice == "name":
                    prop.set_name(new_value)
                elif edit_choice == "condition":
                    prop.set_condition(new_value)
                elif edit_choice == "price to fix":
                    prop.set_total_price_to_fix(new_value)
                elif edit_choice == "price":
                    prop.set_property_price(new_value)
        self.Storage_Layer_Wrapper.write_to_file_property(list_of_properties)

    def fetch_property_from_storage(self, property_ID):
        """property ID = input, if the property ID is in the property list it returns that property"""
        for prop in "get_all_properties":
            if property_ID in prop:
                return prop

    def get_property_work_requests(self, location, property_id) -> list:
        """Get all work requests for a property"""
        work_request_list = []
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        # checks if the property id is in the list of work requests then returns the work requests
        for work_request in all_work_requests:
            if work_request.property_id == property_id:
                work_request_list.append(work_request)
        return work_request_list

    def get_property_maintenance_reports(self, location, property_id):
        """Get all maintenance reports for a property"""
        maintenance_report_list = []
        all_maintenance_reports = (
            self.Storage_Layer_Wrapper.get_all_maintenance_reports()
        )
        # checks if the property id is in the list of maintenance reports then returns the maintenance reports
        for maintenance_report in all_maintenance_reports:
            if maintenance_report.property_id == property_id:
                maintenance_report_list.append(maintenance_report)
        return maintenance_report_list
