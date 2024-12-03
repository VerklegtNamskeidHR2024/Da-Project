from Model_Classes.contractor_model import Contractor

class contractor_UI_menu():
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        pass
        

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
                # edit contractor
                self.display_edit_contracor_menu()
            case "3":
                # give warning 
                # c requirement
                pass
                #self.display_edit_contracor_menu
            case "q":
                # quit back to main menu
                pass
            case _:
                print("wrong input")

        print("we going back")
        return 

    def display_add_contractor_form(self):
        """create contractor"""
        new_contractor = Contractor()
        # system will do this itself
        #new_contractor.set_contractor_id(input("enter ID: "))
        new_contractor.set_company_name(input("enter company name: "))
        new_contractor.set_contact_name(input("enter contact name: "))
        new_contractor.set_opening_hours(input("enter opening hours: "))
        new_contractor.set_phone_number(int(input("enter phone number: ")))
        new_contractor.set_location(self.location)
        # add later
        #new_contractor.set_previous_job_reports()

        print(new_contractor.contractor_id)
        print(new_contractor.company_name)
        print(new_contractor.contact_name)
        print(new_contractor.opening_hours)
        print(new_contractor.phone_number)
        print(new_contractor.location)
        print(new_contractor.previous_job_reports)

    def display_edit_contracor_menu(self):
        """edit contractor menu"""
        # find contracotor from id
        contractor_to_use = self.select_contractor_by_id()
        self.print_single_contractors(contractor_to_use )

        # then show dis
        print("1) Change Contact Name")
        print("2) Change Company Phone Number")
        print("3) Change Opening Hours")
        edit_user_action = input("what do you want to change: ")
        match edit_user_action:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case _:
                print("not valid input")
                return



    def select_contractor_by_id(self):
        id_to_find = input("enter ID to search for:")
        try:
            contractor_from_id = self.logic_wrapper.get_contractor_by_id(self.location, id_to_find)
            return contractor_from_id
        except:
            print("something went wrong")

    def print_single_contractors(self, contractor):
        print("-"*30)
        print(f"{'Contractor ID':<15}: {contractor.contractor_id}")
        print(f"{'Company Name':<15}: {contractor.company_name}")
        print(f"{'Contact Name':<15}: {contractor.contact_name}")
        print(f"{'Location':<15}: {contractor.location}")
        print(f"{'Opening Hours':<15}: {contractor.opening_hours}")
        print(f"{'Phone Number':<15}: {contractor.phone_number}")
        print("-"*30)

    def print_contractors_from_list(self, contractor_list):
        print("-"*78)
        print(f"{"ID":<10}|{"Company name":<25}|{"Name":<20}|{"location":<20}")
        print("-"*78)
        for item in contractor_list:
            print(f"{item.contractor_id:<10}|{item.company_name:<25}|{item.contact_name:<20}|{item.location:<20}")
            
        print("-"*78)
        return


# for printing all diffrent variables of contractor 
""" 
print(new_contractor.contractor_id)
print(new_contractor.company_name)
print(new_contractor.contact_name)
print(new_contractor.opening_hours)
print(new_contractor.phone_number)
print(new_contractor.location)
print(new_contractor.previous_job_reports) """


# keep for later in select by id
""" 
contractor_from_id = []
id_to_find = input("enter ID to search for:")
try:
    contractor_from_id = (self.logic_wrapper.get_contractor_by_id(self.location, id_to_find))
    print("found him")
    self.print_contractors_from_list(contractor_from_id)
except:
    print("something went wrong")
"""