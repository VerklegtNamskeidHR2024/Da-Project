class maintenance_report_logic_manager:
    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper
    def sanity_check_maintencance_report(maintencance_report):
        pass

    def add_maintencance_report_to_storage(maintencance_report):
        pass

    def edit_maintencance_report(maintencance_report):
        pass

    def fetch_maintencance_report_from_storage(maintencance_report_ID):
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
        # debug
        print('in get_all_pending_m_r function brodi')
        pending_reports = []
        list_of_all_reports = self.Storage_Layer_Wrapper.get_all_maintenance_report()
        print('list_of_all_reports')
        print(list_of_all_reports)
        for report in list_of_all_reports:
            if report.report_status == 'Pending':
                pending_reports.append(report)
        if not pending_reports:
            return('No pending Reports')
        else:
            return pending_reports

    def fetch_all_closed_maintencance_reports(maintencance_report_ID) -> list:
        pass

    def fetch_all_incomplete_maintenance_reports(maintencance_report_ID) -> list:
        pass

