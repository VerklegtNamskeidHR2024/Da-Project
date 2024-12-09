from Logic_Layer.logic_layer_wrapper import Logic_Layer_Wrapper

from UI_Layer.employee_ui_layer import employee_UI_menu
from UI_Layer.location_ui_layer import location_UI_menu
from UI_Layer.contractor_ui_layer import contractor_UI_menu
from UI_Layer.maintenance_report_ui_layer import maintenance_report_UI_menu
from UI_Layer.work_request_ui_layer import work_request_UI_menu
from UI_Layer.property_ui_layer import property_UI_menu

from prettytable import PrettyTable 
from colorama import Fore, Style, init

class Main_Menu:
    def __init__(self, rank, location):
        self.logic_wrapper = Logic_Layer_Wrapper(rank, location)
        # calls the select function for what user you want to see the system as and, then - 
        # calls the location select function
        rank = self.select_user_for_system()
        location = self.select_location_for_system()
        self.rank = rank
        self.location = location
        
        # sendir ekki inn self.blahblah útaf það er gert í þessum klasa, vilt bara senda inn location og rank
        # annars er sent inn vitlaust location - Kv Hreimur
        self.employee_UI_menu = employee_UI_menu(self.logic_wrapper, rank, location) # , self.rank, self.location
        self.location_UI_menu = location_UI_menu(self.logic_wrapper, rank, location) # , self.rank, self.location
        self.contractor_UI_menu = contractor_UI_menu(self.logic_wrapper, rank, location) 
        self.maintenance_report_UI_menu = maintenance_report_UI_menu(self.logic_wrapper, rank, location) # , self.rank, self.location
        self.work_request_UI_menu = work_request_UI_menu(self.logic_wrapper, rank, location) # , self.rank, self.location
        self.property_UI_menu = property_UI_menu(self.logic_wrapper, rank, location) # , self.rank, self.location

        # these may need to be sent into each UI class
        #self.rank = rank
        #self.location = location

    # Needs to be implemented in all of the ui menus so we can acctually select the locations
    
    # def set_new_rank(self, new_rank):
    #     self.rank = new_rank

    # def set_new_location(self, new_location):
    #     self.location = new_location

    # def get_location(self):
    #     return self.location

    # def get_rank(self):
    #     return self.rank

    def start_point(self):
        #self.select_user_for_system()
        #self.select_location_for_system()
        self.display_menu_items()

    def show_ascii_art_hq(self):
        print("{:>61}".format("==================="))
        print("{:>44}{:>13}{:>3}".format("|", "NaN Air HQ", "|"))
        print("{:>14}{:>7}{:>15}{:>8}{:>10}{:>6}".format("___________", ".", ": : : :", "|", "_____","|"))
        print("{:>13}{:>12}{:>11}{:>5}{:>3}{:>10}{:>6}{:>4}".format("_\_(*)_/_", "___(*)___", ": : : :", "o o", "|", "| | |", "|", "_ ,"))
        print("{:0}{:>1}{:>31}".format("_______|-|_________/-\__________", ":", "_____|_|__|_____| | |_____| o-o"))

    def create_location_table(self):
        """print for location selection"""
        locations_table = PrettyTable()
        locations_table.field_names = ['ID',"Country", "Location Name"]
        locations_table.add_row(['1',"Iceland", "Reykjavik"])
        locations_table.add_row(['2',"Greenland", "Nuuk"])
        locations_table.add_row(['3',"Greenland", "Kulusuk"])
        locations_table.add_row(['4',"Faroe Islands", "Torshavn"])
        locations_table.add_row(['5',"Shetland Islands", "Tingwall"])
        locations_table.add_row(['6',"Svalbard", "Longyearbyen"])
            
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        locations_table.border = True
        locations_table.junction_char = f"{border_color}+{reset_color}"
        locations_table.horizontal_char = f"{border_color}-{reset_color}"
        locations_table.vertical_char = f"{border_color}|{reset_color}"

        print(locations_table)
        

    def select_user_for_system(self):
        # select a user for the system to use
        return_user = ""
        while return_user == "":
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
            print("Universal System Commands:")
            print("{:>15}{:>5}".format("> Go Back:", "b, B"))
            print("{:>18}{:>5}".format("> Quit System:", "q, Q"))
            print("-" * 70)

            user_action = input("Select a Profile: ")
            match user_action:
                case "1":
                    return_user = "Admin"
                case "2":
                    return_user = "Manager"
                case "3":
                    return_user = "Employee"
                case "q" | "Q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    return
                case _:
                    print("No User Found, Please Try Again.")
        return return_user
    
    def select_location_for_system(self):
        # select location for system to use 
        return_location = ""
        while return_location == "":
            """ print()
            print("{:0}{:>3}{:>8}{:>7}{:>11}".format("1. Reykjavik", "|", "2. Nuuk", "|", "3. Kulusuk"))
            print()
            print("{:0}{:>4}{:>12}{:>3}{:>16}".format("4. Torshavn", "|", "5. Tingwall", "|", "6. Longyearbyen"))
            print() """

            self.create_location_table()

            user_action = input("Select a Location: ")
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
                case "b" | "B":
                    return 
                case "q" | "Q":
                    print("Departing from NaN Air, Thank you for Visiting!")
                    return
                case _:
                    print("No Location Found, Please Try Again.")
        return return_location
                    

    def display_menu_items(self):
        user_action = ""
        while user_action.lower() != "q":
            print()
            print(f" {self.rank} - Home Page")
            print("-" * 70)
            print("1) Properties")
            print("2) Work Requests")
            print("3) Employees")
            print("4) Contractors")
            print("5) Maintenance Reports")
            if self.rank != "Employee":
                print("6) Locations")
            print()
            print("{:<15}".format("> Log Out: log"))
            print("{:<18}".format("> Quit System: q, Q"))
            print("-" * 70)

            user_action = input("Select an Option: ")
            self.user_choice_select(user_action.lower())
        return 

    def user_choice_select(self, user_action):

        # calls the sub menus
        match user_action:
            case "1":
                self.property_UI_menu.start_point_property_UI()
            case "2":
                self.work_request_UI_menu.start_point_work_requests_UI()
            case "3":
                self.employee_UI_menu.start_point_employee_UI()
            case "4":
                self.contractor_UI_menu.start_point_contractor_UI()
            case "5":
                self.maintenance_report_UI_menu.start_point_maintenance_reports_UI()
            case "6" if self.rank != "Employee":
                # only allowed if admin or manager
                self.location_UI_menu.start_point_location_UI()
            case "7":
                self.test_some_stuff()
            case "b" | "B":
                return 
            case "q" | "Q":
                print("Departing from NaN Air, Thank you for Visiting!")
                return
            case _:
                print("Wrong Input")
        return
    
    def test_some_stuff(self):
        """just some tesing with getting data from storage""" 
        
        contractor_list = self.logic_wrapper.get_all_contractors(self.location)
        for item in contractor_list:
            print(f"{item.contractor_id:<10}|{item.location:<20}")
        print("-" * 40)

        employees_list = self.logic_wrapper.get_all_employees(self.location)
        for item in employees_list:
            print(f"{item.staff_id:<10}|{item.location:<20}")
        print("-" * 40)

        # this needs to be looked at
        # works but look at property_storage_manager for more info
        properties_list = self.logic_wrapper.get_all_properities(self.location)
        for item in properties_list:
            print(f"{item.property_id:<10}|{item.location:<20}")
        print("-" * 40)

        report_list = self.logic_wrapper.get_all_maintenance_reports(self.location)
        for item in report_list:
            print(f"{item.report_id:<10}|{item.location:<20}")
        print("-" * 40)

        # this needs to be looked at
        '''work_list = self.logic_wrapper.get_all_work_requests(self.location)
        for item in work_list:
            print(f"{item.work_request_id:<10}|{item.location:<20}")
        print("-" * 40)'''

        location_list = self.logic_wrapper.get_all_locations(self.location)
        for item in location_list:
            print(f"{item.location:<20}")
        print("-" * 40)
