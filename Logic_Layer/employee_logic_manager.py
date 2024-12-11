class employee_logic_manager:
    
    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper
        
        #from Logic_Layer.work_request_logic_manager import work_request_logic_manager
        #from Logic_Layer.maintenance_report_logic_manager import maintenance_report_logic_manager

    # Might not implement
    def get_all_admins(self) -> list:
        all_admins = self.Storage_Layer_Wrapper.get_all_admins()
        return all_admins 

    # Might not implement
    def get_all_managers(self) -> list:
        all_managers = self.Storage_Layer_Wrapper.get_all_managers()
        return all_managers 
    

    def get_manager_by_id(self, staff_id: str) -> object: 
        all_managers = self.Storage_Layer_Wrapper.get_all_managers()
        for manager in all_managers:
            if manager.staff_id == staff_id:
                return manager

    # Might not implement
    def get_all_employees(self) -> list:

        all_employees = self.Storage_Layer_Wrapper.get_all_employees()
        return all_employees


    def get_employee_by_id(self, staff_id: str) -> object:
        all_employees = self.Storage_Layer_Wrapper.get_all_employees()
        for employee in all_employees:
            if employee.staff_id == staff_id:
                return employee

    def get_all_employees_at_location(self, location) -> list:
        employees_sorted_list = []

        all_employees = self.Storage_Layer_Wrapper.get_all_employees()

        for employee in all_employees:
            if employee.location == location:
                employees_sorted_list.append(employee)

        return employees_sorted_list
    

    
    def get_highest_ID(self) -> str:
        highestID = -1
        list_of_all_employees = self.get_all_employees()
        for employee in list_of_all_employees:
            stripped_ID = employee.staff_id[1:]
            if int(stripped_ID) > highestID:
                highestID = int(stripped_ID)
        highestID += 1

        new_employee_id = 'E' + str(highestID)
        return new_employee_id    

        
    def add_new_employee_to_storage(self,employee):
        list_of_all_employees = self.get_all_employees()
        new_employee_id = self.get_highest_ID()
        employee.set_staff_id(new_employee_id)
        list_of_all_employees.append(employee)
        self.Storage_Layer_Wrapper.write_to_file_employee(list_of_all_employees)


    def edit_employee_info(self, employee: object):
        all_employees = self.Storage_Layer_Wrapper.get_all_employees()
        for position, staff in enumerate(all_employees):
            if staff.staff_id == employee.staff_id:
                all_employees[position] = employee
        self.Storage_Layer_Wrapper.write_to_file_employee(all_employees)
        


    def fetch_employee_from_storage(self, social_security_number) -> object:
        employee_list = self.get_all_employees()
        for employee in employee_list:
            if employee.social_security_number == social_security_number:
                return employee
        return "Employee is not in the system"           

    #def fetch_all_work_request_for_employee(self, work_request_ID) -> list:
    def fetch_all_work_request_for_employee(self, staff_id) -> list:
        work_request_list = self.Storage_Layer_Wrapper.get_all_work_requests()
        work_request_by_employee = []
        for wr in work_request_list:
            if wr.staff_id == staff_id:
                work_request_by_employee.append(wr)
        return work_request_by_employee
        

    def fetch_all_maintenance_reports_for_employee(self, staff_id) -> list:
        maintenance_reports_list = self.Storage_Layer_Wrapper.get_all_maintenance_reports()
        maintenance_reports_by_employee = []
        for mr in maintenance_reports_list:
            if mr.staff_id == staff_id:
                maintenance_reports_by_employee.append(mr)
        return maintenance_reports_by_employee
    
    def sanity_check_employee_name(self, name) -> bool:
 
        for chr in name:
            if chr.isalpha() or chr.isspace():
                pass
            else:
                return False
        return True
    
    def sanity_check_ssn(self, ssn) -> bool:

        if len(ssn) == 10:
            return True
        else:
            return False
        
    def sanity_check_phone_number(self, phone_number) -> bool:

        if len(phone_number) == 7:
            return True
        else:
            return False
        
    def sanity_check_email(self, email) -> bool:
        if "@" in email:
            return True
        else:
            return False
        
    def sanity_check_for_employee_location(self, location) -> bool:
        location_list = self.Storage_Layer_Wrapper.get_all_locations()

        for loc in location_list:

            if loc.location == location:
                return True
            return False

    def sanity_check_staff_id(self, rank: str, staff_id: str) -> bool:
        if rank == "Admin":
            all_admins = self.Storage_Layer_Wrapper.get_all_admins()
            for admin in all_admins:
                if admin.staff_id == staff_id:
                    return True
            return False 
    
        if rank == "Manager":
            all_managers = self.Storage_Layer_Wrapper.get_all_managers()
            for manager in all_managers:
                if manager.staff_id == staff_id:
                    return True
            return False
            
        if rank == "Employee":
            all_employees = self.Storage_Layer_Wrapper.get_all_employees()
            for employee in all_employees:
                if employee.staff_id == staff_id:
                    return True    
            return False 

