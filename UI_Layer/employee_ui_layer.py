from Model_Classes.employee_model import Employee

class employee_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
    
    def start_point_employee_UI(self):
        # when this class is called it starts here
        # call other functions in class from here
        self.display_all_employees()
        if self.rank == "Manager" or self.rank == "Admin":
            action = self.action_choice()
            if action == 1:
                self.search_employee()
                #sanity check
                    #display_employee()
                    #choice = employee_options()
                    #if choice == 1:
                        #edit_choice = display_edit_options()
                        #if edit_choice == 1:
                            #edit_employee_phone_number()
                        #elif edit_choice == 2:
                            #edit_employee_location()
                        #elif edit_choice == 3:
                            #edit_employee_email()
                    #elif choice == 2:
                        #display_employee_work_requests()
                    #elif choice == 3:
                        #display_employee_maintenance_report()
            elif action == 2:
                self.add_employee()

            else:
                print("Somthing wrong")

    def display_all_employees(self):
        """The function displays a table with all employees at a location and their basic information"""
        employee_list = self.logic_wrapper.get_all_employees_at_location(self.location)
        print("-" * 75)
        print("{:>15}{:>10}{:>15}".format("Name", "Phone", "Location"))
        print("-" * 75)

        for item in employee_list:
            print("{:>15}{:>10}{:>15}".format(item.name, item.phone_number, item.location))
            # print(f"{item.name :> 15}|{item.phone_number :> 10}|{item.email :> 10}|{self.location :> 15}")
        print("-" * 75)

    def action_choice(self) -> int:
        """The function is asking the user if they want to search or add an employee"""
        
        print()
        print("1. Search Employee")
        print("2. Add Employee")
        print("-" * 35)
        search_or_add = int(input("Enter choice: "))
        return search_or_add 
        

    def search_employee(self) -> int:
        """The Function Is Searching For An Employee by SSN""" 

        print()
        employee_ssn = int(input("Enter Employee Social Security Number: "))
        return employee_ssn


    def display_employee(self, employee):
        """The function displays an employee and all their information"""
        
        print()
        print("-" * 70)
        print("{:<15}{:<10}{:<15}".format("Employee Name", "|", employee.name))
        print("{:<15}{:<10}{:<15}".format("Social Security Number", "|", employee.social_security_number))
        print("{:<15}{:<10}{:<15}".format("Phone Number", "|", employee.phone_number))
        print("{:<15}{:<10}{:<15}".format("Location", "|", employee.location))
        print("{:<15}{:<10}{:<15}".format("Email", "|", employee.email))
        print("{:<15}{:<10}{:<15}".format("Employee ID", "|", employee.staff_id))

        # print(f"{"Employee Name" :< 15}| {employee.name}")
        # print(f"{"Social Security Number" :< 15}| {employee.social_security_number}")
        # print(f"{"Phone Number" :< 15}| {employee.phone_number}")
        # print(f"{"Location"}| {employee.location}")
        # print(f"{"Email":< 15}| {employee.email}")
        # print(f"{"Staff ID"}| {employee.staff_id}")
        print("-" * 70)

    def employee_options(self) -> int:
        print()
        print("1. Edit Employee Details")
        print("2. View Work Requests")
        print("3. View Maintenance Report")
        print("-" * 70)
        option = int(input("Enter Choice: "))
        return option

    def add_employee(self):
        """The function asks for all the information needed for regestering an employee"""
        new_employee = Employee()

        new_employee.set_name(input("Enter Employee Name: "))
        new_employee.set_social_security_number(int(input("Enter Employee Social Security: ")))
        new_employee.set_phone_number(int(input("Enter Employee Phone Number: ")))
        new_employee.set_location(input("Enter Employee Location: "))
        new_employee.set_email(input("Enter Email: "))


    def display_edit_options(self) -> int:
        """The Function displays and asks for the edit option"""
        print()
        print("1. Change Phone Number: ")
        print("2. Change Location: ")
        print("3. Change Email: ")
        print("-" * 70)
        edit_choice = int(input("Enter Your Edit Choice: "))
        return edit_choice

    def edit_employee_phone_number(self, employee):
        """This function sets a new phone number for the employee"""
        try:
            new_phone_number = int(input("Enter New Phone Number: "))
            employee.set_phone_number(new_phone_number)
            #sanity check?
        except:
            print("Somthing Went Wrong")
    
    def edit_employee_location(self, employee):
        """This function sets a new location for the employee"""
        try:
            new_location = input("Enter New Location")
            employee.set_location(new_location)
            #sanity check?
        except:
            print("Somthing Went Wrong")

    def edit_employee_email(self, employee):
        """This function sets a new email for the employee"""
        try:
            new_email = int(input("Enter New Email: "))
            employee.set_email(new_email)
            #sanity check?
        except:
            print("Somthing Went Wrong")

    def display_employee_work_requests():
        pass

    def display_employee_maintenance_report():
        pass

