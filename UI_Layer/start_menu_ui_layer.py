from Logic_Layer.logic_layer_wrapper import LogicLayerWrapper

from UI_Layer.employee_ui_layer import employee_UI_menu
from UI_Layer.location_ui_layer import location_UI_layer
from UI_Layer.contractor_ui_layer import contractor_UI_menu
from UI_Layer.maintenance_report_ui_layer import maintenance_report_UI_menu
from UI_Layer.work_request_ui_layer import work_request_UI_menu 
from UI_Layer.property_ui_layer import property_UI_menu

class main_menu:
    def __init__(self, rank, location):
        self.logic_wrapper = LogicLayerWrapper()

        self.employee_UI_menu = employee_UI_menu(self.logic_wrapper)
        self.location_UI_menu = location_UI_layer(self.logic_wrapper)
        self.contractor_UI_menu = contractor_UI_menu(self.logic_wrapper)
        self.maintenance_report_UI_menu = maintenance_report_UI_menu(self.logic_wrapper)
        self.work_request_UI_menu = work_request_UI_menu(self.logic_wrapper)
        self.property_UI_menu = property_UI_menu(self.logic_wrapper)

        self.rank = rank
        self.location = location

    def display_menu_items(self):
        print(" Manager - Home Page")
        print("------------------------------------------------")
        print("1. Properties")
        print("2. Locations")
        print("3. Work Requests")
        print("4. Employees")
        print("5. Contractors")
        print("6. Maintenance Reports")
        print("------------------------------------------------")

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

def main():
    main = main_menu(1,"rvk") 
    main.display_menu_items()