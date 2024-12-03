class employee_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
    
    def display_all_employees():
        pass

    def action_choice():
        search_or_add = int(input("Enter choice: "))
        if search_or_add == 1:
            pass
        elif search_or_add == 2:
            pass

    def search_employee():
        employee_ssn = int(input("Enter The Social Security Number: "))

    def display_employee():
        pass

    def add_employee():
        employee_name = input("Enter Employee Name: ")
        employee_ssn = int(input("Enter Employee Social Security: "))
        employee_phone_number = int(input("Enter Employee Phone Number: "))
        employee_location = input("Enter Employee Location: ")
        employee_email = input("Enter Email: ")

    def edit_employee():
        pass

    def display_edit_options():
        print()
        print("1. Change Phone Number: ")
        print("2. Change Location: ")
        print("3. Change Email: ")

    def display_employee_work_requests():
        pass

    def display_employee_maintenance_report():
        pass