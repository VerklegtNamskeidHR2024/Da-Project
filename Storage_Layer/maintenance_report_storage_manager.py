import json
from Model_Classes.maintenance_report_model import MaintenanceReport

class maintenance_report_storage:
    def __init__(self):
        pass

    def get_all_maintenance_reports(self) -> list[MaintenanceReport]:
        with open('Data/maintenance_report_storage.json', 'r') as maintenance_report_file:
            maintenance_report_data = json.load(maintenance_report_file)
        maintenance_report_list = [MaintenanceReport(**data) for data in maintenance_report_data]
        return maintenance_report_list
    
    def write_to_file_maintenance_report(self, list_of_maintenance_reports: list[MaintenanceReport]):
        dict_of_maintenance_reports = [maintenance_report.to_dict() for maintenance_report in list_of_maintenance_reports]
        with open('Data/maintenance_report_storage.json', 'w') as maintenance_report_file:
            json.dump(dict_of_maintenance_reports, maintenance_report_file, indent=4)