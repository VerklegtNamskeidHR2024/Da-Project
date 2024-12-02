class WorkRequest:
    def __init__(self, work_request_id:str="", staff_id:str="", property_id:str="", date_of_creation:str="", 
                repetitive_work:bool=False, reopen_interval:int=0, priority:str="", maintenance_report:str="",
                work_request_status:str="", need_contractor:bool=False, contractor_id:str="", mark_as_done:bool=False):
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