class Human:
    def __init__(self,name, social_security_number, phone_number, location, system_permissions, email):
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
    def __init__(self, name, social_security_number, phone_number, location, system_permissions, email, staff_id, ):
        super().__init__(name, social_security_number, phone_number, location, system_permissions, email)
        self.staff_id = staff_id

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id
    
    def get_staff_id(self):
        return self.staff_id
        
class Employee(Human):
    def __init__(self, name, social_security_number, phone_number, location, system_permissions, email, staff_id):
        super().__init__(name, social_security_number, phone_number, location, system_permissions, email)
        self.staff_id = staff_id

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id

    def get_staff_id(self):
        return self.staff_id

class Location:
    def __init__(self, country, location, airport, phone_number, branch_manager, opening_hours, amenities_list):
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
    
        
class Property:
    def __init__(self, name, location, total_price_to_fix):
        self.name = name
        self.location = location
        self.total_price_to_fix = total_price_to_fix

class House(Property):
    def __init__(self, name, location, total_price_to_fix, property_id, property_price):
        super().__init__(name, location, total_price_to_fix)
        self.property_id = property_id
        self.property_price = property_price

class Amenity(Property):
    def __init__(self, name, location, total_price_to_fix, amenity_id):
        super().__init__(name, location, total_price_to_fix)
        self.amenity_id = amenity_id

class WorkRequest:
    def __init__(self, work_request_id, staff_id, property_id, date_of_creation, repetitive_work,
                reopen_interval, priority, maintenance_report, work_request_status, need_contractor,
                contractor_id, mark_as_done):
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

class MaintenanceReport:
    def __init__(self, report_id, report_name, location, property_id, staff_id, regular_maintenance, 
                maintenance_description, report_status, price, mark_as_done, contractor_id, work_request_id):
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

class Contractor:
    def __init__(self, contractor_id, company_name, contact_name, opening_hours, previous_job_reports):
        self.contractor_id = contractor_id
        self.company_name = company_name
        self.contact_name = contact_name
        self.opening_hours = opening_hours
        self.previous_job_reports = previous_job_reports