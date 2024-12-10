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
        """Get all locations"""
        location_sorted_list = []

        all_locations = self.Storage_Layer_Wrapper.get_all_locations()

        for location in all_locations:
            if location.location == location:
                location_sorted_list.append(location)

        return location_sorted_list

    def fetch_all_amenities_for_location_in_storage(self, location) -> list:
        pass

    def sanity_check_location(self, Location): 
        pass

    def add_new_location_to_storage(self, Location):
        pass
    
    def fetch_location_from_storage(self, Location_ID):
        pass

