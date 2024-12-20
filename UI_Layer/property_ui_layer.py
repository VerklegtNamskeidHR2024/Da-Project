
from Model_Classes.house_model import House
from Model_Classes.amenity_model import Amenity
from prettytable import PrettyTable
from colorama import Fore, Style, init
import os
import time
init()

class property_UI_menu:
    def __init__(self, logic_wrapper, rank, location, staff_id):
        """Constructor for the property UI menu"""
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        self.staff_id = staff_id

    def clear_screen(self):
        ''' Clears the screen '''
        # used to clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
    


    def start_point_property_UI(self) -> str:
        """Start point for the property UI"""
        # In almost all functions that receive, and verifies user input are while loops that repeatedly asks the user
        # for specific input. These while loops are held together on the condition that the user either fullfills the
        # neccesary requirements to proceed or that they don't enter q/Q or b/B.
        #
        #
        # Outside of each while loop are return statments that pass back any input that the user had entered. In all cases,
        # except 2, has no affect on the user experience while navigating this menu. Only when the input given is either
        # q/Q or b/B do these while loops and return statments influence the flow of the user experience.
        #
        #
        # When q/Q are entered, at any point while navigating this menu, it is always returned back to this point. Once here,
        # it passes the necessary verification to be returned back to the home page menu where, once again, it is returned one
        # final time to the quit system function that displays the exit message and stops running the script.
        #
        #
        self.clear_screen()
        properties_menu = self.properties_menu_logistics()
        if properties_menu in ["q", "b"]:
            return properties_menu

    def display_properties_menu(self) -> str:
        """Displays the properties menu"""

        
        # Displays the list of all properties and provides options
        print(f"{self.rank} - Properties Page")
        property_list = self.logic_wrapper.get_all_properties_at_location(self.location)
        property_table = PrettyTable(
            ["Property ID", "Name", "Location", "Condition", "Price to Fix", "Price"]
        )
        for property in property_list:
            property_table.add_row(
                [
                    property.property_id,
                    property.name,
                    property.location,
                    property.condition,
                    property.total_price_to_fix,
                    property.property_price,
                ]
            )
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        property_table.border = True
        property_table.junction_char = f"{border_color}+{reset_color}"
        property_table.horizontal_char = f"{border_color}-{reset_color}"
        property_table.vertical_char = f"{border_color}|{reset_color}"

        print(property_table)
        print("1. Select Property")
        if self.rank != "Employee":
            print("2. Add Property")
            print("3. Add Amenity")
        else:
            print("2. Add Amenity")
        print("-" * 80)
        print()
        print("{:>18}".format("Back - [ b, B ]"))
        print("{:>18}".format("Quit - [ q, Q ]"))
        print()
        user_action = input("Select an Option: ").lower()
        return user_action


    def properties_menu_logistics(self) -> str:
        """Logistics for the properties menu"""
        user_action = ""
        while user_action != "q":
            # depending on your choice you will  be sent to the following places
            user_action = self.display_properties_menu()
            match (user_action, self.rank):
                # In all cases below, if the function returns "b" then the the loop starts again, however if it receives "q"
                # then the loop breaks and is returned back to the start point; shutting the program off.
                #
                #
                # If option 1 is selected, the user goes to search for a property by ID in.
                case ("1", self.rank):
                    user_action = self.display_select_property()
                
                # If option 2 is selected, the admin/manager goes to the create property sub-menu.
                case ("2", "Admin") | ("2", "Manager"):
                    user_action = self.display_add_property()

                # If option 2 is selected for an employee and option 3 for an admin/manager, they go
                # to the create property sub-menu.
                case ("2", "Employee") | ("3", "Admin") | ("3", "Manager"):
                    user_action = self.display_add_amenity()

                # If b is entered, it is returned back to the start_point_work_requests_UI function which brings the
                # user back to the home page.
                case ("b", self.rank):
                    self.clear_screen()
                    return "b"
                
                # If q is entered, it is returned back to the start_point_work_requests_UI function which turns off
                # program.
                case ("q", self.rank):
                    return "q"
                
                # Any other input is except the one's listed above are treated as errors and the user given a message to notify them.
                case _:
                    print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)
                    time.sleep(2)
                    self.clear_screen()

        return user_action.lower()


    def display_select_property(self) -> str:
        """Displays the form to select a property."""
       
        # You choose the property id for the properrty you looking for
        
        # The user is asked to enter a property ID to select a property. The user can also enter "q" to quit the program
        while (property_id_selected := input("Enter the Property ID to select: ").strip()) not in ["q", "b", "Q", "B"]:
        # Gets property by id
            is_valid = self.logic_wrapper.sanity_check_properties('property_id', property_id_selected)
            if is_valid is False:
                print()
                print(Fore.RED + "Invalid property ID. Please try again." + Style.RESET_ALL)
                print(Fore.RED + "Invalid property ID. Please try again." + Style.RESET_ALL)
                print()
                continue
            elif is_valid is True:
                selected_property = self.logic_wrapper.get_property_by_id(self.location, property_id_selected)
                # If there is not property with the slected ID you will get a message.
                if selected_property is None:
                    print(Fore.RED + "No property found with the provided ID."+ Style.RESET_ALL)
                    continue
                self.clear_screen()
                # let you choose from the above 2.

                selected_property_options = self.selected_property_logistics(
                    selected_property
                )
                self.clear_screen()
                if selected_property_options == "b":        
                    continue
                return selected_property_options.lower()
        return property_id_selected.lower()


    def selected_property_logistics(self, selected_property: object) -> str:
        """Logistics for the selected property"""

        user_choice = ""
        while user_choice not in [
            "q",
            "Q"
        ]:
            self.print_single_property(selected_property)
            print("-" * 80)
            print("1. View Property Maintenance Reports")
            print("2. View Property Work requests")
            print("3. Edit Property Details")
            print()
            print("{:>18}".format("Back - [ b, B ]"))
            print("{:>18}".format("Quit - [ q, Q ]"))
            print()
            user_choice = input("Enter your choice: ").lower()
            # Print for single selected property
            print()
            match user_choice:
                case "1":
                    # Displays the attched options
                    user_choice = self.display_property_maintenance_reports(selected_property)
                    self.clear_screen()
                    user_choice = self.display_view_attached_options(selected_property)
                case "2":
                    # Lets you edit property details
                    user_choice = self.display_property_work_requests(selected_property)
                    self.clear_screen()
                case "3":
                    user_choice = self.edit_property_logistics(selected_property)
                    self.clear_screen()
                case "b":
                    # Goes back to the previous page
                    return "b"
                    # Exits and turns off the system
                case "q":
                    return "q"
                case _:
                    # If you put an invaild input
                    print(Fore.RED + "Invalid input. Please try again."+ Style.RESET_ALL)
                    time.sleep(2)
                    self.clear_screen()
        return user_choice.lower()


    def display_add_property(self):
        """Displays the form to add a new property."""

        self.clear_screen()
        # Displays the form to add a new property
        new_property = House()
        print()
        print("{:>55}".format(Fore.GREEN + "[ New Property Form ]" + Style.RESET_ALL))
        print("_" * 80)
        str_display = "Property"
        # Asks the user to enter a name for the property they are creating.
        property_name = self.set_name_for_property(str_display, new_property)
        return property_name


    def display_add_amenity(self):
        """Displays the form to add a new property."""
        self.clear_screen()
        new_amenity = Amenity()
        print()
        print("{:>55}".format(Fore.GREEN + "[ New Amenity Form ]" + Style.RESET_ALL))
        print("-" * 80)
        str_display = "Amenity"
        # Asks the user to enter a name for the amenity they are creating.
        amenity_name = self.set_name_for_property(str_display, new_amenity)
        return amenity_name


    def set_name_for_property(self, str_display: str, new_property: object) -> str:
        """Asks the user to enter a name for the property they are creating. Goes through very simple input"""

        while (property_name := input(f"Enter The {str_display} Name: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Checks if the name is valid
            is_valid_name = self.logic_wrapper.sanity_check_properties(
                "name", property_name
            )
            if is_valid_name is False:
                print()
                print(Fore.RED + "Invalid name. Please try again."+ Style.RESET_ALL)
                print()
                continue
            new_property.set_name(property_name)
            # If the rank is admin the user is asked to enter a location for the property they are creating.
            location_for_property = self.set_location_name_for_properties(
                str_display, new_property
            )
            if location_for_property in ["b", "B"]:
                continue
            return location_for_property
            # If the user enters b/B it will go back to the previous page
        return property_name.lower()


    def set_location_name_for_properties(
        self, str_display: str, new_property: object
    ) -> str:

    # Asks the user to enter a location for the property they are creating. Goes through very simple input
        if self.rank:
            while (
                new_location := input(f"Enter The {str_display} Location: ")
            ) not in ["q", "b", "Q", "B"]:
                is_valid_location = self.logic_wrapper.sanity_check_properties(
                    "location", new_location
                )
                if is_valid_location is False:
                    print()
                    print(Fore.RED + "Invalid location. Please try again."+ Style.RESET_ALL)
                    print()
                    continue
                new_property.set_location(new_location)
                # If the rank is admin the user is asked to enter a location for the property they are creating.
                property_condition = self.set_condition_for_property(
                    str_display, new_property
                )
                if property_condition == "b":
                    continue
                return property_condition
            return new_location.lower()
        # If the rank is not admin the location is set to the location of the employee
        new_property.set_location(self.location)
        property_condition = self.set_condition_for_property(str_display, new_property)
        return property_condition

    def set_condition_for_property(self, str_display: str, new_property: object) -> str:
        """Asks the user to enter a condition for the property they are creating. Goes through very simple input"""
        # Asks the user to enter a condition for the property they are creating. Goes through very simple input
        while (new_condition := input(f"Enter The {str_display} Condition: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            is_valid_condition = self.logic_wrapper.sanity_check_properties(
                "condition", new_condition
            )
            if is_valid_condition is False:
                print()
                print(Fore.RED + "Invalid Condition. Please Try Again."+ Style.RESET_ALL)
                print()
                continue
            # Sets the condition for the property
            new_property.set_condition(new_condition)
            property_price = self.set_property_price_to_fix(str_display, new_property)
            if property_price in ["b", "B"]:
                continue
            return property_price
        return new_condition.lower()


    def set_property_price_to_fix(self, str_display: str, new_property: object) -> str:
        """Asks the user to enter a price to fix for the property they are creating. Goes through very simple input"""
        while (new_price_to_fix := input("Enter The Price To Fix: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Checks if the price to fix is valid
            is_valid_price_to_fix = self.logic_wrapper.sanity_check_properties(
                 "price_to_fix", new_price_to_fix
            )
            if is_valid_price_to_fix is False:
                print()
                print(Fore.RED + "Invalid Price To Fix. Please Try Again."+ Style.RESET_ALL)
                print()
                continue
            new_property.set_total_price_to_fix(new_price_to_fix)
            # If the property is a house the user is asked to enter a price for the property they are creating.
            new_price = self.set_property_price(str_display, new_property)
            if new_price in ["b", "B"]:
                continue
            return new_price # returns the new price
        return new_price_to_fix.lower()


    def set_property_price(self, str_display: str, new_property: object) -> str:
        """Asks the user to enter a price for the property they are creating. Goes through very simple input"""
        # Asks the user to enter a price for the property they are creating. Goes through very simple input
        while (new_price := input(f"Enter the {str_display} Price: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Checks if the price is valid
            is_valid_price = self.logic_wrapper.sanity_check_properties(
                "price", new_price
            )
            # If the price is not valid it will print a message
            if is_valid_price is False:
                print()
                print(Fore.RED + "Invalid Price. Please Try Again."+ Style.RESET_ALL)
                print()
                continue
            new_property.set_property_price(new_price)
            # If the property is a house the user is asked to enter a price for the property they are creating.
            if isinstance(new_property, House):
                confirmation = self.property_creation_confirmation(
                    str_display, new_property
                )
                if confirmation in ["b", "B"]:
                    continue
                return confirmation
            # If the property is an amenity the user is asked to enter a description for the amenity they are creating.
            amenity_description = self.set_description_for_amenity(
                str_display, new_property
            )
            if amenity_description in ["b", "B"]:
                continue
            return amenity_description
        return new_price.lower()


    def set_description_for_amenity(self, str_display: str, new_amenity: object) -> str:
        """Asks the user to enter a description for the amenity they are creating. Goes through very simple input
        verification before setting the description attribute to what the user entered and passing the object down
        to be confirmed."""
        # Asks the user to enter a description for the amenity they are creating. Goes through very simple input
        while (amenity_description := input(f"{str_display} Descriptition: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Checks if the description is valid
            is_description_valid = self.logic_wrapper.sanity_check_properties(
                "description", amenity_description
            )
            if is_description_valid is False:
                print()
                print(Fore.RED + "Sigma Sigma on the wall, who is the Skibidiest of them all"+ Style.RESET_ALL)
                print()
                continue
            # Sets the description for the amenity
            new_amenity.set_amenity_description(amenity_description)
            confirmation = self.property_creation_confirmation(str_display, new_amenity)
            # If the user enters b/B it will go back to the previous page
            if confirmation in ["b", "B"]:
                continue
            return confirmation
        return amenity_description.lower()


    def property_creation_confirmation(
        self, str_display: str, new_property: object
    ) -> str:
        """Displays the new property and asks the user to confirm the creation of the property"""

        print()
        # Displays the new property and asks the user to confirm the creation of the property
        while (
            new_property_confirmation := input("Enter 1 to Confirm: ").lower()
        ) != "1":
            # If the user enters b/B it will go back to the previous page
            if new_property_confirmation in ["q", "b", "Q", "B"]:
                return new_property_confirmation.lower()
            print(Fore.RED + "Sigma Sigma on the wall, who is the Skibidiest of them all"+ Style.RESET_ALL)
        print("-" * 80)
        print()
        # Adds the new property to the storage
        self.logic_wrapper.add_new_property_to_storage(str_display, new_property)
        print(Fore.GREEN + f"{str_display} Has Been Created!" + Style.RESET_ALL)
        time.sleep(1)
        self.clear_screen()
        return ""


    def display_view_attached_options(self, selected_property: object) -> str:
        """Displays the options for the selected property"""
        #clears the screen
        self.clear_screen()
        print("-" * 80)
        print("1. Display Work Requests")
        print("2. Display Maintenance Reports")
        print("-" * 80)
        # lets you choice from the above options
        attached_selection = ""
        while attached_selection not in [
            "q",
            "b",
            "Q",
            "B"
        ]:
            # Depending on your choice you will be sent to the following places
            print("-" * 80)
            print("1. Display Work Requests")
            print("2. Display Maintenance Reports")
            print("-" * 80)
            attached_selection = input("Enter choice: ").lower()
            print()
            match attached_selection:
                case "1":
                    # Displays the work requests for the selected property
                    self.display_property_work_requests(selected_property)
                    attached_selection = self.display_property_work_requests(selected_property)
                case "2":
                    # Displays the maintenance reports for the selected property
                    self.display_property_maintenance_reports(selected_property)
                    attached_selection = self.display_property_maintenance_reports(selected_property)
                    self.clear_screen()
                case "b":
                    # Goes back to the previous page
                    return "b"
                case "q":
                    # Exits and turns off the system
                    return "q"
                case _:
                    print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)
        # Displays the attched options
        return attached_selection.lower()


    def display_edit_property_details(self, selected_property: object) -> str:
        """Displays the options to edit the selected property"""
        self.clear_screen()
        self.print_single_property(selected_property)
        print("-" * 80)
        print(f"Editing details for Property ID: {selected_property.property_id}")
        print("1. Change Property Name")
        print("2. Change Property Condition")
        print("3. Change Price to Fix")
        print("4. Change Property Price")
        print()
        print("{:>18}".format("Back - [ b, B ]"))
        print("{:>18}".format("Quit - [ q, Q ]"))
        print("-" * 70)
        # lets you choose from the above options
        edit_choice = input("Select an option to edit: ").lower()
        return edit_choice

    def edit_property_logistics(self, selected_property: object) -> str:
        """Logistics for editing a property"""
        edit_choice = ""
        # lets you choose from the above options
        while edit_choice != "q":
            edit_choice = self.display_edit_property_details(selected_property)
            match edit_choice:
                case "1":
                    # Edits the name of the selected property
                    edit_choice = self.edit_property_name(selected_property)
                case "2":
                    # Edits the condition of the selected property
                    edit_choice = self.edit_property_conditions(selected_property)
                case "3":
                    # Edits the price to fix of the selected property
                    edit_choice = self.edit_price_to_fix(selected_property)
                case "4":
                    # Edits the price of the selected property
                    edit_choice = self.edit_property_price(selected_property)
                case "b":
                    # Goes back to the previous page
                    return "b"
                case "q":
                    # Exits and turns off the system
                    return "q"
                case _:
                    print(Fore.RED + "Invalid input. Please try again."+ Style.RESET_ALL)
        self.clear_screen()
        return edit_choice.lower()


    def edit_property_name(self, selected_property: object) -> str:
        """Edits the name of the selected property"""

        while (new_name := input("Enter new property name: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Checks if the name is valid
            is_valid_name = self.logic_wrapper.sanity_check_properties("name", new_name)
            # If the name is not valid it will print a message
            if is_valid_name is True:
                self.logic_wrapper.edit_existing_property_in_storage(
                    selected_property, self.location, "name", new_name
                )
                print("Property details updated successfully!")
                # If the user enters b/B it will go back to the previous page
                break
        # returns the new name
        return new_name.lower()


    def edit_property_conditions(self, selected_property: object) -> str:
        """Edits the condition of the selected property"""
        # Edits the condition of the selected property
        while (new_condition := input("Enter new conditions: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Checks if the condition is valid
            is_valid_condition = self.logic_wrapper.sanity_check_properties(
                "condition", new_condition
            )
            # If the condition is not valid it will print a message
            if is_valid_condition == True:
                self.logic_wrapper.edit_existing_property_in_storage(
                    selected_property, self.location, "condition", new_condition
                )
                print(Fore.GREEN + "Property details updated successfully!"+ Style.RESET_ALL)
                time.sleep(2)
                break
        return new_condition.lower()


    def edit_price_to_fix(self, selected_property: object) -> str:
        """Edits the price to fix of the selected property"""
        # Edits the price to fix of the selected property
        is_valid_price_to_fix = False
        while (new_price_to_fix := input("Enter new price to fix: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Checks if the price to fix is valid
            is_valid_price_to_fix = self.logic_wrapper.sanity_check_properties(
                "price_to_fix", new_price_to_fix
            )
            # If the price to fix is not valid it will print a message
            if is_valid_price_to_fix == True:
                self.logic_wrapper.edit_existing_property_in_storage(
                    selected_property, self.location, "price to fix", new_price_to_fix
                )
                print(Fore.GREEN +"Property details updated successfully!"+ Style.RESET_ALL)
                time.sleep(2)
                break
        return new_price_to_fix.lower()


    def edit_property_price(self, selected_property: object) -> str:
        """Edits the price of the selected property"""
        # Edits the price of the selected property
        while (new_price := input("Enter new property price: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Checks if the price is valid
            is_valid_price = self.logic_wrapper.sanity_check_properties(
                "price", new_price
            )
            # If the price is not valid it will print a message
            if is_valid_price == True:
                self.logic_wrapper.edit_existing_property_in_storage(
                    selected_property, self.location, "price", new_price
                )
                print(Fore.GREEN + "Property details updated successfully!" + Style.RESET_ALL)
                time.sleep(2)
                break
        return new_price.lower()

    def display_property_work_requests(
        self, selected_property: str
    ) -> str:  
  
        """Displays work requests for a property"""
        self.clear_screen()
        # Displays work requests for a property
        property_work_requests_table = PrettyTable(
            ["Work Request ID", "Description", "Mark as Completed"]
        )
        print("Work Requests for the selected property.")
        # Gets the work requests for the selected property
        property_work_requests = self.logic_wrapper.get_property_work_requests(
            self.location, selected_property.property_id
        )
        # it will check the work requests for the selected property
        # and display the work requests for the selected property
        for work_request in property_work_requests:
            property_work_requests_table.add_row(
                [
                    work_request.work_request_id,
                    work_request.description,
                    work_request.mark_as_completed,
                ]
            )
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        property_work_requests_table.border = True
        property_work_requests_table.junction_char = f"{border_color}+{reset_color}"
        property_work_requests_table.horizontal_char = f"{border_color}-{reset_color}"
        property_work_requests_table.vertical_char = f"{border_color}|{reset_color}"
        print(property_work_requests_table)
        print()
        #checks if the user wants to go back or quit
        print("{:>10}".format("Back - [ b, B ]"))
        print("{:>10}".format("Quit - [ q, Q ]"))
        # lets you choose from the above options
        # depending on your choice you will be sent to the following places
        while (
            property_work_requests_sub_menu := input("Select An Option: ").lower()
        ) not in ["q", "b", "Q", "B"]:
            print("Sigma Sigma on the wall, who is the Skibidiest of them all")
        return property_work_requests_sub_menu.lower()


    def display_property_maintenance_reports(self, selected_property: object) -> str:
        """Displays maintenance reports for a property"""
        property_maintenance_reports_table = PrettyTable(
            ["Report ID", "Report Name", "Description", "Status"]
        )
        self.clear_screen()
        print("Maintenance Reports for the selected property.")
        # Gets the maintenance reports for the selected property
        property_maintenance_reports = (
            self.logic_wrapper.get_property_maintenance_reports(
                self.location, selected_property.property_id
            )
        )
        # it will check the maintenance reports for the selected property
        # and display the maintenance reports for the selected property
        for maintenance_report in property_maintenance_reports:
            property_maintenance_reports_table.add_row(
                [
                    maintenance_report.report_id,
                    maintenance_report.report_name,
                    maintenance_report.maintenance_description,
                    maintenance_report.report_status,
                ]
            )
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        property_maintenance_reports_table.border = True
        property_maintenance_reports_table.junction_char = (
            f"{border_color}+{reset_color}"
        )
        property_maintenance_reports_table.horizontal_char = (
            f"{border_color}-{reset_color}"
        )
        property_maintenance_reports_table.vertical_char = (
            f"{border_color}|{reset_color}"
        )
        print(property_maintenance_reports_table)
        print()
        # #checks if the user wants to go back or quit
        print("{:>10}".format("Back - [ b, B ]"))
        print("{:>10}".format("Quit - [ q, Q ]"))
        # lets you choose from the above options
        while (
            property_maintenance_reports_sub_menu := input("Select An Option: ").lower()
        ) not in ["q", "b", "Q", "B"]:
            print("Sigma Sigma on the wall, who is the Skibidiest of them all")
        return property_maintenance_reports_sub_menu.lower()


    def print_single_property(self, property: object):
        """Prints a single property"""
        # it printes a single property by using the PrettyTable
        single_property_table = PrettyTable(
            ["Property ID", "Name", "Location", "Condition", "Price to Fix", "Price"]
        )
        single_property_table.add_row(
            [
                property.property_id,
                property.name,
                property.location,
                property.condition,
                property.total_price_to_fix,
                property.property_price,
            ]
        )
        border_color = Fore.BLUE
        reset_color = Style.RESET_ALL
        single_property_table.align = 'l'
        single_property_table.border = True
        single_property_table.junction_char = f"{border_color}+{reset_color}"
        single_property_table.horizontal_char = f"{border_color}-{reset_color}"
        single_property_table.vertical_char = f"{border_color}|{reset_color}"
        print(single_property_table)
