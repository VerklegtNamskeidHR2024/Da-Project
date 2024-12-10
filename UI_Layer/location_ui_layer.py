from Model_Classes.location_model import Location
from prettytable import PrettyTable 
from colorama import Fore, Style, init

class location_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        '''Class builder'''
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location  

    def start_point_location_UI(self):
        # when this class is called it starts here
        # call other functions in class from here
        self.display_selected_location_information_printed()

        return


    def location_information(self):
        '''Information about current Location, Needs to fetch information from data storage and insert'''
        current_location = self.get_current_location()

        print()
        print("-" * 70)
        print(f"Country       | {current_location.country}")
        print(f"Location      | {current_location.location}")
        print(f"Airport       | {current_location.airport}")
        print(f"Phone Number  | {current_location.phone_number}")
        print(f"Manager       | {current_location.branch_manager}")
        print(f"Opening Hours | {current_location.opening_hours}")
        print("-" * 70) 


    def display_selected_location_information_printed(self):
        '''Shows information about current Location along with the ascii art.
        If the user is an admin It allows them to edit, add and show other locations'''
        self.location_information()
        
        if self.rank == "Admin":
            print("1) Edit location details")
            print("2) Show other locations")
            print(">Go to Home Page:", "home, Home")
            print(">Quit System:", "q, Q")
            user_choice = input("Enter a command: ")
            match user_choice:
                case "1":
                    self.display_edit_current_location()
                case "2":
                    self.display_all_locations()
        else:
            print(">Go to Home Page:", "home, Home")
            print(">Quit System:", "q, Q")
            user_choice = input("Enter a command: ")


    def display_edit_current_location(self):
        '''Shows location information along with an option to 
        change phone number, manager, amenities and opening hours'''
        current_location = self.get_current_location()
        self.location_information()

        print("1) Phone Number")
        print("2) Manager")
        print("3) Amenities") # wait with this for a bit 
        print("4) Opening Hours")
        print("-" * 70)

        edit_user_action = input("Enter Editing Option: ")
        match edit_user_action:
            case "1":
                self.change_phone_number(current_location)
                print()
            case "2":
                print("needs to be added")
                self.change_manager(current_location)
                print()
            case "3":
                print("needs to be added")
            case "4":
                self.change_opening_hours(current_location)
                print()

    def change_phone_number(self, location) -> None:
        try:
            is_valid = False
            while is_valid == False:
                phone_input = input("Enter phone number: ")
                is_valid = self.logic_wrapper.sanity_check_location("phone_number", phone_input)
                if not phone_input.isdigit() or is_valid != True:
                    print("Invalid input. Please enter numbers only.")
                else:
                    self.logic_wrapper.edit_existing_location_in_storage(location, self.location, 'phone_number', phone_input)
                    self.location_information()
        except:
            print("something went wrong")
    
    def change_manager(self, location) -> None:
        # check this out tomorrow 
        try:
            new_manager_id = input("Enter manager id: ")
            #contractor.set_contact_name(new_contact_name)
            is_valid = self.logic_wrapper.sanity_check_location("manager", new_manager_id)
            if is_valid == True:
                self.logic_wrapper.edit_existing_location_in_storage(location, self.location, 'manager', new_manager_id)
                self.location_information()
            else:
                print("Invalid input. Please try again.")
        except:
            print("something went wrong")

    def change_opening_hours(self, location) -> None:
        new_opening_hours = input("Enter opening hours: ")
        #contractor.set_contact_name(new_contact_name)
        is_valid = self.logic_wrapper.sanity_check_location("opening_hours", new_opening_hours)
        if is_valid == True:
            self.logic_wrapper.edit_existing_location_in_storage(location, self.location, 'opening_hours', new_opening_hours)
            self.location_information()
        else:
            print("Invalid input. Please try again.")
        try:
            pass
        except:
            print("something went wrong")

    # add ameneity change here, ask about it tho

    def get_current_location(self):
        location_list = self.logic_wrapper.get_all_locations()
        #current_location = None
        for loc in location_list:
            if loc.location == self.location:
                #current_location = loc
                return loc
    
    def display_all_locations(self):
        locations_print_table = PrettyTable()
        location_list = self.logic_wrapper.get_all_locations()
        locations_print_table.field_names = ["Country","Location","Airport","Phone Number","Manager","Opening Hours"]
        for location in location_list:
            locations_print_table.add_row([location.country, location.location, location.airport, location.phone_number, location.branch_manager, location.opening_hours])
        
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        locations_print_table.border = True
        locations_print_table.junction_char = f"{border_color}+{reset_color}"
        locations_print_table.horizontal_char = f"{border_color}-{reset_color}"
        locations_print_table.vertical_char = f"{border_color}|{reset_color}"
        print(locations_print_table)