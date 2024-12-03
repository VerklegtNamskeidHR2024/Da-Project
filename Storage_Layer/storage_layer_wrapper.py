# importing all the storage classes
from Storage_Layer.contractor_storage_manager import contractor_storage
from Storage_Layer.employee_storage_manager import employee_storage
from Storage_Layer.location_storage_manager import location_storage
from Storage_Layer.maintenance_report_storage_manager import maintenance_report_storage
from Storage_Layer.property_storage_manager import property_storage
from Storage_Layer.work_request_storage_manager import work_reques_storage

from Model_Classes.contractor_model import Contractor
from Model_Classes.employee_model import Employee
from Model_Classes.property_model import Property
from Model_Classes.maintenance_report_model import MaintenanceReport
from Model_Classes.work_request_model import WorkRequest
from Model_Classes.location_model import Location

class Storage_Layer_Wrapper:
    def __init__(self):
        self.contractor_storage_manager = contractor_storage()
        self.employee_storage_manager = employee_storage()
        self.location_storage_manager = location_storage()
        self.maintenance_report_lstorage_manager = maintenance_report_storage()
        self.property_storage_manager = property_storage()
        self.work_request_storage_manager = work_reques_storage()


    # maybe need to add edit to each?
    ########################################################################################################
    ### CONTRACTOR #########################################################################################
    def add_contractor(self):
        pass

    def get_all_contractor(self):
        all_contractors = contractor_storage.get_all_contractor()
        return all_contractors
        #return self.contractor_storage_manager.get_all_contractor()
    
    def get_contractor(self):
        pass

    def contractor_set_ID_and_add_to_storage(self):
        pass
   
    ########################################################################################################
    ### PROPERTIES #########################################################################################
    def add_property(self):
        pass
    def get_property(self):
        pass
    def get_all_properties(self):
        pass
    def property_set_ID_and_add_to_storage(self):
        pass

    ########################################################################################################
    ### EMPLOYEES ##########################################################################################
    def add_employee(self):
        pass
    def get_employee(self):
        pass
    def get_all_employee(self):
        pass
    def employee_set_ID_and_add_to_storage(self):
        pass
    
    ########################################################################################################
    ### MAINTENANCE_REPORTS ################################################################################
    def maintenance_report_set_ID_and_too_storage(self):
        pass
    def add_maintenance_report(self):
        pass
    def get_maintenance_report(self):
        pass
    def get_all_maintenance_report(self):
        pass

    ########################################################################################################
    ### WORK_REQUESTS ######################################################################################
    def add_work_request(self):
        pass
    def get_work_request(self):
        pass
    def get_all_work_requests(self):
        pass
    def work_request_set_ID_and_add_to_storage():
        pass
    
    ########################################################################################################
    ### LOCATION ###########################################################################################
    def add_location(self):
        pass
    def get_location(self):
        pass
    def get_all_locations(self):
        pass
    def location_set_ID_and_add_to_storage(self):
        pass
    

    # not sure what this is for
    def add_admin(self):
        pass
    def get_admin(self):
        pass
    def get_all_admin(self):
        pass
    def set_id_and_add_to_storage(self):
        pass

    def add_manager(self):
        pass
    def get_manager(self):
        pass
    def get_all_managers(self):
        pass
    def manager_set_ID_and_to_storage(self):
        pass
    
    def get_amenity(self):
        pass
    def get_all_amenities(self):
        pass