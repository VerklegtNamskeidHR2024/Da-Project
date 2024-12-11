import json
from Model_Classes.maintenance_report_model import MaintenanceReport

class maintenance_report_storage:
    def __init__(self):
        """Constructor for maintenance_report_storage"""
        pass

    def get_all_maintenance_reports(self) -> list[MaintenanceReport]:
        """Gets all maintenance reports from the file"""
        with open('Data/maintenance_report_storage.json', 'r') as maintenance_report_file:
            maintenance_report_data = json.load(maintenance_report_file)
        maintenance_report_list = [MaintenanceReport(**data) for data in maintenance_report_data]
        return maintenance_report_list
    '''    
    def write_to_file_maintenance_report(self, list_of_maintenance_reports: list[MaintenanceReport]):
        """Writes the list of maintenance reports to the file"""
        dict_of_maintenance_reports = [maintenance_report.to_dict() for maintenance_report in list_of_maintenance_reports]
        with open('Data/maintenance_report_storage.json', 'w') as maintenance_report_file:
            json.dump(dict_of_maintenance_reports, maintenance_report_file, indent=4) 
    '''

    def write_to_file_maintenance_report(self, list_of_maintenance_reports: list[MaintenanceReport]):
        """Writes the list of maintenance reports to the file"""
        # Read the current data from the file
        with open('Data/maintenance_report_storage.json', 'r') as maintenance_report_file:
            current_data = json.load(maintenance_report_file)
        
        # Write the current data to a temp file
        with open('Data/maintenance_report_storage_temp.json', 'w') as temp_file:
            json.dump(current_data, temp_file, indent=4)
        
        # Write the new data to the original file
        dict_of_maintenance_reports = [maintenance_report.to_dict() for maintenance_report in list_of_maintenance_reports]
        with open('Data/maintenance_report_storage.json', 'w') as maintenance_report_file:
            json.dump(dict_of_maintenance_reports, maintenance_report_file, indent=4)