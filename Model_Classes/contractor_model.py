class Contractor:
    def __init__(self, contractor_id:str="", company_name:str="", contact_name:str="", 
                opening_hours:str="",phone_number:int=0,location:str="", previous_job_reports:list=[]):
        self.contractor_id = contractor_id
        self.company_name = company_name
        self.contact_name = contact_name
        self.opening_hours = opening_hours
        self.phone_number = phone_number
        self.location = location
        self.previous_job_reports = previous_job_reports

    def set_contractor_id(self, contractor_id):
        self.contractor_id = contractor_id

    def set_company_name(self, company_name):
        self.company_name = company_name

    def set_contact_name(self, contact_name):
        self.contact_name = contact_name

    def set_opening_hours(self, opening_hours):
        self.opening_hours = opening_hours

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_location(self, location):
        self.location = location

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
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_location(self):
        return self.location

    def get_previous_job_reports(self):
        return self.previous_job_reports
    
    def to_dict(self):
        return {
            'contractor_id': self.contractor_id,
            'company_name': self.company_name,
            'contact_name': self.contact_name,
            'opening_hours': self.opening_hours,
            'phone_number': self.phone_number,
            'location': self.location,
            'previous_job_reports': self.previous_job_reports
        }