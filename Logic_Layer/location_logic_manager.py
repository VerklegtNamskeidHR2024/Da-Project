class location_logic_manager:

    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def all_location(self) -> list:
        locations_list = []

        all_locations = self.Storage_Layer_Wrapper.get_all_locations()

        for location in all_locations:
            locations_list.append(location)

        return locations_list

    
    def get_all_locations(self) -> list:
        location_sorted_list = []

        all_locations = self.Storage_Layer_Wrapper.get_all_locations()

        for location in all_locations:
            if location.location == location:
                location_sorted_list.append(location)

        return location_sorted_list

    def edit_existing_location_in_storage(self, location, current_location, edit_choice, new_value):
        list_of_locations = self.all_location()
        for location_obj in list_of_locations:
            if location_obj.location == location.location:
                if edit_choice == 'phone_number':
                    location_obj.set_phone_number(new_value)
                elif edit_choice == 'manager':
                    location_obj.set_branch_manager(new_value)
                elif edit_choice == 'amenity':
                    pass
                    #location_obj.set_opening_hours(new_value)
                elif edit_choice == 'opening_hours':
                    location_obj.set_opening_hours(new_value)

        self.Storage_Layer_Wrapper.write_to_file_locations(list_of_locations)



    def sanity_check_location(self, what_to_check, new_value):
        if what_to_check == 'phone_number':
            if len(new_value) == 7:
                return True
            else:
                return False
        if what_to_check == 'manager':
            # needs to check that a manager with that id does not have a location under him
            return False
            if len(new_value) == 7:
                return True
            else:
                return False
        if what_to_check == "opening_hours":
            return True
        

    def fetch_all_amenities_for_location_in_storage(self, location) -> list:
        pass


    def add_new_location_to_storage(self, Location):
        pass
    
    def fetch_location_from_storage(self, Location_ID):
        pass

