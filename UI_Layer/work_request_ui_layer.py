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
        work_request_list = self.logic_wrapper.get_all_work_requests()
        for item in work_request_list:
            print("{:0}{:>3}{:>10}{:>4}{:>51}".format(
                work_request_list["work_request_id"], 
                "|", work_request_list["name"], 
                "|", work_request_list["description"]
                ))
        print("-" * 70)
        
    def display_selected_work_request_information(self):
        print("-" * 70)     
        work_request_list = self.logic_wrapper.get_all_work_requests()
        for item in work_request_list:
            print("{:0}{:>3}{:>10}".format("Work Request ID", "|", work_request_list["work_request_id"])) 
            print("{:0}{:>3}{:>10}".format("Name", "|", work_request_list["name"]))
            print("{:0}{:>3}{:>10}".format("Description", "|", work_request_list["description"]))
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
            print("-" * 70)
            user_choice = input("Select an Option: ")
            match user_choice:
                case "1": 
                    self.select_work_request_by_id()
                case "2":
                    self.create_work_request_form
                case "3": 
                    self.display_closed_work_requests_printed()
                case "q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case "Q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case _:
                    print("Invalid Input, Please Try Again.")
                    self.start_point()
        
        if self.rank == "Employee":
            print("-" * 70)
            print("{:0}{:>2}{:>15}{:>2}{:>19}".format("1. New Requests", "|", "2. Pending Requests", "|", "3. My Requests"))
            print("-" * 70)
            user_choice = input("Select an Option: ")    
            match user_choice:
                case "1": 
                    self.display_new_work_requests_to_accept()
                case "2":
                    self.display_pending_work_requests_printed()
                case "3": 
                    self.display_my_work_requests()
                case "q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case "Q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case _:
                    print("Invalid Input, Please Try Again.")
                    self.start_point()
                

    def select_work_request_by_id(self):
        work_request_selection = input("Enter Request ID: ")

    def create_work_request_form(self):


    def edit_work_request_form(self):

        
    def display_my_work_requests(self):
        self.display_all_work_requests()


    def display_new_work_requests_to_accept(self): 
        self.display_all_work_requests()

    
    def display_pending_work_requests_printed(self): 
        self.display_all_work_requests()


    def display_closed_work_requests_printed(self): 
        self.display_all_work_requests()
