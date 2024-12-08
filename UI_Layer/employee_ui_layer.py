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
                employee_ssn = self.search_employee()

                if self.logic_wrapper.sanity_check_ssn(employee_ssn):
                    employee = self.logic_wrapper.fetch_employee_from_storage(employee_ssn)
                    self.display_employee(employee)
                    choice = self.employee_options()
                    if choice == 1:
                        edit_choice = self.display_edit_options()
                        if edit_choice == 1:
                            self.edit_employee_phone_number(employee)
                        elif edit_choice == 2:
                            self.edit_employee_location(employee)
                        elif edit_choice == 3:
                            self.edit_employee_email(employee)
                    elif choice == 2:
                        self.display_employee_work_requests(employee.staff_id)
                    elif choice == 3:
                        self.display_employee_maintenance_report(employee_ssn)
            elif action == 2:
                self.add_new_employee_to_storage()
            else:
                print("Somthing wrong")

    def display_all_employees(self):
        """The function displays a table with all employees at a location and their basic information"""
        employee_list = self.logic_wrapper.get_all_employees_at_location(self.location)
        print("-" * 70)
        print("{:>15}{:>10}{:>15}".format("Name", "Phone", "Location"))
        print("-" * 70)

        for item in employee_list:
            print("{:>15}{:>10}{:>15}".format(item.name, item.phone_number, item.location))
            # print(f"{item.name :> 15}|{item.phone_number :> 10}|{item.email :> 10}|{self.location :> 15}")
        print("-" * 70)

    def action_choice(self) -> int:
        """The function is asking the user if they want to search or add an employee"""
        
        print()
        print("1. Search Employee")
        print("2. Add Employee")
        print("-" * 70)
        search_or_add = int(input("Enter choice: "))
        return search_or_add 
        

    def search_employee(self) -> int:
        """The Function Is Searching For An Employee by SSN""" 

        print()
        employee_ssn = int(input("Enter Employee Social Security Number: "))

        return employee_ssn


    def display_employee(self, employee):
        """The function displays an employee and all their information"""
        #employee = self.logic_wrapper.fetch_employee_from_storage(ssn)
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

    def add_new_employee_to_storage(self):
        """The function asks for all the information needed for regestering an employee"""
        print("--- Creating a new employee ---")
       
        while (employee_name := input("Enter Employee Name: ")) != "b":
            if employee_name == "":
                print()
                print("This Field Is Required To Fill Out")
                print()
            else:
                is_valid_name = self.logic_wrapper.sanity_check_employee_name(employee_name)
                if is_valid_name:
                    break
                else:
                    print("Employee Name Can Only Contain Letters And Spaces")
     

        while (employee_social_security_number := int(input("Enter Social Security Number: "))) != "b":
            if employee_social_security_number == "":
                print()
                print("This Field Is Required To Fill Out")
                print()
            else:
                is_valid_ssn = self.logic_wrapper.sanity_check_ssn(employee_social_security_number)
                if is_valid_ssn:
                    break
                else:
                    print("Employee Social Security Number Should Be 10 Numbers")                     

        while (employee_phone_number := int(input("Enter Phone Number: "))) != "b":
            if employee_phone_number == "":
                print()
                print("This Field Is Required To Fill Out")
                print()
            else:
                is_valid_pn = self.logic_wrapper.sanity_check_phone_number(employee_phone_number)
                if is_valid_pn:
                    break
                else:
                    print("Employee Phone Number Should Be 7 Numbers") 

        while (employee_location := input("Enter Location: ")) != "b":
            if employee_location == "":
                print()
                print("This Field Is Required To Fill Out")
                print()
            else:
                is_valid_location = self.logic_wrapper.sanity_check_for_employee_location(employee_location)
                if is_valid_location:
                    break
                else:
                    print("Not a valid location.") 
                    print("Valid locations: Reykjavik, Nuuk, Kulusuk, Thorshofn, Tingwall, Longyearbyen""")

        while (employee_email := input("Enter Email: ")) != "b":
            if employee_email == "":
                print()
                print("This Field Is Required To Fill Out")
                print()
            else:
                is_valid_email = self.logic_wrapper.sanity_check_email(employee_email)
                if is_valid_email:
                    break
                else:
                    print("Employee Email should contain @")

        new_employee = Employee(employee_name, employee_social_security_number, employee_phone_number, employee_location, "Employee", employee_email, "")
        new_employee_added = self.logic_wrapper.add_new_employee_to_storage(new_employee)

    def display_edit_options(self) -> int:
        """The Function displays and asks for the edit option"""
        print()
        print("1. Change Phone Number: ")
        print("2. Change Location: ")
        print("3. Change Email: ")
        print("-" * 70)
        edit_choice = int(input("Enter Your Edit Choice: "))
        return edit_choice

    def edit_employee_phone_number(self, employee: object):
        """This function sets a new phone number for the employee"""
        
        while (new_phone_number := int(input("Enter New Phone Number: "))) != "b":
            is_valid_pn = self.logic_wrapper.sanity_check_phone_number(new_phone_number)
            if is_valid_pn:
                employee.set_phone_number(new_phone_number)
                self.logic_wrapper.edit_employee_info(employee)
                break
            else:
                print("Employee Phone Number Should Be 7 Numbers")
    
    def edit_employee_location(self, employee: object):
        """This function sets a new location for the employee"""
        
        while (new_location := input("Enter New Location")) != "b":
            is_valid_location = self.logic_wrapper.sanity_check_location(new_location)
            if is_valid_location:
                employee.set_location(new_location)
                self.logic_wrapper.edit_employee_info(employee)
                break
            else:
                print("Not a valid location.") 
                print("Valid locations: Reykjavik, Nuuk, Kulusuk, Thorshofn, Tingwall, Longyearbyen""")

    def edit_employee_email(self, employee: object):
        """This function sets a new email for the employee"""
        
        while (new_email := int(input("Enter New Email: "))) != "b":
            is_valid_email = self.logic_wrapper.sanity_check_email(new_email)
            if is_valid_email:
                employee.set_phone_number(new_email)
                self.logic_wrapper.edit_employee_info(employee)
                break
            else:
                print("Employee Email should contain @")

    def display_employee_work_requests(self, staff_id):
        """The function displays all work requests by an employee"""
        wr_by_employee_list = self.logic_wrapper.fetch_all_work_request_for_employee(staff_id)
        print()
        print("--- All Work Requests By This Employee ---")
        print("{:>15}{:>10}{:>15}".format("Name", "Work Request ID", "Status"))
        print("-" * 70)
        for wr in wr_by_employee_list:
            print("{:>15}{:>10}{:>15}".format(wr.name, wr.work_request_id, wr.work_request_status))
        print("-" * 70)     

    def display_employee_maintenance_report(self, social_security_number):
        """The function displays all maintenance reports by an employee"""
        mr_by_employee_list = self.logic_wrapper.fetch_all_maintenance_report_for_employee(social_security_number)
        print()
        print("--- All Maintenance Report By This Employee ---")
        print("{:>15}{:>10}{:>15}".format("Name", "Maintenance ID", "Status"))
        print("-" * 70)
        for mr in mr_by_employee_list:
            print("{:>15}{:>10}{:>15}".format(mr.report_name, mr.report_id, mr.report_status))
        print("-" * 70)  

