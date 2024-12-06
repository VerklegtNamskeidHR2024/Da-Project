from Model_Classes.work_request_model import WorkRequest

class work_request_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
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

    # Completed, can be beautified.
    def display_all_work_requests_printed(self, work_request_list: list=None) -> print: 
        """Prints out all open work requests with their ID, Name and Description. """
        try:
            print("{:0}{:>6}{:>5}{:>9}{:>12}".format("ID", "|", "Name", "|", "Description"))
            print("-" * 70)
            for item in sorted(work_request_list):
                print("{:0}{:>3}{:>10}{:>4}{:>51}".format(item.work_request_id, "|", item.name, "|", item.description)) 
            print("-" * 70)
        except TypeError:
            print()
            print("{:>50}".format("No Work Requests To Display")) 
        
    # Completed, can be beautified.
    def display_selected_work_request_information(self, work_request: object=None) -> print:
        """Prints out a selected work requests and all it's information for user to read. """

        print("{:0}{:>14}{:<10}".format("Categories", "|", "Details"))
        print("-" * 35)     
        print("{:0}{:>9}{:<10}".format("Work Request ID", "|", work_request.work_request_id)) 
        print("{:0}{:>20}{:<10}".format("Name", "|", work_request.name))
        print("{:0}{:>13}{:<10}".format("Description", "|", work_request.description))
        print("{:0}{:>16}{:<10}".format("Location", "|", work_request.location)) 
        print("-" * 35)
        print("{:0}{:>3}{:>10}".format("Maintenance Report ID", "|", work_request.maintenance_report_id))
        print("{:0}{:>16}{:<10}".format("Employee ID", "|", work_request.staff_id))
        print("{:0}{:>13}{:<10}".format("Property ID", "|", work_request.property_id)) 
        print("{:0}{:>11}{:<10}".format("Contractor ID", "|", work_request.contractor_id))
        print("-" * 35)
        print("{:0}{:>14}{:<10}".format("Start Date", "|", work_request.start_date))
        print("{:0}{:>7}{:<10}".format("Completition Date", "|", work_request.completition_date)) 
        print("{:0}{:>9}{:<10}".format("Repititive Work", "|", work_request.repetitive_work))
        print("{:0}{:>3}{:<10}".format("Re-Open Interval Days", "|", work_request.reopen_interval)) 
        print("-" * 35)
        print("{:0}{:>16}{:<10}".format("Priority", "|", work_request.priority))
        print("{:0}{:>7}{:<10}".format("Status", "|", work_request.work_request_status))
        print("{:0}{:>7}{:<10}".format("Needs Contractor", "|", work_request.need_contractor))
        print("{:0}{:>11}{:<10}".format("Completed", "|", work_request.mark_as_completed))
        print("{:0}{:>4}{:<10}".format("Accepted by Employee", "|", work_request.accepted_by_employee)) 
        print("-" * 70)

    # Completed, can be beautified.
    def display_work_requests_menu_items(self) -> print:
        """Displays the menu options depending if the user logged in is an admin/manager or
        an employee. It then calls the correct function based on what the user chose. """

        work_request_list = self.logic_wrapper.get_all_work_requests_at_location(self.rank, self.location)
        print()
        print(f"{self.rank} - Work Request Menu")
        print("-" * 70)
        print("{:>50}".format("[ Open and Upcoming Work Requests ]"))
        print()
        self.display_all_work_requests_printed(work_request_list)
        if self.rank != "Employee":
            print("{:0}{:>3}{:>15}{:>3}{:>19}".format("1. Select Request", "|", "2. New Requests", "|", "3. Pending Requests"))
            print("{:0}{:>3}{:>20}{:>3}{:>19}".format("4. My Requests", "|", "5. Closed Requests", "|", "6. Add Request" ))
            print()
        else:
            print("{:0}{:>3}{:>20}".format("1. Select Request", "|", "2. New Requests"))
            print("{:0}{:>3}{:>20}".format("3. Pending Requests", "|", "4. My Requests"))
            print()
        user_choice = input("Select an Option: ")
        print("-" * 70)
        match (user_choice , self.rank):
            case ("1", self.rank): 
                self.select_work_request_by_id()
            case ("2", self.rank):
                self.display_all_new_work_requests_printed()
            case ("3", self.rank):
                self.display_all_pending_work_requests_printed()
            case ("4", self.rank):
                self.display_my_work_requests_printed()
            case ("5", "Admin") | ("5", "Manager"):
                self.display_closed_work_requests_printed()
            case ("6", "Admin") | ("6", "Manager"): 
                self.display_create_work_request_form()
            case "q":
                print("Departing from NaN Air, Thank you for Visiting!")
            case "Q":
                print("Departing from NaN Air, Thank you for Visiting!")
            case _:
                print("Invalid Input, Please Try Again.")
                self.start_point_work_requests_UI()

    # Works, but lacks verification on user input. Also can be beautified
    def select_work_request_by_id(self) -> print:
        """System asks user for the ID of the work request they wish to find and prints out 
        all it's information if it's found, otherwise it gives an error message. """
        try:
            work_request_selected_by_id = input("Enter Request ID: ")
        # if work_request_selected_by_id == "b" or work_request_selected_by_id == "B":
        #     self.display_work_requests_menu_items()
        # elif work_request_selected_by_id == "1":
            
            # is_valid = self.logic_wrapper.sanity_check_work_request_id(work_request_selected_by_id) 
            work_request_object = self.logic_wrapper.get_work_request_by_id(self.rank, self.location, work_request_selected_by_id) # valid_select_conditition
            self.display_selected_work_request_information(work_request_object)
            if work_request_object != None:
                if self.rank != "Employee":
                    self.general_edit_work_request_form(work_request_object)
                else:
                    self.employee_edit_work_request_form(work_request_object)
        except:
            print()
            print("No Work Request With That ID Was Found, Please Try Again.")
            print()
            self.select_work_request_by_id
    
    # Works, but needs verification for user input. Also can be beautified.
    def display_create_work_request_form(self) -> print:
        """Creates a new work request object and asks for different information details that are passed to, and set
        for the class model. Once completed the validity of the request object is verified: if it returns True it's
        created but otherwise it returns the user to the main menu. """

        new_work_request = WorkRequest()
        print()
        print("[ New Work Request Form ]")
        print("-" * 70)
        
        while (request_name := input("Request Name: ").strip()):
            if request_name.isalpha() == True:
                break 
        new_work_request.set_name(request_name)

        while (request_description := input("Request Descrptition: ").strip()):
            if request_description.isalpha() == True:
                break
        new_work_request.set_description(request_description)  

        while (property_id := input("Property ID Assigned: ").strip()):
            is_property_id_valid = self.logic_wrapper.sanity_check_new_work_request_property_id(property_id)
            if is_property_id_valid == True:
                break
        new_work_request.set_property_id(property_id)
        
        while (start_date := input("Start Date: ").strip()):
            if len(start_date) == 6:
                break
        new_work_request.set_start_date(start_date)

        while (completition_date := input("Completition Date: ").strip()):
            if len(completition_date) == 6:
                break
        new_work_request.set_completition_date(completition_date)

        while (repetitive_work := input("Mark Repititive? (Yes or No): ").strip()):
            is_set_repetitive_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(repetitive_work)
            if is_set_repetitive_boolean == True:
                break
        new_work_request.set_repetitive_work(repetitive_work)

        while (interval_days := int(input("Interval of Days Until Request Re-Opens: ").strip())):
            if interval_days > 0:
                break
        new_work_request.set_reopen_interval(interval_days)
        
        while (set_priority := input("Request Priority (High, Medium or Low): ").strip()):
            is_priority_set_valid = self.logic_wrapper.sanity_check_priority_for_request(set_priority)
            if is_priority_set_valid == True:
                break
        new_work_request.set_priority(set_priority)

        while (needs_contractor := input("Request Needs Contractor (Yes or No): ").strip()):
            is_needs_contractor_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(needs_contractor)
            if is_needs_contractor_boolean == True:
                break
        new_work_request.set_need_contractor(needs_contractor)

        if self.rank == "Admin": 
            while set_location := input("Set Location for Work Request: "):
                is_set_location_valid = self.logic_wrapper.sanity_check_location_for_request(set_location)
                if is_set_location_valid == True:
                    break 
            new_work_request.set_location(set_location)
        else:
            new_work_request.set_location(self.location)
        print()    
        while (new_work_request_confirmation := input("Enter 1 to Confirm: ") != "1"):
            print("Sigma Sigma on the wall, who is the Skibidiest of them all")
        print("-" * 70)
        print()
        print(new_work_request.to_dict())
        
        self.logic_wrapper.add_work_request(new_work_request)
        return
         
        # print("Something Went Wrong When Creating the Work Request, Please Try Again.")
        pass
        
    # Displays options, not been tested enough to verify it's functionality. 
    def employee_edit_work_request_form(self, work_request):
        if work_request.mark_as_completed == False:
            print()
            print("-" * 70)
            mark_as_completed = input("Mark as Completed (Yes or No): ")
            is_input_for_mark_completed_valid = self.logic_wrapper.sanity_check_work_request(mark_as_completed)

            if is_input_for_mark_completed_valid == True:
                updated_work_request = work_request.set_mark_as_done(is_input_for_mark_completed_valid)
                self.logic_wrapper.edit_work_requests(updated_work_request)
                self.display_work_requests_menu_items() 
        
        if work_request.acceptance_status == False:
            print()
            print("-" * 70)
            accept_work_request = input("Aceept (Yes or No): ")
            is_input_for_accepted_valid = self.logic_wrapper.sanity_check_work_request(accept_work_request)

            if is_input_for_accepted_valid == True:
                updated_work_request = work_request.set_mark_as_done(is_input_for_accepted_valid)
                self.logic_wrapper.edit_work_requests(updated_work_request)
                self.display_work_requests_menu_items()
        pass
    
    # Displays options, not been tested enough to verify it's functionality.
    def general_edit_work_request_form(self, work_request):
        print()
        print("Choose a Category To Edit")
        print("-" * 70)
        print("{:>18}".format("> 1. Employee ID"))
        print("{:>18}".format("> 2. Property ID"))
        print("{:>24}".format("> 3. Repitition"))
        print("{:>15}".format("> 4. Priority"))
        print("{:>21}".format("> 5. Request Status"))
        print("-" * 70)
        category_to_edit = input("Choose a Category to Edit: ")

        match category_to_edit:
            case "1":
                new_employee_id_for_request = input("Enter New Employee ID: ")
                is_name_input_valid = self.logic_wrapper.sanity_check_work_request(new_employee_id_for_request)
                
                if is_name_input_valid == True:
                    updated_work_request = work_request.set_mark_as_done(is_name_input_valid)
                    self.logic_wrapper.edit_work_requests(updated_work_request)
                    self.display_work_requests_menu_items()

            case "2": 
                new_property_id_for_request = input("Enter New Property ID: ")
                is_property_id_input_valid = self.logic_wrapper.sanity_check_work_request(new_property_id_for_request)
                
                if is_property_id_input_valid == True:
                    updated_work_request = work_request.set_mark_as_done(is_property_id_input_valid)
                    self.logic_wrapper.edit_work_requests(updated_work_request)
                    self.display_work_requests_menu_items()

            case "3":
                update_is_request_repitive = input("Is Repitive? (Yes or No): ")
                is_request_input_valid = self.logic_wrapper.sanity_check_work_request(update_is_request_repitive)
                
                if is_request_input_valid == True:
                    updated_work_request = work_request.set_mark_as_done(is_request_input_valid)
                    self.logic_wrapper.edit_work_requests(updated_work_request)
                    self.display_work_requests_menu_items()

            case "4":
                new_priority_for_request = input("Enter New Priority for Request: ")
                is_priority_input_valid = self.logic_wrapper.sanity_check_work_request(new_priority_for_request)
                
                if is_priority_input_valid == True:
                    updated_work_request = work_request.set_mark_as_done(is_priority_input_valid)
                    self.logic_wrapper.edit_work_requests(updated_work_request)
                    self.display_work_requests_menu_items()

            case "5":
                update_request_status = input("Mark as Completed? (Yes or No): ")
                is_request_input_valid = self.logic_wrapper.sanity_check_work_request(update_request_status)
                
                if is_request_input_valid == True:
                    updated_work_request = work_request.set_mark_as_done(is_request_input_valid)
                    self.logic_wrapper.edit_work_requests(updated_work_request)
                    self.display_work_requests_menu_items()

        # updated_work_request_confirmation_confirmation = input("Enter 1 to Confirm: ")
        pass
            
            
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
        pass


    def display_all_new_work_requests_printed(self): 
        new_work_request_list = self.logic_wrapper.get_all_new_work_requests(self.rank, self.location)
        self.display_all_work_requests_printed(new_work_request_list)
        is_accepted = False

        selected_work_request = input("Enter 1 to Select a Work Request or B to Go Back: ")
        if selected_work_request == "1":
            self.select_work_request_by_id(is_accepted)
        elif selected_work_request == "b" or selected_work_request == "B":
            self.start_point_work_requests_UI()
        else: 
            self.display_all_new_work_requests_to_accept_printed()
        pass
        
    
    def display_all_pending_work_requests_printed(self): 
        pending_work_request_list = self.logic_wrapper.get_all_pending_work_requests(self.rank, self.location)
        self.display_all_work_requests_printed(pending_work_request_list)
        is_pending = True

        selected_work_request = input("Enter 1 to Select a Work Request or B to Go Back: ")
        if selected_work_request == "1":
            self.select_work_request_by_id(is_pending)
        elif selected_work_request == "b" or selected_work_request == "B":
            self.start_point_work_requests_UI()
        else: 
            self.display_all_pending_work_requests_printed()
        pass

    def display_closed_work_requests_printed(self): 
        closed_work_request_list = self.logic_wrapper.get_all_closed_work_requests(self.rank, self.location)
        self.display_all_work_requests_printed(closed_work_request_list)
        is_closed = True
        
        selected_work_request = input("Enter 1 to Select a Work Request or B to Go Back: ")
        if selected_work_request == "1":
            self.select_work_request_by_id(is_closed)
        elif selected_work_request == "b" or selected_work_request == "B":
            self.start_point_work_requests_UI()
        else: 
            self.display_closed_work_requests_printed()
        pass