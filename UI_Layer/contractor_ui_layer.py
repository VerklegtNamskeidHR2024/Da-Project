
class contractor_UI_menu():
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        pass
        

    def display_contractor_menu(self):
        # temp stuff with dummy data in wrapper
        print(self.rank)
        contract_list = self.logic_wrapper.get_all_contractors()
        for item in contract_list:
            print(f"ID: {item.contractor_id}| Name: {item.contact_name}")
        # end temp

        print("Manager - Contractors Page")
        print("------------------------------------------------")
        print("1) Add contractor")
        print("2) Select contractor")
        print("------------------------------------------------")
        user_action = input("Select an Option:  ")
        match user_action:
            case "1":
                self.display_add_contractor_form()
            case "2":
                self.select_contractor()
            case "q":
                # quit back to main menu
                pass
            case _:
                print("wrong input")
        pass
    def display_add_contractor_form(self):
        pass
    
    def select_contractor(self):
        pass

    def print_contractor(self):
        # Maybe just one function for printing contractors even if it is more than one 
        pass