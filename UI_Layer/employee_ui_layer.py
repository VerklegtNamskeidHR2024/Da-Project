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

        display_all_employees = self.display_all_employees_by_locationa()
        if self.rank != "Employee":
            employee_menu = self.employee_menu_selection()
        if employee_menu == "q" or employee_menu == "b":
            return employee_menu

    def employee_menu_selection(self):    
        user_choice = ""
        while user_choice != "q":
            user_choice = self.action_choice()
            if user_choice == "1":
                user_choice = self.search_employee()
            elif user_choice == "2":
                user_choice = self.add_new_employee_to_storage()
            elif user_choice == "b":
                return "b"
            elif user_choice == "q":
                return "q"
        return user_choice
    

    


    def display_all_employees_by_locationa(self):
        """The function displays all employees at a location and their basic information"""
        employee_list = self.logic_wrapper.get_all_employees_at_location(self.location)
        print("-" * 70)
        print("{:>15}{:>10}{:>15}{:>15}".format("Name", "Phone", "Location", "ssn"))
        print("-" * 70)

        for employee in employee_list:
            print("{:>15}{:>10}{:>15}{:>15}".format(employee.name, employee.phone_number, employee.location, employee.social_security_number))
            
        print("-" * 70)
        #if self.rank == "Manager" or self.rank == "Admin":
            #self.action_choice()

    def action_choice(self) -> str:
        """The function is asking the user if they want to search or add an employee and calls the chosen function"""
        
        print()
        print("1. Select Employee")
        print("2. Add Employee")
        print("-" * 70)
        search_or_add = input("Enter choice: ")
        return search_or_add.lower()

        

    def search_employee(self) -> str:
        """The Function Is Searching For An Employee by SSN""" 
        employee_ssn = ""
        while employee_ssn != "q" and employee_ssn != "b":
            print()
            employee_ssn = input("Enter Employee Social Security Number: ")
            print()
            print("Go Back: b, B")
            print("Quit system: q, Q")
            #Makes sure the enterd ssn exists in the system
            is_employee_ssn_valid = self.logic_wrapper.sanity_check_ssn(employee_ssn)
            if is_employee_ssn_valid == True:
                employee = self.logic_wrapper.fetch_employee_from_storage(employee_ssn)
                employee_options = self.employee_options(employee)
                if employee_options == "b":
                    continue
                return employee_options
        #creates a instans of the employee with the maching ssn
        return employee_ssn.lower()

        #return employee_ssn



    def display_employee(self, employee):
        """The function displays an employee and their information"""
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
        print()
        print("Go Back: b, B")
        print("Quit system: q, Q")
        print("-" * 70)
        option = input("Enter Choice: ")
        return option.lower()
        

    def employee_options(self, employee):
        """holds all the options to view information and alter selected employee"""
        option = ""
        while option != "q" and option != "b":
            option = self.display_employee(employee)
            if option.lower() == "b":
                break
            elif option == "1":
                edit_choice = ""
                while edit_choice != "q":
                    edit_choice = self.display_edit_options(employee)
                    if edit_choice == "b":
                        break
                    if edit_choice == "q":
                        return edit_choice.lower()
                    if edit_choice == "1":
                        edit_choice = self.edit_employee_phone_number(employee)
                    elif edit_choice == "2":
                        edit_choice = self.edit_employee_location(employee)
                    elif edit_choice == "3":
                        edit_choice = self.edit_employee_email(employee)
                    elif edit_choice == "q":
                        return "q"
                
            elif option == "2":
                self.display_employee_work_requests(employee)

            
            elif option == "3":
                self.display_employee_maintenance_report(employee)
        return option.lower()
            

        

    def add_new_employee_to_storage(self):
        """The function asks for all the information needed for regestering an employee"""
        print("--- Creating a new employee ---")
       
        while (employee_name := input("Enter Employee Name: ").strip()) != "b":
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
        self.display_all_employees_by_locationa(employee_location)

    def display_edit_options(self, employee) -> str:
        """The Function displays and asks for the edit option"""
        print()
        print("1. Change Phone Number: ")
        print("2. Change Location: ")
        print("3. Change Email: ")
        print()
        print("Go Back: b, B")
        print("Quit system: q, Q")
        print("-" * 70)
        edit_choice = input("Enter Your Edit Choice: ")
        # if edit_choice.lower() == "b":
        #     self.employee_options(employee)
            
        return edit_choice

    def edit_employee_phone_number(self, employee: object):
        """This function sets a new phone number for the employee"""
        
        while (new_phone_number := input("Enter New Phone Number: ")) != "q" and new_phone_number != "Q":
            if new_phone_number.lower() == "b" or new_phone_number.lower() == "B":
                break
            is_valid_pn = self.logic_wrapper.sanity_check_phone_number(new_phone_number)
            if is_valid_pn:
                employee.set_phone_number(new_phone_number)
                self.logic_wrapper.edit_employee_info(employee)
                self.display_employee(employee)
                break
            else:
                print()
                print("Employee Phone Number Should Be 7 Numbers")
        return new_phone_number.lower()
        
        
    
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
            
        self.display_employee(employee)

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
        
        self.display_employee(employee)

    def display_employee_work_requests(self, employee):
        """The function displays all work requests by an employee"""
        wr_by_employee_list = self.logic_wrapper.fetch_all_work_request_for_employee(employee.staff_id)
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
        self.employee_options(employee)   

    def display_employee_maintenance_report(self, employee):
        """The function displays all maintenance reports by an employee"""
        mr_by_employee_list = self.logic_wrapper.fetch_all_maintenance_reports_for_employee(employee.staff_id)
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
        self.employee_options(employee)  

