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
    def get_all_contractors(self, location):
        return self.contractor_logic_manager.get_all_contractors(location)
        # her mynd það kalla í sama fall inn í contractors logic manager 
        # er núna bara með dummy gögn
        """ con1 = Contractor("1","alverk","tumi","8-19",["meow"])
        con2 = Contractor("2","alverk","gabbi","8-19",["meow"])
        con3 = Contractor("3","alverk","jon","8-19",["meow"])
        contractor_list = [con1,con2,con3]
        return contractor_list """

    print('we in da wrapper bro')
    con1 = Contractor("1","alverk","tumi","8-19",["meow"])
    con2 = Contractor("2","alverk","gabbi","8-19",["meow"])
    con3 = Contractor("3","alverk","jon","8-19",["meow"])
    contractor_list = [con1,con2,con3]

    def get_contractor_by_id(self, location, contractor_id) -> Contractor:
        return self.contractor_logic_manager.get_contractor_by_id(location,contractor_id)
    
    def write_to_file(self, list_of_contractors):
        '''con1 = Contractor("1","alverk","tumi","8-19",["meow"])
        con2 = Contractor("2","alverk","gabbi","8-19",["meow"])
        con3 = Contractor("3","alverk","jon","8-19",["meow"])
        contractor_list = [con1,con2,con3]'''
        return self.storage_layer_wrapper.write_to_file(list_of_contractors)
    
    def sanity_check_contractor(self, location, contractor):
        return self.contractor_logic_manager.sanity_check_contractor(location, contractor)
    
    ########################################################################################################
    ### PROPERTIES #########################################################################################
    def get_all_properities(self, location):
        # dummy stuff
        """ prop1 = Property("1", "hremmi diddy cave", "rvk", "96")
        prop2 = Property("2", "Johun plage", "rvk", "swag")
        prop3 = Property("3", "kormakur aka irl jon jones on a bad day cave", "rvk", "19")
        prop4 = Property("4", "Langhals vegur", "rvk", "112")
        property_list = [prop1,prop2,prop3,prop4] """
        return self.property_logic_manager.fetch_all_properties_in_storage(location)

    ########################################################################################################
    ### EMPLOYEES ##########################################################################################
    def get_all_employees(self, location):
        return self.employee_logic_manager.fetch_all_employee_in_storage(location)

    ########################################################################################################
    ### MAINTENANCE_REPORTS ################################################################################
    def get_all_maintenance_reports(self, location):
        return self.maintenance_report_logic_manager.fetch_all_maintencance_reports(location)

    ########################################################################################################
    ### WORK_REQUESTS ######################################################################################
    def get_all_work_requests(self, location): 
        return self.work_request_logic_manager.fetch_all_work_requests_in_storage(location)
    
    ########################################################################################################
    ### LOCATION ###########################################################################################
    def get_all_locations(self ,Location) -> list:
        return self.location_logic_manager.fetch_all_locations_in_storage(Location)

    def fetch_all_amenities_for_location_in_storage(self ,location) -> list:
        return self.location_logic_manager.fetch_all_amenities_for_location_in_storage()
    
    def fetch_location_from_storage(self ,Location_ID):
        return self.location_logic_manager.fetch_location_from_storage()

    def sanity_check_location(self ,Location):
        return self.location_logic_manager.sanity_check_location()

    def add_new_location_to_storage(self ,Location):
        return self.location_logic_manager.add_new_location_to_storage()

    