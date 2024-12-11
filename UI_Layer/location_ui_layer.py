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
        if self.rank == "Admin":
            self.display_selected_location_information_printed_admin()
        if self.rank == "Manager":
            self.display_selected_location_information_printed_manager()

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
        
    def display_selected_location_information_printed_admin(self):
        '''Displays the location information and options for editing the location'''
        self.location_information()
        print("1) Edit location details")
        print("2) Show attached amenities")
        print("3) Show other locations")
        print(">Go to Home Page:", "home, Home")
        print(">Quit System:", "q, Q")
        user_choice = input("Enter a command: ")
        print()
        match user_choice:
            case "1":
                # edit location details
                self.display_edit_current_location()
            case "2":
                # show all amenities
                self.display_attached_amenities()
            case "3":
                # show all locations
                self.display_all_locations()

    def display_selected_location_information_printed_manager(self):
        '''Displays the location information and options for editing the location'''
        # prints infroamtion about the current location
        self.location_information()



        print("1) Edit location details")
        print("2) Show attached amenities")
        print(">Go to Home Page:", "home, Home")
        print(">Quit System:", "q, Q")
        user_choice = input("Enter a command: ")
        print()
        match user_choice:
            case "1":
                # edit location details
                self.display_edit_current_location()
            case "2":
                # show all amenities
                self.display_attached_amenities()

    def display_edit_current_location(self):
        '''Shows location information along with an option to 
        change phone number and opening hours'''
        current_location = self.get_current_location()
        self.location_information()

        print("1) Phone Number")
        print("2) Opening Hours")
        print("-" * 70)

        edit_user_action = input("Enter Editing Option: ")
        match edit_user_action:
            case "1":
                self.change_phone_number(current_location)
                print()
            case "2":
                self.change_opening_hours(current_location)
                print()

    def change_phone_number(self, location) -> None:
        """Change the phone number of the location"""
        try:
            is_valid = False
            while is_valid == False:
                phone_input = input("Enter phone number: ")
                # checks if the phone number is valid
                is_valid = self.logic_wrapper.sanity_check_location("phone_number", phone_input)
                if not phone_input.isdigit() or is_valid != True:
                    print("Invalid input. Please enter numbers only.")
                else:
                    # if the phone number is valid, change the phone number and print the location information
                    self.logic_wrapper.edit_existing_location_in_storage(location, self.location, 'phone_number', phone_input)
                    self.location_information()
        except:
            print("something went wrong")

    def change_opening_hours(self, location) -> None:
        """Change the opening hours of the location"""
        try:
            new_opening_hours = input("Enter opening hours: ")
            # checks if the opening hours are valid
            is_valid = self.logic_wrapper.sanity_check_location("opening_hours", new_opening_hours)
            if is_valid == True:
                # if the opening hours are valid, change the opening hours and print the location information
                self.logic_wrapper.edit_existing_location_in_storage(location, self.location, 'opening_hours', new_opening_hours)
                self.location_information()
            else:
                print("Invalid input. Please try again.")
            
        except:
            print("something went wrong")

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