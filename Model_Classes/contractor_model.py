class Contractor:
    def __init__(self, contractor_id:str="", company_name:str="", contact_name:str="", 
                opening_hours:str="", previous_job_reports:list=[]):
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
    
    def __str__(self):
        return_string = self.contractor_id +" "+ self.contact_name+ " " + self.company_name
        return return_string