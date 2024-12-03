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

        self.employee_UI_menu = employee_UI_menu(self.logic_wrapper)
        self.location_UI_menu = location_UI_layer(self.logic_wrapper)
        self.contractor_UI_menu = contractor_UI_menu(self.logic_wrapper)
        self.maintenance_report_UI_menu = maintenance_report_UI_menu(self.logic_wrapper)
        self.work_request_UI_menu = work_request_UI_menu(self.logic_wrapper)
        self.property_UI_menu = property_UI_menu(self.logic_wrapper)

        self.rank = rank
        self.location = location

    def start_point(self):
        self.select_user_for_system()
        self.select_location_for_system()
        self.display_menu_items()
    
    def show_login_choice_for_system(self):
        print()
        print("Welcome to the NaN Air Properties and Staff System!")
        print("-" * 70)
        self.show_ascii_art_hq()
        print("-" * 70)
        print("Log in as?")
        print("1. Admin")
        print("2. Manager")
        print("3. Employee")
        print()
        print("Universal Commands:")
        print("{:>24}{:>5}".format(">Go to Home Page:", "home, Home"))
        print("{:>20}{:>5}".format(">Quit System:", "q, Q"))
        print("-" * 70)

    def show_ascii_art_hq(self):
        print("{:>61}".format("==================="))
        print("{:>44}{:>13}{:>3}".format("|", "NaN Air HQ", "|"))
        print("{:>14}{:>7}{:>15}{:>8}{:>10}{:>6}".format("___________", ".", ": : : :", "|", "_____","|"))
        print("{:>13}{:>12}{:>11}{:>5}{:>3}{:>10}{:>6}{:>4}".format("_\_(*)_/_", "___(*)___", ": : : :", "o o", "|", "| | |", "|", "_ ,"))
        print("{:0}{:>1}{:>31}".format("_______|-|_________/-\__________", ":", "_____|_|__|_____| | |_____| o-o"))

    def show_location_choice_for_system(self):
        print()
        print("{:0}{:>3}{:>8}{:>7}{:>11}".format("1. Reykjavik", "|", "2. Nuuk", "|", "3. Kulusuk"))
        print()
        print("{:0}{:>4}{:>12}{:>3}{:>16}".format("4. Torshavn", "|", "5. Tingwall", "|", "6. Longyearbyen"))
        print()
    
    def log_in_choice(self):
        selected_user_login_choice = input("Select an Option: ")
        match selected_user_login_choice:
            case "1":
                self.rank = "Admin"
            case "2":
                self.rank = "Manager"
            case "3":
                self.rank = "Employee"
            case "q": 
                print("Departing from NaN Air, Thank you for Visiting!")
                pass
            case "Q":
                print("Departing from NaN Air, Thank you for Visiting!")
                pass
            case _:
                print("No User Found, Please Try Again.")
                self.show_login_choice_for_system()
        
    def location_choice(self):
        selected_location_choice = input("Select a Location: ")
        match selected_location_choice:
            case "1":
                self.location = "Reykjavik"
            case "2":
                self.location = "Nuuk"
            case "3":
                self.location = "Kulusuk"
            case "4":
                self.location = "Torshavn"
            case "5":
                self.location = "Tingwall"
            case "6":
                self.location = "Longyearbyen"
            case "q": 
                print("Departing from NaN Air, Thank you for Visiting!")
                pass
            case "Q":
                print("Departing from NaN Air, Thank you for Visiting!")
                pass
            case _:
                print("No Location Found, Please Try Again.")
                self.show_location_choice_for_system()

    def display_menu_items(self):
        print(" Manager - Home Page")
        print("-" * 70)
        print("1. Properties")
        print("2. Locations")
        print("3. Work Requests")
        print("4. Employees")
        print("5. Contractors")
        print("6. Maintenance Reports")
        print("-" * 70)

        user_action = input("Select an Option:  ")
        self.user_chooice_select(user_action)

    def user_chooice_select(self, user_action):
        # calls the sub menus
        match user_action:
            case "1":
                self.property_UI_menu()
            case "2":
                self.location_UI_menu()
            case "3":
                self.work_request_UI_menu()
            case "4":
                self.employee_UI_menu()
            case "5":
                self.contractor_UI_menu.display_contractor_menu()
            case "6":
                self.maintenance_report_UI_menu()
            case _:
                print("wrong input")

