#from employee_storage_manager import employee_storage
class employee_logic_manager:
    
    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

        #self.employee_list = fetch_employees #needs more information from employee storage

        return

    def fetch_all_employee_in_storage(self,location):
        #needs to add read json
        return self.Storage_Layer_Wrapper.get_all_employee()

    def sanity_check_employee(employee, display):
        pass
        
    def add_new_employee_to_storage(self,employee): 
        pass

    def edit_existing_employee_in_storage(employee):
        pass
    def fetch_employee_from_storage(self, SSN):
        for self.employee in self.employee_list:
            if self.SSN in self.employee:
                return None
           # else

    def fetch_all_work_request(work_request_ID) -> list:
        pass
    def fetch_all_maintenance_reports(maintenance_report_ID) -> list:
        pass