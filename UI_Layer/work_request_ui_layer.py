from Logic_Layer.logic_layer_wrapper import Logic_Layer_Wrapper

class work_request_UI_menu:
    def __init__(self, rank, location):
        self.logic_wrapper = Logic_Layer_Wrapper()
        self.rank = rank
        self.location = location
    
    def start_point(self):
        self.display_all_open_work_requests()
        self.display_work_request_menu_options()
        self.display_selected_work_request_information()
        self.select_work_request_by_id()
        self.create_work_request_form()
        self.edit_work_request_form()

    def display_all_open_work_requests(self):
        """Prints out all open work requests with their ID, Name and Description """
        
        print()
        print("Work Request Menu")
        print("-" * 70)
        print("{:>50}".format("[ Open and Upcoming Work Requests ]"))
        print()
        print("{:0}{:>3}{:>5}{:>9}{:>12}".format("ID", "|", "Name", "|", "Description"))
        print("-" * 70)
        work_request_list = self.logic_wrapper.get_all_work_requests()
        for item in work_request_list:
            print("{:0}{:>3}{:>10}{:>4}{:>51}".format(
                work_request_list["work_request_id"], 
                "|", work_request_list["name"], 
                "|", work_request_list["description"]
                ))

    def display_work_request_menu_options(self):
        """Displays the menu options depending if the user logged in is an admin/manager or an employee.
        It then returns what the user chose. """

        if self.rank == "Admin" or self.rank == "Manager":
            print("-" * 70)
            print("{:0}{:>3}{:>8}{:>7}{:>11}".format("1. Select Request", "|", "2. Add Request", "|", "3. Closed Requests"))
            print("-" * 70)
            user_choice = input("Select an Option: ")
            match user_choice:
                case "1": 
                    return "Select Request"
                case "2":
                    return "Add Request"
                case "3": 
                    return "Closed Requests"
                case "q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case "Q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case _:
                    print("Invalid Input, Please Try Again.")
                    self.display_work_request_menu_options()
        
        if self.rank == "Employee":
            print("-" * 70)
            print("{:0}{:>2}{:>15}{:>2}{:>19}".format("1. Select Request", "|", "2. Add Request", "|", "3. Closed Requests"))
            print("-" * 70)
            user_choice = input("Select an Option: ")    
            match user_choice:
                case "1": 
                    self.select_work_request_by_id()
                case "2":
                    self.create_work_request_form()
                case "3": 
                    return "Closed Requests"
                case "q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case "Q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    pass
                case _:
                    print("Invalid Input, Please Try Again.")
                    self.display_work_request_menu_options()
                

    def select_work_request_by_id(self):
        work_request_selection = input("Enter Request ID: ")
 

    def display_selected_work_request_information(self): 


    def create_work_request_form(self):


    def edit_work_request_form(self):

        
    
    def display_my_work_requests(self):
     

    def display_new_work_requests_to_accept(): 
    
    def display_pending_work_requests_printed(): 

    def display_closed_work_requests_printed(): 