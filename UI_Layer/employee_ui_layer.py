from Model_Classes.employee_model import Employee
import os
from prettytable import PrettyTable 
from colorama import Fore, Style, init
import time

class employee_UI_menu:
    def __init__(self, logic_wrapper, rank, location, staff_id):
        """Constructor for employee_UI_menu"""
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        self.staff_id = staff_id
    
    def clear_screen(self):
        ''' Clears the screen '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_point_employee_UI(self) -> str:
        """The function is the starting point for the employee UI"""
        # when this class is called it starts here
        # call other functions in class from here
        self.clear_screen()
        if self.rank == "Employee":
            display_all_employees = self.display_all_employees_by_locationa()
        else:
            employee_menu = self.employee_menu_selection()
            if employee_menu == "q" or employee_menu == "b":
                return employee_menu

    def employee_menu_selection(self) -> str:
        """The function runs the start menu for the employee"""
        
        user_choice = ""
        while user_choice != "q":
            self.clear_screen()
            self.display_all_employees_by_locationa()
            print()
            print("1. Select Employee")
            print("2. Add Employee")
            print("-" * 70)
         
            user_choice = input("Enter choice: ")
            if user_choice == "1":
                user_choice = self.search_employee()
            elif user_choice == "2":
                user_choice = self.add_new_employee_to_storage()
            elif user_choice.lower() == "b":
                self.clear_screen()
                return "b"
            elif user_choice.lower() == "q":
                return "q"
            else:
                print(Fore.RED + "Wrong input" + Style.RESET_ALL)
                time.sleep(0.5)
                self.clear_screen
        return user_choice
    

    def display_all_employees_by_locationa(self):
        """The function displays all employees at a location and their basic information"""
        employee_print_table = PrettyTable()
        employee_list = self.logic_wrapper.get_all_employees_at_location(self.location)
        employee_print_table.field_names = ["Employee name","Social Secuirty Number","Phone Number","Location", 'Email', 'Employee Id']
        # iterates through the location list and adds the location information to the table
        for item in employee_list:
            employee_print_table.add_row([item.name, item.social_security_number, item.phone_number, item.location, item.email, item.staff_id])
        
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        employee_print_table.border = True
        employee_print_table.junction_char = f"{border_color}+{reset_color}"
        employee_print_table.horizontal_char = f"{border_color}-{reset_color}"
        employee_print_table.vertical_char = f"{border_color}|{reset_color}"
        print('')
        print(employee_print_table)
        print('')

    #def action_choice(self) -> str:
        #"""The function is asking the user if they want to search or add an employee"""
        
        #print()
        #print("1. Select Employee")
        #print("2. Add Employee")
        #print("-" * 70)
        #search_or_add = input("Enter choice: ")
        #return search_or_add.lower()

        

    def search_employee(self) -> str:
        """The Function Is Searching For An Employee by SSN""" 
        employee_ssn = ""
        while employee_ssn.lower() != "q" and employee_ssn.lower() != "b":
            print()
            print("Go Back: b, B")
            print("Quit system: q, Q")
            print()
            employee_ssn = input("Enter Employee Social Security Number: ")

            #Makes sure the enterd ssn exists in the system
            is_employee_ssn_valid = self.logic_wrapper.sanity_check_ssn(employee_ssn)

            if is_employee_ssn_valid == True:
                #fetches an employee with the maching ssn
                employee = self.logic_wrapper.fetch_employee_from_storage(employee_ssn)
                #calls a function that displays the employee and asks for an action
                employee_options = self.employee_options(employee)
                if employee_options == "b" or employee_options == "B":
                    break
                elif employee_options == "q" or employee_options == "Q":
                    return "q"
            
            else:
                print(Fore.RED + "This Social Security Number Is Not In The System" + Style.RESET_ALL)
 
        return employee_ssn.lower()


    def display_employee(self, employee):
        """The function displays an employee and their information and asks what to view or edit"""

        print("-"*30)
        # create a table to print the contractor
        contractor_print_table = PrettyTable()
        contractor_print_table.field_names = ['Information',"Contractor Information"]
        # add the contractor info to the table
        contractor_print_table.add_row(['Name', employee.name])
        contractor_print_table.add_row(['Social Security Number', employee.social_security_number])
        contractor_print_table.add_row(['Phone Number', employee.phone_number])
        contractor_print_table.add_row(['Location', employee.location])
        contractor_print_table.add_row(['Email', employee.email])
        contractor_print_table.add_row(['Employee ID', employee.staff_id])
        # setting some colors for the table
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        contractor_print_table.border = True
        contractor_print_table.junction_char = f"{border_color}+{reset_color}"
        contractor_print_table.horizontal_char = f"{border_color}-{reset_color}"
        contractor_print_table.vertical_char = f"{border_color}|{reset_color}"
        # print the table
        print('')
        print(contractor_print_table)
        print('')

        

    def employee_options(self, employee) -> str:
        """The function displays an employee, asks for a action and calls the corresponding function"""

        option = ""
        while option != "q" and option != "b":
            self.clear_screen()
            option = self.display_employee(employee)
            print()
            print("1. Edit Employee Details")
            print("2. View Work Requests")
            print("3. View Maintenance Report")
            print()
            print("Go Back: b, B")
            print("Quit system: q, Q")
            print("-" * 70)
            option = input("Enter Choice: ")

            if option.lower() == "b":
                break

            elif option.lower() == "q":
                return option
            
            elif option == "1":
                self.clear_screen()
                choice = self.display_edit_options(employee)
                if choice == "b" or choice == "B":
                    continue
                elif choice == "q" or choice == "Q":
                    return choice
                
            elif option == "2":
                self.clear_screen()
                self.display_employee_work_requests(employee)
        
            elif option == "3":
                self.clear_screen()
                self.display_employee_maintenance_report(employee)
        return option.lower()
            

        

    def add_new_employee_to_storage(self):
        """The function asks for all the information needed for regestering an employee"""
        self.clear_screen()
        print()
        print("--- Creating a new employee ---")
        print()
        employee_name = ""
        while employee_name != "b" and employee_name != "q":
            employee_name = input("Enter Employee Name: ")
            if employee_name == "":
                print()
                print(Fore.RED + "This Field Is Required To Fill Out" + Style.RESET_ALL)
                print()

            else:
                #checks if the name contains only letters and spaces
                is_valid_name = self.logic_wrapper.sanity_check_employee_name(employee_name)
                if is_valid_name:
                    break
                else:
                    print(Fore.RED + "Employee Name Can Only Contain Letters And Spaces" + Style.RESET_ALL)
     

        while (employee_social_security_number := input("Enter Social Security Number: ")) != "b":
            if employee_social_security_number == "":
                print()
                print(Fore.RED + "This Field Is Required To Fill Out" + Style.RESET_ALL)
                print()
            else:
                #checks if the ssn contains only 10 numbers
                is_valid_ssn = self.logic_wrapper.sanity_check_ssn_add(employee_social_security_number)
                if is_valid_ssn:
                    break
                else:
                    print(Fore.RED + "Employee Social Security Number Should Be 10 Numbers And Not In The System" + Style.RESET_ALL)                     

        while (employee_phone_number := input("Enter Phone Number: ")) != "b":
            if employee_phone_number == "":
                print()
                print(Fore.RED + "This Field Is Required To Fill Out" + Style.RESET_ALL)
                print()
            else:
                #checks if the phone number contains only 7 numbers
                is_valid_pn = self.logic_wrapper.sanity_check_phone_number(employee_phone_number)
                if is_valid_pn:
                    break
                else:
                    print(Fore.RED + "Employee Phone Number Should Be 7 Numbers" + Style.RESET_ALL) 

        while (employee_location := input("Enter Location: ")) != "b":
            if employee_location == "":
                print()
                print(Fore.RED + "This Field Is Required To Fill Out" + Style.RESET_ALL)
                print()
            else:
                #checks if the location is a valid location
                is_valid_location = self.logic_wrapper.sanity_check_for_employee_location(employee_location)
                if is_valid_location:
                    break
                else:
                    print(Fore.RED + "Not a valid location." + Style.RESET_ALL) 
                    print(Fore.BLUE + "Valid locations: Reykjavik, Nuuk, Kulusuk, Thorshofn, Tingwall, Longyearbyen" + Style.RESET_ALL)

        while (employee_email := input("Enter Email: ")) != "b":
            if employee_email == "":
                print()
                print(Fore.RED + "This Field Is Required To Fill Out" + Style.RESET_ALL)
                print()
            else:
                #checks if the email contains a @ and . symbol
                is_valid_email = self.logic_wrapper.sanity_check_email(employee_email)
                if is_valid_email:
                    break
                else:
                    print(Fore.RED + "Employee Email Needs To Contain @ And ." + Style.RESET_ALL)
        #creates a new employee
        new_employee = Employee(employee_name, employee_social_security_number, employee_phone_number, employee_location, "Employee", employee_email, "")
        #adds the new employee to the storage
        new_employee_added = self.logic_wrapper.add_new_employee_to_storage(new_employee)
        print(Fore.GREEN + "New Employee Added" + Style.RESET_ALL)

    def display_edit_options(self, employee) -> str:
        """The Function displays and asks for the edit option"""
        
        edit_choice = ""
        while edit_choice.lower() != "q":
            print()
            print("1. Change Phone Number: ")
            print("2. Change Location: ")
            print("3. Change Email: ")
            print()
            print("Go Back: b, B")
            print("Quit system: q, Q")
            print("-" * 70)
            edit_choice = input("Enter Your Edit Choice: ")
            if edit_choice.lower() == "b" or edit_choice.lower() == "q":
                return edit_choice
            
            elif edit_choice == "1":
                edit_choice = self.edit_employee_phone_number(employee)

            elif edit_choice == "2":
                edit_choice = self.edit_employee_location(employee)
            
            elif edit_choice == "3":
                edit_choice = self.edit_employee_email(employee)
            
        return edit_choice

    def edit_employee_phone_number(self, employee: object):
        """This function sets a new phone number for the employee"""
        
        while (new_phone_number := input("Enter New Phone Number: ")) != "q" and new_phone_number != "Q":
            if new_phone_number.lower() == "b" or new_phone_number.lower() == "B":
                break
            is_valid_pn = self.logic_wrapper.sanity_check_phone_number(new_phone_number)
            if is_valid_pn:
                #sets the new phone number for this employee
                employee.set_phone_number(new_phone_number)
                #writes the update to the storage
                self.logic_wrapper.edit_employee_info(employee)
                print()
                print(Fore.GREEN + "Employee Information Updated" + Style.RESET_ALL)
               
                break
            else:
                print()
                print(Fore.RED + "Employee Phone Number Should Be 7 Numbers" + Style.RESET_ALL)
        return new_phone_number.lower()
        
        
    
    def edit_employee_location(self, employee: object):
        """This function sets a new location for the employee"""
        
        while (new_location := input("Enter New Location: ")) != "q" and new_location != "Q":
            if new_location.lower() == "b" or new_location.lower() == "B":
                break    
            is_valid_location = self.logic_wrapper.sanity_check_for_employee_location(new_location)
    
            if is_valid_location:
                #sets the new location for this employee
                employee.set_location(new_location)
                #writes the update to the storage
                self.logic_wrapper.edit_employee_info(employee)
                print()
                print(Fore.GREEN + "Employee Information Updated" + Style.RESET_ALL)
              
                break
            else:
                print()
                print(Fore.RED + "Not a valid location." + Style.RESET_ALL) 
                print(Fore.LIGHTBLUE_EX + "Valid locations: Reykjavik, Nuuk, Kulusuk, Thorshofn, Tingwall, Longyearbyen" + Style.RESET_ALL)
            
        return new_location.lower()

    def edit_employee_email(self, employee: object):
        """This function sets a new email for the employee"""
        
        while (new_email := input("Enter New Email: ")) != "q" and new_email != "Q":
            if new_email.lower() == "b" or new_email.lower() == "B":
                break 
            is_valid_email = self.logic_wrapper.sanity_check_email(new_email)
            if is_valid_email:
                #sets the new email for this employee
                employee.set_email(new_email)
                #writes the update to the storage
                self.logic_wrapper.edit_employee_info(employee)
                print()
                print(Fore.GREEN + "Employee Information Updated" + Style.RESET_ALL)
             
                break
            else:
                print()
                print(Fore.RED + "Employee Email Needs To Contain @ And ." + Style.RESET_ALL)
        return new_email.lower()
        
        

    def display_employee_work_requests(self, employee):
        """The function displays all work requests by an employee"""
        
        #gets a list of all the work requests done by this employee
        employee_work_requests = self.logic_wrapper.fetch_all_work_request_for_employee(employee.staff_id)
        if not employee_work_requests:
            print()
            print(Fore.RED + "No Work Request Attached To This Employee" + Style.RESET_ALL)
            print()
            bause_breaker = input("Press Enter To Return To Selected Employee Menu.")

        else:             
            print()
            print("--- All Work Requests By This Employee ---")
            print()
            employee_work_requests_table = PrettyTable(["Name", "ID", "Status"])
            for work_request in employee_work_requests:
                employee_work_requests_table.add_row([work_request.name, work_request.work_request_id, work_request.work_request_status])
            border_color = Fore.MAGENTA
            reset_color = Style.RESET_ALL
            employee_work_requests_table.border = True
            employee_work_requests_table.junction_char = f"{border_color}+{reset_color}"
            employee_work_requests_table.horizontal_char = f"{border_color}-{reset_color}"
            employee_work_requests_table.vertical_char = f"{border_color}|{reset_color}"
            print(employee_work_requests_table)
            bause_breaker = input("\nPress Enter To Return To Selected Employee Menu.")
             
           

    def display_employee_maintenance_report(self, employee):
        """The function displays all maintenance reports by an employee"""
      
        #gets a list of all the maintenance reports done by this employee
        employeee_maintenance_reports = self.logic_wrapper.fetch_all_maintenance_reports_for_employee(employee.staff_id)
        
        if not employeee_maintenance_reports:
            print()
            print(Fore.RED + "No Maintenance Reports Attached To This Employee" + Style.RESET_ALL)
            print()
            bause_breaker = input("Press Enter To Return To Selected Employee Menu.")           
        else:    
            print()
            print("--- All Maintenance Reports By This Employee ---")
            print()
            # create a table to print the maintenances reports
            employeee_maintenance_reports_table = PrettyTable(['Report ID', 'Report Name', 'Description', 'Status'])
            # loop through the maintenance reports and add them to the table if they have the current contractors id
            for maintenance_report in employeee_maintenance_reports:
                employeee_maintenance_reports_table.add_row([maintenance_report.report_id, maintenance_report.report_name, maintenance_report.maintenance_description, maintenance_report.report_status])
            border_color = Fore.MAGENTA
            reset_color = Style.RESET_ALL
            employeee_maintenance_reports_table.border = True
            employeee_maintenance_reports_table.junction_char = f"{border_color}+{reset_color}"
            employeee_maintenance_reports_table.horizontal_char = f"{border_color}-{reset_color}"
            employeee_maintenance_reports_table.vertical_char = f"{border_color}|{reset_color}"
            
            print(employeee_maintenance_reports_table)
            bause_breaker = input("\nPress Enter To Return To Selected Employee Menu.")
            print('')
            

