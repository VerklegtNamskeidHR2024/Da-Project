class Contractor:
    
    def __init__(self, contractor_id:str="", company_name:str="", contact_name:str="", 
                opening_hours:str="",phone_number:int=0,location:str="", previous_job_reports:list=[],
                warningtext:str="Contractor Has No Warning"):
        self.contractor_id = contractor_id
        self.company_name = company_name
        self.contact_name = contact_name
        self.opening_hours = opening_hours
        self.phone_number = phone_number
        self.location = location
        self.previous_job_reports = previous_job_reports
        self.warningtext = warningtext

    def set_contractor_id(self, contractor_id):
        """Sets the contractor id"""
        self.contractor_id = contractor_id

    def set_company_name(self, company_name):
        """Sets the company name"""
        self.company_name = company_name

    def set_contact_name(self, contact_name):
        """Sets the contact name"""
        self.contact_name = contact_name

    def set_opening_hours(self, opening_hours):
        """Sets the opening hours"""
        self.opening_hours = opening_hours

    def set_phone_number(self, phone_number):
        """Sets the phone number"""
        self.phone_number = phone_number

    def set_warningtext(self, warningtext):
        """Sets the warning text"""
        self.warningtext = warningtext

    def set_location(self, location):
        """Sets the location"""
        self.location = location

    def set_previous_job_reports(self, previous_job_reports):
        """Sets the previous job reports"""
        self.previous_job_reports = previous_job_reports

    def get_contractor_id(self):
        """Gets the contractor id"""
        return self.contractor_id

    def get_company_name(self):
        """Gets the company name"""
        return self.company_name

    def get_contact_name(self):
        """Gets the contact name"""
        return self.contact_name

    def get_opening_hours(self):
        """Gets the opening hours"""
        return self.opening_hours
    
    def get_phone_number(self):
        """Gets the phone number"""
        return self.phone_number
    
    def get_location(self):
        """Gets the location"""
        return self.location

    def get_previous_job_reports(self):
        """Gets the previous job reports"""
        return self.previous_job_reports
    
    def to_dict(self):
        """Converts the Contractor object to a dictionary"""
        return {
            'contractor_id': self.contractor_id,
            'company_name': self.company_name,
            'contact_name': self.contact_name,
            'opening_hours': self.opening_hours,
            'phone_number': self.phone_number,
            'location': self.location,
            'previous_job_reports': self.previous_job_reports,
            'warningtext': self.warningtext
        }