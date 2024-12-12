import sys
import time
from Model_Classes.maintenance_report_model import MaintenanceReport
import os
from prettytable import PrettyTable 
from colorama import Fore, Style, init
#initilize colorama and prettytable
init()

class maintenance_report_UI_menu:
    def __init__(self, logic_wrapper, rank, location, staff_id):
        '''Class builder'''
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        self.staff_id = staff_id

    def clear_screen(self):
        ''' Clears the screen '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def quit_system(self):
        ''' Quits the system '''
        print("Departing from NaN Air, Thank you for Visiting!")
        sys.exit()
        
    def start_point_maintenance_reports_UI(self):
        ''' Entry point for the maintenance reports UI '''
        #self.clear_screen()
        #Entry point for the maintenance reports UI
        self.clear_screen()
        self.display_maintenance_report()
        return

       # maintenance_report_menu = self.display_maintenance_report()
       # if maintenance_report_menu in ["q", "b"]:
       #     return maintenance_report_menu

    def display_maintenance_report(self):
        ''' Sends the user to the menu based on their rank '''
        #self.clear_screen()
        # If the user is an admin or manager it goes to the admin/manager menu
        if self.rank in "Admin" or self.rank == "Manager":
            admin_manager_menu = self.select_menu_option_admin_manager()
            if admin_manager_menu in ["q", "b"]:
                return admin_manager_menu

        # If the user is an employee it goes to the employee menu
        elif self.rank == "Employee":
            employee_menu = self.employee_menu(self.staff_id)
            if employee_menu in ["q", "b"]:
                return admin_manager_menu
        else:
            print(Fore.RED + "Invalid rank. Access denied." + Style.RESET_ALL)

    def select_menu_option_admin_manager(self):
        ''' Admin/Manager menu '''
        #self.clear_screen()
        # Starts by displaying all reports
        self.print_all_reports()
        user_choice = ""
        # Then a while loop is started to keep the menu open until the user wants to go back
        while user_choice != "b":
            # The menu is displayed
            print(f"{self.rank} - Maintenance Report Menu")
            print('-' * 50)
            print("1. Pending reports")
            print("2. Closed reports")
            print('3. Create new reports')
            print('4. Edit report')
            print('b. Go back')
            print('-' * 50)
            # The user is asked to select an option
            user_choice = input("Select an Option: ")
            # The user input is checked and the user is sent to the corresponding menu
            if user_choice == "b":
                self.clear_screen()
                return
            elif user_choice == 'q':
                self.quit_system()
            elif user_choice == '1':
                self.clear_screen()
                self.list_pending_reports()
            elif user_choice == '2':
                self.clear_screen()
                self.list_closed_reports()
            elif user_choice == '3':
                self.clear_screen()
                self.display_create_maintenance_report_form()
            elif user_choice == '4':
                self.clear_screen()
                self.edit_report_details(self.location)
            else:
                print(Fore.RED + "Invalid input" + Style.RESET_ALL) 

    def employee_menu(self, staff_id):
        ''' Employee menu '''
        #self.clear_screen()
        # A function is called to get all the reports connected to the employee logged in
        self.get_employee_reports(staff_id)
        self.print_all_reports
        user_choice = ""
        # A while loop is started to keep the menu open until the user wants to go back
        while user_choice != "b":
            print(f"{self.rank} - Maintenance Report Menu")
            print('-' * 50)
            print("1. Create maintenance report")
            print("2. View Incomplete Reports")
            print("3. View Denied Reports")
            print("b. Go back")
            print('-' * 50)
            # The user is asked to select an option
            user_choice = input("Select an Option:  ")
            # The user input is checked and the user is sent to the corresponding menu
            if user_choice == "b":
                self.clear_screen()
                return
            elif user_choice == 'q':
                self.quit_system()
            elif user_choice == '1':
                    self.clear_screen()
                    self.display_create_maintenance_report_form()
            elif user_choice == '2':
                self.clear_screen()
                self.get_incomplete_reports()
            elif user_choice == '3':
                self.clear_screen()
                self.view_denied_reports(self.staff_id, self.location)
            else:
                print(Fore.RED + "Invalid input" + Style.RESET_ALL)
                
    def get_incomplete_reports(self):
        '''displays all incomplete reports'''
        # Display a list of incomplete reports so the user can go back and finish them
        # Create a table to display the reports
        incomplete_reports_table = PrettyTable()
        incomplete_reports_table.title = 'Incomplete Reports'
        incomplete_reports_table.field_names = ['Report ID', 'Report Name', 'Property ID']

        # Get a list of all incomplete reports
        incomplete_report_list = self.logic_wrapper.get_incomplete_maintenance_reports()
        # Loop through the list, adding all the reports to the table
        if incomplete_report_list == []:
            print('No Incomplete Reports!')
            return
        
        for report in incomplete_report_list:
            incomplete_reports_table.add_row([report.report_id, report.report_name, report.property_id])
        # Some settings for the table like setting the border color as blue
        border_color = Fore.BLUE
        # Making a reset color so the color doesn't stay blue
        reset_color = Style.RESET_ALL
        # Toggling the border on
        incomplete_reports_table.border = True
        # Setting all the elements off the table border to blue
        incomplete_reports_table.junction_char = f"{border_color}+{reset_color}"
        incomplete_reports_table.horizontal_char = f"{border_color}-{reset_color}"
        incomplete_reports_table.vertical_char = f"{border_color}|{reset_color}"
        # Then print the table
        print(incomplete_reports_table)
        # Ask the user to select a report to finish
        user_choice = input('Enter report ID: ')
        if user_choice.lower() == 'b':
            self.clear_screen()
            return
        
        elif user_choice == 'q':
            self.quit_system()
        # A check to make sure the report is in the system
        is_report_in_system = self.logic_wrapper.sanity_check_maintencance_report('report id', user_choice, self.location)
        # If the report is in the system the user is sent to the menu to finish the report
        if is_report_in_system == True:
            self.finish_incomplete_report(user_choice)
        else:
            # If the report is not in the system the user is asked to try again
            print(Fore.RED + 'Report ID not found in system please try again' + Style.RESET_ALL)
            time.sleep(1.5)
            self.clear_screen()
            self.get_incomplete_reports()

    def finish_incomplete_report(self, report_id):
        """Function so an employee can finish an incomplete report"""
        # Get the report from the system
        report = self.logic_wrapper.get_single_maintenance_report(report_id)
        # This is used to keep the loop going until the report is finished
        report_complete = False
        # These are used to check if a field in the report is empty so the user can pickup where they left off
        name_empty = not bool(report.report_name)
        location_empty = not bool(report.location)
        property_id_empty = not bool(report.property_id)
        staff_id_empty = not bool(report.staff_id)
        regular_maintenance_empty = not bool(report.regular_maintenance)
        maintenance_description_empty = not bool(report.maintenance_description)
        price_empty = not bool(report.price)
        contractor_id_empty = not bool(report.contractor_id)
        work_request_id_empty = not bool(report.work_request_id)
        
        # A while loop is started to get all required information to finish the report
        while report_complete == False:
            # Here is check if the user has finished the report
            if name_empty == False and location_empty == False and property_id_empty == False and staff_id_empty == False and regular_maintenance_empty == False and maintenance_description_empty == False and price_empty == False and contractor_id_empty == False and work_request_id_empty == False:
                report_complete = True
                # The report status is set to pending and the report is saved in the system with the updated information
                report.set_report_status('Pending')
                self.logic_wrapper.edit_maintencance_report(report, self.location, 'Report Status', 'Pending')
                print(Fore.GREEN + 'Report has been completed' + Style.RESET_ALL)
                time.sleep(1.5)
                self.clear_screen()
            
            # If the report name is empty the user is asked to fill it out
            elif name_empty == True:
                report_name = input('Enter report name: ')
                # A check to make sure the input is valid
                valid_name = self.logic_wrapper.sanity_check_maintencance_report('report name', report_name, self.location)
                # If the input is valid the report name is updated
                if valid_name == True:
                    name_empty = False
                    self.logic_wrapper.edit_maintencance_report(report, self.location, 'Report Name', report_name)
                else:
                    print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

            # If the location is empty the user is asked to fill it out
            elif location_empty == True:
                location = input('Enter location: ')
                # A check to make sure the input is valid
                valid_location = self.logic_wrapper.sanity_check_maintencance_report('location', location, self.location)
                # If the input is valid the location is updated
                if valid_location == True:
                    location_empty = False
                    self.logic_wrapper.edit_maintencance_report(report, self.location, 'Location', location)
                else:
                    print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

            # If the property ID is empty the user is asked to fill it out
            elif property_id_empty == True:
                property_id = input('Enter property ID (P*): ')
                # A check to make sure the input is valid
                valid_property_id = self.logic_wrapper.sanity_check_maintencance_report('property id', property_id, self.location)
                # If the input is valid the property ID is updated
                if valid_property_id == True:
                    property_id_empty = False
                    self.logic_wrapper.edit_maintencance_report(report, self.location, 'Property ID', property_id)
                else:
                    print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

            # If the staff ID is empty the user is asked to fill it out
            elif staff_id_empty == True:
                staff_id = input('Enter staff ID (E*): ')
                # A check to make sure the input is valid
                valid_staff_id = self.logic_wrapper.sanity_check_maintencance_report('staff id', staff_id, self.location)
                # If the input is valid the staff ID is updated
                if valid_staff_id == True:
                    staff_id_empty = False
                    self.logic_wrapper.edit_maintencance_report(report, self.location, 'Staff ID', staff_id)
                else:
                    print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

            # If the regular maintenance is empty the user is asked to fill it out
            elif regular_maintenance_empty == True:
                regular_maintenance = input('Regular Maintenance (yes/no): ')
                # A check to make sure the input is valid
                valid_regular_maintenance = self.logic_wrapper.sanity_check_maintencance_report('regular maintenance', regular_maintenance, self.location)
                # If the input is valid the regular maintenance is updated
                if valid_regular_maintenance == True:
                    regular_maintenance_empty = False
                    self.logic_wrapper.edit_maintencance_report(report, self.location, 'Regular', regular_maintenance)
                else:
                    print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

            # If the maintenance description is empty the user is asked to fill it out
            elif maintenance_description_empty == True:
                maintenance_description = input('Enter maintenance description: ')
                # A check to make sure the input is valid
                valid_maintenance_description = self.logic_wrapper.sanity_check_maintencance_report('maintenance description', maintenance_description, self.location)
                # If the input is valid the maintenance description is updated
                if valid_maintenance_description == True:
                    maintenance_description_empty = False
                    self.logic_wrapper.edit_maintencance_report(report, self.location, 'Description', maintenance_description)
                else:
                    print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

            # If the price is empty the user is asked to fill it out
            elif price_empty == True:
                price = input('Enter price: ')
                # A check to make sure the input is valid
                valid_price = self.logic_wrapper.sanity_check_maintencance_report('cost', price, self.location)
                # If the input is valid the price is updated
                if valid_price == True:
                    price_empty = False
                    self.logic_wrapper.edit_maintencance_report(report, self.location, 'Cost', price)
                else:
                    print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

            # If the contractor ID is empty the user is asked to fill it out
            elif contractor_id_empty == True:
                contractor_id = input('Enter contractor ID (C*): ')
                # A check to make sure the input is valid
                valid_contractor_id = self.logic_wrapper.sanity_check_maintencance_report('contractor id', contractor_id, self.location)
                # If the input is valid the price is updated
                if valid_contractor_id == True:
                    contractor_id_empty = False
                    self.logic_wrapper.edit_maintencance_report(report, self.location, 'Contractor ID', contractor_id)
                else:
                    print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

            # If the work request ID is empty the user is asked to fill it out
            elif work_request_id_empty == True:
                work_request_id = input('Enter work request ID (WR*): ')
                # A check to make sure the input is valid
                valid_work_request_id = self.logic_wrapper.sanity_check_maintencance_report('work request id', work_request_id, self.location)
                # If the input is valid the work request ID is updated
                if valid_work_request_id == True:
                    work_request_id_empty = False
                    self.logic_wrapper.edit_maintencance_report(report, self.location, 'Work Request ID', work_request_id)
                else:
                    print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

    def list_pending_reports(self):
        """ Displays a list of pending reports in the system """
        #self.clear_screen()
        #Display a list of pending reports
        print(f"{self.rank} - Maintenance Report Menu")
        if_reports = self.get_pending_reports()
        print("-" * 70)
        if if_reports == False:
            return
        report_id = input("Enter report ID to manage: ")
        if report_id.lower() == 'b':
            self.clear_screen()
            return
        elif report_id.lower() == 'q':
             self.quit_system()
        report_in_system = self.logic_wrapper.check_if_report_in_system(report_id, self.location)
        if report_in_system == True:
            self.clear_screen()
            selected_report = self.logic_wrapper.get_single_maintenance_report(report_id)
            self.print_single_maintenance_report(selected_report)
            print("1. Accept")
            print("2. Deny")
            print('b. Go back')
            print("-" * 70)
            valid_choice = False
            accept_or_deny = ''
            while valid_choice == False:
                choice = input("Choose: ")
                if choice == "1":
                    valid_choice = True
                    accept_or_deny = 'Accept'
                    self.logic_wrapper.deny_or_accept_maintencance_report_for_admin(report_id, self.location, accept_or_deny)
                    print(Fore.GREEN + f"Report {report_id} has been accepted." + Style.RESET_ALL)
                    time.sleep(1.5)
                    self.clear_screen()

                elif choice == "2":
                    valid_choice = True
                    accept_or_deny = 'Deny'
                    self.logic_wrapper.deny_or_accept_maintencance_report_for_admin(report_id, self.location, accept_or_deny)
                    print(Fore.RED + f"Report {report_id} has been denied." + Style.RESET_ALL)
                    time.sleep(1.5)
                    self.clear_screen()

                elif choice == 'b':
                    valid_choice = True
                    self.clear_screen()

                elif choice == 'q':
                    self.quit_system()
                else:
                    print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Report ID not found in system please try again' + Style.RESET_ALL)
            time.sleep(1.5)
            self.clear_screen()
            self.list_pending_reports()

    def list_closed_reports(self):
        ''' Display a list of closed reports '''
        print(f"{self.rank} - Maintenance Report Menu")
        is_reports = self.get_closed_reports()
        if is_reports == False:
            return
        print("-" * 70)
        report_id = input("Enter report ID to manage: ")
        if report_id.lower() == 'b':
            self.clear_screen()
            return
        elif report_id.lower() == 'q':
             self.quit_system()
        report_in_system = self.logic_wrapper.check_if_report_in_system(report_id, self.location)
        if report_in_system == True:
            self.clear_screen()
            selected_report = self.logic_wrapper.get_single_maintenance_report(report_id)
            self.print_single_maintenance_report(selected_report)
            print("-" * 70)
            print('1. Reopen Report')
            print('b. Go back')
            print("-" * 70)
            valid_choice = False
            while valid_choice == False:
                choice = input('Choose: ')
                if choice == 'b':
                    self.clear_screen()
                    valid_choice = True

                elif choice == 'q':
                    self.quit_system()

                elif choice == '1':
                    valid_choice = True
                    self.logic_wrapper.reopen_closed_report(selected_report, selected_report.location)
                    print(Fore.GREEN + f'Report {report_id} has been reopened' + Style.RESET_ALL)
                    time.sleep(1.5)
                    self.clear_screen()
                else:
                    print(Fore.RED + 'Invalid choice' + Style.RESET_ALL)

    def get_pending_reports(self) -> bool:
        """ Display a list of pending reports """
        #self.clear_screen()
        '''displays all pending report'''
        pending_reports_table = PrettyTable()
        pending_reports_table.title = 'Pending Reports'
        pending_reports_table.field_names = ['Report ID', 'Report Name', 'Property ID']
        print('List of pending reports\n')

        pending_report_list = self.logic_wrapper.get_all_pending_maintenance_reports(self.location)
        if pending_report_list == 'No pending Reports':
            print('No Pending Reports!')
            return False
        else:
            for report in pending_report_list:
                pending_reports_table.add_row([report.report_id, report.report_name, report.property_id])
            border_color = Fore.BLUE
            reset_color = Style.RESET_ALL
            pending_reports_table.border = True
            pending_reports_table.junction_char = f"{border_color}+{reset_color}"
            pending_reports_table.horizontal_char = f"{border_color}-{reset_color}"
            pending_reports_table.vertical_char = f"{border_color}|{reset_color}"
            print(pending_reports_table)
            return True

    def get_closed_reports(self) -> bool:
        """ Display a list of closed reports """
        #self.clear_screen()
        """ Display a list of closed reports """
        closed_report_table = PrettyTable()
        closed_report_table.title = 'Closed Reports'
        closed_report_table.field_names = ['Report ID', 'Report Name', 'Property ID', 'Report Status']
        print("List of closed reports\n")
        closed_report_list = self.logic_wrapper.get_all_closed_maintenance_reports(self.location)
        if closed_report_list == 'No closed reports':
            print('No Closed Reports!')
            return False
        else:
            for report in closed_report_list:
                closed_report_table.add_row([report.report_id, report.report_name, report.property_id, report.report_status])

            border_color = Fore.BLUE
            reset_color = Style.RESET_ALL
            closed_report_table.border = True
            closed_report_table.junction_char = f"{border_color}+{reset_color}"
            closed_report_table.horizontal_char = f"{border_color}-{reset_color}"
            closed_report_table.vertical_char = f"{border_color}|{reset_color}"
            print(closed_report_table)
            return True

    def display_create_maintenance_report_form(self):
        """ Display the form for creating a new maintenance report """
        #self.clear_screen()
        #Create a new maintenance report
        print('Creating a new maintenance report, type "cancel" to stop and save as incomplete at any time')
        #the details that need to be filled out
        is_valid_report_name = False
        is_valid_location = False
        is_valid_property_id = False
        is_valid_staff_id = False
        is_valid_regular_maintenance = False
        is_valid_maintenance_description = False
        is_valid_price = False
        is_valid_contractor_id = False
        is_valid_work_request_id = False
        report_name = ''
        location = ''
        property_id = ''
        staff_id = ''
        regular_maintenance = ''
        maintenance_description = ''
        price = 0
        contractor_id = ''
        work_request_id = ''
        mark_as_done = False

        while is_valid_report_name == False:
            report_name = input("Enter a name for the report: ")
            if report_name.lower() == 'cancel':
                report_name = ''
                self.create_new_maintenance_report(report_name, location, property_id, staff_id, regular_maintenance, maintenance_description, 'Incomplete', price, mark_as_done, contractor_id, work_request_id)
                return
            is_valid_report_name = self.logic_wrapper.sanity_check_maintencance_report('report name', report_name, self.location)
            if is_valid_report_name == False:
                print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

        if self.rank == 'Employee' or self.rank == 'Manager':
            location = self.location
        elif self.rank == 'Admin':  
            while is_valid_location == False:
                location = input('Enter location name: ')
                if location.lower() == 'cancel':
                    location = ''
                    self.create_new_maintenance_report(report_name, location, property_id, staff_id, regular_maintenance, maintenance_description, 'Incomplete', price, mark_as_done, contractor_id, work_request_id)
                    return
                is_valid_location = self.logic_wrapper.sanity_check_maintencance_report('location', location, self.location)
                if is_valid_location == False:
                    print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

        while is_valid_property_id == False:
            property_id = input("Enter property ID (P*): ")
            if property_id.lower() == 'cancel':
                property_id = ''
                self.create_new_maintenance_report(report_name, location, property_id, staff_id, regular_maintenance, maintenance_description, 'Incomplete', price, mark_as_done, contractor_id, work_request_id)
                return
            is_valid_property_id = self.logic_wrapper.sanity_check_maintencance_report('property id', property_id, self.location)
            if is_valid_property_id == False:
                print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

        while is_valid_staff_id == False:
            staff_id = input("Enter employee ID (E*): ")
            if staff_id.lower() == 'cancel':
                staff_id = ''
                self.create_new_maintenance_report(report_name, location, property_id, staff_id, regular_maintenance, maintenance_description, 'Incomplete', price, mark_as_done, contractor_id, work_request_id)
                return
            is_valid_staff_id = self.logic_wrapper.sanity_check_maintencance_report('staff id', staff_id, self.location)
            if is_valid_staff_id == False:
                print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

        while is_valid_regular_maintenance == False:
            regular_maintenance = input("Is it scheduled? (yes/no): ")
            if regular_maintenance.lower() == 'cancel':
                regular_maintenance = ''
                self.create_new_maintenance_report(report_name, location, property_id, staff_id, regular_maintenance, maintenance_description, 'Incomplete', price, mark_as_done, contractor_id, work_request_id)
                return
            is_valid_regular_maintenance = self.logic_wrapper.sanity_check_maintencance_report('regular maintenance', regular_maintenance, self.location)
            if is_valid_regular_maintenance == False:
                print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

        while is_valid_maintenance_description == False:
            maintenance_description = input('Enter maintenance description: ')
            if maintenance_description.lower() == 'cancel':
                maintenance_description = ''
                self.create_new_maintenance_report(report_name, location, property_id, staff_id, regular_maintenance, maintenance_description, 'Incomplete', price, mark_as_done, contractor_id, work_request_id)
                return
            is_valid_maintenance_description = self.logic_wrapper.sanity_check_maintencance_report('maintenance description', maintenance_description, self.location)
            if is_valid_maintenance_description == False:
                print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

        while is_valid_price == False:
            try:
                price = input("Enter a price: ")
                if price == 'cancel':
                    price = 0
                    self.create_new_maintenance_report(report_name, location, property_id, staff_id, regular_maintenance, maintenance_description, 'Incomplete', price, mark_as_done, contractor_id, work_request_id)
                    return
                is_valid_price = self.logic_wrapper.sanity_check_maintencance_report('cost', price, self.location)
                if is_valid_price == False:
                    print(Fore.RED + 'Invalid input' + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + 'Needs to be a number' + Style.RESET_ALL)

        while is_valid_contractor_id == False:
            contractor_id = input('Enter contractor ID (leave empty if no contractor): ')
            if contractor_id.lower() == 'cancel':
                contractor_id = ''
                self.create_new_maintenance_report(report_name, location, property_id, staff_id, regular_maintenance, maintenance_description, 'Incomplete', price, mark_as_done, contractor_id, work_request_id)
                return
            is_valid_contractor_id = self.logic_wrapper.sanity_check_maintencance_report('contractor id', contractor_id, self.location)
            if is_valid_contractor_id == False:
                print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

        while is_valid_work_request_id == False:
            work_request_id = input("Enter the ID of the work request in progress: ")
            if work_request_id.lower() == 'cancel':
                work_request_id = ''
                self.create_new_maintenance_report(report_name, location, property_id, staff_id, regular_maintenance, maintenance_description, 'Incomplete', price, mark_as_done, contractor_id, work_request_id)
                return
            is_valid_work_request_id = self.logic_wrapper.sanity_check_maintencance_report('work request id', work_request_id, self.location)
            if is_valid_work_request_id == False:
                print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

        self.create_new_maintenance_report(report_name, location, property_id, staff_id, regular_maintenance, maintenance_description, 'Pending', price, mark_as_done, contractor_id, work_request_id)

    def create_new_maintenance_report(self, report_name, location, property_id, staff_id, regular_maintenance, maintenance_description, report_status, price, mark_as_done, contractor_id, work_request_id):
        new_maintenance_report = MaintenanceReport('', report_name, location, property_id, staff_id, regular_maintenance,
        maintenance_description, report_status, price, mark_as_done, contractor_id, work_request_id)

        new_maintenance_report_added = self.logic_wrapper.add_new_maintenance_report_to_storage(self.location, new_maintenance_report, regular_maintenance)

    def get_employee_reports(self, staff_id):
        emplyee_report_table = PrettyTable()
        emplyee_report_table.title = staff_id + ' Employee Reports'
        emplyee_report_table.field_names = ['Report ID', 'Report Name', 'Property ID', 'Report Status']

        print(f'List of all reports connected to staff member {staff_id}\n')
        employee_report_list = self.logic_wrapper.get_employee_reports(staff_id)
        for report in employee_report_list:
            emplyee_report_table.add_row([report.report_id, report.report_name, report.property_id, report.report_status])

        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        emplyee_report_table.border = True
        emplyee_report_table.junction_char = f"{border_color}+{reset_color}"
        emplyee_report_table.horizontal_char = f"{border_color}-{reset_color}"
        emplyee_report_table.vertical_char = f"{border_color}|{reset_color}"
        print(emplyee_report_table)

    def print_all_reports(self):
        """Prints all reports"""
        #self.clear_screen()
        '''displays all pending report'''
        print(f'List of all reports at {self.location}\n')
        all_reports_table = PrettyTable()
        all_reports_table.title = 'All Reports'
        all_reports_table.field_names = ['Report ID', 'Report Name', 'Property ID', 'Report Status']
        pending_report_list = self.logic_wrapper.get_all_maintenance_reports_at_location(self.location)
        if pending_report_list == []:
            print(f'No reports in the system at {self.location}')
            time.sleep(1.5)
            self.clear_screen()
        else:
            for report in pending_report_list:
                all_reports_table.add_row([report.report_id, report.report_name, report.property_id, report.report_status])
            border_color = Fore.BLUE
            reset_color = Style.RESET_ALL
            all_reports_table.border = True
            all_reports_table.junction_char = f"{border_color}+{reset_color}"
            all_reports_table.horizontal_char = f"{border_color}-{reset_color}"
            all_reports_table.vertical_char = f"{border_color}|{reset_color}"
            print(all_reports_table)
    
    def edit_report_details(self, location):
        """Edit report details"""
        #self.clear_screen() 
        """Editing report {report_id} (details to be implemented)"""
        edit_report_table = PrettyTable()
        edit_report_table.title = 'Edit Report Details'
        edit_report_table.field_names = ['Report ID', 'Report Name', 'Property ID', 'Report Status']

        all_report_list = self.logic_wrapper.get_all_maintenance_reports_at_location(self.location)
        for report in all_report_list:
            edit_report_table.add_row([report.report_id, report.report_name, report.property_id, report.report_status])

        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        edit_report_table.border = True
        edit_report_table.junction_char = f"{border_color}+{reset_color}"
        edit_report_table.horizontal_char = f"{border_color}-{reset_color}"
        edit_report_table.vertical_char = f"{border_color}|{reset_color}"
        print(edit_report_table)
        print("-" * 70)
        selected_work_request = input('Please type in work request id: ')
        if selected_work_request.lower() == 'b':
            self.clear_screen()
            return
        elif selected_work_request.lower() == 'q':
            self.quit_system()
        report_in_system = self.logic_wrapper.check_if_report_in_system(selected_work_request, self.location)
        if report_in_system == True:
            for report in all_report_list:
                if report.report_id == selected_work_request:
                    maintenance_report_to_use = report
            self.clear_screen()
            self.display_edit_maintenance_report_details(maintenance_report_to_use)
        elif report_in_system == False:
            print(Fore.RED + f'{selected_work_request} not found in the system please try again!' + Style.RESET_ALL)
            time.sleep(1.5)
            self.clear_screen()
            self.edit_report_details(self.location)
        else:
            print(Fore.RED + 'Invalid input' + Style.RESET_ALL)
            time.sleep(1.5)
            self.clear_screen()
            self.edit_report_details(self.location)
            
    def display_edit_maintenance_report_details(self, selected_maintenance_report):
        """ Display the edit maintenance report details menu """
        #self.clear_screen()
        """ Allows editing of maintenance report details. """
        self.clear_screen()
        self.print_single_maintenance_report(selected_maintenance_report)
        edit_choice = ''
        while edit_choice != 'b':
            print(f"Editing details for maintenance report ID: {selected_maintenance_report.report_id}")
            print('1. Change Report Name')
            print('2. Change Staff ID ')
            print('3. Change Regular Maintenance (yes/no)')
            print('4. Change Maintenance Description')
            print('5. Change Cost')
            print('6. Change Contractor ID')
            print('b. Go back')
            print("-" * 70)
            edit_choice = input("Select an option to edit: ")
            
            if edit_choice == 'b':
                self.clear_screen()
                return
            
            elif edit_choice == 'q':
                self.quit_system()

            elif edit_choice == '1':
                is_valid = False
                while is_valid == False:
                    new_report_name = input('Enter new report name: ')
                    is_valid = self.logic_wrapper.sanity_check_maintencance_report('report name', new_report_name, self.location)
                    if is_valid == True:
                        confirm = input(f'Are you sure you want to change the report name to "{new_report_name}"? (yes/no): ')
                        if confirm.lower() == 'yes':
                            print(Fore.GREEN + "Maintenance report details updated successfully!" + Style.RESET_ALL)
                            self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Report Name', new_report_name)
                        else:
                            print(Fore.RED + 'Report name not changed' + Style.RESET_ALL)

            elif edit_choice == '2':
                is_valid = False
                while is_valid == False:
                    new_staff_id = input('Enter new staff ID: ')
                    is_valid = self.logic_wrapper.sanity_check_maintencance_report('staff id', new_staff_id, self.location)
                    if is_valid == True:
                        confirm = input(f'Are you sure you want to change the staff ID to "{new_staff_id}"? (yes/no): ')
                        if confirm.lower() == 'yes':
                            print(Fore.GREEN + "Maintenance report details updated successfully!" + Style.RESET_ALL)
                            self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Staff ID', new_staff_id)
                        else:
                            print(Fore.RED + 'Staff ID not changed' + Style.RESET_ALL)
                
            elif edit_choice == '3':
                is_valid = False
                while is_valid == False:
                    regular_maintenance = input('Regular Maintenance (yes/no)')
                    is_valid = self.logic_wrapper.sanity_check_maintencance_report('regular maintenance', regular_maintenance, self.location)
                    if is_valid == True:
                        confirm = input(f'Are you sure you want to change the regular maintenance to "{regular_maintenance}"? (yes/no): ')
                        if confirm.lower() == 'yes':
                            print(Fore.GREEN + "Maintenance report details updated successfully!" + Style.RESET_ALL)
                            self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Regular', regular_maintenance)
                        else:
                            print(Fore.RED + 'Regular Maintenance not changed' + Style.RESET_ALL)
            
            elif edit_choice == '4':
                is_valid = False
                while is_valid == False:
                    new_report_description = input('Enter new description')
                    is_valid = self.logic_wrapper.sanity_check_maintencance_report('maintenance description', new_report_description, self.location)
                    if is_valid == True:
                        confirm = input(f'Are you sure you want to change the maintenance description to "{new_report_description}"? (yes/no): ')
                        if confirm.lower() == 'yes':
                            print(Fore.GREEN + "Maintenance report details updated successfully!" + Style.RESET_ALL)
                            self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Description', new_report_description)
                        else:
                            print(Fore.RED + 'Maintenance description not changed' + Style.RESET_ALL)
            
            elif edit_choice == '5':
                try:
                    is_valid = False
                    while is_valid == False:
                        new_report_cost = float(input('Enter New Cost'))
                        is_valid = self.logic_wrapper.sanity_check_maintencance_report('cost', new_report_cost, self.location)
                        if is_valid == True:
                            confirm = input(f'Are you sure you want to change the cost to "{new_report_cost}"? (yes/no): ')
                            if confirm.lower() == 'yes':
                                print(Fore.GREEN + "Maintenance report details updated successfully!" + Style.RESET_ALL)
                                self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Cost', new_report_cost)
                            else:
                                print(Fore.RED + 'Cost not changed' + Style.RESET_ALL)
                except ValueError:
                    print('Needs to be a number')
            
            elif edit_choice == '6':
                is_valid = False
                while is_valid == False:
                    new_contractor_id = input('Enter new contractor ID')
                    is_valid = self.logic_wrapper.sanity_check_maintencance_report('contractor id', new_contractor_id, self.location)
                    if is_valid == True:
                        confirm = input(f'Are you sure you want to change the contractor ID to "{new_contractor_id}"? (yes/no): ')
                        if confirm.lower() == 'yes':
                            print(Fore.GREEN + "Maintenance report details updated successfully!" + Style.RESET_ALL)
                            self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Contractor ID', new_contractor_id)
                        else:
                            print(Fore.RED + 'Contractor ID not changed' + Style.RESET_ALL)
            
            else:
                print(Fore.RED + 'Invalid input' + Style.RESET_ALL)
                

        self.display_edit_maintenance_report_details(selected_maintenance_report)

    def view_denied_reports(self, staff_id, location):
        """View denied reports"""
        denied_reports_table = PrettyTable()
        denied_reports_table.title = 'Denied Reports'
        denied_reports_table.field_names = ['Report ID', 'Report Name', 'Property ID', 'Report Status']
        denied_reports = self.logic_wrapper.get_denied_reports(staff_id, location)
        if denied_reports == 'No denied reports':
            print('No denied reports')
            time.sleep(1.5)
            self.clear_screen()
            return
        for report in denied_reports:
            denied_reports_table.add_row([report.report_id, report.report_name, report.property_id, report.report_status])
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        denied_reports_table.border = True
        denied_reports_table.junction_char = f"{border_color}+{reset_color}"
        denied_reports_table.horizontal_char = f"{border_color}-{reset_color}"
        denied_reports_table.vertical_char = f"{border_color}|{reset_color}"
        print(denied_reports_table)
        user_choice = input('Enter report ID: ')
        if user_choice.lower() == 'b':
            self.clear_screen()
            return
        is_report_in_system = self.logic_wrapper.sanity_check_maintencance_report('report id', user_choice, location)
        if is_report_in_system == True:
            self.redo_denied_report(user_choice)
        else:
            print(Fore.RED + 'Report ID not found in system please try again' + Style.RESET_ALL)
            time.sleep(1.5)
            self.clear_screen()
            self.view_denied_reports(staff_id, location)

    def redo_denied_report(self, report_id):
        """Redo denied report"""
        report = self.logic_wrapper.get_single_maintenance_report(report_id)
        report_done = False
        is_valid_report_name = False
        is_valid_staff_id = False
        is_valid_property_id = False
        is_valid_regular_maintenance = False
        is_valid_maintenance_description = False
        is_valid_price = False
        is_valid_contractor_id = False
        is_valid_work_request_id = False
        while report_done == False:
            print("-" * 70)
            print(f"{'Report ID':<30}: {report.report_id}")
            print(f"{'Report Name':<30}: {report.report_name}")
            print(f"{'Location':<30}: {report.location}")
            print(f"{'Property ID':<30}: {report.property_id}")
            print(f"{'Staff ID':<30}: {report.staff_id}")
            print(f"{'Regular Maintenance':<30}: {report.regular_maintenance}")
            print(f"{'Maintenance Description':<30}: {report.maintenance_description}")
            print(f"{'Price':<30}: {report.price}")
            print(f"{'Contractor ID':<30}: {report.contractor_id}")
            print(f"{'Work Request ID':<30}: {report.work_request_id}")
            print("-" * 70)
            print('1. Change Report Name')
            print('2. Change Staff ID ')
            print('3. Change Property ID')
            print('4. Change Regular Maintenance (yes/no)')
            print('5. Change Maintenance Description')
            print('6. Change Cost')
            print('7. Change Contractor ID')
            print('8. Change Work Request ID')
            print('9. Confirm changes')
            print('b. Go back')
            print("-" * 70)
            user_choice = input('Select an option: ')
            if user_choice == 'b':
                self.clear_screen()
                return
            
            elif user_choice == 'q':
                self.quit_system()

            elif user_choice == '1':
                while is_valid_report_name == False:
                    report_name = input('Enter new report name: ')
                    is_valid_report_name = self.logic_wrapper.sanity_check_maintencance_report('report name', report_name, report.location)
                    if is_valid_report_name == True:
                        self.logic_wrapper.edit_maintencance_report(report, report.location, 'Report Name', report_name)
                        print(Fore.GREEN + 'Report name changed' + Style.RESET_ALL)
                    
            
            elif user_choice == '2':
                while is_valid_staff_id == False:
                    staff_id = input('Enter new staff ID (E*): ')
                    is_valid_staff_id = self.logic_wrapper.sanity_check_maintencance_report('staff id', staff_id, report.location)
                    if is_valid_staff_id == True:
                        self.logic_wrapper.edit_maintencance_report(report, report.location, 'Staff ID', staff_id)
                        print(Fore.GREEN + 'Staff ID changed' + Style.RESET_ALL)

            elif user_choice == '3':
                while is_valid_property_id == False:
                    property_id = input('Enter new property ID (P*): ')
                    is_valid_property_id = self.logic_wrapper.sanity_check_maintencance_report('property id', property_id, report.location)
                    if is_valid_property_id == True:
                        self.logic_wrapper.edit_maintencance_report(report, report.location, 'Property ID', property_id)
                        print(Fore.GREEN + 'Property ID changed' + Style.RESET_ALL)
            
            elif user_choice == '4':
                while is_valid_regular_maintenance == False:
                    regular_maintenance = input('Regular Maintenance (yes/no): ')
                    is_valid_regular_maintenance = self.logic_wrapper.sanity_check_maintencance_report('regular maintenance', regular_maintenance, report.location)
                    if is_valid_regular_maintenance == True:
                        self.logic_wrapper.edit_maintencance_report(report, report.location, 'Regular', regular_maintenance)
                        print(Fore.GREEN + 'Regular Maintenance changed' + Style.RESET_ALL)
            
            elif user_choice == '5':
                while is_valid_maintenance_description == False:
                    maintenance_description = input('Enter new maintenance description: ')
                    is_valid_maintenance_description = self.logic_wrapper.sanity_check_maintencance_report('maintenance description', maintenance_description, report.location)
                    if is_valid_maintenance_description == True:
                        self.logic_wrapper.edit_maintencance_report(report, report.location, 'Description', maintenance_description)
                        print(Fore.GREEN + 'Maintenance description changed' + Style.RESET_ALL)

            elif user_choice == '6':
                while is_valid_price == False:
                    try:
                        price = float(input('Enter new price: '))
                        is_valid_price = self.logic_wrapper.sanity_check_maintencance_report('cost', price, report.location)
                        if is_valid_price == True:
                            self.logic_wrapper.edit_maintencance_report(report, report.location, 'Cost', price)
                            print(Fore.GREEN + 'Price changed' + Style.RESET_ALL)
                    except ValueError:
                        print(Fore.RED + 'Needs to be a number' + Style.RESET_ALL)
            
            elif user_choice == '7':
                while is_valid_contractor_id == False:
                    contractor_id = input('Enter new contractor ID (C*): ')
                    is_valid_contractor_id = self.logic_wrapper.sanity_check_maintencance_report('contractor id', contractor_id, report.location)
                    if is_valid_contractor_id == True:
                        self.logic_wrapper.edit_maintencance_report(report, report.location, 'Contractor ID', contractor_id)
                        print(Fore.GREEN + 'Contractor ID changed' + Style.RESET_ALL)

            elif user_choice == '8':
                while is_valid_work_request_id == False:
                    work_request_id = input('Enter new work request ID (WR*): ')
                    is_valid_work_request_id = self.logic_wrapper.sanity_check_maintencance_report('work request id', work_request_id, report.location)
                    if is_valid_work_request_id == True:
                        self.logic_wrapper.edit_maintencance_report(report, report.location, 'Work Request ID', work_request_id)
                        print(Fore.GREEN + 'Work request ID changed' + Style.RESET_ALL)

            elif user_choice == '9':
                self.logic_wrapper.edit_maintencance_report(report, report.location, 'Report Status', 'Pending')
                print(Fore.GREEN + 'Report has been changed to pending' + Style.RESET_ALL)
                report_done = True
                return
            
            else:
                print(Fore.RED + 'Invalid input' + Style.RESET_ALL)

    def print_single_maintenance_report(self, maintenance_report):
        """Prints a single maintenance report"""
        single_report_table = PrettyTable()
        single_report_table.title = 'Maintenance Report'
        single_report_table.field_names = ['Information',"Details"]
        single_report_table.add_row(['Report ID', maintenance_report.report_id])
        single_report_table.add_row(['Report Name', maintenance_report.report_name])
        single_report_table.add_row(['Maintenance Description', maintenance_report.maintenance_description])
        single_report_table.add_row(['Location', maintenance_report.location])
        single_report_table.add_row(['Property ID', maintenance_report.property_id])
        single_report_table.add_row(['Staff ID', maintenance_report.staff_id])
        single_report_table.add_row(['Regular Maintenance', maintenance_report.regular_maintenance])
        single_report_table.add_row(['Price', maintenance_report.price])
        single_report_table.add_row(['Completed', maintenance_report.mark_as_done])
        single_report_table.add_row(['Contractor ID', maintenance_report.contractor_id])
        single_report_table.add_row(['Work Request ID', maintenance_report.work_request_id])


        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        single_report_table.align = 'l'
        single_report_table.border = True
        single_report_table.junction_char = f"{border_color}+{reset_color}"
        single_report_table.horizontal_char = f"{border_color}-{reset_color}"
        single_report_table.vertical_char = f"{border_color}|{reset_color}"
        print(single_report_table)

        print("-" * 70)