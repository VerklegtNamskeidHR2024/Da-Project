class MainMenu:
    def __init__(self, rank: str="", location: str=""):
        self.rank = rank
        self.location = location    

    def show_ascii_art_hq():
        print("{:>61}".format("==================="))
        print("{:>44}{:>13}{:>3}".format("|", "NaN Air HQ", "|"))
        print("{:>14}{:>7}{:>15}{:>8}{:>10}{:>6}".format("___________", ".", ": : : :", "|", "_____","|"))
        print("{:>13}{:>12}{:>11}{:>5}{:>3}{:>10}{:>6}{:>4}".format("_\_(*)_/_", "___(*)___", ": : : :", "o o", "|", "| | |", "|", "_ ,"))
        print("{:0}{:>1}{:>31}".format("_______|-|_________/-\__________", ":", "_____|_|__|_____| | |_____| o-o"))
        pass

    def select_user_for_system(self):
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
        self.selected_user_login_choice = input("Select an Option: ")
        self.log_in_choice(self.selected_user_login_choice)

    def select_location_for_system(self):
        print()
        print("{:0}{:>3}{:>8}{:>7}{:>11}".format("1. Reykjavik", "|", "2. Nuuk", "|", "3. Kulusuk"))
        print()
        print("{:0}{:>4}{:>12}{:>3}{:>16}".format("4. Tórshavn", "|", "5. Tingwall", "|", "6. Longyearbyen"))
        print()
        self.selected_location_choice = input("Select a Location: ")
        self.location_choice(self.selected_location_choice)
    
    def log_in_choice(self):
        match self.selected_user_login_choice:
            case "1":
                self.show_admin_menu()
            case "2":
                self.show_manager_menu()
            case "3":
                self.show_employee_menu()
            else:
                print("Please Try Again.")
        
    def location_choice(self):
        match self.selected_location_choice:
            case "1":
            case "2":
            case "3":
            case "4":
            case "5":
            case "6":
            else:
                print("Please Try Again.")
    


