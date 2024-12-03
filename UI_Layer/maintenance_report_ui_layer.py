class maintenance_report_UI_menu:
    def __init__(self,logic_wrapper):
        self.logic_wrapper = logic_wrapper
    
    def display_all_open_work_requests(self):
        """Prints out all open work requests with their ID, Name and Description """
        
        print()
        print("Work Request Menu")
        print("-" * 70)
        print()
        print("{:>20}".format("[ Open and Upcoming Work Requests ]"))
        print("{:0}{:>3}{:>8}{:>7}{:>11}".format("ID", "|", "Name", "|", "Description"))
        print("-" * 70)
        work_request_list = self.logic_wrapper.get_all_work_requests()
        for item in work_request_list:
            print("{:0}{:>3}{:>8}{:>7}{:>11}".format(
                work_request_list["work_request_id"], 
                "|", work_request_list["name"], 
                "|", work_request_list["description"]
                ))