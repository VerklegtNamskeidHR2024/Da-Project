class StartMenu:
    def __init__(self, role: str="", location: str=""):
        self.role = role
        self.location = location    

    def show_ascii_art_hq():
        print("{:>61}".format("==================="))
        print("{:>44}{:>13}{:>3}".format("|", "NaN Air HQ", "|"))
        print("{:>14}{:>7}{:>15}{:>8}{:>10}{:>6}".format("___________", ".", ": : : :", "|", "_____","|"))
        print("{:>13}{:>12}{:>11}{:>5}{:>3}{:>10}{:>6}{:>4}".format("_\_(*)_/_", "___(*)___", ": : : :", "o o", "|", "| | |", "|", "_ ,"))
        print("{:0}{:>1}{:>31}".format("_______|-|_________/-\__________", ":", "_____|_|__|_____| | |_____| o-o"))

    def show_role_options():
        print()
        print("Welcome to the NaN Air Properties and Staff System!")
        print("-" * 70)
        pass
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
            
    def show_location_options():
        print()
        print("{:0}{:>3}{:>8}{:>7}{:>11}".format("1. Reykjavík", "|", "2. Nuuk", "|", "3. Kulusuk"))
        print()
        print("{:0}{:>4}{:>12}{:>3}{:>16}".format("4. Þórshöfn", "|", "5. Tingwall", "|", "6. Longyearbyen"))
        print()

    def set_role(self, role: str=""): 
        self.role = role
        
    def set_location(self, location: str=""):
        self.location = location

    def get_role(self):
         return self.role
        
    def get_location(self):
        return self.location

        

         
login_choice = StartMenu()
while (login_choice != "q" and login_choice != "Q"):
    login_choice = input("Select an Option: ")

    if login_choice == "1" or login_choice == "admin" or login_choice == "Admin":
        location_choice = input("Select a location: ")

    elif login_choice == "2" or login_choice == "manager" or login_choice == "Manager":
    elif login_choice == "3" or login_choice == "employee" or login_choice == "Employee":

