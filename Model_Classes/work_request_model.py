class WorkRequest:
    def __init__(self, work_request_id:str="", name:str="", description:str="", maintenance_report_id:str="", staff_id:str="", location:str="", property_id:str="", start_date:str="", completition_date:str="", 
                repetitive_work:bool=False, reopen_interval:int=0, priority:str="",
                work_request_status:str="", need_contractor:bool=False, contractor_id:str="", mark_as_completed:bool=False, accepted_by_employee: bool=False):
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
        self.work_request_status = work_request_status
        self.need_contractor = need_contractor
        self.contractor_id = contractor_id
        self.mark_as_completed = mark_as_completed
        self.accepted_by_employee = accepted_by_employee
        ## this and the data in work_request storage does not have the same format

    def set_work_request_id(self, work_request_id):
        self.work_request_id = work_request_id

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id

    def set_location(self, location):
        self.location = location

    def set_property_id(self, property_id):
        self.property_id = property_id

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_completition_date(self, completition_date):
        self.completition_date = completition_date

    def set_repetitive_work(self, repetitive_work):
        self.repetitive_work = repetitive_work

    def set_reopen_interval(self, reopen_interval):
        self.reopen_interval = reopen_interval

    def set_priority(self, priority):
        self.priority = priority

    def set_maintenance_report_id(self, maintenance_report_id):
        self.maintenance_report_id = maintenance_report_id

    def set_work_request_status(self, work_request_status):
        self.work_request_status = work_request_status

    def set_need_contractor(self, need_contractor):
        self.need_contractor = need_contractor

    def set_contractor_id(self, contractor_id):
        self.contractor_id = contractor_id

    def set_mark_as_completed(self, mark_as_completed):
        self.mark_as_completed = mark_as_completed

    def set_accepted_by_employee(self, accepted_by_employee):
        self.accepted_by_employee = accepted_by_employee 

    def get_work_request_id(self):
        return self.work_request_id
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

    def get_staff_id(self):
        return self.staff_id
    
    def get_location(self):
        return self.location

    def get_property_id(self):
        return self.property_id

    def get_start_date(self):
        return self.start_date

    def get_completition_date(self):
        return self.completition_date

    def get_repetitive_work(self):
        return self.repetitive_work

    def get_reopen_interval(self):
        return self.reopen_interval

    def get_priority(self):
        return self.priority

    def get_maintenance_report_id(self):
        return self.maintenance_report_id

    def get_work_request_status(self):
        return self.work_request_status

    def get_need_contractor(self):
        return self.need_contractor

    def get_contractor_id(self):
        return self.contractor_id

    def get_mark_as_completed(self):
        return self.mark_as_completed
    
    def get_accepted_by_employee(self):
        return self.accepted_by_employee

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
            'work_request_status': self.work_request_status,
            'need_contractor': self.need_contractor,
            'contractor_id': self.contractor_id,
            'mark_as_completed': self.mark_as_completed,
            'accepted_by_employee': self.accepted_by_employee
        }
    
    # Gylfi Made 
    def __eq__(self, value: object) -> bool:
        if isinstance(value, WorkRequest):
            value.priority == self.priority
            return True
        return False

    def __lt__(self, value: object) -> bool:
        if isinstance(value, WorkRequest):
            match self.priority:
                case "High":
                    return False
                case "Medium":
                    if value.priority == "High":
                        return True
                    return False
                case "Low":
                    if value.priority == "Low":
                        return False
                    return True
    
    def __gt__(self, value: object) -> bool:
        if isinstance(value, WorkRequest):
            return value < self