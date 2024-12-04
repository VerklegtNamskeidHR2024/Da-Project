from Model_Classes.work_request_model import WorkRequest

class work_request_UI_menu:
    def __init__(self, Logic_Wrapper, rank, location):
        self.logic_wrapper = Logic_Wrapper
        self.rank = rank
        self.location = location


    def start_point_work_requests_UI(self):
        """When this class is called it starts here, calling the display_requests_menu_items first to 
        load the menu and it's options for the user. """
        # Call other functions in class from here

        self.display_work_requests_menu_items()
        # self.display_selected_work_request_information()
        # self.select_work_request_by_id()
        # self.create_work_request_form()
        # self.edit_work_request_form()
        # self.display_my_work_requests()
        # self.display_new_work_requests_to_accept() 
        # self.display_pending_work_requests_printed() 
        # self.display_closed_work_requests_printed() 


    def display_all_work_requests_printed(self, work_request_list):
        """Prints out all open work requests with their ID, Name and Description. """

        print("{:0}{:>3}{:>5}{:>9}{:>12}".format("ID", "|", "Name", "|", "Description"))
        print("-" * 70)
        for item in work_request_list:
            print("{:0}{:>3}{:>10}{:>4}{:>51}".format({item.work_request_id}, "|", {item.name}, "|", {item.description}))
        print("-" * 70)
        

    def display_selected_work_request_information_printed(self, work_request):
        print("{:0}{:>14}{:<10}".format("Categories", "|", "Details"))
        print("-" * 35)     
        print("{:0}{:>9}{:<10}".format("Work Request ID", "|", {work_request.get_work_request_id})) 
        print("{:0}{:>20}{:<10}".format("Name", "|", {work_request.get_name}))
        print("{:0}{:>13}{:<10}".format("Description", "|", {work_request.get_description}))
        print("{:0}{:>16}{:<10}".format("Location", "|", {work_request.get_location})) 
        print("-" * 35)
        print("{:0}{:>3}{:>10}".format("Maintenance Report ID", "|", {work_request.get_maintenance_report}))
        print("{:0}{:>16}{:<10}".format("Employee ID", "|", {work_request.get_staff_id}))
        print("{:0}{:>13}{:<10}".format("Property ID", "|", {work_request.get_property_id})) 
        print("{:0}{:>11}{:<10}".format("Contractor ID", "|", {work_request.get_contractor_id}))
        print("-" * 35)
        print("{:0}{:>14}{:<10}".format("Start Date", "|", {work_request.get_date_of_creation}))
        print("{:0}{:>7}{:<10}".format("Completition Date", "|", {work_request.get_date_of_completition})) 
        print("{:0}{:>9}{:<10}".format("Repititive Work", "|", {work_request.get_repetitive_work}))
        print("{:0}{:>3}{:<10}".format("Re-Open Interval Days", "|", {work_request.get_reopen_interval})) 
        print("-" * 35)
        print("{:0}{:>16}{:<10}".format("Priority", "|", {work_request.get_priority}))
        print("{:0}{:>7}{:<10}".format("Status", "|", {work_request.get_work_request_status}))
        print("{:0}{:>11}{:<10}".format("Completed", "|", {work_request.get_mark_as_completed}))
        print("{:0}{:>4}{:<10}".format("Accepted by Employee", "|", {work_request.get_acceptance_status}))
        print("-" * 70)


    def display_work_requests_menu_items(self):
        """Displays the menu options depending if the user logged in is an admin/manager or
        an employee. It then calls the correct function based on what the user chose. """

        print()
        print("Work Request Menu")
        print("-" * 70)
        print("{:>50}".format("[ Open and Upcoming Work Requests ]"))
        print()
        self.display_all_work_requests_printed()
        if self.rank != "Employee":
            print("{:0}{:>3}{:>8}{:>7}{:>11}".format("1. Select Request", "|", "2. Add Request", "|", "3. Closed Requests"))
            print()
            user_choice = input("Select an Option: ")
            print("-" * 70)
            match user_choice:
                case "1": 
                    self.select_work_request_by_id()
                case "2":
                    self.display_create_work_request_form()
                case "3":
                    self.display_closed_work_requests_printed()
                case "q":
                    pass
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case "Q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case _:
                    print("Invalid Input, Please Try Again.")
                    self.start_point_work_requests_UI()
        
        else:
            print("{:0}{:>2}{:>15}{:>2}{:>19}".format("1. New Requests", "|", "2. Pending Requests", "|", "3. My Requests"))
            print()
            user_choice = input("Select an Option: ")
            print("-" * 70)    
            match user_choice:
                case "1": 
                    self.display_all_new_work_requests_to_accept_printed()
                case "2":
                    self.display_all_pending_work_requests_printed()
                case "3": 
                    self.display_my_work_requests_printed()
                case "q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case "Q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case _:
                    print("Invalid Input, Please Try Again.")
                    self.start_point_work_requests_UI()
                

    def select_work_request_by_id(self):
        """System asks user for the ID of the work request they wish to find, where it then prints out 
        all it's information """

        try:
            work_request_selected_by_id = input("Enter Request ID: ")
            work_request_model = self.logic_wrapper.get_work_request_by_id(self.rank, self.location, work_request_selected_by_id)
            if work_request_model != None:
                self.display_selected_work_request_information_printed(work_request_model)
                if self.rank != "Employee" :
                    self.general_edit_work_request_form(work_request_model)
                else:
                    self.employee_edit_work_request_form(work_request_model)
        except:
            print("Work Request not Found, Please Try Again.")
            self.select_work_request_by_id()


    def display_create_work_request_form(self):
        try:
            new_work_request = WorkRequest()
            print()
            print("[ New Work Request Form ]")
            print("-" * 70)
            new_work_request.set_name(input("Request Name: "))
            new_work_request.set_description(input("Request Descrptition: "))  
            new_work_request.set_property_id(input("Request for Property ID: "))
            new_work_request.set_date_of_creation(input("Start Date: "))
            new_work_request.set_mark_as_done(input("Completition Date: "))
            new_work_request.set_repetitive_work(input("Mark Repititive? (Yes or No): "))
            new_work_request.set_reopen_interval(input("Interval of Days Until Request Re-Opens: "))
            new_work_request.set_priority(input("Request Priority (High, Medium or Low):  "))
            if self.rank != "Admin": 
                new_work_request.set_location_id(input(self.location))
            else:
                new_work_request.set_location_id(input("Set Location for Work Request: "))
            print("-" * 70)
            print()
            new_work_request_confirmation = input("Enter 1 to Confirm: ")
            if new_work_request_confirmation == "1": 
                is_valid = self.logic_wrapper.sanity_check_work_request(new_work_request)
                if is_valid == True:
                    self.logic_wrapper.add_work_request(new_work_request)
                # else:
                #     print("Something Went Wrong When Creating the Work Request, Please Try Again.")
                print("-" * 70)
                print("New Work Request Has Been Created!")
                self.start_point_work_requests_UI()
                # back_to_work_request_menu = input("Enter B to Go Back to Work Request Menu: ")
                # if back_to_work_request_menu == "b" or back_to_work_request_menu == "B":
                #     self.start_point_work_requests_UI()
                # else:
                #     self.start_point_work_requests_UI
        except: 
            print("Something Went Wrong When Creating the Work Request, Please Try Again.")

        
    def employee_edit_work_request_form(self, work_request):
        for 
        if :
            print()
            print("-" * 70)
            mark_as_completed = input("Mark as Completed (Yes or No): ")
            is_input_for_mark_completed_valid = self.logic_wrapper.sanity_check_work_request(mark_as_completed)
            if is_input_for_mark_completed_valid == True:
                updated_work_request = work_request.set_mark_as_done(is_input_for_mark_completed_valid)
                self.logic_wrapper.edit_work_requests(updated_work_request)
        elif :
            print()
            print("-" * 70)
            accept_work_request = input("Aceept (Yes or No): ")
            is_input_for_accepted_valid = self.logic_wrapper.sanity_check_work_request(accept_work_request)
            if is_input_for_accepted_valid == True:
                updated_work_request = work_request.set_mark_as_done(is_input_for_accepted_valid)
                self.logic_wrapper.edit_work_requests(updated_work_request)
    
    
    def general_edit_work_request_form(self, work_request):
            print()
            print("Choose a Category To Edit")
            print("-" * 70)
            print("{:>15}".format("> 1. Employee ID"))
            print("{:>18}".format("> 2. Property ID"))
            print("{:>24}".format("> 3. Repititive Ticket"))
            print("{:>15}".format("> 4. Priority"))
            print("{:>20}".format("> 5. Request Status"))
            print("-" * 70)
            category_to_edit = input("Choose a Category to Edit: ")
            match category_to_edit:
                case "1":
                    new_employee_id_for_request = input("Enter New Employee ID: ")
                    is_name_input_valid = self.logic_wrapper.sanity_check_work_request(new_employee_id_for_request)
                    
                    if is_name_input_valid == True:
                        updated_work_request = work_request.set_mark_as_done(is_name_input_valid)
                        self.logic_wrapper.edit_work_requests(updated_work_request)

                case "2": 
                    new_property_id_for_request = input("Enter New Property ID: ")
                    is_property_id_input_valid = self.logic_wrapper.sanity_check_work_request(new_property_id_for_request)
                    
                    if is_property_id_input_valid == True:
                        updated_work_request = work_request.set_mark_as_done(is_property_id_input_valid)
                        self.logic_wrapper.edit_work_requests(updated_work_request)

                case "3":
                    update_is_request_repitive = input("Is Repitive? (Yes or No): ")
                    is_request_input_valid = self.logic_wrapper.sanity_check_work_request(update_is_request_repitive)
                    
                    if is_request_input_valid == True:
                        updated_work_request = work_request.set_mark_as_done(is_request_input_valid)
                        self.logic_wrapper.edit_work_requests(updated_work_request)

                case "4":
                    new_priority_for_request = input("Enter New Priority for Request: ")
                    is_priority_input_valid = self.logic_wrapper.sanity_check_work_request(new_priority_for_request)
                    
                    if is_priority_input_valid == True:
                        updated_work_request = work_request.set_mark_as_done(is_priority_input_valid)
                        self.logic_wrapper.edit_work_requests(updated_work_request)

                case "5":
                    update_request_status = input("Mark as Completed? (Yes or No): ")
                    is_request_input_valid = self.logic_wrapper.sanity_check_work_request(update_request_status)
                    
                    if is_request_input_valid == True:
                        updated_work_request = work_request.set_mark_as_done(is_request_input_valid)
                        self.logic_wrapper.edit_work_requests(updated_work_request)

            updated_work_request_confirmation_confirmation = input("Enter 1 to Confirm: ")

        
    def display_my_work_requests_printed(self):
        my_work_request_list = self.logic_wrapper.get_my_work_requests(self.rank, self.location)
        self.display_all_work_requests_printed(my_work_request_list)
        
        selected_work_request = input("Enter 1 to Select a Work Request or B to Go Back: ")
        if selected_work_request == "1":
            self.select_work_request_by_id()
        elif selected_work_request == "b" or selected_work_request == "B":
            self.start_point_work_requests_UI()
        else: 
            self.display_my_work_requests_printed()

    def display_all_new_work_requests_to_accept_printed(self): 
        new_work_request_list = self.logic_wrapper.get_all_new_work_requests(self.rank, self.location)
        self.display_all_work_requests_printed(new_work_request_list)
        
        selected_work_request = input("Enter 1 to Select a Work Request or B to Go Back: ")
        if selected_work_request == "1":
            self.select_work_request_by_id()
        elif selected_work_request == "b" or selected_work_request == "B":
            self.start_point_work_requests_UI()
        else: 
            self.display_all_new_work_requests_to_accept_printed()
        
    
    def display_all_pending_work_requests_printed(self): 
        pending_work_request_list = self.logic_wrapper.get_all_pending_work_requests(self.rank, self.location)
        self.display_all_work_requests_printed(pending_work_request_list)
        
        selected_work_request = input("Enter 1 to Select a Work Request or B to Go Back: ")
        if selected_work_request == "1":
            self.select_work_request_by_id()
        elif selected_work_request == "b" or selected_work_request == "B":
            self.start_point_work_requests_UI()
        else: 
            self.display_all_pending_work_requests_printed()


    def display_closed_work_requests_printed(self): 
        closed_work_request_list = self.logic_wrapper.get_all_closed_work_requests(self.rank, self.location)
        self.display_all_work_requests_printed(closed_work_request_list)
        
        selected_work_request = input("Enter 1 to Select a Work Request or B to Go Back: ")
        if selected_work_request == "1":
            self.select_work_request_by_id()
        elif selected_work_request == "b" or selected_work_request == "B":
            self.start_point_work_requests_UI()
        else: 
            self.display_closed_work_requests_printed()