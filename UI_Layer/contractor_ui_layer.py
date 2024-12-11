from Model_Classes.contractor_model import Contractor
from prettytable import PrettyTable 
from colorama import Fore, Style, init

# missing list
# give contractor warning

class contractor_UI_menu():
    def __init__(self, logic_wrapper, rank, location, staff_id) -> None:
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        self.staff_id = staff_id
    
    def start_point_contractor_UI(self) -> str:
        # when this class is called it starts here
        # call other functions in class from here
        if self.rank == "Employee":
            employee_contractors_menu = self.display_contractor_employee_menu_logistics()
            if employee_contractors_menu in ["q", "b"]:
                return employee_contractors_menu
        else:
            admin_manager_contractors_menu = self.display_contractor_menu_admin_and_manager_logistics()
            if admin_manager_contractors_menu in ["q", "b"]:
                return admin_manager_contractors_menu	
    

    def display_all_contractors(self) -> str:
        """Function to display all contractors at the selected locations"""
        contractor_list = self.logic_wrapper.get_all_contractors_at_location(self.location)
        print('-' * 70)
        print(f'{"ID":<6}|{"Company Name":>25}|{"Contact Name":>20}|{"Location":>20}')
        print("-" * 75)

        for item in contractor_list:
            print(f"{item.contractor_id:<6}|{item.company_name:>25}|{item.contact_name:>20}|{item.location:>20}")
        print('-' * 70)

    # display contractor menu
    def display_contractor_employee_menu_logistics(self) -> str:
        # create list for printing all contractors for first menu in contractors
        #Can Remove this added the other function to have same code with other files - Kv Hreimur
        user_action = ""
        while user_action != "q":
            print(f"{self.rank} - Contractors Page")
            self.display_all_contractors()
            print("-" * 70)
            print("1) Select Contractor")
            print("-" * 70)
            user_action = input("Select an Option:  ").lower()
            match user_action:
                case "1":
                    try:
                        self.display_view_contractor()
                    except:
                        print("something went wrong")
                case "q":
                    # quit back to main menu
                    pass
                case _:
                    print("wrong input")

        # test print
        #print("we going back to main menu in UI layer")
        return 
    
    def display_contractor_menu_admin_and_manager_logistics(self) -> None:
        # create list for printing all contractors for first menu in contractors
        #Can Remove this added the other function to have same code with other files - Kv Hreimur
        '''print('old contractor list')
        contractor_list = self.logic_wrapper.get_all_contractors(self.location)
        self.print_contractors_from_list(contractor_list)'''
        
        user_action = ""
        while user_action != "q":
            print(f"{self.rank} - Contractors Page")
            self.display_all_contractors()
            print("-" * 70)
            print("1) Add Contractor")
            print("2) Edit Contractor")
            print("3) View Contractor")
            print("-" * 70)

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
                case "4":
                    # give warning 
                    # finish this a later point
                    pass

                case "q":
                    # quit back to main menu
                    pass
                case _:
                    print("wrong input")

            # test print
            #print("we going back to main menu in UI layer")
            return 

    # display add contractor
    def display_add_contractor_form(self) -> None:
        """create contractor"""
        is_valid_phone_number = False
        try:
            new_contractor = Contractor()
            new_contractor.set_company_name(input("enter company name: "))
            new_contractor.set_contact_name(input("enter contact name: "))
            new_contractor.set_opening_hours(input("enter opening hours: "))
            while is_valid_phone_number == False:
                new_contractor.set_phone_number(int(input("enter phone number: ")))
                is_valid_phone_number = self.logic_wrapper.sanity_check_contractor(new_contractor,"")
                if is_valid_phone_number == False:
                    print("Invalid phone number. Please try again.")
            new_contractor.set_location(self.location)
            # add later
            # new_contractor.set_previous_job_reports()
            new_contractor_added = self.logic_wrapper.add_new_contractor(self.rank, self.location, new_contractor)
            if new_contractor_added == True:
                print("contractor has been added")
            #self.display_all_contractors()
        except:
            print("something went wrong with making new contractor")

    def display_view_contractor(self):
        '''Shows contractor information'''
        try:
            contractor_to_use = self.select_contractor_by_id()
            if contractor_to_use == None:
                print("No contractor with that ID")
                return
        except:
            print("something went wrong")
            return
        self.print_single_contractor(contractor_to_use)
        print("1) View work requests")#Shows all work requests the contractor has done
        print("2) Give warning")#maybe
        edit_user_action = input("What action would you like to perform: ")
        match edit_user_action:
            case "1":
                self.display_contractor_work_requests(contractor_to_use)
            case "2":                
                # give warning 
                # finish this a later point
                pass
            case _:
                print("not valid input")
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
                print("Not Valid Input")
                return
    
    # change contact name
    def change_contact_name(self, contractor) -> None:
        """change contact name for contractor"""
        try:
            new_contact_name = input("Enter new contact name: ")
            #contractor.set_contact_name(new_contact_name)
            is_valid = self.logic_wrapper.sanity_check_contractor(contractor, new_contact_name)
            if is_valid == True:
                self.logic_wrapper.edit_existing_contractor_in_storage(contractor, self.location, 'contact_name', new_contact_name)
            self.print_single_contractor(contractor)
        except:
            print("something went wrong")

    # change phone number
    def change_phone_number(self, contractor) -> None:
        try:
            is_valid = False
            while is_valid == False:
                phone_input = input("enter phone number: ")
                is_valid = self.logic_wrapper.sanity_check_contractor(contractor, phone_input)
                if not phone_input.isdigit() or is_valid != True:
                    print("Invalid input. Please enter numbers only.")
                else:
                    self.logic_wrapper.edit_existing_contractor_in_storage(contractor, self.location, 'phone_number', phone_input)
                    self.print_single_contractor(contractor)
        except:
            print("something went wrong")

    # change opening hours
    def change_opening_hours(self, contractor):
        try:
            new_opening_hours = input("Enter new opening Hours: ")
            is_valid = self.logic_wrapper.sanity_check_contractor(contractor, new_opening_hours)
            if is_valid == True:
                self.logic_wrapper.edit_existing_contractor_in_storage(contractor, self.location, 'opening_hours', new_opening_hours)
            self.print_single_contractor(contractor)
        except:
            print("something went wrong")

    # select contractor by ID
    def select_contractor_by_id(self) -> None:
        """print a single contractor"""
        id_to_find = input("enter ID to select contractor: ")
        try:
            contractor_from_id = self.logic_wrapper.get_contractor_by_id(self.location, id_to_find)
            if not contractor_from_id:
                print(f"No contractor found with ID: {id_to_find}")
                return None
            return contractor_from_id
        except:
            print("something went wrong")

    # print single contractor
    def print_single_contractor(self, contractor: object) -> str:
        print("-"*30)
        contractor_print_table = PrettyTable()
        contractor.field_names = ['info',""]
        contractor_print_table.add_row(['Contractor ID', contractor.contractor_id])
        contractor_print_table.add_row(['Company Name', contractor.company_name])
        contractor_print_table.add_row(['Contact Name', contractor.contact_name])
        contractor_print_table.add_row(['Location', contractor.location])
        contractor_print_table.add_row(['Opening Hours', contractor.opening_hours])
        contractor_print_table.add_row(['Phone Number', contractor.phone_number])

        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        contractor_print_table.border = True
        contractor_print_table.junction_char = f"{border_color}+{reset_color}"
        contractor_print_table.horizontal_char = f"{border_color}-{reset_color}"
        contractor_print_table.vertical_char = f"{border_color}|{reset_color}"
        print(contractor_print_table)
        """ print(f"{'Contractor ID':<15}: {contractor.contractor_id}")
        print(f"{'Company Name':<15}: {contractor.company_name}")
        print(f"{'Contact Name':<15}: {contractor.contact_name}")
        print(f"{'Location':<15}: {contractor.location}")
        print(f"{'Opening Hours':<15}: {contractor.opening_hours}")
        print(f"{'Phone Number':<15}: {contractor.phone_number}") """
        print("-"*30)

    def display_contractor_maintenance_reports(self, selected_contractor: object) -> str:
        ''' Displays maintenance reports for a contractor '''
        Contractor_maintenance_reports_table = PrettyTable(['Report ID', 'Report Name', 'Description', 'Status'])
        print("Maintenance Reports for the selected contractor.")
        property_maintenance_reports = self.logic_wrapper.get_contractor_maintenance_reports(self.location, selected_contractor.contractor_id)
        for maintenance_report in property_maintenance_reports:
            Contractor_maintenance_reports_table.add_row([maintenance_report.report_id, maintenance_report.report_name, maintenance_report.maintenance_description, maintenance_report.report_status])
        border_color = Fore.MAGENTA
        reset_color = Style.RESET_ALL
        Contractor_maintenance_reports_table.border = True
        Contractor_maintenance_reports_table.junction_char = f"{border_color}+{reset_color}"
        Contractor_maintenance_reports_table.horizontal_char = f"{border_color}-{reset_color}"
        Contractor_maintenance_reports_table.vertical_char = f"{border_color}|{reset_color}"
        print(Contractor_maintenance_reports_table)
        print('')
        print("{:>20}".format("> Go Back: b, B"))
        print("{:>20}".format("> Quit System: q, Q"))
        while (
            contractor_maintenance_reports_sub_menu := input("Select An Option: ").lower()
        ) not in ["q", "b", "Q", "B"]:
            print("Sigma Sigma on the wall, who is the Skibidiest of them all")
        return contractor_maintenance_reports_sub_menu.lower()
    
    def display_contractor_work_requests(self, selected_contractor: object) -> str:
        ''' Displays work requests for a property '''
        contractor_work_requests_table = PrettyTable(['Work Request ID', 'Description', 'Mark as Completed'])
        print("Work Requests for the selected property.")
        contractor_work_requests = self.logic_wrapper.get_contractor_work_requests(self.location, selected_contractor.contractor_id)
        for work_request in contractor_work_requests:
            contractor_work_requests_table.add_row([work_request.work_request_id, work_request.description, work_request.mark_as_completed])
        border_color = Fore.MAGENTA
        reset_color = Style.RESET_ALL
        contractor_work_requests_table.border = True
        contractor_work_requests_table.junction_char = f"{border_color}+{reset_color}"
        contractor_work_requests_table.horizontal_char = f"{border_color}-{reset_color}"
        contractor_work_requests_table.vertical_char = f"{border_color}|{reset_color}"
        print(contractor_work_requests_table)
        bause_breaker = input("\nPress Enter to return to main menu.")
        print('')
        print("{:>20}".format("> Go Back: b, B"))
        print("{:>20}".format("> Quit System: q, Q"))
        while (
            contractor_work_requests_sub_menu := input("Select An Option: ").lower()
        ) not in ["q", "b", "Q", "B"]:
            print("Sigma Sigma on the wall, who is the Skibidiest of them all")
        return contractor_work_requests_sub_menu.lower()


