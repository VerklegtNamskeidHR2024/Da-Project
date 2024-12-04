class maintenance_report_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location

    def start_point_maintenance_reports_UI(self):
       # when this class is called it starts here
       # call other functions in class from here
       pass
    
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
            pass
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
               print("maintenance report 2")
               print("""Property ID: (1503) 
                     Staff ID: (26)
                     Contractor ID: (x)
                     Scheduled: yes
                     Work done: Clean windows
                     Status: pending
                     Price: 0kr 
                     Report ID: (2)""")
               user_input = input("1. mark as ready: ")
               user_input = input("2. edit report details: ")
               if user_input == "1":
                  # maybe a code/function that let know the report ready 
                  print("report has been marked ready")
               elif user_input == "2":
                  pass
                  
                  
               
            





