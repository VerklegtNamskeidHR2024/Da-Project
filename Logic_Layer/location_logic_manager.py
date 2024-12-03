class location_logic_manager:

    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def fetch_all_locations_in_storage(self, Location) -> list:
        return self.Storage_Layer_Wrapper.get_all_locations()

    def fetch_all_amenities_for_location_in_storage(self, location) -> list:
        pass

    def sanity_check_location(self, Location):
        pass

    def add_new_location_to_storage(self, Location):
        pass
    
    def fetch_location_from_storage(self, Location_ID):
        pass

