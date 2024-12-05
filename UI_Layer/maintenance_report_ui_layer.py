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
        elif self.rank == "Employee":
            self.employee_menu()
        else:
            print("Invalid rank. Access denied.")

    def admin_or_manager_menu(self):
        #Menu for admin or manager roles
        print(f"{self.rank} - maintenance report Page")
        print("------------------------------------------------")
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

    def list_closed_reports(self):
        #Display a list of closed reports
        """need the closed report list here"""
        print("List of closed reports (to be implemented)")

    def employee_menu(self):
        #Menu for employee role
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
        print("""Property ID: (1503)
Staff ID: (26)
Contractor ID: (x)
Scheduled: yes
Work done: Clean windows
Status: pending
Price: 0kr
Report ID: (2)""")
        print("1. Mark as ready")
        print("2. Edit report details")
        user_input = input("Choose: ")

        if user_input == "1":
            print(f"Report {report_id} has been marked as ready.")
        elif user_input == "2":
            pass
            """Editing report details (functionality to be implemented)"""
        else:
            print("Invalid choice.")

    
