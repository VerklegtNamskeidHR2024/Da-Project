class maintenance_report_UI_menu:
    def __init__(self,logic_wrapper, rank):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
    
    def display_maintenance_report(self):
     if self.rank == "admin" or "manager":
        print("1. pending reports ")
        print("2. closed reports")
        user_choice = input("choose: ")
        if user_choice == "1":
           #need to put a code here that puts the list of pending reports
           report_id = int(input("Enter report ID: "))
           #after putting the report_id nedded decription of the report 
           print("1. Accept")
           print("2. Deny")
           choice = int(input("choose"))
           if choice == "1":
              print("report has been accpeted")
           elif choice == 2:
              print("report has been denyed ") 
           else:
              print("invaild number")
        elif user_choice == "2":
            #list of all closed reports here
        else:
           print("invaild choice")
           
           
     elif self.rank == "Employee":
         print("1. Create maintenance reports:")
         print("2. Incomplete maintenance reports:")
         user_choice == int(input("Select an option: "))
         if user_choice == "1":
            print("new maintenace report")
            report_name = input("Enter a nane for report: ")
            Property_ID = int(input("Enter properity ID: "))
            Employee_ID = int(input("Enter employee ID: "))
            #if nedded Contractor = input("Contractor name")
            scheduled = input ("")
            work_done = input("what maintenance was done")
            report_status = input("pending or finsihed")
            price = int(input("enter a price"))
            work_request_ID = int(input("Enter ID of the work request in progress: "))
         elif user_choice == "2":
            print("incomplete maintenance reports")
            #here needs to be all incomplate maintenance imports 
            report_id = int(input("Enter report ID: "))
            #the reports id incomplte reports
            edit_maintenance = int(input("1. Edit maintenance report: "))
            if edit_maintenance == "1":
               print("pending maintenance reports")
               print("edit maintenance report 2")
                """Property ID: (1503) 
                    Staff ID: (26)
                    Contractor ID: (x)
                    Scheduled: yes
                    Work done: Clean windows
                    Status: pending
                    Price: 20.000kr 
                    Report ID: (2)"""

                
               
            





