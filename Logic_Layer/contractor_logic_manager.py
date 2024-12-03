
class contractor_logic_manager:
    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper
    def get_all_contractors(self):
        print("in contractor logic")
        return self.Storage_Layer_Wrapper.get_all_contractor()