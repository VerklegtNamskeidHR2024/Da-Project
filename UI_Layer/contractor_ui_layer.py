from Model_Classes.contractor_model import Contractor

# missing list
# diffrent option based on what user you are
# add new contractor
# edit contractor 

class contractor_UI_menu():
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
    
    def start_point_contractor_UI(self):
        # when this class is called it starts here
        # call other functions in class from here
        self.display_contractor_menu()
        return
    

    def display_all_contractors(self):
        """Function to display all contractors at the selected locations"""
        contractor_list = self.logic_wrapper.get_all_contractors_at_location(self.location)
        print('-' * 70)
        print(f'{"ID":<6}|{"Company Name":>25}|{"Contact Name":>20}|{"Location":>20}')
        print("-" * 75)

        for item in contractor_list:
            print(f"{item.contractor_id:<6}|{item.company_name:>25}|{item.contact_name:>20}|{item.location:>20}")
        print('-' * 70)


    # display contractor menu
    def display_contractor_menu(self):
        print(f"{self.rank} - Contractors Page")
        # create list for printing all contractors for first menu in contractors
        #Can Remove this added the other function to have same code with other files - Kv Hreimur
        '''print('old contractor list')
        contractor_list = self.logic_wrapper.get_all_contractors(self.location)
        self.print_contractors_from_list(contractor_list)'''
        self.display_all_contractors()

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

            case "5":
                self.logic_wrapper.write_to_file(list_of_contractors = [])
            case "q":
                # quit back to main menu
                pass
            case _:
                print("wrong input")

        # test print
        print("we going back to main menu in UI layer")
        return 

    # display add contractor
    def display_add_contractor_form(self):
        """create contractor"""
        new_contractor = Contractor()
        # system will do this itself
        # new_contractor.set_contractor_id(input("enter ID: "))
        new_contractor.set_company_name(input("enter company name: "))
        new_contractor.set_contact_name(input("enter contact name: "))
        new_contractor.set_opening_hours(input("enter opening hours: "))
        new_contractor.set_phone_number(int(input("enter phone number: ")))
        new_contractor.set_location(self.location)
        # add later
        # new_contractor.set_previous_job_reports()
        try:
            new_contractor_added = self.logic_wrapper.add_new_contractor(new_contractor)
            if new_contractor_added == True:
                print("contractor has been added")
            
        except:
            print("something went wrong with making new contractor")

        print(new_contractor.contractor_id)
        print(new_contractor.company_name)
        print(new_contractor.contact_name)
        print(new_contractor.opening_hours)
        print(new_contractor.phone_number)
        print(new_contractor.location)
        print(new_contractor.previous_job_reports)

    # display edit contractor
    def display_edit_contracor_menu(self):
        """edit contractor menu"""
        # find contracotor from id
        try:
            contractor_to_use = self.select_contractor_by_id()
            if contractor_to_use == None:
                return
        except:
            print("something went wrong")

        # print the contractor info
        self.print_single_contractor(contractor_to_use)

        # then show dis
        print("1) Change Contact Name")
        print("2) Change Company Phone Number")
        print("3) Change Opening Hours")
        edit_user_action = input("what do you want to change: ")
        match edit_user_action:
            case "1":
                self.change_contact_name(contractor_to_use)
            case "2":
                self.change_phone_number(contractor_to_use)
            case "3":
                self.change_opening_hours(contractor_to_use)
            case _:
                print("not valid input")
                return
    
    # change contact name
    def change_contact_name(self, contractor):
        """change contact name for contractor"""
        try:
            new_contact_name = input("Enter new contact name: ")
            contractor.set_contact_name(new_contact_name)
            self.logic_wrapper.sanity_check_contractor(self.location, contractor)
            #self.print_single_contractor(contractor)
            # needs to call sanity check
        except:
            print("something went wrong")

    # change phone number
    def change_phone_number(self, contractor):
        try:
            new_phone_number = int(input("Enter new company phone number: "))
        except:
            print("something went wrong")

    # change opening hours
    def change_opening_hours(self, contractor):
        try:
            new_opening_hours = input("Enter new opening Hours: ")
        except:
            print("something went wrong")

    # select contractor by ID
    def select_contractor_by_id(self):
        """print a single contractor"""
        id_to_find = input("enter ID to select contractor: ")
        try:
            contractor_from_id = self.logic_wrapper.get_contractor_by_id(self.location, id_to_find)
            if contractor_from_id == None:
                print("No contractor with that ID found")
            return contractor_from_id
        except:
            print("something went wrong")

    # print single contractor
    def print_single_contractor(self, contractor):
        print("-"*30)
        print(f"{'Contractor ID':<15}: {contractor.contractor_id}")
        print(f"{'Company Name':<15}: {contractor.company_name}")
        print(f"{'Contact Name':<15}: {contractor.contact_name}")
        print(f"{'Location':<15}: {contractor.location}")
        print(f"{'Opening Hours':<15}: {contractor.opening_hours}")
        print(f"{'Phone Number':<15}: {contractor.phone_number}")
        print("-"*30)

    # CAN REMOVE THIS
    # print contractors from list
    def print_contractors_from_list(self, contractor_list):
        print("-"*78)
        print(f"{'ID':<10}|{'Company name':<25}|{'Name':<20}|{'location':<20}")
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