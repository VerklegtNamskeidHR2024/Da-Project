import sys
import time
import os

from Logic_Layer.logic_layer_wrapper import Logic_Layer_Wrapper

from UI_Layer.employee_ui_layer import employee_UI_menu
from UI_Layer.location_ui_layer import location_UI_menu
from UI_Layer.contractor_ui_layer import contractor_UI_menu
from UI_Layer.maintenance_report_ui_layer import maintenance_report_UI_menu
from UI_Layer.work_request_ui_layer import work_request_UI_menu
from UI_Layer.property_ui_layer import property_UI_menu

from prettytable import PrettyTable 
from colorama import Fore, Style, init
init()

class Main_Menu:
    def __init__(self, rank: str="", location: str="", staff_id: str=""):
        # calls the select function for what user you want to see the system as and, then - 
        # calls the location select function

        self.logic_wrapper = Logic_Layer_Wrapper(rank, location, staff_id)
        
    
        rank = self.select_user_for_system()
        # calls the function to get the staff id
        staff_id = self.enter_and_validate_staff_id(rank)
        # calls the function to get the location
        if rank == "Admin":
            location = self.select_location_for_system()
        else:
            location = self.assigned_location_for_system(rank, staff_id)
        # sets the rank, location and staff id
        self.staff_id = staff_id
        self.rank = rank
        self.location = location
 

        
        self.employee_UI_menu = employee_UI_menu(self.logic_wrapper, self.rank, self.location, self.staff_id)
        self.location_UI_menu = location_UI_menu(self.logic_wrapper, self.rank, self.location, self.staff_id)
        self.contractor_UI_menu = contractor_UI_menu(self.logic_wrapper, self.rank, self.location, self.staff_id) 
        self.maintenance_report_UI_menu = maintenance_report_UI_menu(self.logic_wrapper, self.rank, self.location, self.staff_id)
        self.work_request_UI_menu = work_request_UI_menu(self.logic_wrapper, self.rank, self.location, self.staff_id)
        self.property_UI_menu = property_UI_menu(self.logic_wrapper, self.rank, self.location, self.staff_id)


    def start_point(self):
        """Starts the main menu for the system"""
        # calls the user home page logistics
        user_home_page = self.user_home_page_logistics()
        if user_home_page == "q":
            self.quit_system_message()


    def quit_system_message(self):
        """Prints out a message when the user quits the system"""
        print("Departing from NaN Air, Thank you for Visiting!")
        quit_string = "Departing from NaN Air, Thank you for Visiting!"

    def clear_screen(self):
        ''' Clears the screen '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_ascii_art_hq(self):
        """Prints out the ASCII art for the NaN Air HQ"""
        # prints out the ascii art for the NaN Air HQ
        print("{:>61}".format("==================="))
        print("{:>44}{:>13}{:>3}".format("|", "NaN Air HQ", "|"))
        print("{:>14}{:>7}{:>15}{:>8}{:>10}{:>6}".format("___________", ".", ": : : :", "|", "_____", "|"))
        print("{:>13}{:>12}{:>11}{:>5}{:>3}{:>10}{:>6}{:>4}".format("_\\_(*)_/_", "___(*)___", ": : : :", "o o", "|", "| | |", "|", "_ ,"))
        print("{:0}{:>1}{:>31}".format("_______|-|_________/-\\__________", ":", "_____|_|__|_____| | |_____| o-o"))

    def fun_print(self, text_to_print = "i need input bro", delay_in = 0.05):
        """send me a string ;)"""
        delay = delay_in
        print(text_print)
        # checks if the delay is a float or an integer
        start = len(text_to_print)
        text_print = ""
        # prints out the text with a delay
        for i, char in enumerate(text_to_print):
            text_print = text_to_print[:i+1] + '*' * (start - i - 1)
            
            print(text_print, end="\r", flush=True)
            
            time.sleep(delay)  
        print()


    def create_location_table(self):
        """Prints out a table of available locations for the user to select. """
        # prints out the table of locations for the user to select
        locations_table = PrettyTable()
        locations_table.field_names = ['ID',"Country", "Location Name"]
        locations_table.add_row(['1',"Iceland", "Reykjavik"])
        locations_table.add_row(['2',"Greenland", "Nuuk"])
        locations_table.add_row(['3',"Greenland", "Kulusuk"])
        locations_table.add_row(['4',"Faroe Islands", "Thorshofn"])
        locations_table.add_row(['5',"Shetland Islands", "Tingwall"])
        locations_table.add_row(['6',"Svalbard", "Longyearbyen"])
            
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        locations_table.border = True
        locations_table.junction_char = f"{border_color}+{reset_color}"
        locations_table.horizontal_char = f"{border_color}-{reset_color}"
        locations_table.vertical_char = f"{border_color}|{reset_color}"

        print(locations_table)
        

    def select_user_for_system(self) -> str:
        """Selects a user for the system to use"""
        '''print()
        loading = "Loading" + ("." * 20)
        for char in loading:
            sys.stdout.write(char)
            sys.stdout.flush() 
            time.sleep(0.04)
        print()'''
        self.ascii_art()
        time.sleep(2)
        self.clear_screen()

        # prints out the welcome message and the ascii art for the NaN Air HQ
        return_user = ""
        while return_user == "":
            print()
            print("{:>70}".format(Fore.BLUE + "[ Welcome to the NaN Air Properties and Staff System! ]" + Style.RESET_ALL))
            print("-" * 80)
            self.show_ascii_art_hq()
            # prints out the log in options for the user
            print("-" * 70)
            print("Log in as?")
            print("1. Admin")
            print("2. Manager")
            print("3. Employee")
            print()
            print("Universal System Commands (Not Applicable During Log-In)")
            print("_" * 60)
            print()
            print("{:>18}".format("Back - [ b, B ]"))
            print("{:>18}".format("Quit - [ q, Q ]"))
            print("-" * 80)
            # user selects a profile
            user_action = input("Select a Profile: ").lower()
            # checks the user input
            match user_action:
                case "1":
                    return_user = "Admin"
                    break
                case "2":
                    return_user = "Manager"
                    break
                case "3":
                    return_user = "Employee"
                    break
                case _:
                    print(Fore.RED + "No User Found, Please Try Again." + Style.RESET_ALL)
                    time.sleep(1)
                    self.clear_screen()
        return return_user
    

    def enter_and_validate_staff_id(self, rank) -> str:
        """Enter and validate the staff ID for the user"""
        print("-" * 80)
        is_staff_id_valid = False
        # Get the staff ID from the user
        while is_staff_id_valid is False:
            staff_id = input("Enter Your Staff ID: ")
            is_staff_id_valid = self.logic_wrapper.sanity_check_staff_id(rank, staff_id)
            if is_staff_id_valid is False: 
                print(Fore.RED + "ID Does Not Exist In The System, Please Try Again." + Style.RESET_ALL)
                time.sleep(0.5)
                self.clear_screen
        return staff_id
    

    def select_location_for_system(self) -> str:
        """Select a location for the system to use"""
        self.clear_screen()
        return_location = ""
        # prints out the table of locations
        while return_location == "":
            self.clear_screen()
            print("{:>60}".format(Fore.BLUE + "[ Welcome to the NaN Air Properties and Staff System! ]" + Style.RESET_ALL))
            print("-" * 80)
            self.show_ascii_art_hq()
            print("-" * 80)
            location_table = PrettyTable()
            location_table.field_names = ['ID',"Location", "Country"]
            location_table.add_row(['1',"Iceland", "Reykjavik"])
            location_table.add_row(['2',"Greenland", "Nuuk"])
            location_table.add_row(['3',"Greenland", "Kulusuk"])
            location_table.add_row(['4',"Faroe Islands", "Thorshofn"])
            location_table.add_row(['5',"Shetland Islands", "Tingwall"])
            location_table.add_row(['6',"Svalbard", "Longyearbyen"])

            border_color = Fore.BLUE
            reset_color = Style.RESET_ALL
            location_table.border = True
            location_table.junction_char = f"{border_color}+{reset_color}"
            location_table.horizontal_char = f"{border_color}-{reset_color}"
            location_table.vertical_char = f"{border_color}|{reset_color}"
            print(location_table)
            print("-" * 80)
            # user selects a location
            user_action = input("Select a Location: ").lower()
            match user_action:
                case "1":
                    return_location = "Reykjavik"
                case "2":
                    return_location = "Nuuk"
                case "3":
                    return_location = "Kulusuk"
                case "4":
                    return_location = "Thorshofn"
                case "5":
                    return_location = "Tingwall"
                case "6":
                    return_location = "Longyearbyen"
                case _:
                    print(Fore.RED + "No Location Found, Please Try Again." + Style.RESET_ALL)
                    time.sleep(1)
                    self.clear_screen
        self.clear_screen()
        return return_location


    def assigned_location_for_system(self, rank: str, staff_id: str) -> str:
        """Get the location for the user based on their rank and staff ID"""
        # Get the location based on the rank and staff ID
        if rank == "Manager":
            manager = self.logic_wrapper.get_manager_by_id(staff_id)
            manager_location = manager.location
            return manager_location
        
        if rank == "Employee":
            employee = self.logic_wrapper.get_employee_by_id(staff_id)
            employee_location = employee.location
            return employee_location
        


    def display_menu_items(self):
        """Displays the menu items for the user"""
        # Displays the menu items for the user
        print()
        print(f"Current Location - {self.location}")
        print()
        # Displays the home page menu items
        print(f" {self.rank} - Home Page")
        print("-" * 80)
        print("1. Properties")
        print("2. Work Requests")
        print("3. Employees")
        print("4. Contractors")
        print("5. Maintenance Reports")
        # Only displays the location option if the user is an admin or manager
        if self.rank != "Employee":
            print("6. Locations")
        print("_" * 80)
        print()
        print("{:>10}".format("Quit - [ q, Q ]"))
        print("-" * 80)

        user_action = input("Select an Option: ").lower()
        return user_action

    def user_home_page_logistics(self):
        """Manages the user home page logistics"""

        # Calls the sub menus
        self.clear_screen()
        user_action = ""
        # user_action = self.display_menu_items()
        while user_action != "q":
            user_action = user_action = self.display_menu_items()
            match user_action:
                case "1":
                    # Calls the property UI menu
                    user_action = self.property_UI_menu.start_point_property_UI()
                case "2":
                    # Calls the work request UI menu
                    user_action = self.work_request_UI_menu.start_point_work_requests_UI()
                case "3":
                    # Calls the employee UI menu
                    user_action = self.employee_UI_menu.start_point_employee_UI()
                case "4":
                    # Calls the contractor UI menu
                    user_action = self.contractor_UI_menu.start_point_contractor_UI()
                case "5":
                    # Calls the maintenance report UI menu
                    self.maintenance_report_UI_menu.start_point_maintenance_reports_UI()
                case "6" if self.rank != "Employee":
                    # This option is only displayed if the user is an admin or manager
                    user_action = self.location_UI_menu.start_point_location_UI()
                case "q":
                    # Quits the system
                    return "q"
                case _:
                    # If the user enters an invalid input
                    print(Fore.RED + "Wrong Input" + Style.RESET_ALL)
                    time.sleep(1)
                    self.clear_screen()
                    continue
        self.clear_screen()
        return user_action
    
    def ascii_art(self):
        ascii_art = """
                                                                                                                                                                    
                                                                                                                                                                    
                                                                                                                                                                  
                            """ + Style.BRIGHT + """   $&&&&&&&&&&&&&&                         &&&&     :&&&   X&    &$  ;&&&    &  """ + Style.RESET_ALL + """                                                        
                        """+ Style.BRIGHT +"""   &&&""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&                   """ + Style.BRIGHT + """ &       +&    X&   &  &   &        &                                                          
                        &&""" + Fore.RED + Style.BRIGHT + """x;;;;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&                """ + Style.BRIGHT + """ &&&&&   &&&&&&&&+   &&     &&&&    &                                                          
                      &&""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&              """ + Style.BRIGHT + """      && &&         &&&&        &&  &                                                          
                    &&""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&            """ + Style.BRIGHT + """ &&&&&&   &&&&&&&  &    &  &&&&&&   &                                                          
                   &&""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&                                                                                                          
                  &""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&&&                                                                                                         
                 &""" + Fore.RED + Style.BRIGHT + """+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""X&&&&&&&&&""" + Fore.BLUE + Style.BRIGHT + """+""" + Style.RESET_ALL + Style.BRIGHT + """&               &&&&&&&&&&       &&&&&&&&&&     &&&&&&&&&&&&&&&&&&&           X&&&&&&&&&&&&&&&&&&&&&     
                &&""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&&&&""" + Fore.BLUE + Style.BRIGHT + """+X""" + Style.RESET_ALL + Style.BRIGHT + """&              &&       &&&  &&&        ;&   &&                   &&&    X&&&;               &&&        
                &""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&&&&&""" + Fore.BLUE + Style.BRIGHT + """+x&""" + Style.RESET_ALL + Style.BRIGHT + """X            && ;;;;;;;  &&&&  ;;;;;;;  &: && +;;;;;;;   ;;;;;;;;. &&&&&&  :;;;;;;;;;;   &&&           
               &&""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&&&&&&""" + Fore.BLUE + Style.BRIGHT + """++x""" + Style.RESET_ALL + Style.BRIGHT + """&            &X  ;;;;;;;; &&&  ;;;;;;;;: &$&& ;;;;;;;;;: : ;;;;;;;;;  X  ;;;;;;;;;;;.  &&&              
               &""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;;;;;;;;;+""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&&&&&&""" + Fore.BLUE + Style.BRIGHT + """++++""" + Style.RESET_ALL + Style.BRIGHT + """&           &&  ;;;;;;;;;  &. ;;;;;;;;;; &&& .;;;;;;;;;;: & .;;;;;;;;;;;;;;;;;;;;   &&&                 
               &""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&&&&&&&""" + Fore.BLUE + Style.BRIGHT + """+++++""" + Style.RESET_ALL + Style.BRIGHT + """&          ;&: ;;;;;;;;;; $ ;;;;;;;;;;; &&$ ;;;;;;;;;;;;: &$ ;;;;;;;;;;;;;;;;  x&&&                    
               &""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&&&&&&&&""" + Fore.BLUE + Style.BRIGHT + """++++++""" + Style.RESET_ALL + Style.BRIGHT + """&          && ;;;;;;;;;;;  ;;;;;;;;;;;; && ;;;;;;;.;;;;;;: &  :;;;;;;;;;;;  $&&&                       
               &&""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&&&&&&&&X""" + Fore.BLUE + Style.BRIGHT + """+++++++""" + Style.RESET_ALL + Style.BRIGHT + """&         X&  ;;;;;;;;;;;;;;;;;;;;;;;;; & .;;;;;;  ;;;;;;;::;;;;;;;;;;;;;; &&&                         
                &""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&&&&&&&&""" + Fore.BLUE + Style.BRIGHT + """+++++++++""" + Style.RESET_ALL + Style.BRIGHT + """&&         && ;;;;;;; ;;;;;;;;;; +;;;;;;   ;;;;;;  & ;;;;;;;;;;;;;;;;;;;;;;;  &&                        
                &&""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&&&&&&&&""" + Fore.BLUE + Style.BRIGHT + """++++++++++++""" + Style.RESET_ALL + Style.BRIGHT + """&         && .;;;;;;  ;;;;;;;;;  ;;;;;;;  ;;;;;;. &&  ;;;;;;;;;;;;  :;;;;;;;;;  &&                      
                 &""" + Fore.RED + Style.BRIGHT + """;;;;;;;;;;;;""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&&&&&&""" + Fore.BLUE + Style.BRIGHT + """++++++++++++++++""" + Style.RESET_ALL + Style.BRIGHT + """&          && ;;;;;;:  :;;;;;;;   :;;;;;;..;;;;;;   ;;;;;;;;;;;:  &&&  ;;;;;;;;;: &&&                    
                  &""" + Fore.RED + Style.BRIGHT + """;;;;;;;+""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&&&&""" + Fore.BLUE + Style.BRIGHT + """+++++++++++++++++++++++""" + Style.RESET_ALL + Style.BRIGHT + """&;         && :;;;;;; &$ ;;;;;;  & .;;;;;;;;;;;;; ;;;;;;;;;;;;;;; :&& && .;;;;;;;;;  &&                   
                   &""" + Fore.RED + Style.BRIGHT + """;+""" + Style.RESET_ALL + Style.BRIGHT +"""&&&&&""" + Fore.BLUE + Style.BRIGHT + """+++++++++++++++++++++++++++++;""" + Style.RESET_ALL + Style.BRIGHT + """&           &$ ;;;;;;: && +;;;. &&&  ;;;;;;;;;;;;;;;;;;;;;;:;;;;;;; .&& &&+ ;;;;;;;;;;  &&                 
                    """ + Style.BRIGHT +""" &&""" + Fore.BLUE + Style.BRIGHT + """+++++++++++++++++++++++++++++++++""" + Style.RESET_ALL + """&&           && ;;;;;;; &&&&X;+&&&& &; ;;;;;;;;;;;;;;;;;;;:   .;;;;;;;  &&  &&  ;;;;;;;;;: &&&               
                    """ + Style.BRIGHT +"""  &&""" + Fore.BLUE + Style.BRIGHT + """+++++++++++++++++++++++++++++""" + Style.RESET_ALL + """X&;            &+ ;;;;;;  &X  .;;     && ;;;;;;;;;;;;;;;;.  &&&& ;;;;;;;; .&&  &&X ;;;;;;;;;;  &&              
                    """ + Style.BRIGHT +"""    &&""" + Fore.BLUE + Style.BRIGHT + """+++++++++++++++++++++++++""" + Style.RESET_ALL + """&&              && ;;;;;;  &&           && ;;;;;;;;;;;;;   &&&   && ;;;;;;;;  &&   &&  ;;;;;;;;;; +&&            
                    """ + Style.BRIGHT +"""      +&&x""" + Fore.BLUE + Style.BRIGHT + """++++++++++++++++++""" + Style.RESET_ALL + """&&&               x&.      ;&&X            && ;;;;;;;    ;&&&&       &&   ...... :&&   :&&X   :..::..  &&;         
                    """ + Style.BRIGHT +"""          &&&&&$x++++$&&&&&                   &&&&&&&&&&               && :;::   &&&&&             &&&&&&&&&&&&&X     &&&&&&&&&&&&&&&&&    
                     """ + Style.BRIGHT +"""                                                                      &&&&&&&&&&                                                               
        """
        print(ascii_art)
            