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
    def __init__(self, rank, location, staff_id):
        # creating the storage layer wrapper
        self.storage_layer_wrapper = Storage_Layer_Wrapper()
        self.rank = rank
        self.staff_id = staff_id
        self.location = location

        # creating all the logic classes.
        # Send the storage layer wrapper into each manager so they can talk to the same instance-
        # of the storage layer wrapper.
        self.contractor_logic_manager = contractor_logic_manager(self.storage_layer_wrapper)
        self.employee_logic_manager = employee_logic_manager(self.storage_layer_wrapper)
        self.location_logic_manager = location_logic_manager(self.storage_layer_wrapper)
        self.property_logic_manager = property_logic_manager(self.storage_layer_wrapper)
        self.work_request_logic_manager = work_request_logic_manager(self.storage_layer_wrapper)
        self.maintenance_report_logic_manager = maintenance_report_logic_manager(self.storage_layer_wrapper)

    ##############################################################################################################################################
    ### CONTRACTOR ###############################################################################################################################

    def get_all_contractors_at_location(self, location: str) -> list[Contractor]:
        return self.contractor_logic_manager.get_all_contractors_at_location(location)
        # returns a list of all contractors at a specific location

    def get_contractor_by_id(self, location: str, contractor_id: str) -> Contractor:
        return self.contractor_logic_manager.get_contractor_by_id(location, contractor_id)
        # returns a contractor object by contractor_id

    def sanity_check_contractor(self,what_to_check, new_value) -> bool:
        """check if all info in a contractor object"""
        return self.contractor_logic_manager.sanity_check_contractor(what_to_check, new_value)
        # checks if all info in a contractor object is correct
    
    def add_new_contractor(self, rank: str, location: str, contractor: object):
        return self.contractor_logic_manager.add_new_contractor_to_storage(rank, location, contractor)
        # adds a new contractor to the storage
    
    def get_contractor_maintenance_reports(self, location: str, contractor_id: str) -> list[MaintenanceReport]:
        return self.contractor_logic_manager.get_contractor_maintenance_reports(location, contractor_id)
        # returns a list of all maintenance reports for a specific contractor
    
    def get_contractor_work_requests(self, location: str, property_id: str) -> list[WorkRequest]:
        return self.contractor_logic_manager.get_contractor_work_requests(location, property_id)
        # returns a list of all work requests for a specific contractor
    
    def write_to_file_checker(self, new_list: list) -> list[Contractor]:
        return self.contractor_logic_manager.write_to_file_checker(new_list)
        # writes a list to a file
    
    def edit_existing_contractor_in_storage(self, contractor: object, location: str, edit_choice: str, new_value: str):
        return self.contractor_logic_manager.edit_existing_contractor_in_storage(contractor, location, edit_choice, new_value)
        # edits an existing contractor in the storage
    
    ##############################################################################################################################################
    ### PROPERTIES ###############################################################################################################################

    def get_all_properties_at_location(self, location: str) -> list[Property]:
        return self.property_logic_manager.get_all_properties_at_location(location)
        # returns a list of all properties at a specific location
    
    def get_property_by_id(self, location: str, property_id: str) -> Property:
        return self.property_logic_manager.get_property_by_id(location, property_id)
        # returns a property object by property_id
    
    def get_property_work_requests(self, location: str, property_id: str) -> list[WorkRequest]:
        return self.property_logic_manager.get_property_work_requests(location, property_id)
        # returns a list of all work requests for a specific property
    
    def get_property_maintenance_reports(self, location: str, property_id: str) -> list[MaintenanceReport]:
        return self.property_logic_manager.get_property_maintenance_reports(location, property_id)
        # returns a list of all maintenance reports for a specific property
    
    def sanity_check_properties(self, what_to_check: str, new_value: str) -> bool:
        return self.property_logic_manager.sanity_check_properties(what_to_check, new_value)
        # checks if all info in a property object is correct

    def add_new_property_to_storage(self, str_display: str, new_property: object):
        return self.property_logic_manager.add_new_property_to_storage(str_display, new_property)
        # adds a new property to the storage
    
    def edit_existing_property_in_storage(self, existing_property: object, location: str, edit_choice: str, new_value: str):
        return self.property_logic_manager.edit_existing_property_in_storage(existing_property, location, edit_choice, new_value)
        # edits an existing property in the storage

    ##############################################################################################################################################
    ### EMPLOYEES ################################################################################################################################
    
    def get_employee_by_id(self, staff_id: str) -> str:
        return self.employee_logic_manager.get_employee_by_id(staff_id) 
        # returns a list of all employees at a specific location
    
    def get_manager_by_id(self, staff_id: str) -> str:
        return self.employee_logic_manager.get_manager_by_id(staff_id)

    def get_all_employees_at_location(self, location: str) -> list[Employee]:
        return self.employee_logic_manager.get_all_employees_at_location(location)
        # returns a list of all employees
    
    def add_new_employee_to_storage(self, new_employee: object):
        return self.employee_logic_manager.add_new_employee_to_storage(new_employee)
        # adds a new employee to the storage

    def edit_employee_info(self, employee: object):
        return self.employee_logic_manager.edit_employee_info(employee)
        # edits an existing employee in the storage
    
    def fetch_employee_from_storage(self, social_security_number: str) -> Employee:
        return self.employee_logic_manager.fetch_employee_from_storage(social_security_number)
        # returns an employee object by social_security_number

    def fetch_all_work_request_for_employee(self, staff_id) -> list[WorkRequest]:
        return self.employee_logic_manager.fetch_all_work_request_for_employee(staff_id)
        # returns a list of all work requests for a specific employee

    def fetch_all_maintenance_reports_for_employee(self, staff_id) -> list[MaintenanceReport]:
        return self.employee_logic_manager.fetch_all_maintenance_reports_for_employee(staff_id)
        # returns a list of all maintenance reports for a specific employee

    def sanity_check_staff_id(self, rank: str, staff_id: str) -> bool:
        return self.employee_logic_manager.sanity_check_staff_id(rank, staff_id)

    def sanity_check_employee_name(self, name: str) -> bool:
        return self.employee_logic_manager.sanity_check_employee_name(name)
        # checks if the name of an employee is correct
    
    def sanity_check_ssn(self, ssn: str) -> bool:
        return self.employee_logic_manager.sanity_check_ssn(ssn)
        # checks if the social security number of an employee is correct

    def sanity_check_ssn_add(self, ssn: str) -> bool:
        return self.employee_logic_manager.sanity_check_ssn_add(ssn)
    
    def sanity_check_phone_number(self, phone_number: str) -> bool:
        return self.employee_logic_manager.sanity_check_phone_number(phone_number)
        # checks if the phone number of an employee is correct
    
    def sanity_check_email(self, email: str) -> bool:
        return self.employee_logic_manager.sanity_check_email(email)
        # checks if the email of an employee is correct
    
    def sanity_check_for_employee_location(self, location: str) -> bool:
        return self.employee_logic_manager.sanity_check_for_employee_location(location)
        # checks if the location of an employee is correct

    ##############################################################################################################################################
    ### MAINTENANCE_REPORTS ######################################################################################################################

    def get_all_maintenance_reports_at_location(self, location: str) -> list[MaintenanceReport]:
        return self.maintenance_report_logic_manager.get_all_maintencance_reports_at_location(location)
        # returns a list of all maintenance reports at a specific location
    
    def get_all_pending_maintenance_reports(self, location: str) -> list[MaintenanceReport]:
        return self.maintenance_report_logic_manager.fetch_all_pending_maintencance_reports(location)
        # returns a list of all pending maintenance reports
    
    def get_all_closed_maintenance_reports(self, location: str) -> list[MaintenanceReport]:
        return self.maintenance_report_logic_manager.fetch_all_closed_maintencance_reports(location)
        # returns a list of all closed maintenance reports
    
    def add_new_maintenance_report_to_storage(self,location, new_report: object, is_regular: bool):
        return self.maintenance_report_logic_manager.add_maintencance_report_to_storage(location, new_report, is_regular)
        # adds a new maintenance report to the storage
    
    def check_if_report_in_system(self, maintenance_report_id: str, location: str) -> bool:
        return self.maintenance_report_logic_manager.check_if_report_in_system(maintenance_report_id, location)
        # checks if a maintenance report is in the system
    
    def deny_or_accept_maintencance_report_for_admin(self, maintencance_report_id: str, location: str, accept_or_deny: bool) -> bool: 
        return self.maintenance_report_logic_manager.deny_or_accept_maintencance_report_for_admin(maintencance_report_id, location, accept_or_deny)
        # denies or accepts a maintenance report for an admin
    
    def edit_maintencance_report(self, maintenance_report: object, location: str, edit_choice: str, new_value: str):
        return self.maintenance_report_logic_manager.edit_maintencance_report(maintenance_report, location, edit_choice, new_value)
        # edits a maintenance report
    
    def get_employee_reports(self, staff_id: str) -> list[MaintenanceReport]:
        return self.maintenance_report_logic_manager.get_employee_reports(staff_id)
        # returns a list of all maintenance reports for a specific employee
    
    def get_incomplete_maintenance_reports(self,) -> list[MaintenanceReport]:
        return self.maintenance_report_logic_manager.get_incomplete_maintenance_reports()
        # returns a list of all incomplete maintenance reports
    
    def get_single_maintenance_report(self, report_id: str) -> MaintenanceReport:
        return self.maintenance_report_logic_manager.get_single_maintenance_report(report_id)

    def get_denied_reports(self, staff_id: str, location: str) -> list[MaintenanceReport]:
        return self.maintenance_report_logic_manager.get_denied_reports(staff_id, location)
    
    def reopen_closed_report(self, report, location):
        return self.maintenance_report_logic_manager.reopen_closed_report(report, location)
    
    def sanity_check_maintencance_report(self, what_to_check, new_value, location):
        location_list = self.get_all_locations() # get all locations
        return self.maintenance_report_logic_manager.sanity_check_maintencance_report(what_to_check, new_value, location)
        # checks if all info in a maintenance report object is correct

    ##############################################################################################################################################
    ### WORK_REQUESTS ############################################################################################################################

    def get_all_work_requests_at_location(self, rank: str, location: str, staff_id: str) -> list[WorkRequest]: 
        """Returns a list of all work requests at a specific location and whos status is "Open". """
        return self.work_request_logic_manager.get_all_work_requests_at_location(rank, location, staff_id)

    def get_work_request_by_date(self, rank: str, staff_id: str, location: str, work_request_date: str) -> WorkRequest:
        """Returns a work request object by a date. """
        return self.work_request_logic_manager.get_work_request_by_date(rank, staff_id, location, work_request_date)

    def get_work_request_by_id(self, rank: str, staff_id: str, location: str, work_request_id: str) -> WorkRequest:
        """Returns a work request object by a work request ID. """
        return self.work_request_logic_manager.get_work_request_by_id(rank, staff_id, location, work_request_id)  
    
    def get_all_new_work_requests(self, location: str) -> list[WorkRequest]:
        """Returns a list of all work requests whos status is "New". """
        return self.work_request_logic_manager.get_all_new_work_requests_in_storage(location)
    
    def get_all_closed_work_requests(self, location: str) -> list[WorkRequest]:
        """Returns a list of all work requests whos status is "Closed". """
        return self.work_request_logic_manager.get_all_closed_work_requests_in_storage(location)
    
    def get_all_pending_work_requests(self, rank: str, location: str, staff_id: str) -> list[WorkRequest]:
        """Returns a list of all work requests whos status is "Pending". """
        return self.work_request_logic_manager.get_all_pending_work_requests_in_storage(rank, location, staff_id)
        
    def get_my_work_requests(self, rank: str, location: str, staff_id: str) -> list[WorkRequest]:
        """Returns a list of all work requests depending on if the rank is employee or other. """
        return self.work_request_logic_manager.get_my_work_request(rank, location, staff_id)

    def edit_work_request(self, work_request: object):
        """Replaces a pre-existing work requesst with the same, updated version of itself. """
        self.work_request_logic_manager.edit_work_request(work_request)
    
    def auto_re_open_work_request(self, work_request: object):
        """If marked repetitive, the work request being marked complete is re-added to the storage with a new start date and ID. """
        self.work_request_logic_manager.auto_re_open_work_request(work_request)

    def add_work_request(self, work_request: object):
        """Receives a new instance of a work request and adds it to the storage. """
        self.work_request_logic_manager.add_work_request(work_request)

    def sanity_check_start_date(self, start_date: str) -> bool:
        """Verifies if the start date given by the user is valid. Returns True if so, otherwise False. """
        return self.work_request_logic_manager.sanity_check_start_date(start_date)
    
    def sanity_check_completition_date(self, start_date: str, completition_date_given: str) -> bool:
        """Verifies if the start date given by the user is valid. Returns True if so, otherwise False. """
        return self.work_request_logic_manager.sanity_check_completition_date(start_date, completition_date_given)

    def sanity_check_request_low_level_logistics(self, category: str, value_to_be_verified: str) -> bool:
        """Verifies if the input given by the user is valid. Returns True if so, otherwise False. """
        return self.work_request_logic_manager.sanity_check_request_low_level_logistics(category, value_to_be_verified)
    
    def sanity_check_work_request_property_id(self, property_id: str) -> bool:
        """Verifies if the property ID given by the user is valid. Returns True if so, otherwise False. """
        return self.work_request_logic_manager.sanity_check_work_request_property_id(property_id)
        
    def sanity_check_boolean_input_work_requests(self, yes_or_no: str) -> bool:
        """Verifies if the user entered Yes or No. Returns True or False if so, otherwise None. """
        return self.work_request_logic_manager.sanity_check_boolean_input_work_requests(yes_or_no)
        
    def sanity_check_priority_for_request(self, priority: str) -> bool:
        """Verifies if the priority given by the user is valid. Returns True if so, otherwise False. """
        return self.work_request_logic_manager.sanity_check_priority_for_request(priority)
        
    def sanity_check_location_for_request(self, location: str) -> bool:
        """Verifies if the location given by the user is valid. Returns True if so, otherwise False. """
        return self.work_request_logic_manager.sanity_check_location_for_request(location)
        
    def sanity_check_employee_id_for_request(self, staff_id: str) -> bool:
        """Verifies if the employee ID given by the user is valid. Returns True if so, otherwise False. """
        return self.work_request_logic_manager.sanity_check_employee_id_for_request(staff_id)
        
    ##############################################################################################################################################
    ### LOCATION #################################################################################################################################

    def get_all_locations(self) -> list:
        return self.location_logic_manager.all_location()
        # returns a list of all locations

    def fetch_all_amenities_for_location_in_storage(self, location: str) -> list[Location]:
        return self.location_logic_manager.fetch_all_amenities_for_location_in_storage(location)
        # returns a list of all amenities for a specific location
    
    def fetch_amenity_by_id(self, amenity_ID: str, location: str) -> object:
        return self.location_logic_manager.fetch_amenity_by_id(amenity_ID, location)
        # returns an amenity object by amenity_ID

    def edit_amenity(self, amenity: object, new_condition: str):
        return self.location_logic_manager.edit_amenity(amenity, new_condition)
        # edits an existing amenity in the storage
    
    def fetch_location_from_storage(self, location_id: str) -> Location:
        return self.location_logic_manager.fetch_location_from_storage(location_id)
        # returns a location object by Location_ID

    def sanity_check_location(self, what_to_check: str, new_value: str) -> bool:
        return self.location_logic_manager.sanity_check_location(what_to_check, new_value)
        # checks if all info in a location object is correct

    def add_new_location_to_storage(self, location: object):
        return self.location_logic_manager.add_new_location_to_storage(location)
        # adds a new location to the storage

    def edit_existing_location_in_storage(self, location: object, current_location: str, edit_choice: str, new_value: str):
        return self.location_logic_manager.edit_existing_location_in_storage(location, current_location, edit_choice, new_value)
        # adds a new location to the storage


