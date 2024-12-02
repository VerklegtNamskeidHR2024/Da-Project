class StartMenu:
    def __init__(self, role: str, location_choice: str):
        self.role = role
        self.location = location_choice    

    def show_ascii_nan_hq_monstrosity(self):
            print("{:>61}".format("==================="))
            print("{:>44}{:>13}{:>3}".format("|", "NaN Air HQ", "|"))
            print("{:>14}{:>7}{:>15}{:>8}{:>10}{:>6}".format("___________", ".", ": : : :", "|", "_____","|"))
            print("{:>13}{:>12}{:>11}{:>5}{:>3}{:>10}{:>6}{:>4}".format("_\_(*)_/_", "___(*)___", ": : : :", "o o", "|", "| | |", "|", "_ ,"))
            print("{:0}{:>1}{:>31}".format("_______|-|_________/-\__________", ":", "_____|_|__|_____| | |_____| o-o"))

    def show_role_options(self):
        role = ""
        while (role != "q" and role != "Q"):
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
            
            
    def set_roles(self, role: str): 
        role = input("Select an Option: ")
        if role == "1" or role == "admin" or role == "Admin": 
            
        elif role == "2" or role == "manager" or role == "Manager":
            
        elif role == "3" or role == "employee" or role == "Employee":
    
    def set_locations(self, location_choice: str):
        print()
        print("{:0}{:>3}{:>8}{:>7}{:>11}".format("1. Reykjavík", "|", "2. Nuuk", "|", "3. Kulusuk"))
        print()
        print("{:0}{:>4}{:>12}{:>3}{:>16}".format("4. Þórshöfn", "|", "5. Tingwall", "|", "6. Longyearbyen"))
        print()
        location_choice = input("Select a location: ")
         
