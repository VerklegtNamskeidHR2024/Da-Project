class maintenance_report_logic_manager:
    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def sanity_check_maintencance_report(maintencance_report):
        pass

    def get_highest_ID(self, location):
        highestID = -1
        list_of_all_reports = self.get_all_maintencance_reports_at_location(location)
        for report in list_of_all_reports:
            stripped_ID = report.report_id[2:]
            if int(stripped_ID) > highestID:
                highestID = int(stripped_ID)
        highestID += 1

        new_report_id = 'MR' + str(highestID)
        return new_report_id

    def add_maintencance_report_to_storage(self, location, maintenance_report, is_regular):
        highestID = -1
        list_of_all_reports = self.get_all_maintencance_reports_at_location(location)
        for report in list_of_all_reports:
            stripped_ID = report.report_id[2:]
            if int(stripped_ID) > highestID:
                highestID = int(stripped_ID)
        highestID += 1

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

    def edit_maintencance_report(maintenance_report):
        pass

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