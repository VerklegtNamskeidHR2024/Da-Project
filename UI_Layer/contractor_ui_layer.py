from Model_Classes.contractor_model import Contractor
from prettytable import PrettyTable 
from colorama import Fore, Style, init
import os

class contractor_UI_menu():
    def __init__(self, logic_wrapper, rank, location, staff_id) -> None:
        """Constructor for contractor_UI_menu"""
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        self.staff_id = staff_id

    def clear_screen(self):
        ''' Clears the screen '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_point_contractor_UI(self) -> None:
        """When this class is called it starts here. Goes into diffrent menus based on your rank. """
        # In almost all functions that receive, and verifies user input are while loops that repeatedly asks the user
        # for specific input. These while loops are held together on the condition that the user either fullfills the
        # neccesary requirements to proceed or that they don't enter q/Q or b/B.
        #
        #
        # Outside of each while loop are return statments that pass back any input that the user had entered. In all cases,
        # except 2, has no affect on the user experience while navigating this menu. Only when the input given is either
        # q/Q or b/B do these while loops and return statments influence the flow of the user experience.
        #
        #
        # When q/Q are entered, at any point while navigating this menu, it is always returned back to this point. Once here,
        # it passes the necessary verification to be returned back to the home page menu where, once again, it is returned one
        # final time to the quit system function that displays the exit message and stops running the script.
        #
        #
        if self.rank == "Employee":
            employee_contractors_menu = self.display_contractor_employee_menu()
            if employee_contractors_menu in ["q", "b"]:
                return employee_contractors_menu
        else:
            admin_manager_contractors_menu = self.display_contractor_menu_admin_and_manager()
            if admin_manager_contractors_menu in ["q", "b"]:
                return admin_manager_contractors_menu	
    


    def display_all_contractors(self) -> str:
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

    def display_contractor_employee_menu(self) -> None:
        """display contractor menu for employee"""
        loop = True
        while loop == True:
            print(f"{self.rank} - Contractors Page")
            self.display_all_contractors()

            print("------------------------------------------------")
            print("1) View contractor")
            print(">Go to Home Page: b, B")
            print("------------------------------------------------")

            user_action = input("Select an Option:  ")
            match user_action:
                # In the case below, if the function returns "b" then the the loop starts again, however if it receives "q"
                # then the loop breaks and is returned back to the start point; shutting the program off.
                #
                # An employee only has access to this option in the contractors menu. 
                case "1":
                    user_action = self.display_view_contractor()

                # If b is entered, it is returned back to the start_point_work_requests_UI function which brings the
                # user back to the home page.
                case "b":
                    return "b"
                
                # If q is entered, it is returned back to the start_point_work_requests_UI function which turns off
                # program.
                case "q":
                    # quit back to main menu
                    pass
                case _:
                    print(Fore.RED + "Wrong input" + Style.RESET_ALL)
        return 
    
    def display_contractor_menu_admin_and_manager(self) -> None:
        """display contractor menu for admin and manager"""
        loop = True
        while loop == True:
            print(f"{self.rank} - Contractors Page")
            self.display_all_contractors()

            print("------------------------------------------------")
            print("1. Add contractor")
            print("2. edit contractor")
            print("3. View contractor")
            print(">Go to Home Page: b, B")
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
                case "b" | "B":
                    # quit back to main menu
                    loop = False
                    pass
                case _:
                    print(Fore.RED + "Wrong input" + Style.RESET_ALL)
        return 

    def display_add_contractor_form(self) -> None:
        """create contractor"""
        try:
            self.clear_screen()
            print("-------------------Add Contractor Form-------------------")

            valid_company_name = False
            valid_contact_name = False
            valid_opening_hours = False
            valid_phone_number = False

            new_contractor = Contractor()
            # set the company name, contact name, opening hours and phone number for the new contractor
            # it then sends the value you are entering to the sanity check function to check if it is valid
            # if it is valid then it sets the value to the new contractor
            while valid_company_name == False:
                company_name = input(f"{"| Enter company name ":<30}| ")
                if self.logic_wrapper.sanity_check_contractor("company_name", company_name) == True:
                    new_contractor.set_company_name(company_name)
                    valid_company_name = True
                else:
                    print(Fore.RED + "Invalid company name. Please try again." + Style.RESET_ALL)
            while valid_contact_name == False:
                contact_name = input(f"{"| Enter contact name ":<30}| ")
                if self.logic_wrapper.sanity_check_contractor("contact_name", contact_name) == True:
                    new_contractor.set_contact_name(contact_name)
                    valid_contact_name = True
                else:
                    print(Fore.RED + "Invalid contact name. Please try again." + Style.RESET_ALL)
            while valid_opening_hours == False:
                opening_hours = input(f"{"| Enter opening hours ":<30}| ")
                if self.logic_wrapper.sanity_check_contractor("opening_hours", opening_hours) == True:
                    new_contractor.set_opening_hours(opening_hours)
                    valid_opening_hours = True
                else:
                    print(Fore.RED + "Invalid opening hours. Please try again. Use This format Example: 08-16" + Style.RESET_ALL)
            while valid_phone_number == False:
                phone_number = input(f"{"| Enter phone number ":<30}| ")
                if self.logic_wrapper.sanity_check_contractor("phone_number", phone_number) == True:
                    new_contractor.set_phone_number(phone_number)
                    valid_phone_number = True
                else:
                    print(Fore.RED + "Invalid phone number. Please try again. No letters or special characters and lenght of 7." + Style.RESET_ALL)
            # set the location for the new contractor from the current location
            new_contractor.set_location(self.location)

            try:
                # add the new contractor to the storage
                self.logic_wrapper.add_new_contractor(self.rank, self.location, new_contractor)
                print("---------------------------------------------------------")
                self.clear_screen()
                print("Contractor added")
            except:
                self.clear_screen()
                print("something went wrong with making new contractor") 
        except:
            self.clear_screen()
            print("something went wrong with making new contractor")

    def display_view_contractor(self) -> None:
        '''Shows contractor information'''
        # find contracotor from id
        found_contractor = False
        while found_contractor == False:
            try:
                print(">Go to Home Page: b, B")
                contractor_to_use = self.select_contractor_by_id()
                if contractor_to_use:
                    found_contractor = True
                elif contractor_to_use == False:
                    return
                else:
                    pass
            except:
                print(Fore.RED + "something went wrong" + Style.RESET_ALL)
        
        self.clear_screen()
        loop = True
        while loop == True:
            contractor = self.logic_wrapper.get_contractor_by_id(self.location, contractor_to_use.contractor_id)
            # if contractor is found print the contractor info
            self.print_single_contractor(contractor)

            # show the options for the contractor
            print("1) View work requests")
            print("2) View maintenance reports")
            print("2) Give warning")
            print(">Go to Home Page: b, B")
            edit_user_action = input("What action would you like to perform: ")

            match edit_user_action:
                case "1":
                    # show work requests
                    self.display_contractor_work_requests(contractor)
                case "2":
                    # show maintenance reports
                    self.display_contractor_maintenance_reports(contractor)
                case "3":           
                    # give contractor warning     
                    self.display_contractor_warning(contractor)
                case "b" | "B":
                    loop = False
                case _:
                    print("not valid input")
        return

    def display_contractor_warning(self, contractor) -> None:
        """Give contractor warning"""
        try:
            warning = input("Enter warning for contractor: ")
            # checks if the warning is valid
            is_valid = self.logic_wrapper.sanity_check_contractor("warning", warning)
            # if the warning is valid then give the contractor a warning
            if is_valid == True:
                self.logic_wrapper.edit_existing_contractor_in_storage(contractor, self.location, 'warning', warning)
            self.clear_screen()
            print(Fore.GREEN + "Contractor has been given a warning." + Style.RESET_ALL)
            return
        except:
            self.clear_screen()
            print("something went wrong")
            return

    def display_edit_contractor_menu(self) -> None:
        """edit contractor menu"""
        # find contracotor from id
        # allows the user to select a contractor by id
        # and then back out or try again
        found_contractor = False
        while found_contractor == False:
            try:
                print(">Go to Home Page: b, B")
                contractor_to_use = self.select_contractor_by_id()
                if contractor_to_use:
                    found_contractor = True
                elif contractor_to_use == False:
                    return
                else:
                    pass
            except:
                print(Fore.RED + "something went wrong" + Style.RESET_ALL)

        self.clear_screen()
        loop = True
        while loop == True:
            # print the contractor info
            contractor = self.logic_wrapper.get_contractor_by_id(self.location, contractor_to_use.contractor_id)
            self.print_single_contractor(contractor)
            # shows the available options to change contractor by
            print("------------------------------------------------")
            print("1) Change Contact Name")
            print("2) Change Company Phone Number")
            print("3) Change Opening Hours")
            print(">Go to Home Page: b, B")
            print("------------------------------------------------")
            edit_user_action = input("what do you want to change: ")
            match edit_user_action:
                case "1":
                    self.change_contact_name(contractor)
                case "2":
                    self.change_phone_number(contractor)
                case "3":
                    self.change_opening_hours(contractor)
                case "b" | "B":
                    loop = False
                case _:
                    print((Fore.RED + "Not Valid Input" + Style.RESET_ALL))
        return
    
    def change_contact_name(self, contractor) -> None:
        """change contact name for contractor"""
        try:
            new_contact_name = input("Enter new contact name: ")
            # checks if the contact name is valid
            is_valid = self.logic_wrapper.sanity_check_contractor("contact_name", new_contact_name)
            # if the contact name is valid then change the contact name
            if is_valid == True:
                self.logic_wrapper.edit_existing_contractor_in_storage(contractor, self.location, 'contact_name', new_contact_name)
                self.clear_screen()
                print(Fore.GREEN + "Contact name has been changed." + Style.RESET_ALL)
            else:
                self.clear_screen()
                print(Fore.RED + "Invalid contact name" + Style.RESET_ALL)
            return
        except:
            self.clear_screen()
            print(Fore.RED + "something went wrong" + Style.RESET_ALL)
            return

    def change_phone_number(self, contractor) -> None:
        """change phone number for contractor"""
        try:
            is_valid = False
            while is_valid == False:
                phone_input = input("enter phone number: ")
                # checks if the phone number is valid
                is_valid = self.logic_wrapper.sanity_check_contractor("phone_number", phone_input)
                if is_valid == True:
                    # if the phone number is valid then change the phone number
                    self.logic_wrapper.edit_existing_contractor_in_storage(contractor, self.location, 'phone_number', phone_input)
                    self.clear_screen()
                    print(Fore.GREEN + "Phone number has been changed." + Style.RESET_ALL)
                    return
                else:
                    self.clear_screen()
                    print(Fore.RED + "Invalid phone number. Please try again. No letters or special characters and lenght of 7." + Style.RESET_ALL)
                return
        except:
            self.clear_screen()
            print(Fore.RED + "something went wrong" + Style.RESET_ALL)
            return

    def change_opening_hours(self, contractor) -> None:
        """change opening hours for contractor"""
        try:
            new_opening_hours = input("Enter new opening Hours: ")\
            # checks if the opening hours are valid
            is_valid = self.logic_wrapper.sanity_check_contractor("opening_hours", new_opening_hours)
            if is_valid == True:
                # if the opening hours are valid then change the opening hours
                self.logic_wrapper.edit_existing_contractor_in_storage(contractor, self.location, 'opening_hours', new_opening_hours)
                self.clear_screen()
                print(Fore.GREEN + "Opening hours have been changed." + Style.RESET_ALL)
            else:
                self.clear_screen()
                print(Fore.RED + "Invalid input opening hours" + Style.RESET_ALL)
        except:
            self.clear_screen()
            print(Fore.RED + "something went wrong" + Style.RESET_ALL)

    def select_contractor_by_id(self) -> None:
        """get a contractor by ID"""
        id_to_find = input("enter ID to select contractor: ")
        if id_to_find in ["b", "B"]:
            return False
        
        try:
            # calls get contractor by id from logic layer
            contractor_from_id = self.logic_wrapper.get_contractor_by_id(self.location, id_to_find)
            if not contractor_from_id:
                # returns None if he is not found
                print(Fore.RED + f"No contractor found with that ID: {id_to_find}" + Style.RESET_ALL)
                return None
            # returns the contractor if he is found
            return contractor_from_id
        except:
            print(Fore.RED + "Something went wrong." + Style.RESET_ALL)


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

    def display_contractor_maintenance_reports(self, selected_contractor: object) -> str:
        ''' Displays maintenance reports for a contractor '''
        # get the maintenance reports for the contractor
        contractor_maintenance_reports = self.logic_wrapper.get_contractor_maintenance_reports(self.location, selected_contractor.contractor_id)
        if not contractor_maintenance_reports:
            print(Fore.RED + "No maintenance reports for the selected contractor." + Style.RESET_ALL)
            return
        else:
            # create a table to print the maintenance reports
            Contractor_maintenance_reports_table = PrettyTable(['Report ID', 'Report Name', 'Description', 'Status'])
            print("Maintenance Reports for the selected contractor.")
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
            bause_breaker = input("\nPress Enter to return.")
            print('')
            self.clear_screen()
            return

    def display_contractor_work_requests(self, selected_contractor: object) -> str:
        ''' Displays work requests for a property '''
        # get the work requests for the contractor
        contractor_work_requests = self.logic_wrapper.get_contractor_work_requests(self.location, selected_contractor.contractor_id)
        if not contractor_work_requests:
            print(Fore.RED + "No work requests for the selected contractor." + Style.RESET_ALL)
            return
        else:
            contractor_work_requests_table = PrettyTable(['Work Request ID', 'Description', 'Mark as Completed'])
            print("Work Requests for the selected Contractor.")
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
            bause_breaker = input("\nPress Enter to return.")
            print('')
            self.clear_screen()
            return

