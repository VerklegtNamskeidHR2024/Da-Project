#from UI_Layer.start_menu_ui_layer import main
from UI_Layer.start_menu_ui_layer import Main_Menu

def show_ascii_art_hq():
        # print("                                            ===================    "
        # "                                                   |   NaN Air HQ  |     "  
        # "   ___________      .           : : : :            |     _____     |     "                                          
        # "    _\_(*)_/_   ___(*)___       : : : :       o o  |     | | |     | _ , "
        # "_______|-|_________/-\__________   :     _____|_|__|_____| | |_____| o-o")
        

        print("{:>61}".format("==================="))
        print("{:>44}{:>13}{:>3}".format("|", "NaN Air HQ", "|"))
        print("{:>14}{:>7}{:>15}{:>8}{:>10}{:>6}".format("___________", ".", ": : : :", "|", "_____","|"))
        print("{:>13}{:>12}{:>11}{:>5}{:>3}{:>10}{:>6}{:>4}".format("_\_(*)_/_", "___(*)___", ": : : :", "o o", "|", "| | |", "|", "_ ,"))
        print("{:0}{:>1}{:>31}".format("_______|-|_________/-\__________", ":", "_____|_|__|_____| | |_____| o-o"))
        pass


def select_user_for_system():
    # select a user for the system to use
    return_user = ""
    while return_user == "":
        print()
        print("Welcome to the NaN Air Properties and Staff System!")
        print("-" * 70)
        show_ascii_art_hq()
        print("-" * 70)
        print("Log in as?")
        print("1. Admin")
        print("2. Manager")
        print("3. Employee")
        print()
        print("Universal System Commands:")
        print("{:>15}".format("> Go Back: b, B"))
        print("{:>15}".format("> Log Out: log"))
        print("{:>18}".format("> Quit System: q, Q"))
        print("-" * 70)

        user_action = input("Select a Profile: ")
        match user_action:
            case "1":
                return_user = "Admin"
            case "2":
                return_user = "Manager"
            case "3":
                return_user = "Employee"
            case "q" | "Q":
                print("Departing from NaN Air, Thank you for Visiting!")
                return
            case _:
                print("No User Found, Please Try Again.")
    return return_user
    
def select_location_for_system():
    # select location for system to use 
    return_location = ""
    while return_location == "":
        print()
        print("{:0}{:>3}{:>8}{:>7}{:>11}".format("1. Reykjavik", "|", "2. Nuuk", "|", "3. Kulusuk"))
        print()
        print("{:0}{:>4}{:>12}{:>3}{:>16}".format("4. Torshavn", "|", "5. Tingwall", "|", "6. Longyearbyen"))
        print()

        user_action = input("Select a Location: ")
        match user_action:
            case "1":
                return_location = "Reykjavik"
            case "2":
                return_location = "Nuuk"
            case "3":
                return_location = "Kulusuk"
            case "4":
                return_location = "Torshavn"
            case "5":
                return_location = "Tingwall"
            case "6":
                return_location = "Longyearbyen"
            case "b" | "B":
                return 
            case "q" | "Q":
                print("Departing from NaN Air, Thank you for Visiting!")
                return
            case _:
                print("No Location Found, Please Try Again.")
    return return_location

def main():
    selected_user = select_user_for_system()
    selected_location = select_location_for_system()
    main = Main_Menu(selected_user, selected_location)
    main.start_point()

if __name__ == "__main__":
    main()