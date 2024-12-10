from Model_Classes.employee_model import Employee

class employee_UI_menu:
    def __init__(self, logic_wrapper, rank, location, staff_id):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        self.staff_id = staff_id

    def start_point_employee_UI(self):
        # when this class is called it starts here
        # call other functions in class from here

        self.display_all_employees_by_locationa(self.location)




    def display_all_employees_by_locationa(self, location):
        """The function displays a table with all employees at a location and their basic information"""
        employee_list = self.logic_wrapper.get_all_employees_at_location(location)
        print("-" * 70)
        print("{:>15}{:>10}{:>15}{:>15}".format("Name", "Phone", "Location", "ssn"))
        print("-" * 70)

        for item in employee_list:
            print("{:>15}{:>10}{:>15}{:>15}".format(item.name, item.phone_number, item.location, item.social_security_number))
            
        print("-" * 70)
        if self.rank == "Manager" or self.rank == "Admin":
            self.action_choice()

    def action_choice(self) -> str:
        """The function is asking the user if they want to search or add an employee"""
        
        print()
        print("1. Select Employee")
        print("2. Add Employee")
        print("-" * 70)
        search_or_add = input("Enter choice: ")
        if search_or_add == "1":
            self.search_employee()
        elif search_or_add == "2":
            self.add_new_employee_to_storage()
        elif search_or_add.lower == "b":
            return
        return search_or_add 
        

    def search_employee(self) -> str:
        """The Function Is Searching For An Employee by SSN""" 

        print()
        employee_ssn = input("Enter Employee Social Security Number: ")
        if employee_ssn.lower == "b":
            self.action_choice()
        
        elif self.logic_wrapper.sanity_check_ssn(employee_ssn):
            employee = self.logic_wrapper.fetch_employee_from_storage(employee_ssn)
            self.display_employee(employee)
        
 
        return employee_ssn



    def display_employee(self, employee):
        """The function displays an employee and all their information"""
        #employee = self.logic_wrapper.fetch_employee_from_storage(ssn)
        print()
        print("-" * 70)
        print("{:<25}{:<5}{:<15}".format("Employee Name", "|", employee.name))
        print("{:<25}{:<5}{:<15}".format("Social Security Number", "|", employee.social_security_number))
        print("{:<25}{:<5}{:<15}".format("Phone Number", "|", employee.phone_number))
        print("{:<25}{:<5}{:<15}".format("Location", "|", employee.location))
        print("{:<25}{:<5}{:<15}".format("Email", "|", employee.email))
        print("{:<25}{:<5}{:<15}".format("Employee ID", "|", employee.staff_id))
        print("-" * 70)
        print()
        print("1. Edit Employee Details")
        print("2. View Work Requests")
        print("3. View Maintenance Report")
        print("-" * 70)
        option = input("Enter Choice: ")

        if option.lower() == "b":
            self.action_choice()

        elif option == "1":
            edit_choice = self.display_edit_options()
            if edit_choice == "1":
                self.edit_employee_phone_number(employee)
            elif edit_choice == "2":
                self.edit_employee_location(employee)
            elif edit_choice == "3":
                self.edit_employee_email(employee)
        
        elif option == "2":
            self.display_employee_work_requests(employee.staff_id)

        
        elif option == "3":
            self.display_employee_maintenance_report(employee.staff_id)


        

    def employee_options(self) -> str:
        print()
        print("1. Edit Employee Details")
        print("2. View Work Requests")
        print("3. View Maintenance Report")
        print("-" * 70)
        option = input("Enter Choice: ")

        if option.lower() == "b":
            self.action_choice()
            

        

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
     

        while (employee_social_security_number := input("Enter Social Security Number: ")) != "b":
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

        while (employee_phone_number := input("Enter Phone Number: ")) != "b":
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
        return

    def display_edit_options(self) -> str:
        """The Function displays and asks for the edit option"""
        print()
        print("1. Change Phone Number: ")
        print("2. Change Location: ")
        print("3. Change Email: ")
        print("-" * 70)
        edit_choice = input("Enter Your Edit Choice: ")
        if edit_choice.lower() == "b":
            self.employee_options()
        return edit_choice

    def edit_employee_phone_number(self, employee: object):
        """This function sets a new phone number for the employee"""
        
        while (new_phone_number := input("Enter New Phone Number: ")) != "b":
            is_valid_pn = self.logic_wrapper.sanity_check_phone_number(new_phone_number)
            if is_valid_pn:
                employee.set_phone_number(new_phone_number)
                self.logic_wrapper.edit_employee_info(employee)
                break
            else:
                print()
                print("Employee Phone Number Should Be 7 Numbers")
    
    def edit_employee_location(self, employee: object):
        """This function sets a new location for the employee"""
        
        while (new_location := input("Enter New Location: ")) != "b":
            is_valid_location = self.logic_wrapper.sanity_check_for_employee_location(new_location)
    
            if is_valid_location == True:
            
                employee.set_location(new_location)
                self.logic_wrapper.edit_employee_info(employee)
                break
            else:
                print()
                print("Not a valid location.") 
                print("Valid locations: Reykjavik, Nuuk, Kulusuk, Thorshofn, Tingwall, Longyearbyen""")

    def edit_employee_email(self, employee: object):
        """This function sets a new email for the employee"""
        
        while (new_email := input("Enter New Email: ")) != "b":
            is_valid_email = self.logic_wrapper.sanity_check_email(new_email)
            if is_valid_email:
                employee.set_email(new_email)
                self.logic_wrapper.edit_employee_info(employee)
                break
            else:
                print()
                print("Employee Email should contain @")

    def display_employee_work_requests(self, staff_id):
        """The function displays all work requests by an employee"""
        wr_by_employee_list = self.logic_wrapper.fetch_all_work_request_for_employee(staff_id)
        if not wr_by_employee_list:
            print()
            print("No Work Request Attached To This Employee")
        else: 
            print()
            print("--- All Work Requests By This Employee ---")
            print()
            print("{:>15}{:>10}{:>15}".format("Name", "ID", "Status"))
            print("-" * 70)
            for wr in wr_by_employee_list:
                print("{:>15}{:>10}{:>15}".format(wr.name, wr.work_request_id, wr.work_request_status))
            print("-" * 70)     

    def display_employee_maintenance_report(self, staff_id):
        """The function displays all maintenance reports by an employee"""
        mr_by_employee_list = self.logic_wrapper.fetch_all_maintenance_reports_for_employee(staff_id)
        if not mr_by_employee_list:
            print()
            print("No Maintenance Report Attached To This Employee")
        else:
            print()
            print("--- All Maintenance Report By This Employee ---")
            print()
            print("{:<25}{:<10}{:<15}".format("Name", "ID", "Status"))
            print("-" * 70)
            for mr in mr_by_employee_list:
                print("{:<25}{:<10}{:<15}".format(mr.report_name, mr.report_id, mr.report_status))
            print("-" * 70)  

