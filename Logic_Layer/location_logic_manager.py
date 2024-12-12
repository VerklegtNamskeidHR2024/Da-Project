class location_logic_manager:

    def __init__(self, Storage_Layer_Wrapper):
        """Constructor for location logic manager"""
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def all_location(self) -> list:
        """Get all locations"""
        locations_list = [] # initialize an empty list to hold locations

        all_locations = self.Storage_Layer_Wrapper.get_all_locations() # get all locations

        for location in all_locations:  # iterate through all locations
            locations_list.append(location)    # append each location to the locations list

        return locations_list

    
    def get_all_locations(self, Location) -> list:
        """Get all locations based on location"""
        location_sorted_list = []

        all_locations = self.Storage_Layer_Wrapper.get_all_locations()
        # checks if the location is in the list of locations then returns the locations
        for location in all_locations:
            if location.location == location:
                location_sorted_list.append(location)

        return location_sorted_list

    def edit_existing_location_in_storage(self, location, current_location, edit_choice, new_value):
        """Edit an existing location in the storage"""
        list_of_locations = self.all_location()
        # Iterate through the list of locations and edit the location with the matching location ID
        for location_obj in list_of_locations:
            if location_obj.location == location.location:
                if edit_choice == 'phone_number':
                    location_obj.set_phone_number(new_value)
                elif edit_choice == 'amenity':
                    pass
                    #location_obj.set_opening_hours(new_value)
                elif edit_choice == 'opening_hours':
                    location_obj.set_opening_hours(new_value)

        self.Storage_Layer_Wrapper.write_to_file_locations(list_of_locations)


    def sanity_check_location(self, what_to_check, new_value) -> bool:
        """Check if all info in a location object is correct"""
        # checks if the phone number is 7 digits
        # so it does not let the user input a phone number that is not 7 digits
        if what_to_check == 'phone_number':
            if len(new_value) == 7:
                return True
            else:
                return False
        # is just here to return true if the what_to_check is opening_hours
        # since there is nothing to check in opening hours
        if what_to_check == "opening_hours":
            if len(new_value) <= 5 and len(new_value) >= 3 and "-" in new_value:
                try:
                    new_value = new_value.split("-")
                    int(new_value[0])
                    int(new_value[1])
                    return True
                except ValueError:
                    return False
            else:
                return False
        
    def edit_amenity(self ,amenity_in, new_condition) -> bool:
        """Edit an amenity"""
        # gets all amenities in list so we can edit the amenity 
        # and then write the list of amenities to the storage
        amenities = self.Storage_Layer_Wrapper.get_all_amenities()
        # iterate through the list of amenities and edit the amenity with the matching property_id
        for amenity in amenities:
            if amenity.property_id == amenity_in.property_id:
                # sets the new condition to the amenity
                amenity.set_condition(new_condition)
                # writes the list of amenities to the storage with the new condition
                self.Storage_Layer_Wrapper.write_to_file_amenities(amenities)
                return True
        return False
        
    def fetch_amenity_by_id(self, amenity_ID, location) -> object:
        """Fetch an amenity by ID"""
        # gets all amenities in list so we can fetch the amenity by ID
        amenities = self.Storage_Layer_Wrapper.get_all_amenities()
        # iterate through the list of amenities and return the amenity with the matching property_id
        for amenity in amenities:
            if amenity.property_id == amenity_ID and amenity.location == location:
                return amenity

    def fetch_all_amenities_for_location_in_storage(self, location) -> list:
        """Fetch all amenities for a location"""
        # gets all amenities in list so we can fetch all amenities for a location
        amenities = self.Storage_Layer_Wrapper.get_all_amenities()
        # create a list we can append the amenities with the matching location to
        amenities_list = []
        for amenity in amenities:
            if amenity.location == location:
                amenities_list.append(amenity)
        return amenities_list

