import json
from Model_Classes.maintenance_report_model import MaintenanceReport

class maintenance_report_storage:
    maintenance_report_list = []

    def __init__(self):
        pass
    def maintenance_report_set_ID_and_too_storage(self):
        pass
    def add_maintenance_report(self):
        pass

    def get_all_maintenance_report(self):
        with open('Data/maintenance_report_storage.json', 'r') as maintenance_report_file:
            maintenance_report_data = json.load(maintenance_report_file)
        maintenance_report_list = [MaintenanceReport(**data) for data in maintenance_report_data]
        return maintenance_report_list