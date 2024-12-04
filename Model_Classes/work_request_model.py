class WorkRequest:
    def __init__(self, work_request_id:str="", name:str="", description:str="", maintenance_report_id:str="", staff_id:str="", location:str="", property_id:str="", start_date:str="", completition_date:str="", 
                repetitive_work:bool=False, reopen_interval:int=0, priority:str="", maintenance_report:str="",
                work_request_status:str="", need_contractor:bool=False, contractor_id:str="", mark_as_completed:bool=False):
        self.work_request_id = work_request_id
        self.name = name
        self.description = description
        self.maintenance_report_id = maintenance_report_id
        self.staff_id = staff_id
        self.location = location
        self.property_id = property_id
        self.start_date = start_date
        self.completition_date = completition_date
        self.repetitive_work = repetitive_work
        self.reopen_interval = reopen_interval
        self.priority = priority
        self.maintenance_report = maintenance_report
        self.work_request_status = work_request_status
        self.need_contractor = need_contractor
        self.contractor_id = contractor_id
        self.mark_as_completed = mark_as_completed

        ## this and the data in work_request storage does not have the same format

    def set_work_request_id(self, work_request_id):
        self.work_request_id = work_request_id

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id

    def set_location_id(self, location):
        self.location = location

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
    
    def get_location(self):
        return self.location

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
    
    def to_dict(self):
        return {
            'work_request_id': self.work_request_id,
            'name': self.name,
            'description': self.description,
            'maintenance_report_id': self.maintenance_report_id,
            'staff_id': self.staff_id,
            'location': self.location,
            'property_id': self.property_id,
            'start_date': self.start_date,
            'completition_date': self.completition_date,
            'repetitive_work': self.repetitive_work,
            'reopen_interval': self.reopen_interval,
            'priority': self.priority,
            'maintenance_report': self.maintenance_report,
            'work_request_status': self.work_request_status,
            'need_contractor': self.need_contractor,
            'contractor_id': self.contractor_id,
            'mark_as_completed': self.mark_as_completed
        }