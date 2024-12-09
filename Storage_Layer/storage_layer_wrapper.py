# importing all the storage classes
from Storage_Layer.contractor_storage_manager import contractor_storage
from Storage_Layer.employee_storage_manager import employee_storage
from Storage_Layer.location_storage_manager import location_storage
from Storage_Layer.maintenance_report_storage_manager import maintenance_report_storage
from Storage_Layer.property_storage_manager import property_storage
from Storage_Layer.work_request_storage_manager import work_reques_storage
from Storage_Layer.admin_storage_manager import admin_storage
from Storage_Layer.amenity_storage_manager import amenity_storage
from Storage_Layer.manager_storage_manager import manager_storage

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
        self.maintenance_report_storage_manager = maintenance_report_storage()
        self.property_storage_manager = property_storage()
        self.work_request_storage_manager = work_reques_storage()
        self.admin_storage_manager = admin_storage()
        self.manager_storage_manager = manager_storage()
        self.amenity_storage_manager = amenity_storage()


    # maybe need to add edit to each?
    # No we dont do it in logic and send the list down to to re write it
    ########################################################################################################
    ### CONTRACTOR #########################################################################################
    
    def get_all_contractor(self):
        all_contractors = self.contractor_storage_manager.get_all_contractor()
        #all_contractors = contractor_storage.get_all_contractor()
        return all_contractors
        #return self.contractor_storage_manager.get_all_contractor()
    
    def write_to_file_contractor(self, list_of_contractors):
        write_to_file_contractor = self.contractor_storage_manager.write_to_file_contractor(list_of_contractors)
   
    ########################################################################################################
    ### PROPERTIES #########################################################################################
    
    def get_all_properties_at_location(self):
        return self.property_storage_manager.get_all_properties()
    
    def write_to_file_property(self, list_of_all_properties):
        write_to_file_property = self.property_storage_manager.write_to_file_property(list_of_all_properties)

    ########################################################################################################
    ### EMPLOYEES ##########################################################################################
    
    def get_all_employees(self):
        all_employees = self.employee_storage_manager.get_all_employees()
        return all_employees
    
    def write_to_file_employee(self, list_of_employees):
        write_to_file_employee = self.employee_storage_manager.write_to_file_employee(list_of_employees)
    
    ########################################################################################################
    ### MAINTENANCE_REPORTS ################################################################################
    
    def get_all_maintenance_reports(self):
        all_maintenance_reports = self.maintenance_report_storage_manager.get_all_maintenance_reports()
        return all_maintenance_reports
    
    def write_to_file_maintenance_reports(self, list_of_maintenance_reports):
        write_to_file_maintenance_reports = self.maintenance_report_storage_manager.write_to_file_maintenance_report(list_of_maintenance_reports)

    ########################################################################################################
    ### WORK_REQUESTS ######################################################################################
    
    def get_all_work_requests(self):
        all_work_requests = self.work_request_storage_manager.get_all_work_requests()
        return all_work_requests
    
    def write_to_file_work_requests(self, list_of_work_requests):
        write_to_file_work_requests = self.work_request_storage_manager.write_to_file_work_requests(list_of_work_requests)
    
    ########################################################################################################
    ### LOCATION ###########################################################################################
    
    def get_all_locations(self):
        all_locations = self.location_storage_manager.get_all_locations()
        return all_locations
    
    def write_to_file_locations(self, list_of_locations):
        write_to_file_locations = self.location_storage_manager.write_to_file_location(list_of_locations)
    
    ########################################################################################################
    ### ADMIN ##############################################################################################
    
    def get_all_admin(self):
        all_admins = self.admin_storage_manager.get_all_admin()
        return all_admins
    
    def write_to_file_admin(self, list_of_admins):
        write_to_file_admin = self.admin_storage_manager.write_to_file_admin(list_of_admins)
    
    ########################################################################################################
    ### MANAGER ############################################################################################
    
    def get_all_managers(self):
        all_managers = self.manager_storage_manager.get_all_managers()
        return all_managers
    
    def write_to_file_managers(self, list_of_managers):
        write_to_file_manager = self.manager_storage_manager.write_to_file_managers(list_of_managers)
    
    ########################################################################################################
    ### AMENITY ############################################################################################
    
    def get_all_amenities(self):
        all_amenities = self.amenity_storage_manager.get_all_amenities()
        return all_amenities
    
    def write_to_file_amenities(self, list_of_amenities):
        write_to_file_amenities = self.amenity_storage_manager.write_to_file_amenities(list_of_amenities)