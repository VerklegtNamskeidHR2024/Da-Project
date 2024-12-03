
class contractor_logic_manager:
    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def get_all_contractors(self, location):
        location_sorted_list = []

        all_contractors = self.Storage_Layer_Wrapper.get_all_contractor()

        for contractor in all_contractors:
            if contractor.location == location:
                location_sorted_list.append(contractor)

        return location_sorted_list
    
    def get_contractor_by_id(self, location, contractor_id) -> object:
        """Find a contracor by contractor_id"""
        
        # reuse get_all_contractors
        location_sorted_contractors = self.get_all_contractors(location)

        for contractor in location_sorted_contractors:
            if contractor.contractor_id == contractor_id:
                return contractor 
        return