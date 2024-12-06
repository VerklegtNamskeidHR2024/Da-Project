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
    def get_all_contractors_at_location(self, location):
        return self.contractor_logic_manager.get_all_contractors_at_location(location)
        # her mynd það kalla í sama fall inn í contractors logic manager 
        # er núna bara með dummy gögn
        """ con1 = Contractor("1","alverk","tumi","8-19",["meow"])
        con2 = Contractor("2","alverk","gabbi","8-19",["meow"])
        con3 = Contractor("3","alverk","jon","8-19",["meow"])
        contractor_list = [con1,con2,con3]
        return contractor_list """

    print('we in da wrapper bro')
    '''con1 = Contractor("1","alverk","tumi","8-19",["meow"])
    con2 = Contractor("2","alverk","gabbi","8-19",["meow"])
    con3 = Contractor("3","alverk","jon","8-19",["meow"])
    contractor_list = [con1,con2,con3]'''

    def get_contractor_by_id(self, rank, location, contractor_id) -> Contractor:
        return self.contractor_logic_manager.get_contractor_by_id(location,contractor_id)
   
    def sanity_check_contractor(self, contractor):
        """check if all info in a contractor object"""
        return self.contractor_logic_manager.sanity_check_contractor(contractor)
    
    def add_new_contractor(self, contractor):
        return self.contractor_logic_manager.add_new_contractor(contractor)
    
    def write_to_file_checker(self, new_list):
        return self.contractor_logic_manager.write_to_file_checker(new_list)
    
    ########################################################################################################
    ### PROPERTIES #########################################################################################

    def get_all_properties_at_location(self, location):
        return self.property_logic_manager.get_all_properties_at_location(location)

    def add_new_property_to_storage(self, rank, location, new_property):
        return self.property_logic_manager.add_new_property_to_storage(rank, location, new_property)
    
    def get_property_by_id(self,property_id):
        return self.property_logic_manager.get_property_by_id(property_id)

    ########################################################################################################
    ### EMPLOYEES ##########################################################################################
    def get_all_employees_at_location(self, location):
        return self.employee_logic_manager.get_all_employees_at_location(location)
    
    def get_all_employees(self):
        return self.employee_logic_manager.get_all_employees() 
    
    def add_new_employee_to_storage(self, location, new_employee):
        return self.employee_logic_manager.add_new_employee_to_storage(location, new_employee)

    def edit_existing_employee_in_storage(self):
        return self.employee_logic_manager.edit_existing_employee_in_storage()
    
    def fetch_employee_from_storage(self, social_security_number):
        return self.employee_logic_manager.fetch_employee_from_storage(social_security_number)

    def fetch_all_work_request_for_employee(self):
        return self.employee_logic_manager.fetch_all_work_request_for_employee()

    def fetch_all_maintenance_reports_for_employee(self):
        return self.employee_logic_manager.fetch_all_maintenance_reports_for_employee()    

    ########################################################################################################
    ### MAINTENANCE_REPORTS ################################################################################
    def get_all_maintenance_reports_at_location(self, location):
        return self.maintenance_report_logic_manager.get_all_maintencance_reports_at_location(location)
    
    def get_all_pending_maintenance_reports(self, location) -> list[MaintenanceReport]:
        return self.maintenance_report_logic_manager.fetch_all_pending_maintencance_reports(location)
    
    def get_all_closed_maintenance_reports(self, location) -> list[MaintenanceReport]:
        return self.maintenance_report_logic_manager.fetch_all_closed_maintencance_reports(location)
    
    def add_new_maintenance_report_to_storage(self,location, new_report, is_regular):
        return self.maintenance_report_logic_manager.add_maintencance_report_to_storage(location, new_report, is_regular)
    
    def check_if_report_in_system(self, maintenance_report_id, location):
        return self.maintenance_report_logic_manager.check_if_report_in_system(maintenance_report_id, location)
    
    def deny_or_accept_maintencance_report_for_admin(self, maintencance_report_ID, location, accept_or_deny): 
        return self.maintenance_report_logic_manager.deny_or_accept_maintencance_report_for_admin(maintencance_report_ID, location, accept_or_deny)
    
    def edit_maintencance_report(self, maintenance_report, location, edit_choice, new_value):
        return self.maintenance_report_logic_manager.edit_maintencance_report(maintenance_report, location, edit_choice, new_value)
    
    def sanity_check_maintencance_report(self, what_to_check, new_value, location):
        location_list = self.get_all_locations()
        return self.maintenance_report_logic_manager.sanity_check_maintencance_report(what_to_check, new_value, location, )

    ########################################################################################################
    ### WORK_REQUESTS ######################################################################################
    def get_all_work_requests_at_location(self, rank, location) -> list: 
        return self.work_request_logic_manager.get_all_work_requests_at_location(rank, location)
        # dummy data
        """wr1 = WorkRequest("WR0001","Fix roof","roof had giant hole in it","MR001", "E1234", "Reykjavik", "H001", "01-01-24", "11-01-24", False, 0, "Low", "MR0002", "Pending", False, "", False)

        wr2 = WorkRequest("WR0002","Toilet cleaning","clean the damn toilets","MR002", "E1342", "Nuuk", "H002", "01-03-24", "15-03-24", True, 5, "High", "Open", False, "", False)

        wr3 = WorkRequest("WR0003","Decorate Doors","doors are ulg as shit","MR003", "E4312", "Torshavn", "H003", "21-12-24", "25-12-24", False, 1, "Medium", "Open", False, "", False)

        work_request_list1 = [wr1, wr2, wr3]
        return work_request_list1"""

    def get_work_request_by_id(self, rank: str, location: str, work_request_id: str) -> object:
        return self.work_request_logic_manager.fetch_work_request_by_id(rank, location, work_request_id)
        # dummy data 
        """wr1 = WorkRequest("WR0001", "Fix roof", "roof had giant hole in it", "MR001", "E1234", "Reykjavik", "H001", "01-01-24", "11-01-24", False, 0, "Low", "MR0002", "Pending", False, "", False)

        wr2 = WorkRequest("WR0002","Toilet cleaning","clean the damn toilets","MR002", "E1342", "Nuuk", "H002", "01-03-24", "15-03-24", True, 5, "High", "Open", False, "", False)

        wr3 = WorkRequest("WR0003","Decorate Doors","doors are ulg as shit","MR003", "E4312", "Torshavn", "H003", "21-12-24", "25-12-24", False, 1, "Medium", "Open", False, "", False)

        work_request_list2 = [wr1, wr2, wr3]
        for object in work_request_list2:
            if object.work_request_id == Work_request_id:
                return object
            else: 
                return """
    
    def get_all_new_work_requests(self, rank, location) -> list:
        return self.work_request_logic_manager.fetch_all_new_work_requests_in_storage(rank, location)
    
    def get_all_open_work_requests(self, rank, location) -> list:
        return self.work_request_logic_manager.fetch_all_open_work_requests_in_storage(rank, location)
    
    def get_all_closed_work_requests(self, rank, location) -> list: 
        return self.work_request_logic_manager.fetch_all_closed_work_requests_in_storage(rank, location)
    
    def get_all_pending_work_requests(self, rank, location) -> list:
        return self.work_request_logic_manager.fetch_all_pending_work_requests_in_storage(rank, location)
    
    def get_my_work_requests(self, rank, location) -> list:
        return self.work_request_logic_manager.fetch_my_work_request(rank, location)
    
    def edit_work_request(self, rank, location, WorkRequest) -> bool:
        return self.work_request_logic_manager.edit_work_request(rank, location, WorkRequest)
    
    def add_work_request(self, WorkRequest: object) -> bool:
        return self.work_request_logic_manager.add_work_request(WorkRequest)

    def sanity_check_work_request_id(self, rank, location, WorkRequest) -> bool: 
        return self.work_request_logic_manager.sanity_check_work_request_id(rank, location, WorkRequest)
    
    def sanity_check_new_work_request_property_id(self, property_id: str) -> bool:
        return self.work_request_logic_manager.sanity_check_new_work_request_property_id(property_id)
    
    def sanity_check_boolean_input_work_requests(self, yes_or_no: str) -> bool:
        return self.work_request_logic_manager.sanity_check_boolean_input_work_requests(yes_or_no)
    
    def sanity_check_location_for_request(self, location: str) -> bool:
        return self.work_request_logic_manager.sanity_check_location_for_request(location)
    
    def sanity_check_priority_for_request(self, priority: str) -> bool:
        return self.work_request_logic_manager.sanity_check_priority_for_request(priority)

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

