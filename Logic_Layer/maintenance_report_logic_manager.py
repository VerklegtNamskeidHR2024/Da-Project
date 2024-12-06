class maintenance_report_logic_manager:
    def __init__(self, Storage_Layer_Wrapper, location):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper
        self.location = location
        from Logic_Layer.property_logic_manager import property_logic_manager
        from Logic_Layer.location_logic_manager import location_logic_manager
        from Logic_Layer.contractor_logic_manager import contractor_logic_manager
        from Logic_Layer.employee_logic_manager import employee_logic_manager
        from Logic_Layer.work_request_logic_manager import work_request_logic_manager

    def sanity_check_maintencance_report(self, what_to_check, new_value, location):
        if what_to_check == 'report name':
            if len(new_value) > 3:
                return True
            else:
                return False
        elif what_to_check in 'location':
            list_of_all_locations = self.Location_Logic_Manager.get_all_locations()
            for location in list_of_all_locations:
                if location.location == new_value:
                    return True
            return False
        elif what_to_check in 'property id':
            list_of_all_properties = self.Property_Logic_Manager.get_all_properties()
            for property in list_of_all_properties:
                if property.property_id == new_value:
                    return True
            return False
        elif what_to_check in 'staff id':
            list_of_all_employees = self.Employee_Logic_Manager.get_all_employees_at_location(location)
            for employee in list_of_all_employees:
                if employee.staff_id == new_value:
                    return True
            return False
        elif what_to_check in 'regular maintenance':
            if new_value in 'yes' or new_value in 'no':
                return True
            else:
                return False
        elif what_to_check in 'maintenance description':
            if len(new_value) > 3:
                return True
            else:
                return False
            
        elif what_to_check in 'report status':
            if new_value in 'pending' or new_value in 'closed':
                return True
            else:
                return False
        
        elif what_to_check in 'cost':
            try:
                float(new_value)
                return True
            except ValueError:
                return False
            
        elif what_to_check in 'mark as done':
            if new_value in 'Yes' or new_value in 'No' or new_value in 'yes' or new_value in 'no':
                return True
            else:
                return False
            
        elif what_to_check in 'contractor id':
            list_of_all_contractors = self.Contractor_Logic_Manager.get_all_contractors()
            for contractor in list_of_all_contractors:
                if contractor.contractor_id == new_value:
                    return True
            return False
            
        elif what_to_check in 'work request id':
            list_of_all_work_requests = self.Work_Request_Logic_Manager.get_all_work_requests(location)
            for work_request in list_of_all_work_requests:
                if work_request.work_request_id == new_value:
                    return True
            return False
        
        

    def get_highest_ID(self, location):
        highestID = -1
        list_of_all_reports = self.get_all_maintencance_reports(location)
        for report in list_of_all_reports:
            stripped_ID = report.report_id[2:]
            if int(stripped_ID) > highestID:
                highestID = int(stripped_ID)
        highestID += 1

        new_report_id = 'MR' + str(highestID)
        return new_report_id

    def get_all_maintencance_reports(self, location) -> list:
        maintenance_report_list = []

        all_maintenance_reports = self.Storage_Layer_Wrapper.get_all_maintenance_report()

        for maintenance_report in all_maintenance_reports:
            maintenance_report_list.append(maintenance_report)

        return maintenance_report_list

    def add_maintencance_report_to_storage(self, location, maintenance_report, is_regular):
        list_of_all_reports = self.get_all_maintencance_reports(location)
        new_report_id = self.get_highest_ID(location)
        if is_regular == 'yes' or is_regular == 'Yes' or is_regular == 'YES':
            maintenance_report.set_regular_maintenance(True)
        elif is_regular == 'no' or is_regular == 'No' or is_regular == 'NO':
            maintenance_report.set_regular_maintenance(False)
        maintenance_report.set_report_id(new_report_id)
        maintenance_report.set_report_status('Pending')
        list_of_all_reports.append(maintenance_report)
        self.Storage_Layer_Wrapper.write_to_file_maintenance_reports(list_of_all_reports)

    def check_if_report_in_system(self, maintenance_report_id, location) -> bool:
        list_of_reports = self.get_all_maintencance_reports_at_location(location)
        for report in list_of_reports:
            if report.report_id == maintenance_report_id:
                return True
        return False

    def edit_maintencance_report(self, maintenance_report, location, edit_choice, new_value):
        list_of_reports = self.get_all_maintencance_reports_at_location(location)
        for report in list_of_reports:
            if report.report_id == maintenance_report.report_id:
                if edit_choice == 'Report Name':
                    report.set_report_name(new_value)
                elif edit_choice == 'Staff ID':
                    report.set_staff_id(new_value)
                elif edit_choice == 'Description':
                    report.set_maintenance_description(new_value)
                elif edit_choice == 'Cost':
                    report.set_price(new_value)
                elif edit_choice == 'Regular':
                    if new_value == 'Yes' or new_value == 'yes':
                        report.set_regular_maintenance(True)
                    elif new_value == 'No' or new_value == 'no':
                        report.set_regular_maintenance(False)
                elif edit_choice == 'Contractor ID':
                    report.set_contractor_id(new_value)
        self.Storage_Layer_Wrapper.write_to_file_maintenance_reports(list_of_reports)

    def get_all_maintencance_reports_at_location(self, location) -> list:
        maintenance_report_sorted_list = []

        all_maintenance_reports = self.Storage_Layer_Wrapper.get_all_maintenance_report()

        for maintenance_report in all_maintenance_reports:
            if maintenance_report.location == location:
                maintenance_report_sorted_list.append(maintenance_report)

        return maintenance_report_sorted_list

    def deny_or_accept_maintencance_report_for_admin(self, maintencance_report_ID, location, accept_or_deny): 
        list_of_reports = self.get_all_maintencance_reports_at_location(location)

        for report in list_of_reports:
            if report.report_id == maintencance_report_ID:
                if accept_or_deny == 'Accept':
                    report.set_mark_as_done(True)
                elif accept_or_deny == 'Deny':
                    report.set_mark_as_done(False)

        self.Storage_Layer_Wrapper.write_to_file_maintenance_reports(list_of_reports)

    def fetch_all_pending_maintencance_reports(self, location) -> list:
        pending_reports = []
        list_of_all_reports = self.get_all_maintencance_reports_at_location(location)
        for report in list_of_all_reports:
            if report.report_status == 'Pending':
                pending_reports.append(report)

        if not pending_reports:
            return 'No pending Reports'
        else:
            return pending_reports

    def fetch_all_closed_maintencance_reports(self, location) -> list:
        closed_reports = []
        list_of_all_reports = self.get_all_maintencance_reports_at_location(location)
        for report in list_of_all_reports:
            if report.report_status == 'Closed':
                closed_reports.append(report)
        
        if not closed_reports:
            return 'No closed reports'
        else:
            return closed_reports