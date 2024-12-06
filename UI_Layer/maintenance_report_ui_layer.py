from Model_Classes.maintenance_report_model import MaintenanceReport
class maintenance_report_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location

    def start_point_maintenance_reports_UI(self):
        #Entry point for the maintenance reports UI
        self.display_maintenance_report()
        return

    def display_maintenance_report(self):
        # if the choice is admin or mangers it goes to the admin_or_manager_menu
        if self.rank == "Admin" or self.rank == "Manager":
            self.admin_or_manager_menu()

        #if the choice is employee it goes to employee menu 
        elif self.rank == "Employee":
            self.employee_menu()
        else:
            print("Invalid rank. Access denied.")

    def admin_or_manager_menu(self):
        #Menu for admin or manager roles
        print(f"{self.rank} - Maintenance Report Menu")
        print("------------------------------------------------")
        # choice between 2 choices 
        print("1. Pending reports")
        print("2. Closed reports")
        print('3. Create new reports')
        print('4. Edit report')
        print("------------------------------------------------")
        user_choice = input("Choose: ")

        if user_choice == "1":
            self.list_pending_reports()
        elif user_choice == "2":
            self.list_closed_reports()
        elif user_choice == '3':
            self.display_create_maintenance_report_form()
        elif user_choice == '4':
            self.edit_report_details(self.location)
        else:
            print("Invalid choice.")

    #Completed - And Accepting/Denying Reports
    def list_pending_reports(self):
        #Display a list of pending reports
        print(f"{self.rank} - Maintenance Report Menu")

        """List of pending reports (to be implemented)"""
        self.get_pending_reports()
        print("------------------------------------------------")
        report_id = input("Enter report ID to manage: ")
        report_in_system = self.logic_wrapper.check_if_report_in_system(report_id, self.location)
        if report_in_system == True:
            print("------------------------------------------------")
            print("1. Accept")
            print("2. Deny")
            print("------------------------------------------------")
            valid_choice = False
            accept_or_deny = ''
            while valid_choice == False:
                choice = input("Choose: ")
                if choice == "1":
                    valid_choice = True
                    accept_or_deny = 'Accept'
                    self.logic_wrapper.deny_or_accept_maintencance_report_for_admin(report_id, self.location, accept_or_deny)
                    print(f"Report {report_id} has been accepted.")
                elif choice == "2":
                    valid_choice = True
                    accept_or_deny = 'Deny'
                    self.logic_wrapper.deny_or_accept_maintencance_report_for_admin(report_id, self.location, accept_or_deny)
                    print(f"Report {report_id} has been denied.")
                else:
                    print("Invalid choice.")
        else:
            print('Report ID not found in system please try again')
            self.list_pending_reports()
    
    #Completed
    def get_pending_reports(self):
        '''displays all pending report'''
        print('List of pending reports\n')
        pending_report_list = self.logic_wrapper.get_all_pending_maintenance_reports(self.location)
        for report in pending_report_list:
            print(f'{report.report_id:<10}{report.report_name:<10}{report.property_id:>10}')

    #Completed
    def list_closed_reports(self):
        #Display a list of closed reports
        """need the closed report list here"""
        print("List of closed reports\n")
        closed_report_list = self.logic_wrapper.get_all_closed_maintenance_reports(self.location)
        if closed_report_list == 'No closed reports':
            print('No Closed Reports!')
        else:
            for report in closed_report_list:
                print(f'{report.report_id:<10}{report.report_name:<10}{report.property_id:>10}')
    
    def employee_menu(self):
        #Menu for employee role
        print(f"{self.rank} - Maintenance Report Menu")
        print("------------------------------------------------")
        
        print("1. Create maintenance report")
        print("------------------------------------------------")
        user_action = input("Select an Option:  ")
        match user_action:
            case "1":
                # create maintenance reports 
                self.display_create_maintenance_report_form()
            case "q":
                """quit back to main menu"""
                pass
            case _:
                print("wrong input")

        # test print
        print("we going back to main menu in UI layer")
        return 
 
    #Completed - But needs to do sanity check!
    def display_create_maintenance_report_form(self):
        #Create a new maintenance report
        print("Creating a new maintenance report")
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
        #while loop to check if the input is valid
        while is_valid_report_name == False:
            report_name = input("Enter a name for the report: ")
            is_valid_report_name = self.logic_wrapper.sanity_check_maintencance_report('report name', report_name, self.location)
            if is_valid_report_name == False:
                print('Invalid input')
        while is_valid_location == False:
            location = input('Enter location name: ')
            is_valid_location = self.logic_wrapper.sanity_check_maintencance_report('location', location, self.location)
            if is_valid_location == False:
                print('Invalid input')
        while is_valid_property_id == False:
            property_id = input("Enter property ID: ")
            is_valid_property_id = self.logic_wrapper.sanity_check_maintencance_report('property id', property_id, self.location)
            if is_valid_property_id == False:
                print('Invalid input')

        while is_valid_staff_id == False:
            staff_id = input("Enter employee ID: ")
            is_valid_staff_id = self.logic_wrapper.sanity_check_maintencance_report('staff id', staff_id, self.location)
            if is_valid_staff_id == False:
                print('Invalid input')

        while is_valid_regular_maintenance == False:
            regular_maintenance = input("Is it scheduled? (yes/no): ")
            is_valid_regular_maintenance = self.logic_wrapper.sanity_check_maintencance_report('regular maintenance', regular_maintenance, self.location)
            if is_valid_regular_maintenance == False:
                print('Invalid input')

        while is_valid_maintenance_description == False:
            maintenance_description = input('Enter maintenance description: ')
            is_valid_maintenance_description = self.logic_wrapper.sanity_check_maintencance_report('maintenance description', maintenance_description, self.location)
            if is_valid_maintenance_description == False:
                print('Invalid input')

        while is_valid_price == False:
            try:
                price = float(input("Enter a price: "))
                is_valid_price = self.logic_wrapper.sanity_check_maintencance_report('cost', price, self.location)
                if is_valid_price == False:
                    print('Invalid input')
            except ValueError:
                print('Needs to be a number')

        while is_valid_contractor_id == False:
            contractor_id = input('Enter contractor ID (leave empty if no contractor): ')
            is_valid_contractor_id = self.logic_wrapper.sanity_check_maintencance_report('contractor id', contractor_id, self.location)
            if is_valid_contractor_id == False:
                print('Invalid input')

        while is_valid_work_request_id == False:
            work_request_id = input("Enter the ID of the work request in progress: ")
            is_valid_work_request_id = self.logic_wrapper.sanity_check_maintencance_report('work request id', work_request_id, self.location)
            if is_valid_work_request_id == False:
                print('Invalid input')

        
        
        '''report_name = input("Enter a name for the report: ")
        location = input('Enter location name: ')
        property_id = input("Enter property ID: ")
        staff_id = input("Enter employee ID: ")
        regular_maintenance = bool(input("Is it scheduled? (yes/no): "))
        maintenance_description = input('Enter maintenance description: ')
        price = float(input("Enter a price: "))
        contractor_id = input('Enter contractor ID (leave empty if no contractor): ')
        work_request_id = input("Enter the ID of the work request in progress: ")'''

        new_maintenance_report = MaintenanceReport('', report_name, location, property_id, staff_id, False,
        maintenance_description,'',price, False, contractor_id, work_request_id)

        new_maintenance_report_added = self.logic_wrapper.add_new_maintenance_report_to_storage(self.location, new_maintenance_report, regular_maintenance)

    #WIP
    def edit_report_details(self, location):
        """Editing report {report_id} (details to be implemented)"""
        all_report_list = self.logic_wrapper.get_all_maintenance_reports_at_location(self.location)
        for report in all_report_list:
            print(f'{report.report_id:<10}{report.report_name:<10}')
        print("-" * 70)
        selected_work_request = input('Please type in work request id: ')
        report_in_system = self.logic_wrapper.check_if_report_in_system(selected_work_request, self.location)
        if report_in_system == True:
            for report in all_report_list:
                if report.report_id == selected_work_request:
                    maintenance_report_to_use = report
            self.print_single_maintenance_report(maintenance_report_to_use)
            self.display_edit_maintenance_report_details(maintenance_report_to_use)
        elif report_in_system == False:
            print(f'{selected_work_request} not found in the system please try again!')
            self.edit_report_details()
        else:
            pass
            # print the maintenance report  info
            # self.print_single_maintenance_report(maintenance_report_to_use)

            # Dont see a use for this - Hreimur
            '''print("1. Mark as ready")
            print("2. Edit report details")
            user_input = input("Choose: ")

            match user_input:
                case"1":
                    print(f"Report {report_id} has been marked as ready.")
                case "2":
                    self.display_edit_maintenance_report_details(maintenance_report_to_use)
                case _:
                    print("Invalid choice.")'''

    #Completed - But needs to do sanity check! - And also find incomplete reports
    # need to implement so user can stop making a report mid way through and that would give the report an incomplete status
    def display_edit_maintenance_report_details(self, selected_maintenance_report):
        """ Allows editing of maintenance report details. """
        print(f"Editing details for maintenance report ID: {selected_maintenance_report.report_id}")
        print('1. Change Report Name')
        print('2. Change Staff ID ')
        print('3. Change Regular Maintenance (yes/no)')
        print('4. Change Maintenance Description')
        print('5. Change Cost')
        print('6. Change Contractor ID')
        print('7. Go back')
        print("-" * 70)

        edit_choice = input("Select an option to edit: ")

        match edit_choice:
            case "1":
                is_valid = False
                while is_valid == False:
                    new_report_name = input('Enter new report name: ')
                    is_valid = self.logic_wrapper.sanity_check_maintencance_report('report name', new_report_name, self.location)
                    if is_valid == True:
                        self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Report Name', new_report_name)
            case '2':
                is_valid = False
                while is_valid == False:
                    new_staff_id = input('Enter new staff ID: ')
                    is_valid = self.logic_wrapper.sanity_check_maintencance_report('staff ID', new_staff_id, self.location)
                    if is_valid == True:
                        self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Staff ID', new_staff_id)
                
            case '3':
                is_valid = False
                while is_valid == False:
                    regular_maintenance = input('Regular Maintenance (yes/no)')
                    is_valid = self.logic_wrapper.sanity_check_maintencance_report('regular maintenance', regular_maintenance, self.location)
                    if is_valid == True:
                        self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Regular', regular_maintenance)
            case '4':
                is_valid = False
                while is_valid == False:
                    new_report_description = input('Enter new description')
                    is_valid = self.logic_wrapper.sanity_check_maintencance_report('maintenance description', new_report_description, self.location)
                    if is_valid == True:
                        self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Description', new_report_description)
            case '5':
                try:
                    is_valid = False
                    while is_valid == False:
                        new_report_cost = float(input('Enter New Cost'))
                        is_valid = self.logic_wrapper.sanity_check_maintencance_report('cost', new_report_cost, self.location)
                        if is_valid == True:
                            self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Cost', new_report_cost)
                except ValueError:
                    print('Needs to be a number')
            case '6':
                is_valid = False
                while is_valid == False:
                    new_contractor_id = input('Enter new contractor ID')
                    is_valid = self.logic_wrapper.sanity_check_maintencance_report('contractor id', new_contractor_id, self.location)
                    if is_valid == True:
                        self.logic_wrapper.edit_maintencance_report(selected_maintenance_report, self.location, 'Contractor ID', new_contractor_id)
            case '7':
                self.admin_or_manager_menu()
            case _:
                print("Invalid input")

        print("Maintenance report details updated successfully!")
        self.display_edit_maintenance_report_details(selected_maintenance_report)

    def print_single_maintenance_report(self, maintenance_report):
            print("-"*30)
            print(f"{'Report ID':<15}: {maintenance_report.report_id}")
            print(f"{'Report Name':<15}: {maintenance_report.report_name}")
            print(f"{'Maintenance Description':<15}: {maintenance_report.maintenance_description}")
            print(f"{'Location':<15}: {maintenance_report.location}")
            print(f"{'Property ID':<15}: {maintenance_report.property_id}")
            print(f"{'Staff ID':<15}: {maintenance_report.staff_id}")
            print(f"{'Regular Maintenance':<15}: {maintenance_report.regular_maintenance}")
            print(f"{'Price':<15}: {maintenance_report.price}")
            print(f"{'Completed':<15}: {maintenance_report.mark_as_done}")
            print(f"{'Contractor ID':<15}: {maintenance_report.contractor_id}")
            print(f"{'Work Request ID':<15}: {maintenance_report.work_request_id}")
            print("-"*30)