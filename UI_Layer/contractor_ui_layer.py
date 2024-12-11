from Model_Classes.contractor_model import Contractor
from prettytable import PrettyTable 
from colorama import Fore, Style, init

# missing list
# !!!!!give contractor warning!!!!!

class contractor_UI_menu():
    def __init__(self, logic_wrapper, rank, location, staff_id) -> None:
        """Constructor for contractor_UI_menu"""
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        self.staff_id = staff_id
    
    def start_point_contractor_UI(self) -> None:
        """Start point for contractor UI"""
        # when this class is called it starts here
        # goes into diffrent menus based on your rank
        print(self.rank)
        if self.rank == "Employee":
            self.display_contractor_employee_menu()
        else:
            self.display_contractor_menu_admin_and_manager()
        return
    

    def display_all_contractors(self,) -> None:
        """Function to display all contractors at the selected locations"""
        # gets a list of all contractors at the location
        contractor_print_table = PrettyTable()
        contractor_list = self.logic_wrapper.get_all_contractors_at_location(self.location)
        contractor_print_table.field_names = ["ID","Company Name","Contact Name","Location"]
        # iterates through the location list and adds the location information to the table
        for item in contractor_list:
            contractor_print_table.add_row([item.contractor_id, item.company_name, item.contact_name, item.location])
        
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        contractor_print_table.border = True
        contractor_print_table.junction_char = f"{border_color}+{reset_color}"
        contractor_print_table.horizontal_char = f"{border_color}-{reset_color}"
        contractor_print_table.vertical_char = f"{border_color}|{reset_color}"
        print('')
        print(contractor_print_table)
        print('')

    # display contractor menu
    def display_contractor_employee_menu(self) -> None:
        """display contractor menu for employee"""
        print(f"{self.rank} - Contractors Page")
        self.display_all_contractors()

        print("------------------------------------------------")
        print("1) View contractor")
        print("------------------------------------------------")

        user_action = input("Select an Option:  ")
        match user_action:
            case "1":
                self.display_view_contractor()
            case "q":
                # quit back to main menu
                pass
            case _:
                print("wrong input")

        return 
    
    def display_contractor_menu_admin_and_manager(self) -> None:
        """display contractor menu for admin and manager"""
        print(f"{self.rank} - Contractors Page")
        self.display_all_contractors()

        print("------------------------------------------------")
        print("1) Add contractor")
        print("2) edit contractor")
        print("3) View contractor")
        print("------------------------------------------------")

        user_action = input("Select an Option:  ")
        match user_action:
            case "1":
                # create contractor
                self.display_add_contractor_form()
            case "2":
                # edit contractor
                self.display_edit_contractor_menu()
            case "3":
                self.display_view_contractor()
            case "q":
                # quit back to main menu
                pass
            case _:
                print("wrong input")
        return 

    # display add contractor 
    # taka allt svona ut
    def display_add_contractor_form(self) -> None:
        """create contractor"""
        is_valid_phone_number = False
        try:
            new_contractor = Contractor()
            # set the company name, contact name, opening hours and phone number for the new contractor
            new_contractor.set_company_name(input("enter company name: "))
            new_contractor.set_contact_name(input("enter contact name: "))
            new_contractor.set_opening_hours(input("enter opening hours: "))
            # looping until a valid number is enterd
            while is_valid_phone_number == False:
                new_contractor.set_phone_number(int(input("enter phone number: ")))
                # will return false if phone number is not valid thus looping until a valid number is enterd
                is_valid_phone_number = self.logic_wrapper.sanity_check_contractor(new_contractor,"")
                if is_valid_phone_number == False:
                    print("Invalid phone number. Please try again.")
            new_contractor.set_location(self.location)
                # add later
                # new_contractor.set_previous_job_reports()

            # add the new contractor to the storage
            new_contractor_added = self.logic_wrapper.add_new_contractor(self.rank, self.location, new_contractor)
            if new_contractor_added == True:
                print("contractor has been added")
        except:
            print("something went wrong with making new contractor")

    def display_view_contractor(self) -> None:
        '''Shows contractor information'''

        try:
            # find contracotor from id
            contractor_to_use = self.select_contractor_by_id()
            # if no contractor is found
            if contractor_to_use == None:
                print("No contractor with that ID")
                return
        except:
            print("something went wrong")
            return
        # if contractor is found print the contractor info
        self.print_single_contractor(contractor_to_use)

        # show the options for the contractor
        print("1) View work requests")
        print("2) Give warning")
        edit_user_action = input("What action would you like to perform: ")

        match edit_user_action:
            case "1":
                # show work requests
                self.display_contractor_work_requests(contractor_to_use)
            case "2":                
                self.display_contractor_warning(contractor_to_use)
            case _:
                print("not valid input")
                return

    def display_contractor_warning(self, contractor) -> None:
        """Give contractor warning"""
        try:
            warning = input("Enter warning for contractor: ")
            # checks if the contact name is valid
            is_valid = self.logic_wrapper.sanity_check_contractor(contractor)
            # if the contact name is valid then change the contact name
            if is_valid == True:
                self.logic_wrapper.edit_existing_contractor_in_storage(contractor, self.location, 'warning', warning)
            print('Contractor has been given a warning.')
            return
        except:
            print("something went wrong")
            return

    # display edit contractor
    def display_edit_contractor_menu(self) -> None:
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

        # shows the available options to change contractor by
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
    def change_contact_name(self, contractor) -> None:
        """change contact name for contractor"""
        try:
            new_contact_name = input("Enter new contact name: ")
            # checks if the contact name is valid
            is_valid = self.logic_wrapper.sanity_check_contractor(contractor)
            # if the contact name is valid then change the contact name
            if is_valid == True:
                self.logic_wrapper.edit_existing_contractor_in_storage(contractor, self.location, 'contact_name', new_contact_name)
            print('Contact name has been changed.')
            return
        except:
            print("something went wrong")
            return

    # change phone number
    def change_phone_number(self, contractor) -> None:
        """change phone number for contractor"""
        try:
            is_valid = False
            while is_valid == False:
                phone_input = input("enter phone number: ")
                # checks if the phone number is valid
                is_valid = self.logic_wrapper.sanity_check_contractor(contractor)
                if not phone_input.isdigit() or is_valid != True:
                    print("Invalid input. Please enter numbers only.")
                else:
                    # if the phone number is valid then change the phone number
                    self.logic_wrapper.edit_existing_contractor_in_storage(contractor, self.location, 'phone_number', phone_input)
                    print('Phone number has been changed.')
                    return

        except:
            print("something went wrong")
            return

    # change opening hours
    def change_opening_hours(self, contractor) -> None:
        """change opening hours for contractor"""
        try:
            new_opening_hours = input("Enter new opening Hours: ")\
            # checks if the opening hours are valid
            is_valid = self.logic_wrapper.sanity_check_contractor(contractor)
            if is_valid == True:
                # if the opening hours are valid then change the opening hours
                self.logic_wrapper.edit_existing_contractor_in_storage(contractor, self.location, 'opening_hours', new_opening_hours)
            self.print_single_contractor(contractor)
        except:
            print("something went wrong")

    # select contractor by ID
    def select_contractor_by_id(self) -> None:
        """get a contractor by ID"""
        id_to_find = input("enter ID to select contractor: ")
        try:
            # calls get contractor by id from logic layer
            contractor_from_id = self.logic_wrapper.get_contractor_by_id(self.location, id_to_find)
            if not contractor_from_id:
                # returns None if he is not found
                print(f"No contractor found with ID: {id_to_find}")
                return None
            # returns the contractor if he is found
            return contractor_from_id
        except:
            print("something went wrong")

    # print single contractor
    def print_single_contractor(self, contractor) -> None:
        """print a single contractor"""
        print("-"*30)
        # create a table to print the contractor
        contractor_print_table = PrettyTable()
        contractor_print_table.field_names = ['Information',"Contractor Information"]
        # add the contractor info to the table
        contractor_print_table.add_row(['Contractor ID', contractor.contractor_id])
        contractor_print_table.add_row(['Company Name', contractor.company_name])
        contractor_print_table.add_row(['Contact Name', contractor.contact_name])
        contractor_print_table.add_row(['Location', contractor.location])
        contractor_print_table.add_row(['Opening Hours', contractor.opening_hours])
        contractor_print_table.add_row(['Phone Number', contractor.phone_number])
        contractor_print_table.add_row(['Warning', contractor.warningtext])
        # setting some colors for the table
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        contractor_print_table.border = True
        contractor_print_table.junction_char = f"{border_color}+{reset_color}"
        contractor_print_table.horizontal_char = f"{border_color}-{reset_color}"
        contractor_print_table.vertical_char = f"{border_color}|{reset_color}"
        # print the table
        print(contractor_print_table)
        print("-"*30)

    def display_contractor_maintenance_reports(self, selected_contractor) -> None:
        """Display maintenance reports for a contractor"""
        ''' Displays maintenance reports for a contractor '''
        # create a table to print the maintenance reports
        Contractor_maintenance_reports_table = PrettyTable(['Report ID', 'Report Name', 'Description', 'Status'])
        print("Maintenance Reports for the selected contractor.")
        # get the maintenance reports for the contractor
        contractor_maintenance_reports = self.logic_wrapper.get_contractor_maintenance_reports(self.location, selected_contractor.contractor_id)
        # loop through the maintenance reports and add them to the table if they have the current contractors id
        for maintenance_report in contractor_maintenance_reports:
            Contractor_maintenance_reports_table.add_row([maintenance_report.report_id, maintenance_report.report_name, maintenance_report.maintenance_description, maintenance_report.report_status])
        border_color = Fore.MAGENTA
        reset_color = Style.RESET_ALL
        Contractor_maintenance_reports_table.border = True
        Contractor_maintenance_reports_table.junction_char = f"{border_color}+{reset_color}"
        Contractor_maintenance_reports_table.horizontal_char = f"{border_color}-{reset_color}"
        Contractor_maintenance_reports_table.vertical_char = f"{border_color}|{reset_color}"
        print('')
        print(Contractor_maintenance_reports_table)
        print('')
        return
    
    def display_contractor_work_requests(self, selected_contractor) -> None:
        ''' Displays work requests for a contractor '''
        # create a table to print the work requests
        contractor_work_requests_table = PrettyTable(['Work Request ID', 'Description', 'Mark as Completed'])
        print("Work Requests for the selected Contractor.")
        # get the work requests for the contractor
        contractor_work_requests = self.logic_wrapper.get_contractor_work_requests(self.location, selected_contractor.contractor_id)
        # loop through the work requests and add them to the table if they have the current contractors id
        for work_request in contractor_work_requests:
            contractor_work_requests_table.add_row([work_request.work_request_id, work_request.description, work_request.mark_as_completed])
        border_color = Fore.MAGENTA
        reset_color = Style.RESET_ALL
        contractor_work_requests_table.border = True
        contractor_work_requests_table.junction_char = f"{border_color}+{reset_color}"
        contractor_work_requests_table.horizontal_char = f"{border_color}-{reset_color}"
        contractor_work_requests_table.vertical_char = f"{border_color}|{reset_color}"
        print('')
        print(contractor_work_requests_table)
        bause_breaker = input("\nPress Enter to return to main menu.")
        print('')
        return

    # CAN REMOVE THIS
    # print contractors from list
    def print_contractors_from_list(self, contractor_list):
        """print contractors from list"""
        print("-"*78)
        print(f"{'ID':<10}|{'Company name':<25}|{'Name':<20}|{'location':<20}")
        print("-"*78)
        for item in contractor_list:
            print(f"{item.contractor_id:<10}|{item.company_name:<25}|{item.contact_name:<20}|{item.location:<20}")
            
        print("-"*78)
        return
    
