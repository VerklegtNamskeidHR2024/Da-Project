class work_request_UI_menu:
    def __init__(self, Logic_Wrapper, rank, location):
        self.logic_wrapper = Logic_Wrapper
        self.rank = rank
        self.location = location
    
    def start_point(self):
        self.display_work_requests_menu_items()
        # self.display_selected_work_request_information()
        # self.select_work_request_by_id()
        # self.create_work_request_form()
        # self.edit_work_request_form()
        # self.display_my_work_requests()
        # self.display_new_work_requests_to_accept() 
        # self.display_pending_work_requests_printed() 
        # self.display_closed_work_requests_printed() 

    def display_all_work_requests(self):
        """Prints out all open work requests with their ID, Name and Description. """
        print("{:0}{:>3}{:>5}{:>9}{:>12}".format("ID", "|", "Name", "|", "Description"))
        print("-" * 70)
        work_request_list = self.logic_wrapper.get_all_work_requests(self.rank, self.location)
        for item in work_request_list:
            print("{:0}{:>3}{:>10}{:>4}{:>51}".format({item.work_request_id}, "|", {item.name}, "|", {item.description}))
        print("-" * 70)
        
    def display_selected_work_request_information(self, work_request_id):
        print("{:0}{:>14}{:<10}".format("Categories", "|", "Details"))
        print("-" * 35)     
        work_request_list = self.logic_wrapper.get_work_request_by_id(self.rank, self.location, work_request_id)
        for item in work_request_list:
            print("{:0}{:>9}{:<10}".format("Work Request ID", "|", {item.work_request_id})) 
            print("{:0}{:>20}{:<10}".format("Name", "|", {item.name}))
            print("{:0}{:>13}{:<10}".format("Description", "|", {item.description}))
            print("{:0}{:>16}{:<10}".format("Location", "|", {item.location})) 
            print("-" * 35)
            print("{:0}{:>3}{:>10}".format("Maintenance Report ID", "|", {item.maintenance_report_id}))
            print("{:0}{:>16}{:<10}".format("Staff ID", "|", {item.staff_id}))
            print("{:0}{:>13}{:<10}".format("Property ID", "|", {item.property})) 
            print("{:0}{:>11}{:<10}".format("Contractor ID", "|", {item.contractor_id}))
            print("-" * 35)
            print("{:0}{:>14}{:>10}".format("Start Date", "|", {item.start_date}))
            print("{:0}{:>7}{:>10}".format("Completition Date", "|", {item.completition_date})) 
            print("{:0}{:>9}{:>10}".format("Repititive Work", "|", {item.repetitive_work}))
            print("{:0}{:>3}{:>10}".format("Re-Open Interval Days", "|", {item.re_open_Interval_Days})) 
            print("-" * 35)
            print("{:0}{:>16}{:>10}".format("Priority", "|", {item.priority}))
            print("{:0}{:>7}{:>10}".format("Mark as Completed", "|", {item.mark_as_completed}))
            print("{:0}{:>11}{:>10}".format("Mark as Ready", "|", {item.mark_as_ready}))
            print("{:0}{:>4}{:>10}".format("Accepted by Employee", "|", {item.accepted_by_employee}))
        print("-" * 70)

    def display_work_requests_menu_items(self):
        """Displays the menu options depending if the user logged in is an admin/manager or
        an employee. It then calls the correct function based on what the user chose. """
        print()
        print("Work Request Menu")
        print("-" * 70)
        print("{:>50}".format("[ Open and Upcoming Work Requests ]"))
        print()
        self.display_all_work_requests()
        if self.rank == "Admin" or self.rank == "Manager":
            print("{:0}{:>3}{:>8}{:>7}{:>11}".format("1. Select Request", "|", "2. Add Request", "|", "3. Closed Requests"))
            print()
            user_choice = input("Select an Option: ")
            print("-" * 70)
            match user_choice:
                case "1": 
                    self.select_work_request_by_id()
                case "2":
                    pass
                    # self.create_work_request_form
                case "3":
                    pass
                    # self.display_closed_work_requests_printed()
                case "q":
                    pass
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case "Q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case _:
                    print("Invalid Input, Please Try Again.")
                    self.start_point()
        
        if self.rank == "Employee":
            print("{:0}{:>2}{:>15}{:>2}{:>19}".format("1. New Requests", "|", "2. Pending Requests", "|", "3. My Requests"))
            print()
            user_choice = input("Select an Option: ")
            print("-" * 70)    
            match user_choice:
                case "1": 
                    pass
                    # self.display_new_work_requests_to_accept()
                case "2":
                    pass
                    # self.display_pending_work_requests_printed()
                case "3": 
                    pass
                    # self.display_my_work_requests()
                case "q":
                    pass
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case "Q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case _:
                    print("Invalid Input, Please Try Again.")
                    self.start_point()
                

    def select_work_request_by_id(self):
        try:
            work_request_selected_by_id = input("Enter Request ID: ")
            self.display_selected_work_request_information(self.rank, self.location, work_request_selected_by_id)
            print(f"Work Request {work_request_selected_by_id} Found!")
        except:
            print("Work Request not Found, Please Try Again.")
            self.select_work_request_by_id()

    # def create_work_request_form(self):


    # def edit_work_request_form(self):

        
    # def display_my_work_requests(self):
    #     self.display_all_work_requests()


    # def display_new_work_requests_to_accept(self): 
    #     self.display_all_work_requests()

    
    # def display_pending_work_requests_printed(self): 
    #     self.display_all_work_requests()


    # def display_closed_work_requests_printed(self): 
    #     self.display_all_work_requests()
