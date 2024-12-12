from Model_Classes.location_model import Location
import os
from prettytable import PrettyTable 
from colorama import Fore, Style, init

class location_UI_menu:
    def __init__(self, logic_wrapper, rank, location, staff_id):
        '''Class builder'''
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location  
        self.staff_id = staff_id

    def start_point_location_UI(self):
        # when this class is called it starts here
        # call other functions in class from here
        self.clear_screen()
        if self.rank == "Admin":
            continue_running = self.display_selected_location_information_printed_admin()
        if self.rank == "Manager":
            continue_running = self.display_selected_location_information_printed_manager()
        if continue_running in ["q", "b"]:
            self.clear_screen()
            return continue_running

    def clear_screen(self):
        ''' Clears the screen '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def location_information(self):
        '''Information about current Location, Needs to fetch information from data storage and insert'''
        # gets current location
        current_location = self.get_current_location()

        location_table = PrettyTable()
        location_table.field_names = ['Current Location',"Information"]
        location_table.add_row([f'Country ',current_location.country])
        location_table.add_row(['Location',current_location.location])
        location_table.add_row(['Airport',current_location.airport])
        location_table.add_row(['Phone Number',current_location.phone_number])
        location_table.add_row(['Manager',current_location.branch_manager])
        location_table.add_row(['Opening Hours',current_location.opening_hours])

        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        location_table.border = True
        location_table.junction_char = f"{border_color}+{reset_color}"
        location_table.horizontal_char = f"{border_color}-{reset_color}"
        location_table.vertical_char = f"{border_color}|{reset_color}"
        print(location_table)
        # prints the information for this location
        
    def display_selected_location_information_printed_admin(self) -> bool:
        '''Displays the location information and options for editing the location'''

        user_choice = ""
        while user_choice != "q":
            print()
            print(f"{self.rank} - Location Menu")
            print("-" * 80)
            self.location_information()
            print("-" * 80)
            print("1. Edit Location Details")
            print("2. Show Attached Amenities")
            print("3. Show All Locations")
            print()
            print("{:>18}".format("Back - [ b, B ]"))
            print("{:>18}".format("Quit - [ q, Q ]"))
            print("-" * 80)
            user_choice = input("Enter a command: ").lower()
            match user_choice.lower():
                case "1":
                    # edit location details
                    self.clear_screen()
                    user_choice = self.display_edit_current_location()
                    self.clear_screen()
                case "2":
                    # show all amenities
                    self.clear_screen()
                    user_choice = self.display_amenities_menu()
                    self.clear_screen()
                case "3":
                    # show all locations
                    self.clear_screen()
                    user_choice = self.display_all_locations()
                    self.clear_screen()
                case "b":
                    return "b"
                case "q":
                    return "q"
                case _:
                    print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)
        self.clear_screen()
        return user_choice.lower()

    def display_selected_location_information_printed_manager(self) -> bool:
        '''Displays the location information and options for editing the location'''
        # prints infroamtion about the current location

        user_choice = ""
        while user_choice not in ["q", "b"]:
            print("{:>50}".format("[ Edit Location ]"))
            print("-" * 80)
            self.location_information()
            print("-" * 80)
            print("1. Edit Location Details")
            print("2. Show Attached Amenities")
            print()
            print("{:>18}".format("Back - [ b, B ]"))
            print("{:>18}".format("Quit - [ q, Q ]"))
            print("-" * 80)
            user_choice = input("Enter a command: ").lower()
            match user_choice.lower():
                case "1":
                    # edit location details
                    self.clear_screen()
                    user_choice = self.display_edit_current_location()
                    self.clear_screen()
                case "2":
                    # show all amenities
                    self.clear_screen()
                    user_choice = self.display_amenities_menu()
                    self.clear_screen()
                case "q":
                    return "q"
                case "b":
                    return "b"
                case _:
                    print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)
        self.clear_screen()
        return user_choice.lower()

    def display_edit_current_location(self) -> None:
        '''Shows location information along with an option to 
        change phone number and opening hours'''

        edit_user_action = ""
        while edit_user_action != "q":
            print("{:>30}".format("[ Edit Location Options ]"))
            print("-" * 80)
            current_location = self.get_current_location()
            self.location_information()
            print("1. Phone Number")
            print("2. Opening Hours")
            print()
            print("{:>18}".format("Back - [ b, B ]"))
            print("{:>18}".format("Quit - [ q, Q ]"))
            print("-" * 80)

            edit_user_action = input("Enter Editing Option: ").lower()
            match edit_user_action:
                case "1":
                    edit_user_action = self.change_phone_number(current_location)
                case "2":
                    edit_user_action = self.change_opening_hours(current_location)
                case "q":
                    self.clear_screen()
                    return "q"
                case "b":
                    self.clear_screen()
                    return "b"
                case _:
                    print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)
        self.clear_screen()
        return edit_user_action.lower()

    def change_phone_number(self, location) -> None:
        """Change the phone number of the location"""
        try:
            while (phone_input := input("Enter A Phone Number: ")) not in ["q", "b", "Q", "B"]:
                # checks if the phone number is valid
                is_valid = self.logic_wrapper.sanity_check_location("phone_number", phone_input)
                if phone_input.isdigit() is False and is_valid is False:
                    print()
                    print(Fore.RED + "Invalid Input. Please Enter Numbers Only." + Style.RESET_ALL)
                    print()
                    continue
                # if the phone number is valid, change the phone number and print the location information
                self.logic_wrapper.edit_existing_location_in_storage(location, self.location, 'phone_number', phone_input)
                self.clear_screen()
                print(Fore.GREEN + "Phone Number Changed Successfully." + Style.RESET_ALL)
                return ""
            self.clear_screen()
            return phone_input.lower()
        except ValueError:
            print(Fore.RED + "Something Went Wrong." + Style.RESET_ALL)

    def change_opening_hours(self, location) -> None:
        """Change the opening hours of the location"""
        try:
            while (new_opening_hours := input("Enter Opening Hours: ")) not in ["q", "b", "Q", "B"]:
            # checks if the opening hours are valid
                is_valid = self.logic_wrapper.sanity_check_location("opening_hours", new_opening_hours)
                if is_valid is True:
                    print()
                    print(Fore.RED + "Invalid input. Please try again."+ Style.RESET_ALL) 
                    print()
                    continue
                # if the opening hours are valid, change the opening hours and print the location information
                self.logic_wrapper.edit_existing_location_in_storage(location, self.location, 'opening_hours', new_opening_hours)
                self.clear_screen()
                print(Fore.GREEN + "Opening hours changed successfully." + Style.RESET_ALL)
                return ""
            self.clear_screen()
            return new_opening_hours.lower()
        except ValueError:
            print(Fore.RED + "Something Went Wrong." + Style.RESET_ALL) 

    def display_amenities_menu(self) -> None:
        """Display the amenities menu"""
        user_action = ""
        while user_action != "q":
            self.display_attached_amenities()
            print("1. Edit Amenity Condition")
            print()
            print("{:>18}".format("Back - [ b, B ]"))
            print("{:>18}".format("Quit - [ q, Q ]"))
            print("-" * 80)
            user_action = input("Select An Option: ").lower()
            match user_action.lower():
                case "1":
                    self.clear_screen()
                    user_action = self.edit_amenity()
                    self.clear_screen()
                case "q":
                    return "q"
                case "b":
                    return "b"
                case _:
                    print(Fore.RED + "Invalid input. Please try again."+ Style.RESET_ALL)
        self.clear_screen()
        return user_action.lower()
        
    def edit_amenity(self) -> None:
        """Edit an amenity"""
        
        while (amenity_ID := input("Enter the ID of the Amenity You Want To Edit: ")) not in ["q", "b", "Q", "B"]:
            amenity = self.logic_wrapper.fetch_amenity_by_id(amenity_ID, self.location)
            if amenity is not None:
            # if the amenity exists, display the amenity and let the user input a new condition
                self.display_single_amenity(amenity)
                new_condition = input("Enter New Condition: ")
                changed_amenity = self.logic_wrapper.edit_amenity(amenity, new_condition)
                # if the amenity condition is changed, print a success message
                if changed_amenity:
                    self.clear_screen()
                    print()
                    print(Fore.GREEN + "Amenity Condition Was Successfully Changed!" + Style.RESET_ALL)
                    print()
                    return ""
                print(Fore.RED + f"No Amenity Found With That ID {amenity_ID}" + Style.RESET_ALL)
        self.clear_screen()
        return amenity_ID.lower()


        #amenities_list = self.logic_wrapper.fetch_all_amenities_for_location_in_storage(self.location)

    def display_single_amenity(self, amenity):
        """Display a single amenity"""
        # prints the information for the amenity the class is called with
        print("-" * 70)
        amenitiy_table = PrettyTable()
        amenitiy_table.field_names = ['Amenity Name', 'Property ID', 'Location', 'Condition', 'Price to fix', 'Description']
        amenitiy_table.add_row([amenity.name, amenity.property_id, amenity.location, amenity.condition, amenity.total_price_to_fix, amenity.amenity_description ])
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        amenitiy_table.border = True
        amenitiy_table.junction_char = f"{border_color}+{reset_color}"
        amenitiy_table.horizontal_char = f"{border_color}-{reset_color}"
        amenitiy_table.vertical_char = f"{border_color}|{reset_color}"
        print(amenitiy_table)
        print("-" * 80)
        

    def display_attached_amenities(self):
        """Display all amenities attached to the location"""
        # gets all amenities for the location
        amenities_list = self.logic_wrapper.fetch_all_amenities_for_location_in_storage(current_location.location)
        if not amenities_list:
            print(Fore.RED + "No Amenities Found." + Style.RESET_ALL)
            return
        else:
            # when admin needs to select location
            current_location = self.get_current_location()
            print(f"Amenities Attached To {current_location.location}:")
            print("-" * 70)
            amenities_table = PrettyTable()
            amenities_table.field_names = ['Amenity Name', 'Property ID', 'Location', 'Condition', 'Price to fix', 'Description']
            for amenity in amenities_list:
                amenities_table.add_row([amenity.name, amenity.property_id, amenity.location, amenity.condition, amenity.total_price_to_fix, amenity.amenity_description ])
            border_color = Fore.BLUE
            reset_color = Style.RESET_ALL
            amenities_table.border = True
            amenities_table.junction_char = f"{border_color}+{reset_color}"
            amenities_table.horizontal_char = f"{border_color}-{reset_color}"
            amenities_table.vertical_char = f"{border_color}|{reset_color}"
            print(amenities_table)
            print("-" * 80)

    def get_current_location(self):
        """Get the current location and return it"""
        # gets all locations
        location_list = self.logic_wrapper.get_all_locations()
        # iterates through the list of locations and returns the location that matches the current location
        for loc in location_list:
            if loc.location == self.location:
                #current_location = loc
                return loc
    
    def display_all_locations(self):
        """prints all locations"""
        # create a table to print all locations
        locations_print_table = PrettyTable()
        location_list = self.logic_wrapper.get_all_locations()
        locations_print_table.field_names = ["Country","Location","Airport","Phone Number","Manager","Opening Hours"]
        # iterates through the location list and adds the location information to the table
        for location in location_list:
            locations_print_table.add_row([location.country, location.location, location.airport, location.phone_number, location.branch_manager, location.opening_hours])
        
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        locations_print_table.border = True
        locations_print_table.junction_char = f"{border_color}+{reset_color}"
        locations_print_table.horizontal_char = f"{border_color}-{reset_color}"
        locations_print_table.vertical_char = f"{border_color}|{reset_color}"
        print(locations_print_table)
        print()
        print("{:>18}".format("Back - [ b, B ]"))
        print("{:>18}".format("Quit - [ q, Q ]"))
        print("-" * 80)
        while (
            all_locations := input("Select An Option: ").lower()
        ) not in ["q", "b", "Q", "B"]:
            print(Fore.RED + "Sigma Sigma on the wall, who is the Skibidiest of them all" + Style.RESET_ALL)
        self.clear_screen()
        return all_locations.lower()
