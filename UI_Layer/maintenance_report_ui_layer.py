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
        if self.rank in ["Admin", "Manager"]:
            self.admin_or_manager_menu()
        #if the choice is employee it goes to employee menu 
        elif self.rank == "Employee":
            self.employee_menu()
        else:
            print("Invalid rank. Access denied.")

    def admin_or_manager_menu(self):
        #Menu for admin or manager roles
        print(f"{self.rank} - maintenance report Page")
        print("------------------------------------------------")
        # choice between 2 choices 
        print("1. Pending reports")
        print("2. Closed reports")
        print("------------------------------------------------")
        user_choice = input("Choose: ")

        if user_choice == "1":
            self.list_pending_reports()
        elif user_choice == "2":
            self.list_closed_reports()
        else:
            print("Invalid choice.")

    def list_pending_reports(self):
        #Display a list of pending reports
        print(f"{self.rank} - maintenance report Page")

        """List of pending reports (to be implemented)"""
        self.get_pending_reports()
        print("------------------------------------------------")
        report_id = input("Enter report ID to manage: ")
        print("------------------------------------------------")
        print("1. Accept")
        print("2. Deny")
        print("------------------------------------------------")
        choice = input("Choose: ")

        if choice == "1":
            print(f"Report {report_id} has been accepted.")
        elif choice == "2":
            print(f"Report {report_id} has been denied.")
        else:
            print("Invalid choice.")

    def get_pending_reports(self):
            pending_report_list = self.logic_wrapper.get_all_pending_maintenance_reports(self.location)
            print(pending_report_list)
            for report in pending_report_list:
                print(report)

    def list_closed_reports(self):
        #Display a list of closed reports
        """need the closed report list here"""
        print("List of closed reports (to be implemented)")

    def employee_menu(self):
        #Menu for employee role
        print(f"{self.rank} - maintenance report Page")

        print("------------------------------------------------")
        print("1. Create maintenance report")
        print("2. Incomplete maintenance reports")
        print("------------------------------------------------")
        user_action = input("Select an Option:  ")
        match user_action:
            case "1":
                # create maintenance reports 
                self.display_create_maintenance_report_form()
            case "2":
                # view incomplete reports
                 self.view_incomplete_reports()
            case "q":
                """quit back to main menu"""
                pass
            case _:
                print("wrong input")

        # test print
        print("we going back to main menu in UI layer")
        return 

        

    def display_create_maintenance_report_form(self):
        #Create a new maintenance report
        new_maintenance_report = MaintenanceReport()
        print("Creating a new maintenance report")
        #the details that need to be filled out
        new_maintenance_report.set_report_name = input("Enter a name for the report: ")
        new_maintenance_report.set_property_id = input("Enter property ID: ")
        new_maintenance_report.set_employee_id = int(input("Enter employee ID: "))
        new_maintenance_report.set_scheduled = input("Is it scheduled? (yes/no): ")
        new_maintenance_report.set_work_done = input("What maintenance was done: ")
        new_maintenance_report.set_report_status = input("Report status (pending/finished): ")
        new_maintenance_report.set_price = input("Enter a price: ")
        new_maintenance_report.set_work_request_id = input("Enter the ID of the work request in progress: ")
        # can add contractor also if it applies 
        try:
            new_maintenance_report_added = self.logic_wrapper.add_new_maintenance_report(new_maintenance_report)
            if new_maintenance_report_added == True:
                print("maintenance report has been added")
            
        except:
            print("something went wrong with making new maintenance report")

        print(new_maintenance_report.report_name)
        print(new_maintenance_report.property_id)
        print(new_maintenance_report.employee_id)
        print(new_maintenance_report.scheduled)
        print(new_maintenance_report.work_done)
        print(new_maintenance_report.report_status)
        print(new_maintenance_report.price)
        print(new_maintenance_report.work.request_id)

    def view_incomplete_reports(self):
        # View and edit incomplete maintenance reports"""
        """need here list of incomplete maintenance report"""
        report_id = input("Enter report ID to edit: ")
        print("1. Edit maintenance report")
        edit_choice = input("Choose: ")
        match edit_choice:
            case "1":
                self.edit_report_details(report_id)
            case "q":
                #quit back to mainmenu
                pass
            case _:
                print("wrong input")

    def edit_report_details(self, report_id):
        #Edit the details of a maintenance report
        """Editing report {report_id} (details to be implemented)"""
       
        try:
            maintenance_report_to_use = self.selected_maintenance_report_by_id()
            if maintenance_report_to_use == None:
                return
        except:
            print("something went wrong")

        # print the maintenance report  info
        self.print_single_maintenance_report(maintenance_report_to_use)

        print("1. Mark as ready")
        print("2. Edit report details")
        user_input = input("Choose: ")

        match user_input:
            case"1":
                print(f"Report {report_id} has been marked as ready.")
            case "2":
                pass
                display_edit_maintenance_report_details()
            case _:
                print("Invalid choice.")

    
    def display_edit_maintenance_report_details(self, selected_maintenance_report):
        """
        Allows editing of maintenance report details.
        """
        print(f"Editing details for maintenance report ID: {selected_maintenance_report.report_id}")
        print("1. Change Property ID")
        print("2. Change Staff ID")
        print("3. Change Contractor ID")
        print("4. Change Scheduled Date")
        print("5. Change Work Done")
        print("6. Change Status")
        print("7. Change Price")
        print("-" * 70)

        edit_choice = input("Select an option to edit: ")

        match edit_choice:
            case "1":
                new_property_id = input("Enter new Property ID: ")
                selected_maintenance_report.property_id = new_property_id
                print("Property ID updated successfully.")
            case "2":
                new_staff_id = input("Enter new Staff ID: ")
                selected_maintenance_report.staff_id = new_staff_id
                print("Staff ID updated successfully.")
            case "3":
                new_contractor_id = input("Enter new Contractor ID: ")
                selected_maintenance_report.contractor_id = new_contractor_id
                print("Contractor ID updated successfully.")
            case "4":
                new_scheduled_date = input("Enter new Scheduled Date: ")
                selected_maintenance_report.scheduled_date = new_scheduled_date
                print("Scheduled Date updated successfully.")
            case "5":
                new_work_done = input("Enter new Work Done description: ")
                selected_maintenance_report.work_done = new_work_done
                print("Work Done updated successfully.")
            case "6":
                new_status = input("Enter new Status: ")
                selected_maintenance_report.status = new_status
                print("Status updated successfully.")
            case "7":
                try:
                    new_price = float(input("Enter new Price: "))
                    selected_maintenance_report.price = new_price
                    print("Price updated successfully.")
                except ValueError:
                    print("Invalid input.")
            case _:
                print("Invalid input")
        print("Maintenance report details updated successfully!")

    def print_single_maintenance_report(self, maintenance_report):
            print("-"*30)
            print(f"{'Property ID':<15}: {maintenance_report.property_id}")
            print(f"{'Staff ID':<15}: {maintenance_report.property_name}")
            print(f"{'Contractor ID':<15}: {maintenance_report.contractor_id}")
            print(f"{'Scheduled date':<15}: {maintenance_report.scheduled_date}")
            print(f"{'Work done':<15}: {maintenance_report.work_done}")
            print(f"{'Status':<15}: {maintenance_report.status}")
            print(f"{'Price':<15}: {maintenance_report.price}")
            print("-"*30)