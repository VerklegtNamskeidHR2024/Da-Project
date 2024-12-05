class maintenance_report_logic_manager:
    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def sanity_check_maintencance_report(maintencance_report):
        pass

    def add_maintencance_report_to_storage(self, location, maintenance_report):
        highestID = 0
        list_of_all_reports = self.get_all_maintencance_reports_at_location(location)
        for report in list_of_all_reports:
            stripped_ID = report.report_id[2:]
            if int(stripped_ID) > highestID:
                highestID = int(stripped_ID)
                highestID += 1
        new_report_id = 'MR' + highestID
        print(new_report_id)
        maintenance_report.set_report_id(new_report_id)
        list_of_all_reports.append(maintenance_report)
        print('Write this shit')
        self.Storage_Layer_Wrapper.write_to_file_maintenance_reports(list_of_all_reports)

    def edit_maintencance_report(maintencance_report):
        pass

    def get_all_maintencance_reports_at_location(self, location) -> list:
        maintenance_report_sorted_list = []

        all_maintenance_reports = self.Storage_Layer_Wrapper.get_all_maintenance_report()

        for maintenance_report in all_maintenance_reports:
            if maintenance_report.location == location:
                maintenance_report_sorted_list.append(maintenance_report)

        return maintenance_report_sorted_list

    def mark_report_as_ready(maintencance_report_ID):
        pass

    def deny_or_accept_maintencance_report_for_admin(maintencance_report_ID): 
        pass

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

    def fetch_all_incomplete_maintenance_reports(maintencance_report_ID) -> list:
        pass

