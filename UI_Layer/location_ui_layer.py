from Model_Classes.location_model import Location
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
        continue_running = True
        while continue_running == True:
            if self.rank == "Admin":
                continue_running = self.display_selected_location_information_printed_admin()
            if self.rank == "Manager":
                continue_running = self.display_selected_location_information_printed_manager()

        return


    def location_information(self):
        '''Information about current Location, Needs to fetch information from data storage and insert'''
        # gets current location
        current_location = self.get_current_location()

        location_table = PrettyTable()
        location_table.field_names = ['Current location',"Information"]
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
        print("-" * 34)
        self.location_information()
        print("-" * 34)
        print("1) Edit location details")
        print("2) Show attached amenities")
        print("3) Show all locations")
        print(">Go to Home Page: b, B")
        user_choice = input("Enter a command: ")
        print("-" * 34)
        print()
        match user_choice.lower():
            case "1":
                # edit location details
                self.display_edit_current_location()
                return True
            case "2":
                # show all amenities
                self.display_amenities_menu()
                return True
            case "3":
                # show all locations
                self.display_all_locations()
                return True
            case "b":
                return False
            case _:
                print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)
                return True

    def display_selected_location_information_printed_manager(self) -> bool:
        '''Displays the location information and options for editing the location'''
        # prints infroamtion about the current location
        print("-" * 34)
        self.location_information()
        print("-" * 34)
        print("1) Edit location details")
        print("2) Show attached amenities")
        print(">Go to Home Page: b, B")
        user_choice = input("Enter a command: ")
        print("-" * 34)

        print()
        match user_choice.lower():
            case "1":
                # edit location details
                self.display_edit_current_location()
                return True
            case "2":
                # show all amenities
                self.display_amenities_menu()
                return True
            case "b":
                return False
            case _:
                print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)
                return True

    def display_edit_current_location(self) -> None:
        '''Shows location information along with an option to 
        change phone number and opening hours'''
        current_location = self.get_current_location()
        self.location_information()

        print("1) Phone Number")
        print("2) Opening Hours")
        print("Go Back: b, B")
        print("-" * 34)

        edit_user_action = input("Enter Editing Option: ")
        match edit_user_action:
            case "1":
                self.change_phone_number(current_location)
                print()
            case "2":
                self.change_opening_hours(current_location)
                print()
            case "b", "B":
                return
            case _:
                print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)

    def change_phone_number(self, location) -> None:
        """Change the phone number of the location"""
        try:
            is_valid = False
            while is_valid == False:
                phone_input = input("Enter phone number: ")
                # checks if the phone number is valid
                is_valid = self.logic_wrapper.sanity_check_location("phone_number", phone_input)
                if not phone_input.isdigit() or is_valid != True:
                    print(Fore.RED + "Invalid input. Please enter numbers only." + Style.RESET_ALL)
                else:
                    # if the phone number is valid, change the phone number and print the location information
                    self.logic_wrapper.edit_existing_location_in_storage(location, self.location, 'phone_number', phone_input)
                    print("Phone number changed successfully.")
        except:
            print(Fore.RED + "something went wrong." + Style.RESET_ALL) 

    def change_opening_hours(self, location) -> None:
        """Change the opening hours of the location"""
        try:
            new_opening_hours = input("Enter opening hours: ")
            # checks if the opening hours are valid
            is_valid = self.logic_wrapper.sanity_check_location("opening_hours", new_opening_hours)
            if is_valid == True:
                # if the opening hours are valid, change the opening hours and print the location information
                self.logic_wrapper.edit_existing_location_in_storage(location, self.location, 'opening_hours', new_opening_hours)
                print("Opening hours changed successfully.")
            else:
                print(Fore.RED + "Invalid input. Please try again."+ Style.RESET_ALL) 
            
        except:
            print(Fore.RED + "something went wrong." + Style.RESET_ALL) 

    def display_amenities_menu(self) -> None:
        """Display the amenities menu"""
        self.display_attached_amenities()
        print("1) edit amenity condition")
        print("Go Back: b, B")
        user_action = input("Enter a command: ")
        match user_action.lower():
            case "1":
                self.edit_amenity()
            case "b", "B":
                return
            case _:
                print(Fore.RED + "Invalid input. Please try again."+ Style.RESET_ALL)
        
    def edit_amenity(self) -> None:
        """Edit an amenity"""
        is_valid = False
        while is_valid == False:
            amenity_ID = input("Enter the ID of amenity you want to edit: ")
            amenity = self.logic_wrapper.fetch_amenity_by_id(amenity_ID, self.location)
            if amenity != None:
                self.display_single_amenity(amenity)
                new_condition = input("Enter new condition: ")
                changed_amenity = self.logic_wrapper.edit_amenity(amenity, new_condition)
                if changed_amenity:
                    print("Amenity condition changed successfully.")
                    is_valid = True
                
            else:
                print(Fore.RED + f"no amenity found with ID {amenity_ID}" + Style.RESET_ALL)
        return


        #amenities_list = self.logic_wrapper.fetch_all_amenities_for_location_in_storage(self.location)

    def display_single_amenity(self, amenity):
        """Display a single amenity"""
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
        print("-" * 70)
        

    def display_attached_amenities(self):
        """Display all amenities attached to the location"""
        # when admin needs to select location
        current_location = self.get_current_location()
        # gets all amenities for the location
        amenities_list = self.logic_wrapper.fetch_all_amenities_for_location_in_storage(current_location.location)
        print(f"Amenities attached to {current_location.location}:")
        print("-" * 70)
        amenities_table = PrettyTable()
        amenities_table.field_names = ['Amenity Name', 'Property ID', 'Location', 'Condition', 'Price to fix', 'Description']
        print('List of incomplete reports\n')

        for amenity in amenities_list:
            amenities_table.add_row([amenity.name, amenity.property_id, amenity.location, amenity.condition, amenity.total_price_to_fix, amenity.amenity_description ])
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        amenities_table.border = True
        amenities_table.junction_char = f"{border_color}+{reset_color}"
        amenities_table.horizontal_char = f"{border_color}-{reset_color}"
        amenities_table.vertical_char = f"{border_color}|{reset_color}"
        print(amenities_table)
        print("-" * 70)

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