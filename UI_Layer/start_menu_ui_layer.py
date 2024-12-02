class StartMenu:
    def __init__(self, log_in_choice: str, location_choice: str):
        self.log_in_choice = log_in_choice
        self.location_choice = location_choice    

    def show_ascii_nan_hq_monstrosity(self):
            print("{:>61}".format("==================="))
            print("{:>44}{:>13}{:>3}".format("|", "NaN Air HQ", "|"))
            print("{:>14}{:>7}{:>15}{:>8}{:>10}{:>6}".format("___________", ".", ": : : :", "|", "_____","|"))
            print("{:>13}{:>12}{:>11}{:>5}{:>3}{:>10}{:>6}{:>4}".format("_\_(*)_/_", "___(*)___", ": : : :", "o o", "|", "| | |", "|", "_ ,"))
            print("{:0}{:>1}{:>31}".format("_______|-|_________/-\__________", ":", "_____|_|__|_____| | |_____| o-o"))

    def show_roles_options(self):
        log_in_choice = ""
        while (log_in_choice != "q" and log_in_choice != "Q"):
            print()
            print("Welcome to the NaN Air Properties and Staff System!")
            print("-" * 70)

            print("-" * 70)
            print("Log in as?")
            print("1. Admin")
            print("2. Manager")
            print("3. Employee")
            print()
            print("Universal Commands:")
            print("{:>24}{:>5}".format(">Go to Home Page:", "home, Home"))
            print("{:>20}{:>5}".format(">Quit System:", "q, Q"))
            print("-" * 70)
            
            log_in_choice = input("Select an Option: ")
            if log_in_choice == "1" or log_in_choice == "admin" or log_in_choice == "Admin": 
                print()
                print("{:<1}{:>3}{:>8}{:>7}{:>11}".format("1. Reykjavík", "|", "2. Nuuk", "|", "3. Kulusuk"))
                print()
                print("{:<1}{:>4}{:>12}{:>3}{:>16}".format("4. Þórshöfn", "|", "5. Tingwall", "|", "6. Longyearbyen"))
                print()
                location_choice = input("Select a location: ")
            elif log_in_choice == "2" or log_in_choice == "manager" or log_in_choice == "Manager":
                
            elif log_in_choice == "3" or log_in_choice == "employee" or log_in_choice == "Employee":
            
    def set_roles(): 

    def set_locations():