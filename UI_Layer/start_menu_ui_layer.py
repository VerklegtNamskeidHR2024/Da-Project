from Logic_Layer.logic_layer_wrapper import Logic_Layer_Wrapper

from UI_Layer.employee_ui_layer import employee_UI_menu
from UI_Layer.location_ui_layer import location_UI_layer
from UI_Layer.contractor_ui_layer import contractor_UI_menu
from UI_Layer.maintenance_report_ui_layer import maintenance_report_UI_menu
from UI_Layer.work_request_ui_layer import work_request_UI_menu 
from UI_Layer.property_ui_layer import property_UI_menu

class Main_Menu:
    def __init__(self, rank, location):
        self.logic_wrapper = Logic_Layer_Wrapper()

        # calls the select function for what user you want to see the system as and, then - 
        # calls the location select function
        self.rank = self.select_user_for_system()
        self.location = self.select_location_for_system()

        self.employee_UI_menu = employee_UI_menu(self.logic_wrapper) # , self.rank, self.location
        self.location_UI_menu = location_UI_layer(self.logic_wrapper) # , self.rank, self.location
        # so its like this one when the class contrstructor is set up in the class correctly
        self.contractor_UI_menu = contractor_UI_menu(self.logic_wrapper, self.rank, self.location) 
        self.maintenance_report_UI_menu = maintenance_report_UI_menu(self.logic_wrapper) # , self.rank, self.location
        self.work_request_UI_menu = work_request_UI_menu(self.logic_wrapper, self.rank, self.location) # , self.rank, self.location
        self.property_UI_menu = property_UI_menu(self.logic_wrapper) # , self.rank, self.location

        # these may need to be sent into each UI class
        #self.rank = rank
        #self.location = location

    def start_point(self):
        #self.select_user_for_system()
        #self.select_location_for_system()
        self.display_menu_items()

    def select_user_for_system(self):
        # select a user for the system to use
        return_user = ""
        while return_user == "":
            print("select user to see system as")
            print("1) Admin")
            print("2) Manager")
            print("3) Employee")
            user_action = input("what user would you like: ")
            match user_action:
                case "1":
                    return_user = "Admin"
                case "2":
                    return_user = "Manager"
                case "3":
                    return_user = "Employee"
                case _:
                    print("No User Found, Please Try Again.")
        return return_user
    
    def select_location_for_system(self):
        # select location for system to use 
        return_location = ""
        while return_location == "":
            print("select a location to see system as")
            print("1) Reykjavik")
            print("2) Nuuk")
            print("3) Kulusuk")
            print("4) Torshavn")
            print("5) Tingwall")
            print("6) Longyearbyen") 
            user_action = input("what location would you like: ")
            match user_action:
                case "1":
                    return_location = "Reykjavik"
                case "2":
                    return_location = "Nuuk"
                case "3":
                    return_location = "Kulusuk"
                case "4":
                    return_location = "Torshavn"
                case "5":
                    return_location = "Tingwall"
                case "6":
                    return_location = "Longyearbyen"
                case _:
                    print("No Location Found, Please Try Again.")
        return return_location
                    

    def display_menu_items(self):
        # admin manager
        print(self.rank)
        print(self.location)
        print(f" {self.rank} - Home Page")
        print("-" * 70)
        print("1. Properties")
        print("2. Work Requests")
        print("3. Employees")
        print("4. Contractors")
        print("5. Maintenance Reports")
        if self.rank != "Employee":
            print("6. Locations")

        print("-" * 70)

        user_action = input("Select an Option:  ")
        self.user_chooice_select(user_action)

    def user_chooice_select(self, user_action):
        # calls the sub menus
        match user_action:
            case "1":
                self.property_UI_menu()
            case "2":
                self.work_request_UI_menu()
            case "3":
                self.employee_UI_menu()
            case "4":
                self.contractor_UI_menu.display_contractor_menu()
            case "5":
                self.maintenance_report_UI_menu()
            case "6" if self.rank != "Employee":
                # only allowed if admin or manager
                self.location_UI_menu()
            case "Q":
                # quit program
                pass
            case _:
                print("wrong input")
                self.display_menu_items()
