class employee_logic_manager:
    
    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper
        from Logic_Layer.work_request_logic_manager import work_request_logic_manager
        from Logic_Layer.maintenance_report_logic_manager import maintenance_report_logic_manager


    def get_all_employees(self) -> list:
        employees_list = []

        all_employees = self.Storage_Layer_Wrapper.get_all_employee()

        for employee in all_employees:
            employees_list.append(employee)

        return employees_list

    def get_all_employees_at_location(self, location) -> list:
        employees_sorted_list = []

        all_employees = self.Storage_Layer_Wrapper.get_all_employee()

        for employee in all_employees:
            if employee.location == location:
                employees_sorted_list.append(employee)

        return employees_sorted_list
    

    
    def get_highest_ID(self) -> str:
        highestID = -1
        list_of_all_employees = self.get_all_employees()
        for employee in list_of_all_employees:
            stripped_ID = employee.employee_id[1:]
            if int(stripped_ID) > highestID:
                highestID = int(stripped_ID)
        highestID += 1

        new_employee_id = 'E' + str(highestID)
        return new_employee_id    

    def sanity_check_employee(employee, display):
        pass
        
    def add_new_employee_to_storage(self,employee):
        list_of_all_employees = self.get_all_employees()
        new_employee_id = self.get_highest_ID()
        employee.set_employee_id(new_employee_id)
        list_of_all_employees.append(employee)
        self.Storage_Layer_Wrapper.write_to_file_employee(list_of_all_employees)

    def edit_existing_employee_in_storage(self, employee):
        pass
    def fetch_employee_from_storage(self, social_security_number) -> object:
        employee_list = self.get_all_employees()
        for employee in employee_list:
            if employee.social_security_number == social_security_number:
                return employee
        return "Employee is not in the system"           

    #def fetch_all_work_request_for_employee(self, work_request_ID) -> list:
    def fetch_all_work_request_for_employee(self, social_security_number) -> list:
        work_request_list = self.work_request_logic_mananger.get_all_work_requests()
        work_request_by_employee = []
        for wr in work_request_list:
            if wr.staff_id == social_security_number:
                work_request_by_employee.append(wr)
        return work_request_by_employee
        

    def fetch_all_maintenance_reports_for_employee(self, social_security_number) -> list:
        maintenance_reports_list = self.maintenance_report_logic_mananger.get_all_maintenance_reports()
        maintenance_reports_by_employee = []
        for mr in maintenance_reports_list:
            if mr.staff_id == social_security_number:
                maintenance_reports_by_employee.append(mr)
        return maintenance_reports_by_employee