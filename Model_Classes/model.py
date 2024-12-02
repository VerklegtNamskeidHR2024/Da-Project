class Human:
    def __init__(self,name: str, social_security_number: int, phone_number: int, location: str,
                system_permissions: str, email: str):
        self.name = name
        self.social_security_number = social_security_number
        self.phone_number = phone_number
        self.location = location
        self.system_permissions = system_permissions
        self.email = email

    def set_name(self, name):
        self.name = name
    
    def set_social_security_number(self, social_security_number):
        self.social_security_number = social_security_number
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_location(self, location):
        self.location = location

    def set_system_permissions(self, system_permissions):
        self.system_permissions = system_permissions
    
    def set_email(self, email):
        self.email = email
    
    def get_name(self):
        return self.name
    
    def get_social_security_number(self):
        return self.social_security_number
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_location(self):
        return self.location
    
    def get_system_permissions(self):
        return self.system_permissions
    
    def get_email(self):
        return self.email
    
class Manager(Human):
    def __init__(self, name: str, social_security_number: int, phone_number: int, location: str, system_permissions: str,
                email: str, staff_id: str):
        super().__init__(name, social_security_number, phone_number, location, system_permissions, email)
        self.staff_id = staff_id

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id
    
    def get_staff_id(self):
        return self.staff_id
        
class Employee(Human):
    def __init__(self, name: str, social_security_number: int, phone_number: int, location: str, system_permissions: str,
                email: str, staff_id: str):
        super().__init__(name, social_security_number, phone_number, location, system_permissions, email)
        self.staff_id = staff_id

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id

    def get_staff_id(self):
        return self.staff_id

class Location:
    def __init__(self, country: str, location: str, airport: str, phone_number: str, branch_manager: str, 
                opening_hours: str, amenities_list: list):
        self.country = country
        self.location = location
        self.airport = airport
        self.phone_number = phone_number
        self.branch_manager = branch_manager
        self.opening_hours = opening_hours
        self.amenities_list = amenities_list

    def set_country(self, country):
        self.country = country

    def set_location(self, location):
        self.location = location
    
    def set_airport(self, airport):
        self.airport = airport
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_branch_manager(self, branch_manager):
        self.branch_manager = branch_manager

    def set_opening_hours(self, opening_hours):
        self.opening_hours = opening_hours

    def set_amenities_list(self, amenities_list):
        self.amenities_list = amenities_list
    
    def get_country(self):
        return self.country
    
    def get_location(self):
        return self.location
    
    def get_airport(self):
        return self.airport
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_branch_manager(self):
        return self.branch_manager
    
    def get_opening_hours(self):
        return self.opening_hours
    
    def get_amenities_list(self):
        return self.amenities_list
        
class Property:
    def __init__(self, name: str, location: str, total_price_to_fix: float):
        self.name = name
        self.location = location
        self.total_price_to_fix = total_price_to_fix

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def set_total_price_to_fix(self, total_price_to_fix):
        self.total_price_to_fix = total_price_to_fix

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_total_price_to_fix(self):
        return self.total_price_to_fix

class House(Property):
    def __init__(self, name: str, location: str, total_price_to_fix: float, property_id: str, property_price: float):
        super().__init__(name, location, total_price_to_fix)
        self.property_id = property_id
        self.property_price = property_price

    def set_property_id(self, property_id):
        self.property_id = property_id

    def set_property_price(self, property_price):
        self.property_price = property_price

    def get_property_id(self):
        return self.property_id

    def get_property_price(self):
        return self.property_price

class Amenity(Property):
    def __init__(self, name: str, location: str, total_price_to_fix: float, amenity_id: str):
        super().__init__(name, location, total_price_to_fix)
        self.amenity_id = amenity_id

    def set_amenity_id(self, amenity_id):
        self.amenity_id = amenity_id

    def get_amenity_id(self):
        return self.amenity_id

class WorkRequest:
    def __init__(self, work_request_id: str, staff_id: str, property_id: str, date_of_creation: str, repetitive_work: bool,
                reopen_interval: int, priority: str, maintenance_report: str, work_request_status: bool, 
                need_contractor: bool, contractor_id: str, mark_as_done: bool):
        self.work_request_id = work_request_id
        self.staff_id = staff_id
        self.property_id = property_id
        self.date_of_creation = date_of_creation
        self.repetitive_work = repetitive_work
        self.reopen_interval = reopen_interval
        self.priority = priority
        self.maintenance_report = maintenance_report
        self.work_request_status = work_request_status
        self.need_contractor = need_contractor
        self.contractor_id = contractor_id
        self.mark_as_done = mark_as_done

    def set_work_request_id(self, work_request_id):
        self.work_request_id = work_request_id

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id

    def set_property_id(self, property_id):
        self.property_id = property_id

    def set_date_of_creation(self, date_of_creation):
        self.date_of_creation = date_of_creation

    def set_repetitive_work(self, repetitive_work):
        self.repetitive_work = repetitive_work

    def set_reopen_interval(self, reopen_interval):
        self.reopen_interval = reopen_interval

    def set_priority(self, priority):
        self.priority = priority

    def set_maintenance_report(self, maintenance_report):
        self.maintenance_report = maintenance_report

    def set_work_request_status(self, work_request_status):
        self.work_request_status = work_request_status

    def set_need_contractor(self, need_contractor):
        self.need_contractor = need_contractor

    def set_contractor_id(self, contractor_id):
        self.contractor_id = contractor_id

    def set_mark_as_done(self, mark_as_done):
        self.mark_as_done = mark_as_done

    def get_work_request_id(self):
        return self.work_request_id

    def get_staff_id(self):
        return self.staff_id

    def get_property_id(self):
        return self.property_id

    def get_date_of_creation(self):
        return self.date_of_creation

    def get_repetitive_work(self):
        return self.repetitive_work

    def get_reopen_interval(self):
        return self.reopen_interval

    def get_priority(self):
        return self.priority

    def get_maintenance_report(self):
        return self.maintenance_report

    def get_work_request_status(self):
        return self.work_request_status

    def get_need_contractor(self):
        return self.need_contractor

    def get_contractor_id(self):
        return self.contractor_id

    def get_mark_as_done(self):
        return self.mark_as_done

class MaintenanceReport:
    def __init__(self, report_id: str, report_name: str, location: str, property_id: str, staff_id: str, 
                regular_maintenance: bool, maintenance_description: str, report_status: bool, price: float,
                mark_as_done: bool, contractor_id: str, work_request_id: str):
        self.report_id = report_id
        self.report_name = report_name
        self.location = location
        self.property_id = property_id
        self.staff_id = staff_id
        self.regular_maintenance = regular_maintenance
        self.maintenance_description = maintenance_description
        self.report_status = report_status
        self.price = price
        self.mark_as_done = mark_as_done
        self.contractor_id = contractor_id
        self.work_request_id = work_request_id

    def set_report_id(self, report_id):
        self.report_id = report_id

    def set_report_name(self, report_name):
        self.report_name = report_name

    def set_location(self, location):
        self.location = location

    def set_property_id(self, property_id):
        self.property_id = property_id

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id

    def set_regular_maintenance(self, regular_maintenance):
        self.regular_maintenance = regular_maintenance

    def set_maintenance_description(self, maintenance_description):
        self.maintenance_description = maintenance_description

    def set_report_status(self, report_status):
        self.report_status = report_status

    def set_price(self, price):
        self.price = price

    def set_mark_as_done(self, mark_as_done):
        self.mark_as_done = mark_as_done

    def set_contractor_id(self, contractor_id):
        self.contractor_id = contractor_id

    def set_work_request_id(self, work_request_id):
        self.work_request_id = work_request_id

    def get_report_id(self):
        return self.report_id

    def get_report_name(self):
        return self.report_name

    def get_location(self):
        return self.location

    def get_property_id(self):
        return self.property_id

    def get_staff_id(self):
        return self.staff_id

    def get_regular_maintenance(self):
        return self.regular_maintenance

    def get_maintenance_description(self):
        return self.maintenance_description

    def get_report_status(self):
        return self.report_status

    def get_price(self):
        return self.price

    def get_mark_as_done(self):
        return self.mark_as_done

    def get_contractor_id(self):
        return self.contractor_id

    def get_work_request_id(self):
        return self.work_request_id

class Contractor:
    def __init__(self, contractor_id: str, company_name: str, contact_name: str, 
                opening_hours: str, previous_job_reports: list):
        self.contractor_id = contractor_id
        self.company_name = company_name
        self.contact_name = contact_name
        self.opening_hours = opening_hours
        self.previous_job_reports = previous_job_reports

    def set_contractor_id(self, contractor_id):
        self.contractor_id = contractor_id

    def set_company_name(self, company_name):
        self.company_name = company_name

    def set_contact_name(self, contact_name):
        self.contact_name = contact_name

    def set_opening_hours(self, opening_hours):
        self.opening_hours = opening_hours

    def set_previous_job_reports(self, previous_job_reports):
        self.previous_job_reports = previous_job_reports

    def get_contractor_id(self):
        return self.contractor_id

    def get_company_name(self):
        return self.company_name

    def get_contact_name(self):
        return self.contact_name

    def get_opening_hours(self):
        return self.opening_hours

    def get_previous_job_reports(self):
        return self.previous_job_reports