from Logic_Layer.logic_layer_wrapper import LogicLayerWrapper

from UI_Layer.employee_ui_layer import employee_UI_menu
from UI_Layer.location_ui_layer import location_UI_layer
from UI_Layer.contractor_ui_layer import contractor_UI_menu
from UI_Layer.maintenance_report_ui_layer import maintenance_report_UI_menu
from UI_Layer.work_request_ui_layer import work_request_UI_menu 
from UI_Layer.property_ui_layer import property_UI_menu

class main_menu:
    def __init__(self):
        self.logic_wrapper = LogicLayerWrapper()
        self.employee_UI_menu = employee_UI_menu(self.logic_wrapper)
        self.location_UI_menu = location_UI_layer(self.logic_wrapper)
        self.contractor_UI_menu = contractor_UI_menu(self.logic_wrapper)
        self.maintenance_UI_report_menu = maintenance_report_UI_menu(self.logic_wrapper)
        self.work_request_UI_menu = work_request_UI_menu(self.logic_wrapper)
        self.property_UI_menu = property_UI_menu(self.logic_wrapper)
    def display_menu_items(self):
        print()




def main():
    main = main_menu() 