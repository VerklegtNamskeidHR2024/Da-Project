from Model_Classes.work_request_model import WorkRequest

class work_request_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location


    def start_point_work_requests_UI(self):
        """When this class is called it starts here, calling the display_requests_menu_items function 
        first to load the menu and it's options for the user. """

        self.display_work_requests_menu_items()

    # Completed, can be beautified.
    def display_all_work_requests_printed(self, work_request_list: list): 
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
    def display_selected_work_request_information(self, work_request: object):
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
    def display_work_requests_menu_items(self):
        """Displays the menu options depending if the user logged in is an admin/manager or
        an employee. It then calls the correct function based on what the user chose. """

        print()
        print(f"{self.rank} - Work Request Menu")
        print("-" * 70)
        print("{:^50}".format("[ Open and Upcoming Work Requests ]"))
        print()
        status = "Open"
        is_accepted = True
        work_request_list = self.logic_wrapper.get_all_work_requests_at_location(self.rank, self.location, status, is_accepted)
        self.display_all_work_requests_printed(work_request_list)
        if self.rank != "Employee":
            print("{:0}{:>3}{:>15}{:>3}{:>19}".format("1. Select Request", "|", "2. New Requests", "|", "3. Pending Requests"))
            print("{:0}{:>3}{:>20}{:>3}{:>19}".format("4. My Requests", "|", "5. Closed Requests", "|", "6. Add Request" ))
            print()
            print("{:>15}{:>5}".format("> Go Back:", "b, B"))
            print("{:>18}{:>5}".format("> Quit System:", "q, Q"))
            print()
        else:
            print("{:0}{:>3}{:>20}".format("1. Select Request", "|", "2. New Requests"))
            print("{:0}{:>3}{:>20}".format("3. Pending Requests", "|", "4. My Requests"))
            print()
            print("{:>15}{:>5}".format("> Go Back:", "b, B"))
            print("{:>18}{:>5}".format("> Quit System:", "q, Q"))
            print()
        while (user_choice := input("Select an Option: ")) != "q": 
            print("-" * 70)
            match (user_choice , self.rank):
                case ("1", self.rank): 
                    self.select_work_request_by_id(status, is_accepted)
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
                case "q" | "Q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                case "b" | "B":
                    print("Departing from NaN Air, Thank you for Visiting!")
                case _:
                    print("Invalid Input, Please Try Again.")

    # Works, but lacks more detailed verification on user input. Also can be beautified
    def select_work_request_by_id(self, status: str, is_accepted: bool):
        """System asks user for the ID of the work request they wish to find and prints out 
        all it's information if it's found, otherwise it gives an error message. """

        while (work_request_selected_by_id := input("Enter Request ID: ")) != "b":
            if len(work_request_selected_by_id) < 3:
                print()
                print("Must Enter A Valid Work Request ID")
                print()
            work_request_object = self.logic_wrapper.get_work_request_by_id(self.rank, self.location, work_request_selected_by_id, status, is_accepted) 
            if work_request_object != None:
                self.display_selected_work_request_information(work_request_object)
                if self.rank != "Employee":
                    self.general_edit_work_request_form(work_request_object)
                    return
                else:
                    if work_request_object.acceptance_status == False:
                        self.employee_accept_work_request_(work_request_object)
                        return
                    elif work_request_object.mark_as_completed == False:
                        self.mark_work_request_completed(work_request_object)
                        return
            print()
            print("Work Request Could Not Be Found, Please Try Again.")
            print()
            continue
        return
    
    # Completed, verification of user input can be improved. Also can be beautified.
    def display_create_work_request_form(self):
        """Creates a new work request object and asks for different information details that are passed to, and set
        for the class model. Once completed the validity of the request object is verified: if it returns True it's
        created but otherwise it returns the user to the main menu. """

        new_work_request = WorkRequest()
        print()
        print("[ New Work Request Form ]")
        print("-" * 70)
        print()
        print("{:>15}{:>5}".format("> Go Back:", "b, B"))
        print("{:>18}{:>5}".format("> Quit System:", "q, Q"))
        print()
        print("-" * 70)
        while (request_name := input("Request Name: ")) != "b":
            if len(request_name) < 5:
                print()
                print("This Field Is Required To Fill Out")
                print()
            else:
                break
        new_work_request.set_name(request_name)

        while (request_description := input("Request Descriptition: ")) != "b":
            if len(request_description) < 10:
                print()
                print("This Field Is Required To Fill Out")   
                print() 
            else:
                break
        new_work_request.set_description(request_description)  

        while (property_id := input("Property ID Assigned: ")) != "b":
                is_property_id_valid = self.logic_wrapper.sanity_check_work_request_property_id(property_id)
                if is_property_id_valid == True:
                    break
                print()
                print("This Field Is Required To Fill Out")
                print()
        new_work_request.set_property_id(property_id)
        
        while (start_date := input("Start Date: ")) != "b":
            if len(start_date) == 8:
                break
            print()
            print("This Field Is Required To Fill Out")
            print()
        new_work_request.set_start_date(start_date)

        while (completition_date := input("Completition Date (Not Required): ")) != "b":
            if len(completition_date) == 8 or completition_date == "":
                break
            print()
            print("Completition Date Must Be Formatted Correctly")
            print()
        new_work_request.set_completition_date(completition_date)

        while (repetitive_work := input("Mark Repititive? (Yes or No): ")) != "b":
            is_set_repetitive_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(repetitive_work)
            if is_set_repetitive_boolean == True or is_set_repetitive_boolean == False:
                break
            print()
            print("This Field Is Required To Fill Out")
            print()
        new_work_request.set_repetitive_work(is_set_repetitive_boolean)

        while (interval_days := input("Interval of Days Until Request Re-Opens: ")) != "b":
            try:
                if int(interval_days) >= 0:
                    break
                print()
                print("This Field Is Required To Fill Out")
                print()
            except ValueError:
                print()
                print("Alphabetic Characters Are Not, Please Try Again.")
                print()
                continue
        new_work_request.set_reopen_interval(interval_days)
        
        while (set_priority := input("Request Priority (High, Medium or Low): ")) != "b":
            is_priority_set_valid = self.logic_wrapper.sanity_check_priority_for_request(set_priority)
            if is_priority_set_valid == True:
                break
            print()
            print("This Field Is Required TO Fill Out")
            print()
        new_work_request.set_priority(set_priority)

        while (needs_contractor := input("Request Needs Contractor (Yes or No): ")) != "b":
            is_needs_contractor_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(needs_contractor)
            if is_needs_contractor_boolean == True:
                break
            print()
            print("This Field Is Required TO Fill Out")
            print()
        new_work_request.set_need_contractor(needs_contractor)

        if self.rank == "Admin": 
            while (set_location := input("Set Location for Work Request: ")) != "b":
                is_set_location_valid = self.logic_wrapper.sanity_check_location_for_request(set_location)
                if is_set_location_valid == True:
                    break 
                print()
                print("This Field Is Required TO Fill Out")
                print()
            new_work_request.set_location(set_location)
        else:
            new_work_request.set_location(self.location)
        print()    
        while (new_work_request_confirmation := input("Enter 1 to Confirm: ")) != "1":
            print("Sigma Sigma on the wall, who is the Skibidiest of them all")
        print("-" * 70)
        print()
        self.logic_wrapper.add_work_request(new_work_request)
        print("Work Request Has Been Created")
        return
         

    # Displays options, not been tested enough to verify it's functionality. 
    def employee_accept_work_request_(self, work_request: object):
        """Allows the employee accept a new work request. """

        print()
        print("-" * 70)
        print()
        print("{:>15}{:>5}".format("> Go Back:", "b, B"))
        print("{:>18}{:>5}".format("> Quit System:", "q, Q"))
        print()
        print("-" * 70)
        while (accept_work_request := input("Aceept (Yes or No): ")) != "b":
            if len(accept_work_request) < 2: 
                print()
                print("This Field Is Required to Fill Out.")
                print()
            is_accepted_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(accept_work_request)
            if is_accepted_boolean == True:
                updated_work_request = work_request.set_accepted_by_employee(is_accepted_boolean)
                self.logic_wrapper.edit_work_request(updated_work_request)
                print()
                print("Work Request Has Been Accepted!")
                print()
                break
            if is_accepted_boolean == False:
                updated_work_request = work_request.set_accepted_by_employee(is_accepted_boolean)
                self.logic_wrapper.edit_work_request(updated_work_request)
                print()
                print("Work Request Has Been Rejected!")
                print()
                break
            print("Mama they took my dingus")
        return
        

    def mark_work_request_completed(self, work_request: object):
        """Allows the user to mark a work request completed. """

        print()
        print("-" * 70)
        print()
        print("{:>15}{:>5}".format("> Go Back:", "b, B"))
        print("{:>18}{:>5}".format("> Quit System:", "q, Q"))
        print()
        print("-" * 70)
        mark_as_completed = ""
        while (mark_as_completed := input("Mark as Completed (Yes or No): ")) != "b":
            is_marked_completed_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(mark_as_completed)
            if is_marked_completed_boolean == True:
                while (updated_work_request_confirmation := input("Enter 1 to Confirm: ")) != "1":
                    print("Mama they took my dingus")
                updated_work_request = work_request.set_mark_as_done(is_marked_completed_boolean)
                self.logic_wrapper.edit_work_request(updated_work_request)
                print()
                print("Work Request Has Been Marked Completed!")
                print()
                break
            if is_marked_completed_boolean == False:
                while (updated_work_request_confirmation := input("Enter 1 to Confirm: ")) != "1":
                    print("Mama they took my dingus")
                updated_work_request = work_request.set_mark_as_done(is_marked_completed_boolean)
                self.logic_wrapper.edit_work_request(updated_work_request)
                print()
                print("Work Request Has Been Marked Not Completed.")
                print()
                break
            print("Mama they took my dingus")
            continue
        return
    
    # Displays options, not been tested enough to verify it's functionality.
    def general_edit_work_request_form(self, work_request: object):
        """Allows the Admin or Manager to edit specific details about a work request of their choosing. """

        print()
        print("Choose a Category To Edit")
        print("-" * 70)
        print("{:>15}".format("> 1. Employee ID"))
        print("{:>15}".format("> 2. Property ID"))
        print("{:>15}".format("> 3. Repitive"))
        print("{:>15}".format("> 4. Priority"))
        print("{:>15}".format("> 5. Completed"))
        print()
        print("{:>18}{:>5}".format("> Go Back:", "b, B"))
        print("{:>18}{:>5}".format("> Quit System:", "q, Q"))
        print()
        print("-" * 70)

        while (category_to_edit := input("Choose a Category to Edit: ")) != "b":
            match category_to_edit:
                case "1":
                    self.edit_employee_id_for_work_request(work_request)
                    return
                case "2":
                    self.edit_property_id_for_request(work_request)   
                    return
                case "3":
                    self.edit_repitive_work_request(work_request)
                    return
                case "4":
                    self.edit_priority_for_request(work_request)
                    return
                case "5":
                    self.mark_work_request_completed(work_request)
                    return
                case _:
                    print("Mama they took my dingus")
                    continue
        return 

    
    def edit_employee_id_for_work_request(self, work_request: object):
        while (edit_employee_id_for_request := input("New Employee ID: ")) != "b":
            is_employee_valid = self.logic_wrapper.sanity_check_employee_id_for_request(edit_employee_id_for_request)
            if is_employee_valid == True:
                print()
                while (updated_work_request_confirmation := input("Enter 1 to Confirm: ")) != "1":
                    print("Mama they took my dingus")
                work_request.set_staff_id(edit_employee_id_for_request)
                self.logic_wrapper.edit_work_request(work_request)
                break
            print("Mama they took my dingus")
            continue
        return
            

    def edit_property_id_for_request(self, work_request: object):
        while (edit_property_id_for_request := input("New Property ID: ")) != "b":
            is_property_id_valid = self.logic_wrapper.sanity_check_work_request_property_id(edit_property_id_for_request)
            if is_property_id_valid == True:
                print()
                while (updated_work_request_confirmation := input("Enter 1 to Confirm: ")) != "1":
                    print("Mama they took my dingus")
                work_request.set_property_id(edit_property_id_for_request)
                self.logic_wrapper.edit_work_request(work_request)
                break
            print("Mama they took my dingus")
            continue
        return


    def edit_repitive_work_request(self, work_request: object):
        while (edit_repitive_work_request := input("Is Repitive? (Yes or No): ")) != "b":
            is_repetitive_boolean = self.logic_wrapper.sanity_check_boolean_input_work_requests(edit_repitive_work_request)
            
            if is_repetitive_boolean == True:
                print()
                while (updated_work_request_confirmation := input("Enter 1 to Confirm: ")) != "1":
                    print("Mama they took my dingus")
                work_request.set_repetitive_work(is_repetitive_boolean)
                self.logic_wrapper.edit_work_request(work_request)
                break
            if is_repetitive_boolean == False: 
                print()
                while (updated_work_request_confirmation := input("Enter 1 to Confirm: ")) != "1":
                    print("Mama they took my dingus")
                work_request.set_repetitive_work(is_repetitive_boolean)
                self.logic_wrapper.edit_work_request(work_request)
                break
            print("Mama they took my dingus")
            continue
        return


    def edit_priority_for_request(self, work_request: object):    
        while (edit_priority_for_request := input("Priority for Request: ")) != "b":
            is_priority_valid = self.logic_wrapper.sanity_check_priority_for_request(edit_priority_for_request)
            
            if is_priority_valid == True:
                print()
                while (updated_work_request_confirmation := input("Enter 1 to Confirm: ")) != "1":
                    print("Mama they took my dingus")
                work_request.set_priority(edit_priority_for_request)
                self.logic_wrapper.edit_work_request(work_request)
                break
            print("Mama they took my dingus")
            continue
        return
        
    
    # The functions below could very well be combined into one bigger function.
    # Displays work requests, but no verification on if it matches rank.
    def display_my_work_requests_printed(self):
        """Prints out all work requests related to the user logged in. """
 
        print()
        print("{:^50}".format("[ My Work Requests ]"))
        print("-" * 70)
        is_accepted = True
        status = ""
        my_work_request_list = self.logic_wrapper.get_my_work_requests(self.rank, self.location, status, is_accepted)
        self.display_all_work_requests_printed(my_work_request_list)
        print()
        print("{:>15}{:>5}".format("> Go Back:", "b, B"))
        print("{:>18}{:>5}".format("> Quit System:", "q, Q"))
        print("-" * 70)
        while (selected_work_request := input("Enter 1 to Select a Work Request: ")) != "1":
            print("Mama they took my dingus")
        self.select_work_request_by_id(status, is_accepted)
    
        
    
    # Completed, can be beautifed.
    def display_all_new_work_requests_printed(self): 
        """Prints out all new work requests that haven't been accepted by an employee. """
        
        print()
        print("{:^50}".format("[ New Work Requests ]"))
        print("-" * 70)
        is_accepted = False
        status = "New"
        new_work_request_list = self.logic_wrapper.get_all_new_work_requests(self.rank, self.location, status, is_accepted)
        self.display_all_work_requests_printed(new_work_request_list)
        print()
        print("{:>15}{:>5}".format("> Go Back:", "b, B"))
        print("{:>18}{:>5}".format("> Quit System:", "q, Q"))
        print("-" * 70)
        while (selected_work_request := int(input("Enter 1 To Select A Work Request: "))) != "1":
            print("Mama they took my dingus")
        self.select_work_request_by_id(status, is_accepted)
    
    
    # Completed, can be beautifed.
    def display_all_pending_work_requests_printed(self): 
        """Prints out all pending work requests that haven't been marked closed by a manager or admin. """
        
        print()
        print("{:^50}".format("[ Pending Work Requests ]"))
        print("-" * 70)
        is_accepted = True
        status = "Pending"
        pending_work_request_list = self.logic_wrapper.get_all_pending_work_requests(self.rank, self.location, status, is_accepted)
        self.display_all_work_requests_printed(pending_work_request_list)
        print()
        print("{:>15}{:>5}".format("> Go Back:", "b, B"))
        print("{:>18}{:>5}".format("> Quit System:", "q, Q"))
        print("-" * 70)
        while (selected_work_request := input("Enter 1 To Select A Work Request: ")) != "1":
            print("Mama they took my dingus")
        self.select_work_request_by_id(status, is_accepted)

    # Completed, can be beautifed.
    def display_closed_work_requests_printed(self): 
        """Prints out all closed work requests. """

        print()
        print("{:^50}".format("[ Closed Work Requests ]"))
        print("-" * 70)
        is_accepted = True
        status = "Closed"
        closed_work_request_list = self.logic_wrapper.get_all_closed_work_requests(self.rank, self.location, status, is_accepted)
        self.display_all_work_requests_printed(closed_work_request_list)
        print()
        print("{:>15}{:>5}".format("> Go Back:", "b, B"))
        print("{:>18}{:>5}".format("> Quit System:", "q, Q"))
        print("-" * 70)
        while (selected_work_request := input("Enter 1 To Select A Work Request: ")) != "1":
            print("Mama they took my dingus")
        self.select_work_request_by_id(status, is_accepted)
    