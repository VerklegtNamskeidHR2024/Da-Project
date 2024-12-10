from Model_Classes.work_request_model import WorkRequest

class work_request_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location

    # Completed. 
    def start_point_work_requests_UI(self) -> str:
        """When an instance of this class is created, the class object calls this function first which in 
        turn calls the function to load the work request menu and it's options for the user. """

       
        work_request_menu = self.menu_selection_logistics()
        if work_request_menu == "q" or work_request_menu == "b": 
            return work_request_menu 
        

    # Completed. Can be beautified.
    def display_all_work_requests_printed(self, work_request_list: list): 
        """Prints out all open work requests with their ID, Name and Description. """
        
        if len(work_request_list) == 0:
            print()
            print("{:>50}".format("No Work Requests To Display")) 
            print()
        else:
            print("{:0}{:>6}{:>5}{:>9}{:>12}".format("ID", "|", "Name", "|", "Description"))
            print("-" * 70)
            for item in sorted(work_request_list):
                print("{:0}{:>3}{:>10}{:>4}{:>51}".format(item.work_request_id, "|", item.name, "|", item.description)) 
            print("-" * 70)
        
        
    # Completed. Can be beautified.
    def display_selected_work_request_information(self, work_request: object):
        """Receives a single, user-selected work request and displays all of its information for them to read. """
        
        print("-" * 70)
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
        print("{:0}{:>9}{:<10}".format("Repititive Work", "|", str(work_request.repetitive_work)))
        print("{:0}{:>3}{:<10}".format("Re-Open Interval Days", "|", work_request.reopen_interval)) 
        print("-" * 35)
        print("{:0}{:>16}{:<10}".format("Priority", "|", work_request.priority))
        print("{:0}{:>7}{:<10}".format("Status", "|", work_request.work_request_status))
        print("{:0}{:>7}{:<10}".format("Needs Contractor", "|", str(work_request.need_contractor)))
        print("{:0}{:>11}{:<10}".format("Completed", "|", str(work_request.mark_as_completed)))
        print("{:0}{:>4}{:<10}".format("Accepted by Employee", "|", str(work_request.accepted_by_employee))) 
        print("-" * 70)

    # Completed. Can be beautified.
    def display_work_requests_menu_items(self) -> str:
        """Displays all open work requests and menu options depending on if the user logged in is an admin/manager
        or an employee. It then asks the user to select an option which is sent to be verified in the function 
        below. """

        print()
        print(f"{self.rank} - Work Request Menu")
        print("-" * 70)
        print("{:>50}".format("[ Open and Upcoming Work Requests ]"))
        print()
        work_request_list = self.logic_wrapper.get_all_work_requests_at_location(self.rank, self.location)
        self.display_all_work_requests_printed(work_request_list)
        if self.rank != "Employee":
            print("{:0}{:>3}{:>15}{:>3}{:>19}".format("1. Select Request", "|", "2. New Requests", "|", "3. Pending Requests"))
            print("{:0}{:>3}{:>20}{:>3}{:>19}".format("4. My Requests", "|", "5. Closed Requests", "|", "6. Add Request" ))
            print()
            print("{:>20}".format("> Go Back: b, B"))
            print("{:>20}".format("> Quit System: q, Q"))
            print()
        else:
            print("{:0}{:>3}{:>20}".format("1. Select Request", "|", "2. New Requests"))
            print("{:0}{:>3}{:>20}".format("3. Pending Requests", "|", "4. My Requests"))
            print()
            print("{:>20}".format("> Go Back: b, B"))
            print("{:>20}".format("> Quit System: q, Q"))
            print()
        user_choice = input("Select an Option: ").lower()
        return user_choice 
    
    # Completed. Has a functioning quit and back feature. Can be beautified.
    def menu_selection_logistics(self) -> str:
        """Calls the menu display function above and performs low-level logicistics to interpret the user input it received.
        If it's verified as an invalid input the system displays an error message and performs the operation again. """

        user_choice = ""
        while user_choice != "q": 
            user_choice = self.display_work_requests_menu_items()
            match (user_choice , self.rank):
                case ("1", self.rank): 
                    user_choice = self.select_work_request_by_id()
                case ("2", self.rank):
                    user_choice = self.display_and_select_new_work_requests()
                case ("3", self.rank):
                    user_choice = self.display_and_select_pending_work_requests()
                case ("4", self.rank):
                    user_choice = self.display_and_select_my_work_request()
                case ("5", "Admin") | ("5", "Manager"):
                    user_choice = self.display_and_select_closed_work_requests()
                case ("6", "Admin") | ("6", "Manager"): 
                    user_choice = self.display_create_work_request_form()
                case ("b", self.rank):
                    return "b"
                case ("q", self.rank):
                    
                    return "q"
                case _:
                    print("Invalid Input, Please Try Again.")
        return user_choice
        

    # Completed. Could make it so that it verifies where in the system the user is selecting a work request from.
    # 
    # 
    # Example of current functionality: "User is viewing a list of new work requests, enters the ID of a closed work
        # request and receives it."
    # 
    # 
    # Example of desired functionality: "User is viewing a list of new work requests, enters the ID of a closed work 
        # request and is given an error message (akin to: Can't Access This Work Request At The Moment). "
    # 
    # 
    # Has a functioning quit and back feature. Can be beautified.
    def select_work_request_by_id(self) -> str:
        """System asks the user to enter an ID of the work request they wish to select. If found, the system 
        will display all of its information and directs them to the editing function below. Otherwise it gives 
        an error message and restarts its operation. """

        print()
        print("-" * 70)
        print()
        while (work_request_selected_by_id := input("Enter Request ID: ")) != "q" and work_request_selected_by_id != "Q":
            if work_request_selected_by_id.lower() == "b" or work_request_selected_by_id == "B":
                break
            if len(work_request_selected_by_id) < 3:
                print()
                print("Must Enter A Valid Work Request ID")
                print()
            work_request_object = self.logic_wrapper.get_work_request_by_id(self.rank, self.location, work_request_selected_by_id) 
            if work_request_object != None:
                self.display_selected_work_request_information(work_request_object)
                edit_work_request = self.edit_work_request_logistics(work_request_object)
                if edit_work_request == "b":
                    continue
                return edit_work_request.lower()
            else:
                print()
                print("Work Request Could Not Be Found, Please Try Again.")
                print()
        return work_request_selected_by_id.lower()
    
    # Completed. Has a functioning quit and back feature. Can be beautified.
    def edit_work_request_logistics(self, work_request_object) -> str: 
        """Receives a single, user-selected work request and gives the user the ability to edit its information; 
        the extent of which corresponding to the user's rank. Also verifies what can be edited based on what the
        work requests attributes are set as. """
            
        if self.rank != "Employee":
            edit_work_request = self.general_edit_work_request_selected_option(work_request_object)
            return edit_work_request.lower()
        
        elif (work_request_object.mark_as_completed == True and work_request_object.work_request_status == "Pending"):
            print()
            print("{:>20}".format("> Go Back: b, B"))
            print("{:>20}".format("> Quit System: q, Q"))
            print()
            while(go_back_or_quit := input("Select an Option: ").lower()) != "q" and go_back_or_quit != "b":
                print()
                print("Nah Ah, You Can't Do That...")
                print()
            return go_back_or_quit.lower()
        
        elif (work_request_object.accepted_by_employee == False and work_request_object.work_request_status == "New"):
            accept_work_request = self.employee_accept_work_request_(work_request_object)
            return accept_work_request.lower()
        
        elif (work_request_object.mark_as_completed == False and work_request_object.work_request_status == "Open"):
            mark_completed = self.mark_work_request_completed(work_request_object)
            return mark_completed.lower()
                            
    
    # Completed. Can be beautified.
    def display_create_work_request_form(self) -> str:
        """When this function is called, it begins by creating a new instance of a work request which is then passed down to the 
        functions below where many of its attributes are set by the user. """

        new_work_request = WorkRequest()
        print()
        print("[ New Work Request Form ]")
        print("-" * 70)
        print()
        print("{:>15}".format("> Go Back: b, B"))
        print("{:>20}".format("> Quit System: q, Q"))
        print()
        print("-" * 70)
        request_name = self.set_name_for_request(new_work_request)
        return request_name

    # Completed. Has a functioning quit and back feature. Can be beautified.
    def set_name_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter a name for the work request they are creating. Goes through very simple input 
        verification before setting the name attribute to what the user entered and passing the object down 
        to the next function. """

        while (request_name := input("Request Name: ")) != "q" and request_name != "Q":
            if request_name == "b" or request_name == "B":
                break
            if len(request_name) < 5:
                print()
                print("This Field Is Required To Fill Out")
                print()
            else:
                new_work_request.set_name(request_name)
                request_description = self.set_description_for_request(new_work_request)
                if request_description == "b":
                    continue 
                return request_description
        return request_name.lower()

    # Completed. Has a functioning quit and back feature. Can be beautified.
    def set_description_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter a description for the work request they are creating. Goes through very simple input 
        verification before setting the description attribute to what the user entered and passing the object down 
        to the next function. """

        while (request_description := input("Request Descriptition: ")) != "q" and request_description != "Q":
            if request_description == "b" or request_description == "B":
                break
            if len(request_description) < 10:
                print()
                print("This Field Is Required To Fill Out")   
                print() 
            else:
                new_work_request.set_description(request_description)
                property_id = self.set_property_id_for_request(new_work_request)  
                if property_id == "b":
                    continue
                return property_id
        return request_description.lower()

    # Completed. Has a functioning quit and back feature. Can be beautified.
    def set_property_id_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter the property ID for the work request they are creating. Its then sent to the logic
        layer where the input is verified. If its verified as valid, it sets the property ID attribute to what the user
        entered before passing the object down to the next function. Otherwise it begins the operation again. """

        while (property_id := input("Assign A Property ID To The Request: ")) != "q" and property_id != "Q":
            if property_id == "b" or property_id == "B":
                break
            is_property_id_valid = self.logic_wrapper.sanity_check_work_request_property_id(property_id)
            if is_property_id_valid == True:
                new_work_request.set_property_id(property_id)
                start_date = self.set_start_date_for_request(new_work_request)
                if start_date == "b":
                    continue
                return start_date
            else:
                print()
                print("This Field Is Required To Fill Out")
                print()
        return property_id.lower()
    
    # Completed. Has a functioning quit and back feature. Can be beautified.
    def set_start_date_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter the start date for the work request they are creating. Goes through very simple input 
        verification before setting the start date attribute to what the user entered and passing the object down to 
        the next function. """
         
        while (start_date := input("Set The Start Date: ")) != "q" and start_date != "Q":
            if start_date == "b" or start_date == "B":
                break
            if len(start_date) == 8:
                new_work_request.set_start_date(start_date)
                completition_date = self.set_completition_date_for_request(new_work_request)
                if completition_date == "b":
                    continue
                return completition_date
            else:
                print()
                print("This Field Is Required To Fill Out")
                print()
        return start_date.lower()

    # Completed. Has a functioning quit and back feature. Can be beautified.
    def set_completition_date_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter the completition date for the work request they are creating. Goes through very simple input 
        verification where, it has to either be nothing (since this field is not required to fill out) or exactly 8 characters long.
        The completion date attribute is then set to what the user entered and the object passed down to the next function. """

        while (completition_date := input("Set The Completition Date (Not Required): ")) != "q" and completition_date != "Q":
            if completition_date == "b" or completition_date == "B":
                break
            if len(completition_date) == 8 or completition_date == "":
                new_work_request.set_completition_date(completition_date)
                repetitive_work = self.set_repetitive_work_for_request(new_work_request)
                if repetitive_work == "b":
                    continue
                return repetitive_work
            else:
                print()
                print("Completition Date Must Be Formatted Correctly")
                print()
        return completition_date.lower()

    # Completed. Has a functioning quit and back feature. Can be beautified.
    def set_repetitive_work_for_request(self, new_work_request: object) -> str:
        while (repetitive_work := input("Mark Request Repititive? (Yes or No): ")) != "q" and repetitive_work != "Q":
            if repetitive_work == "b" or repetitive_work == "B":
                break 
            is_set_repetitive_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(repetitive_work)
            if is_set_repetitive_boolean == True or is_set_repetitive_boolean == False:
                new_work_request.set_repetitive_work(is_set_repetitive_boolean)
                interval_days = self.set_interval_days_for_request(new_work_request)
                if interval_days == "b":
                    continue
                return interval_days
            else:
                print()
                print("This Field Is Required To Fill Out")
                print()
        return repetitive_work.lower()

    # Completed. Has a functioning quit and back feature. Can be beautified.
    def set_interval_days_for_request(self, new_work_request: object):
        while (interval_days := input("Set The Interval Of Days Until Request Re-Opens: ")) != "q" and interval_days != "Q":
            try:
                if interval_days == "b" or interval_days == "B":
                    break    
                if interval_days == "":
                    print()
                    print("This Field Is Required To Fill Out")
                    print()
                elif int(interval_days) >= 0:
                    new_work_request.set_reopen_interval(interval_days)
                    set_priority = self.set_priority_for_request(new_work_request)
                    if set_priority == "b":
                        continue
                    return set_priority
            except ValueError:
                print()
                print("Alphabetic Characters Are Not Allowed, Please Try Again.")
                print()
                continue
        return interval_days.lower()
        
    # Completed. Has a functioning quit and back feature. Can be beautified.
    def set_priority_for_request(self, new_work_request: object):
        while (set_priority := input("Set The Request Priority (High, Medium or Low): ")) != "q" and set_priority != "Q":
            if set_priority == "b" or set_priority == "B":
                break
            is_priority_set_valid = self.logic_wrapper.sanity_check_priority_for_request(set_priority)
            if is_priority_set_valid == True:
                new_work_request.set_priority(set_priority)
                needs_contractor = self.set_needs_contractor_for_request(new_work_request)
                if needs_contractor == "b":
                    continue
                return needs_contractor
            else:
                print()
                print("This Field Is Required TO Fill Out")
                print()
        return set_priority.lower()
        
    # Completed. Has a functioning quit and back feature. Can be beautified.
    def set_needs_contractor_for_request(self, new_work_request: object):
        while (needs_contractor := input("Request Needs Contractor? (Yes or No): ")) != "q" and needs_contractor != "Q":
            if needs_contractor == "b" or needs_contractor == "B":
                break
            is_needs_contractor_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(needs_contractor)
            if is_needs_contractor_boolean == True or is_needs_contractor_boolean == False:
                new_work_request.set_need_contractor(needs_contractor)
                set_location = self.set_location_for_request(new_work_request)
                if set_location == "b":
                    continue
                return set_location
            else:
                print()
                print("This Field Is Required TO Fill Out")
                print()
        return needs_contractor.lower()
        
    # Completed. Has a functioning quit and back feature. Can be beautified.
    def set_location_for_request(self, new_work_request: object):
        if self.rank == "Admin": 
            while (set_location := input("Set Location for Work Request: ")) != "q" and set_location != "Q":
                if set_location == "b" or set_location == "B":
                    break
                is_set_location_valid = self.logic_wrapper.sanity_check_location_for_request(set_location)
                if is_set_location_valid == True:
                    new_work_request.set_location(set_location)
                    confirmation = self.work_request_confirmation(new_work_request) 
                    if confirmation == "b":
                        continue
                    return confirmation 
                else:
                    print()
                    print("This Field Is Required TO Fill Out")
                    print()
            return set_location.lower()
        else:
            new_work_request.set_location(self.location)
    
    # Completed. Has a functioning quit and back feature. Can be beautified.
    def work_request_confirmation(self, new_work_request: object):
        print()    
        while (new_work_request_confirmation := input("Enter 1 to Confirm: ").lower()) != "1": 
            if new_work_request_confirmation == "q" or new_work_request_confirmation == "b":
                return new_work_request_confirmation.lower()
            else:
                print("Sigma Sigma on the wall, who is the Skibidiest of them all")
        print("-" * 70)
        print()
        self.logic_wrapper.add_work_request(new_work_request)
        print("Work Request Has Been Created!")
        print()
        return
        
    # Completed. Has a functioning quit and back feature. Can be beautified.
    def employee_accept_work_request_(self, work_request: object):
        """Allows the employee accept a new work request. """

        print("{:>20}".format("> Go Back: b, B"))
        print("{:>20}".format("> Quit System: q, Q"))
        print()
        print("-" * 70)

        while (accept_work_request := input("Aceept (Yes or No): ")) != "q" and accept_work_request != "Q":
            if accept_work_request == "b" or accept_work_request == "B":
                break
            if len(accept_work_request) < 2: 
                print()
                print("This Field Is Required to Fill Out.")
                print()

            is_accepted_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(accept_work_request)
            if is_accepted_boolean == True:
                print()
                # Asks for staff ID
                while (staff_id := input("Enter Your Staff ID: ")) != "q" and staff_id != "Q": 
                    is_staff_id_valid = self.logic_wrapper.sanity_check_sanity_check_staff_id_for_request(staff_id)
                    if is_staff_id_valid == True:
                        while (update_confirmation := input("Enter 1 to Confirm: ").lower()) != "1":
                            if update_confirmation == "q" or update_confirmation == "b":
                                return update_confirmation.lower()
                            print("Mama they took my dingus")
                        work_request.set_accepted_by_employee(is_accepted_boolean)
                        self.logic_wrapper.edit_work_request(work_request)
                        print()
                        print("Work Request Has Been Accepted!")
                        print()
                        return
                    else:
                        print("Invalid")

            if is_accepted_boolean == False:
                while (update_confirmation := input("Enter 1 to Confirm: ").lower()) != "1":
                    if update_confirmation == "q" or update_confirmation == "b":
                        return update_confirmation.lower()
                    print("Mama they took my dingus")
                work_request.set_accepted_by_employee(is_accepted_boolean)
                work_request.set_staff_id(staff_id)
                self.logic_wrapper.edit_work_request(work_request)
                print()
                print("Work Request Has Been Rejected!")
                print()
                return
            else:
                print("Invalid")
        return accept_work_request.lower()
        
    # Completed. Has a functioning quit and back feature. Can be beautified.
    def mark_work_request_completed(self, work_request: object):
        """Allows the user to mark a work request completed. """

        print()
        print("-" * 70)
        print()
        print("{:>20}".format("> Go Back: b, B"))
        print("{:>20}".format("> Quit System: q, Q"))
        print()
        print("-" * 70)
        while (mark_as_completed := input("Mark as Completed (Yes or No): ")) != "q" and mark_as_completed != "Q":
            if mark_as_completed == "b" or mark_as_completed == "B":
                break
            if len(mark_as_completed) < 2:
                print()
                print("Invalid")
                print()

            is_marked_completed_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(mark_as_completed)
            if is_marked_completed_boolean == True:
                print()
                while (update_confirmation := input("Enter 1 to Confirm: ").lower()) != "1":
                    if update_confirmation == "q" or update_confirmation == "b":
                        return update_confirmation.lower()
                    print("Mama they took my dingus")
                work_request.set_mark_as_done(is_marked_completed_boolean)
                self.logic_wrapper.edit_work_request(work_request)
                print()
                print("Work Request Has Been Marked Completed!")
                print()
                break

            if update_confirmation == False:
                print()
                while (update_confirmation := input("Enter 1 to Confirm: ").lower()) != "1":
                    if update_confirmation == "q" or update_confirmation == "b":
                        return update_confirmation.lower()
                    print("Mama they took my dingus")
                work_request.set_mark_as_done(is_marked_completed_boolean)
                self.logic_wrapper.edit_work_request(work_request)
                print()
                print("Work Request Has Been Marked Not Completed.")
                print()
                break
            else:
                print("Mama they took my dingus")
        return mark_as_completed.lower()
    
    # Completed. Has a functioning quit and back feature. Can be beautified.
    def general_edit_work_request_menu(self) -> str:
        """Displays all the categories that an admin or manager are able to edit about a work request they have selected.
        It then asks them to select one of the 5, where the input is then sent to, and verified in the function below. """

        print()
        print("Choose a Category To Edit")
        print("-" * 70)
        print("{:>15}".format("> 1. Employee ID"))
        print("{:>15}".format("> 2. Property ID"))
        print("{:>15}".format("> 3. Mark Repitive"))
        print("{:>15}".format("> 4. Priority"))
        print("{:>15}".format("> 5. Mark Completed"))
        print()
        print("{:>18}".format("> Go Back: b, B"))
        print("{:>18}".format("> Quit System: q, Q"))
        print()
        print("-" * 70)
        category_to_edit = input("Choose a Category to Edit: ").lower()
        return category_to_edit.lower()

    # Completed. Has a functioning quit and back feature. Can be beautified.
    def general_edit_work_request_selected_option(self, work_request: object) -> str:
        """Calls the edit menu function above and performs low-level logicistics to interpret the user input it received.
        If it's verified as an invalid input the system displays an error message and performs the operation again. """

        category_to_edit = ""
        while category_to_edit != "q":
            category_to_edit = self.general_edit_work_request_menu()
            match category_to_edit:
                case "1":
                    category_to_edit = self.edit_employee_id_for_work_request(work_request)
                case "2":
                    category_to_edit = self.edit_property_id_for_request(work_request)   
                case "3":
                    category_to_edit = self.edit_repitive_work_request(work_request)
                case "4":
                    category_to_edit = self.edit_priority_for_request(work_request)
                case "5":
                    category_to_edit = self.mark_work_request_completed(work_request)
                case "b":
                    return "b"
                case "q":
                    return "q"
                case _:
                    print("Mama they took my dingus")
        return category_to_edit.lower()

    # Completed. Has a functioning quit and back feature. Can be beautified.
    def edit_employee_id_for_work_request(self, work_request: object):
        
        while (edit_employee_id_for_request := input("New Employee ID: ")) != "q" and edit_employee_id_for_request != "Q":
            if edit_employee_id_for_request == "b" or edit_employee_id_for_request == "B":
                break
            is_employee_valid = self.logic_wrapper.sanity_check_employee_id_for_request(edit_employee_id_for_request)
            if is_employee_valid == True:
                print()
                while (update_confirmation := input("Enter 1 to Confirm: ").lower()) != "1":
                    if update_confirmation == "q" or update_confirmation == "b":
                        return update_confirmation.lower()
                    else:
                        print("Sigma Sigma on the wall, who is the Skibidiest of them all")
                work_request.set_staff_id(edit_employee_id_for_request)
                self.logic_wrapper.edit_work_request(work_request)
                return
            else:
                print("Mama they took my dingus")
        return edit_employee_id_for_request.lower()
            
    # Completed. Has a functioning quit and back feature. Can be beautified.
    def edit_property_id_for_request(self, work_request: object):
        while (edit_property_id_for_request := input("New Property ID: ")) != "q" and edit_property_id_for_request != "Q":
            if edit_property_id_for_request == "b" or edit_property_id_for_request == "B":
                break
            is_property_id_valid = self.logic_wrapper.sanity_check_work_request_property_id(edit_property_id_for_request)
            if is_property_id_valid == True:
                print()
                while (update_confirmation := input("Enter 1 to Confirm: ").lower()) != "1":
                    if update_confirmation == "q" or update_confirmation == "b":
                        return update_confirmation.lower()
                    else:
                        print("Sigma Sigma on the wall, who is the Skibidiest of them all")
                work_request.set_property_id(edit_property_id_for_request)
                self.logic_wrapper.edit_work_request(work_request)
                return
            else:
                print("Mama they took my dingus")
        return edit_property_id_for_request.lower()

    # Completed. Has a functioning quit and back feature. Can be beautified.
    def edit_repitive_work_request(self, work_request: object):
        while (edit_repitive_work_request := input("Is Repitive? (Yes or No): ")) != "q" and edit_repitive_work_request != "Q":
            if edit_repitive_work_request == "b" or edit_repitive_work_request == "B":
                break
            is_repetitive_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(edit_repitive_work_request)
            if is_repetitive_boolean == True or is_repetitive_boolean == False:
                print()
                while (update_confirmation := input("Enter 1 to Confirm: ").lower()) != "1":
                    if update_confirmation == "q" or update_confirmation == "b":
                        return update_confirmation.lower()
                    else:
                        print("Sigma Sigma on the wall, who is the Skibidiest of them all")
                work_request.set_repetitive_work(is_repetitive_boolean)
                self.logic_wrapper.edit_work_request(work_request)
                return
            else:
                print("Mama they took my dingus")
        return edit_repitive_work_request.lower()

    # Completed. Has a functioning quit and back feature. Can be beautified.
    def edit_priority_for_request(self, work_request: object):    
        while (edit_priority_for_request := input("Priority for Request: ")) != "q" and edit_priority_for_request != "Q":
            if edit_priority_for_request == "b" or edit_priority_for_request == "B":
                break
            is_priority_valid = self.logic_wrapper.sanity_check_priority_for_request(edit_priority_for_request)
            if is_priority_valid == True:
                print()
                while (update_confirmation := input("Enter 1 to Confirm: ").lower()) != "1":
                    if update_confirmation == "q" or update_confirmation == "b":
                        return update_confirmation.lower()
                    else:
                        print("Sigma Sigma on the wall, who is the Skibidiest of them all")
                work_request.set_priority(edit_priority_for_request)
                self.logic_wrapper.edit_work_request(work_request)
                return
            else:
                print("Mama they took my dingus")
        return edit_priority_for_request.lower()
    

    """The functions below could very well be combined into one, larger function. """

    # Works. Only displays work requests in the selected location and if they have been accepted by an employee. 
    # Needs to filter the work requests displayed by staff ID as well to be fully functioning. Could do so by having the user
    # enter a staff ID during the log in menu.
    # 
    # 
    # Has a functioning quit and back feature. Can be beautified.
    def display_and_select_my_work_request(self):
        """Displays all work requests that have been accepted by an employee. """

        while (staff_id := input("Enter Your Staff ID: ")) != "q" and staff_id != "Q": 
            if staff_id == "b" or staff_id == "B":
                return staff_id.lower()
            is_staff_id_valid = self.logic_wrapper.sanity_check_staff_id_for_request(staff_id)
            if is_staff_id_valid == True:
                break
            else:
                print("Invalid")

        selected_work_request = ""
        while selected_work_request != "q" and selected_work_request != "b":
            print()
            print("{:>50}".format("[ My Work Requests ]"))
            print("-" * 70)
            my_work_request_list = self.logic_wrapper.get_my_work_requests(self.rank, self.location)
            self.display_all_work_requests_printed(my_work_request_list)
            print()
            print("{:>15}".format("> Go Back: b, B"))
            print("{:>18}".format("> Quit System: q, Q"))
            print("-" * 70)
            selected_work_request = self.select_work_request_by_id()
        return selected_work_request.lower()

    
    # Completed. Can be beautifed.
    def display_and_select_new_work_requests(self): 
        """Displays all new work requests that haven't been accepted by an employee. """
        
        selected_work_request = ""
        while selected_work_request != "q" and selected_work_request != "b":
            print()
            print("{:>50}".format("[ New Work Requests ]"))
            print("-" * 70)
            new_work_request_list = self.logic_wrapper.get_all_new_work_requests(self.rank, self.location)
            self.display_all_work_requests_printed(new_work_request_list)
            print()
            print("{:>15}".format("> Go Back: b, B"))
            print("{:>18}".format("> Quit System: q, Q"))
            print("-" * 70)
            selected_work_request = self.select_work_request_by_id()
        return selected_work_request.lower()
        
    
    
    # Completed. Can be beautifed.
    def display_and_select_pending_work_requests(self): 
        """Prints out all pending work requests that haven't been marked closed by a manager or admin. """
        
        selected_work_request = ""
        while selected_work_request != "q" and selected_work_request != "b":
            print()
            print("{:>50}".format("[ Pending Work Requests ]"))
            print("-" * 70)
            pending_work_request_list = self.logic_wrapper.get_all_pending_work_requests(self.rank, self.location)
            self.display_all_work_requests_printed(pending_work_request_list)
            print()
            print("{:>15}".format("> Go Back: b, B"))
            print("{:>18}".format("> Quit System: q, Q"))
            print("-" * 70)
            selected_work_request = self.select_work_request_by_id()
        return selected_work_request.lower()


    # Completed. Can be beautifed.
    def display_and_select_closed_work_requests(self): 
        """Displats all closed work requests. """

        selected_work_request = ""
        while selected_work_request != "q" and selected_work_request != "b":
            print()
            print("{:>50}".format("[ Closed Work Requests ]"))
            print("-" * 70)
            closed_work_request_list = self.logic_wrapper.get_all_closed_work_requests(self.rank, self.location)
            self.display_all_work_requests_printed(closed_work_request_list)
            print()
            print("{:>20}".format("> Go Back: b, B"))
            print("{:>20}".format("> Quit System: q, Q"))
            print("-" * 70)
            selected_work_request = self.select_work_request_by_id()
        return selected_work_request.lower()