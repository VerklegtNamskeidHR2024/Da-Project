class maintenance_report_logic_manager:
    def __init__(self, storage_layer_wrapper):
        """Constructor for maintenance report logic manager"""
        self.storage_layer_wrapper = storage_layer_wrapper

    def sanity_check_maintencance_report(self, what_to_check, new_value, location) -> bool:
        """Check if all info in a maintenance report object is correct"""
        # check if the report name is longer than 3 characters
        if what_to_check == 'report name': 
            if len(new_value) > 3:
                return True
            else:
                return False
        # check if the location is in the system
        elif what_to_check == 'location':
            list_of_all_locations = self.storage_layer_wrapper.get_all_locations()
            for loc in list_of_all_locations:
                if loc.location == new_value:
                    return True
            return False
        # check if the property id is in the system
        elif what_to_check in 'property id':
            list_of_all_properties = self.storage_layer_wrapper.get_all_properties_at_location()
            for property in list_of_all_properties:
                if property.property_id == new_value:
                    return True
            return False
        # check if the staff id is in the system
        elif what_to_check in 'staff id':
            list_of_all_employees = self.storage_layer_wrapper.get_all_employees()
            for employee in list_of_all_employees:
                if employee.staff_id == new_value:
                    return True
            return False
        # check if the regular maintenance is yes or no
        elif what_to_check in 'regular maintenance':
            if new_value in 'yes' or new_value in 'no':
                return True
            else:
                return False
        # check if the maintenance description is longer than 3 characters
        elif what_to_check in 'maintenance description':
            if len(new_value) > 3:
                return True
            else:
                return False
        # check if the report status is pending or closed  
        elif what_to_check in 'report status':
            if new_value in 'pending' or new_value in 'closed':
                return True
            else:
                return False
        # check if the price is a number
        elif what_to_check in 'cost':
            try:
                float(new_value)
                return True
            except ValueError:
                return False
        # check if the mark as done is yes or no   
        elif what_to_check in 'mark as done':
            if new_value in 'Yes' or new_value in 'No' or new_value in 'yes' or new_value in 'no':
                return True
            else:
                return False
        # check if the contractor id is in the system   
        elif what_to_check in 'contractor id':
            list_of_all_contractors = self.storage_layer_wrapper.get_all_contractor()
            for contractor in list_of_all_contractors:
                if contractor.contractor_id == new_value or new_value == '':
                    return True
            return False
        # check if the work request id is in the system   
        elif what_to_check in 'work request id':
            list_of_all_work_requests = self.storage_layer_wrapper.get_all_work_requests()
            for work_request in list_of_all_work_requests:
                if work_request.work_request_id == new_value:
                    return True
            return False
        # check if the report id is in the system
        elif what_to_check in 'report id':
            list_of_all_reports = self.get_all_maintencance_reports_at_location(location)
            for report in list_of_all_reports:
                if report.report_id == new_value:
                    return True
            return False
        
    def get_highest_ID(self, location):
        """Get the highest ID for a maintenance report"""
        highestID = -1 # initialize the highest id to -1
        list_of_all_reports = self.get_all_maintencance_reports(location) # get all maintenance reports at a location

        for report in list_of_all_reports: # iterate through all reports
            stripped_ID = report.report_id[2:] # get the id of the report
            if int(stripped_ID) > highestID: # checks if the id is higher than the highest id
                highestID = int(stripped_ID) # checks if the id is higher than the highest id
        highestID += 1 # if the id is higher than the highest id increment the highest id by 1

        new_report_id = 'MR' + str(highestID) 
        return new_report_id

    def get_all_maintencance_reports(self, location) -> list:
        """Get all maintenance reports"""
        maintenance_report_list = []

        all_maintenance_reports = self.storage_layer_wrapper.get_all_maintenance_reports()

        for maintenance_report in all_maintenance_reports: # iterate through all maintenance reports
            maintenance_report_list.append(maintenance_report) # append the maintenance report to the maintenance report list

        return maintenance_report_list

    def add_maintencance_report_to_storage(self, location, maintenance_report, is_regular):
        """Add a maintenance report to the storage"""
        list_of_all_reports = self.get_all_maintencance_reports(location) # get all maintenance reports at a location
        new_report_id = self.get_highest_ID(location) # get the highest id for a maintenance report
        #checks if the maintenance report is regular or not
        if is_regular == 'yes' or is_regular == 'Yes' or is_regular == 'YES':
            maintenance_report.set_regular_maintenance(True)
        elif is_regular == 'no' or is_regular == 'No' or is_regular == 'NO':
            maintenance_report.set_regular_maintenance(False)
        
        maintenance_report.set_report_id(new_report_id)

        list_of_all_reports.append(maintenance_report)
        self.storage_layer_wrapper.write_to_file_maintenance_reports(list_of_all_reports)

    def check_if_report_in_system(self, maintenance_report_id, location) -> bool:
        """Check if a maintenance report is in the system"""
        list_of_reports = self.get_all_maintencance_reports_at_location(location)

        for report in list_of_reports: # iterate through all reports
            if report.report_id == maintenance_report_id: # checks if the report id is the same as the maintenance report id
                return True # return true if the report is in the system or else false
        return False
    
    def get_employee_reports(self, staff_id) -> list:
        """Get all reports for an employee"""
        employee_reports = [] # initialize an empty list to hold employee reports
        all_reports = self.get_all_maintencance_reports('') # get all maintenance reports
        # iterate through all reports and append the reports for an employee to the employee reports list 
        for report in all_reports:
            if report.staff_id == staff_id:
                employee_reports.append(report)  # it adds it in the report list if the staff id is the same as the staff id in the report

        return employee_reports
    
    def get_incomplete_maintenance_reports(self, location) -> list:
        """Get all incomplete maintenance reports"""
        incomplete_reports = [] # initialize an empty list to hold incomplete reports
        all_reports = self.get_all_maintencance_reports_at_location(location)

        for report in all_reports:
            if report.report_status == 'Incomplete': # checks if the report status is incomplete
                incomplete_reports.append(report) # append the report to the incomplete reports list

        return incomplete_reports

    def edit_maintencance_report(self, maintenance_report, location, edit_choice, new_value):
        """Edit a maintenance report"""
        list_of_reports = self.get_all_maintencance_reports_at_location(location)
        # iterate through all reports and edit the report
        for report in list_of_reports:
            # checks if the report id is the same as the maintenance report id
            if report.report_id == maintenance_report.report_id:
                # checks if the choice is equal to the report name, staff id, description, cost, regular, contractor id
                if edit_choice == 'Report Name':
                    report.set_report_name(new_value)
                
                elif edit_choice == 'Location':
                    report.set_location(new_value)

                elif edit_choice == 'Property ID':
                    report.set_property_id(new_value)
                
                elif edit_choice == 'Staff ID':
                    report.set_staff_id(new_value)

                elif edit_choice == 'Regular':
                    if new_value == 'Yes' or new_value == 'yes':
                        report.set_regular_maintenance(True)
                    elif new_value == 'No' or new_value == 'no':
                        report.set_regular_maintenance(False)

                elif edit_choice == 'Description':
                    report.set_maintenance_description(new_value)

                elif edit_choice == 'Report Status':
                    report.set_report_status(new_value)

                elif edit_choice == 'Cost':
                    report.set_price(new_value)

                elif edit_choice == 'Contractor ID':
                    report.set_contractor_id(new_value)

                elif edit_choice == 'Work Request ID':
                    report.set_work_request_id(new_value)

        self.storage_layer_wrapper.write_to_file_maintenance_reports(list_of_reports)

    def get_all_maintencance_reports_at_location(self, location) -> list:
        """Get all maintenance reports at a location"""
        maintenance_report_sorted_list = [] # initialize an empty list to hold sorted maintenance reports

        all_maintenance_reports = self.storage_layer_wrapper.get_all_maintenance_reports() # get all maintenance reports
        # iterate through all maintenance reports and append the maintenance reports at a location to the sorted list
        for maintenance_report in all_maintenance_reports: 
            if maintenance_report.location == location:
                maintenance_report_sorted_list.append(maintenance_report)

        return maintenance_report_sorted_list

    def deny_or_accept_maintencance_report_for_admin(self, maintencance_report_ID, location, accept_or_deny): 
        """Deny or accept a maintenance report for an admin"""
        list_of_reports = self.get_all_maintencance_reports_at_location(location)  # get all maintenance reports at a location

        for report in list_of_reports: # iterate through all reports
            if report.report_id == maintencance_report_ID: # checks if the report id is the same as the maintenance report id
                if accept_or_deny == 'Accept': # checks if the admin accepts the report
                    report.set_mark_as_done(True)
                    report.set_report_status('Closed')
                elif accept_or_deny == 'Deny': # checks if the admin denies the report
                    report.set_mark_as_done(False)
                    report.set_report_status('Denied')

        self.storage_layer_wrapper.write_to_file_maintenance_reports(list_of_reports)

    def fetch_all_pending_maintencance_reports(self, location) -> list:
        """Get all pending maintenance reports"""
        pending_reports = []
        list_of_all_reports = self.get_all_maintencance_reports_at_location(location)
        # iterate through all reports and append the pending reports to the pending reports list
        for report in list_of_all_reports:
            if report.report_status == 'Pending':
                pending_reports.append(report)

        if not pending_reports:
            return 'No pending Reports'
        else:
            return pending_reports

    def fetch_all_closed_maintencance_reports(self, location) -> list:
        """Get all closed maintenance reports""" 
        closed_reports = [] # initialize an empty list to hold closed reports
        list_of_all_reports = self.get_all_maintencance_reports_at_location(location) # get all maintenance reports at a location

        for report in list_of_all_reports: # iterate through all reports
            if report.report_status == 'Closed': # checks if the report status is closed
                closed_reports.append(report) #  append the report to the closed reports list
        
        if not closed_reports: # checks if there are no closed reports
            return 'No closed reports' # return no closed reports if there are no closed reports
        else:
            return closed_reports
        
    def get_denied_reports(self, staff_id, location):
        denied_reports = []
        list_of_all_reports = self.get_all_maintencance_reports_at_location(location)

        for report in list_of_all_reports:
            if report.staff_id == staff_id and report.report_status == 'Denied':
                denied_reports.append(report)

        if not denied_reports:
            return 'No denied reports'
        else:
            return denied_reports
        

    def get_single_maintenance_report(self, report_id):
        all_reports = self.get_all_maintencance_reports('')
        for report in all_reports:
            if report.report_id == report_id:
                return report