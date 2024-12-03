from Model_Classes.contractor_model import Contractor
from Model_Classes.employee_model import Employee
from Model_Classes.property_model import Property
from Model_Classes.maintenance_report_model import MaintenanceReport
from Model_Classes.work_request_model import WorkRequest
from Model_Classes.location_model import Location
from Model_Classes.human_model import Human
# not sure if model classes are in here 

from Storage_Layer.storage_layer_wrapper import Storage_Layer_Wrapper

# importing all the logic classes
from Logic_Layer.contractor_logic_manager import contractor_logic_manager
from Logic_Layer.employee_logic_manager import employee_logic_manager
from Logic_Layer.location_logic_manager import location_logic_manager
from Logic_Layer.maintenance_report_logic_manager import maintenance_report_logic_manager
from Logic_Layer.property_logic_manager import property_logic_manager
from Logic_Layer.work_request_logic_manager import work_request_logic_manager


class Logic_Layer_Wrapper:
    def __init__(self):
        # creating the storage layer wrapper
        self.storage_layer_wrapper = Storage_Layer_Wrapper()

        # creating all the logic classes.
        # Send the storage layer wrapper into each manager so they can talk to the same instance-
        # of the storage layer wrapper.
        self.contractor_logic_manager = contractor_logic_manager(self.storage_layer_wrapper)
        self.employee_logic_manager = employee_logic_manager(self.storage_layer_wrapper)
        self.location_logic_manager = location_logic_manager(self.storage_layer_wrapper)
        self.maintenance_report_logic_manager = maintenance_report_logic_manager(self.storage_layer_wrapper)
        self.property_logic_manager = property_logic_manager(self.storage_layer_wrapper)
        self.work_request_logic_manager = work_request_logic_manager(self.storage_layer_wrapper)

    ########################################################################################################
    ### CONTRACTOR #########################################################################################
    def get_all_contractors(self):
        # her mynd það kalla í sama fall inn í contractors logic manager 
        # er núna bara með dummy gögn
        con1 = Contractor("1","alverk","tumi","8-19",["meow"])
        con2 = Contractor("2","alverk","gabbi","8-19",["meow"])
        con3 = Contractor("3","alverk","jon","8-19",["meow"])
        contractor_list = [con1,con2,con3]
        return contractor_list
    
    ########################################################################################################
    ### PROPERTIES #########################################################################################
    def get_all_properities(self):
        # dummy stuff
        prop1 = ("1", "hremmi diddy cave", "rvk", "96")
        prop2 = ("2", "Johun plage", "rvk", "swag")
        prop3 = ("3", "kormakur aka irl jon jones on a bad day cave", "rvk", "19")
        prop4 = ("4", "Langhals vegur", "rvk", "112")
        property_list = [prop1,prop2,prop3,prop4]
        return property_list

    ########################################################################################################
    ### EMPLOYEES ##########################################################################################
    def get_all_employees(self):
        pass

    ########################################################################################################
    ### MAINTENANCE_REPORTS ################################################################################
    def get_all_maintenance_reports(self):
        pass

    ########################################################################################################
    ### WORK_REQUESTS ######################################################################################
    def get_all_work_requests(self):
        pass

    ########################################################################################################
    ### LOCATION ###########################################################################################
    def get_all_locations(self):
        pass
    