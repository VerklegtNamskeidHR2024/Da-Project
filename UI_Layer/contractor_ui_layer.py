

class contractor_UI_menu():
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def display_contractor_menu(self):
        # temp stuff with dummy data in wrapper
        contract_list = self.logic_wrapper.get_all_contractors()
        for item in contract_list:
            print(item)
        # end temp

        print("Manager - Contractors Page")
        print("------------------------------------------------")
        print("1) Add contractor")
        print("2) Select contractor")
        print("------------------------------------------------")
        user_action = input("Select an Option:  ")
        match user_action:
            case "1":
                pass
            case "2":
                pass
            case _:
                print("wrong input")

        
    def print_contractor(self):
        # Maybe just one function for printing contractors even if it is more than one 
        pass