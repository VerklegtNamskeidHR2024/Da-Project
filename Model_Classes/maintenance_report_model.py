class MaintenanceReport:
    def __init__(self, report_id:str="", report_name:str="", location:str="", property_id:str="", staff_id:str="",
                regular_maintenance:bool=False, maintenance_description:str="", report_status:str="", price:float=0.0,
                mark_as_done:bool=False, contractor_id:str="", work_request_id:str=""):
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
    
    def to_dict(self):
        return {
            'report_id': self.report_id,
            'report_name': self.report_name,
            'location': self.location,
            'property_id': self.property_id,
            'staff_id': self.staff_id,
            'regular_maintenance': self.regular_maintenance,
            'maintenance_description': self.maintenance_description,
            'report_status': self.report_status,
            'price': self.price,
            'mark_as_done': self.mark_as_done,
            'contractor_id': self.contractor_id,
            'work_request_id': self.work_request_id
        }