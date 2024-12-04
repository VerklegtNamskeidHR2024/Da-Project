class maintenance_report_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location

    def start_point_maintenance_reports_UI(self):
        """Entry point for the maintenance reports UI"""
        self.display_maintenance_report()

    def display_maintenance_report(self):
        if self.rank in ["admin", "manager"]:
            self.admin_or_manager_menu()
        elif self.rank == "Employee":
            self.employee_menu()
        else:
            print("Invalid rank. Access denied.")

    def admin_or_manager_menu(self):
        """Menu for admin or manager roles"""
        print("1. Pending reports")
        print("2. Closed reports")
        user_choice = input("Choose: ")

        if user_choice == "1":
            self.list_pending_reports()
        elif user_choice == "2":
            self.list_closed_reports()
        else:
            print("Invalid choice.")

    def list_pending_reports(self):
        """Display a list of pending reports"""
        print("List of pending reports (to be implemented)")
        report_id = input("Enter report ID to manage: ")
        print("1. Accept")
        print("2. Deny")
        choice = input("Choose: ")

        if choice == "1":
            print(f"Report {report_id} has been accepted.")
        elif choice == "2":
            print(f"Report {report_id} has been denied.")
        else:
            print("Invalid choice.")

    def list_closed_reports(self):
        """Display a list of closed reports"""
        print("List of closed reports (to be implemented)")

    def employee_menu(self):
        """Menu for employee role"""
        print("1. Create maintenance report")
        print("2. Incomplete maintenance reports")
        user_choice = input("Select an option: ")

        if user_choice == "1":
            self.create_maintenance_report()
        elif user_choice == "2":
            self.view_incomplete_reports()
        else:
            print("Invalid choice.")

    def create_maintenance_report(self):
        """Create a new maintenance report"""
        print("Creating a new maintenance report")
        report_name = input("Enter a name for the report: ")
        property_id = input("Enter property ID: ")
        employee_id = input("Enter employee ID: ")
        scheduled = input("Is it scheduled? (yes/no): ")
        work_done = input("What maintenance was done: ")
        report_status = input("Report status (pending/finished): ")
        price = input("Enter a price: ")
        work_request_id = input("Enter the ID of the work request in progress: ")
        # can add contractor also if it applies 
        print("Report created (functionality to be implemented).")

    def view_incomplete_reports(self):
        """View and edit incomplete maintenance reports"""
        print("List of incomplete maintenance reports (to be implemented)")
        report_id = input("Enter report ID to edit: ")
        print("1. Edit maintenance report")
        edit_choice = input("Choose: ")

        if edit_choice == "1":
            self.edit_report_details(report_id)
        else:
            print("Invalid choice.")

    def edit_report_details(self, report_id):
        """Edit the details of a maintenance report"""
        print(f"Editing report {report_id} (details to be implemented)")
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
            print("Editing report details (functionality to be implemented).")
        else:
            print("Invalid choice.")
