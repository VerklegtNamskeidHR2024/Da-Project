from Model_Classes.contractor_model import Contractor

class contractor_UI_menu():
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location

    def display_contractor_menu(self):
        
        print(f"{self.rank} - Contractors Page")

        # create list for printing all contractors for first menu in contractors
        contractor_list = self.logic_wrapper.get_all_contractors(self.location)
        self.print_contractors_from_list(contractor_list)

        print("------------------------------------------------")
        print("1) Add contractor")
        print("2) edit contractor")
        print("2) give contractor warning")
        print("------------------------------------------------")

        user_action = input("Select an Option:  ")
        match user_action:
            case "1":
                # create contractor
                self.display_add_contractor_form()
            case "2":
                # edit

                self.select_contractor_by_id()
            case "3":
                # give warning
                self.display_edit_contracor_menu
            case "q":
                # quit back to main menu
                pass
            case _:
                print("wrong input")

    def display_add_contractor_form(self):
        """create contractor"""
        return
    
    def display_edit_contracor_menu(self):
        """edit contractor menu"""
        # find contracotor from id
        # then show dis
        print("1) Change Contact Name")
        print("2) Change Company Phone Number")
        print("3) Change Opening Hours")
        edit_user_action = input("what do you want to change: ")


    def select_contractor_by_id(self):
        contractor_from_id = []
        id_to_find = input("enter ID to search for:")
        try:
            contractor_from_id.append(self.logic_wrapper.get_contractor_by_id(self.location, id_to_find))
            print("found him")
            self.print_contractors_from_list(contractor_from_id)
        except:
            print("something went wrong")

    def print_contractors_from_list(self, contractor_list):
        print("-"*78)
        print(f"{"ID":<10}|{"Company name":<25}|{"Name":<20}|{"location":<20}")
        print("-"*78)
        for item in contractor_list:
            print(f"{item.contractor_id:<10}|{item.company_name:<25}|{item.contact_name:<20}|{item.location:<20}")
            
        print("-"*78)
        return
    
        """ "contractor_id": "C0001",
        "company_name": "Daniela and Daughters",
        "contact_name": "Daniela",
        "opening_hours": "8-16",
        "phone_number": 1234567,
        "location": "Reykjavik", """