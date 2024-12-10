from Model_Classes.house_model import House
from prettytable import PrettyTable 
from colorama import Fore, Style, init
init()
class property_UI_menu:
    def __init__(self, logic_wrapper, rank, location, staff_id):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        self.staff_id = staff_id

    def start_point_property_UI(self):
        
        #Entry point for the property UI.
        properties_menu = self.properties_menu_logistics()
        if properties_menu == "q" or properties_menu == "b": 
            return properties_menu 

    def display_properties_menu(self):   

        # NEEDS to be changed to match with other UI files!!!!
        #Displays the list of all properties and provides options
        print(f"\033[94m{self.rank}\033[0m - Properties Page")
        property_list = self.logic_wrapper.get_all_properties_at_location(self.location)
        property_table = PrettyTable(['Property ID', 'Name', 'Location', 'Condition', 'Price to Fix', 'Price'])
        for property in property_list:
            property_table.add_row([property.property_id, property.name, property.location, property.condition, property.total_price_to_fix, property.property_price])
        border_color = Fore.MAGENTA
        reset_color = Style.RESET_ALL
        property_table.border = True
        property_table.junction_char = f"{border_color}+{reset_color}"
        property_table.horizontal_char = f"{border_color}-{reset_color}"
        property_table.vertical_char = f"{border_color}|{reset_color}"

        print(property_table)
        print("1. Select Property")
        if self.rank == "Employee":
            print("2. Add Amenities")
        else:
            print("2. Add Property")
        print("-" * 70)

        user_action = input("Select an Option:  ").lower()
        return user_action 

    def properties_menu_logistics(self):
        user_action = ""
        while user_action != "q":
        #depending on your choice you will  be sent to the following places 
            user_action = self.display_properties_menu()
            match (user_action, self.rank):
                case ("1", self.rank):
                    user_action = self.display_select_property()
                case ("2", "Admin") | ("2", "Manager"):
                    user_action = self.display_add_property()
                case "b":
                    return "b"
                case "q":
                    return "q"
                case _:
                    print("Invalid input.Please try again.")
        return user_action

    def display_select_property(self):
        #Displays options for a selected property.
        # You choose the property id for the properrty you looking for

        while (property_id_selected := input("Enter the Property ID to select: ")) != "q" and property_id_selected != "Q":
            if property_id_selected.lower() == "b" or property_id_selected == "B":
                break
        # Gets property by id
            if len(property_id_selected) < 3:
                print()
                print("Must Enter A Valid Property ID")
                print()
            selected_property = self.logic_wrapper.get_property_by_id(self.location, property_id)

            # If there is not property with the slected id you will get a message 
            if not selected_property:
                print("No property found with the provided ID.")
                #and it returns to the start point
                return
            # print for single selected property 
            self.print_single_property(selected_property)
            print("1. View Attached Items")
            print("2. Edit Property Details")
            # let you choose from the above 2.
            user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                # Displays the attched options
                self.display_view_attached_options(selected_property)
            case "2":
                # Lets you edit property details
                self.display_edit_property_details(selected_property)
            case "b":
                # Goes back to the previous page  
                return "b"
                # Exits and turns off the system
            case "q":
                return "q"
            case _:
                #if you put an invaild input
                print("Invalid input. Please try again.")

    def display_add_property(self):
        '''Displays the form to add a new property.'''
        is_valid_name = False
        is_valid_location = False
        is_valid_condition = False
        is_valid_price_to_fix = False
        is_valid_price = False
        while is_valid_name == False:
            new_name = input("Enter the property name: ")
            is_valid_name = self.logic_wrapper.sanity_check_properties('name', new_name)
            if is_valid_name == False:
                print("Invalid name. Please try again.")
        while is_valid_location == False:
            new_location = input("Enter the property location: ")
            is_valid_location = self.logic_wrapper.sanity_check_properties('location', new_location)
            if is_valid_location == False:
                print("Invalid location. Please try again.")
        while is_valid_condition == False:
            new_condition = input("Enter the property condition: ")
            is_valid_condition = self.logic_wrapper.sanity_check_properties('condition', new_condition)
            if is_valid_condition == False:
                print("Invalid condition. Please try again.")
        while is_valid_price_to_fix == False:
            new_price_to_fix = input("Enter the price to fix: ")
            is_valid_price_to_fix = self.logic_wrapper.sanity_check_properties('price_to_fix', new_price_to_fix)
            if is_valid_price_to_fix == False:
                print("Invalid price to fix. Please try again.")
        while is_valid_price == False:
            new_price = input("Enter the property price: ")
            is_valid_price = self.logic_wrapper.sanity_check_properties('price', new_price)
            if is_valid_price == False:
                print("Invalid price. Please try again.")
        new_property = House('', new_name, new_location, new_condition, new_price_to_fix, new_price)
        self.logic_wrapper.add_new_property_to_storage(self.rank, self.location, new_property)

    def display_add_amenity(self):
        '''Displays the form to add a new property.'''
        is_valid_name = False
        is_valid_location = False
        is_valid_condition = False
        is_valid_price_to_fix = False
        is_valid_price = False
        while is_valid_name == False:
            new_name = input("Enter the property name: ")
            is_valid_name = self.logic_wrapper.sanity_check_properties('name', new_name)
            if is_valid_name == False:
                print("Invalid name. Please try again.")
        while is_valid_location == False:
            new_location = input("Enter the property location: ")
            is_valid_location = self.logic_wrapper.sanity_check_properties('location', new_location)
            if is_valid_location == False:
                print("Invalid location. Please try again.")
        while is_valid_condition == False:
            new_condition = input("Enter the property condition: ")
            is_valid_condition = self.logic_wrapper.sanity_check_properties('condition', new_condition)
            if is_valid_condition == False:
                print("Invalid condition. Please try again.")
        while is_valid_price_to_fix == False:
            new_price_to_fix = input("Enter the price to fix: ")
            is_valid_price_to_fix = self.logic_wrapper.sanity_check_properties('price_to_fix', new_price_to_fix)
            if is_valid_price_to_fix == False:
                print("Invalid price to fix. Please try again.")
        while is_valid_price == False:
            new_price = input("Enter the property price: ")
            is_valid_price = self.logic_wrapper.sanity_check_properties('price', new_price)
            if is_valid_price == False:
                print("Invalid price. Please try again.")
        new_property = House('', new_name, new_location, new_condition, new_price_to_fix, new_price)
        self.logic_wrapper.add_new_property_to_storage(self.rank, self.location, new_property)


    def display_view_attached_options(self, selected_property):
        #Displays attached options for a property.
        print("-" * 70)
        print("1. Display Work Requests")
        print("2. Display Maintenance Reports")
        print("-" * 70)
        #lets you choice from the above options
        attached_selection = input("Enter choice: ")
        match attached_selection:
            case "1":
                self.display_property_work_requests(selected_property)
            case "2":
                self.display_property_maintenance_reports(selected_property)
            case _:
                print("Invalid input. Please try again.")

    def display_edit_property_details(self, selected_property):
        #allows editing of property details.
        print(f"Editing details for Property ID: {selected_property.property_id}")
        print("1. Change Property Name")
        print("2. Change Property Condition")
        print("3. Change Price to Fix")
        print("4. Change Property Price")

        edit_choice = input("Select an option to edit: ")
        match edit_choice:
            case "1":
                is_valid_name = False
                while is_valid_name == False:
                    new_name = input("Enter new property name: ")
                    is_valid_name = self.logic_wrapper.sanity_check_properties('name', new_name)
                    if is_valid_name == True:
                        self.logic_wrapper.edit_existing_property_in_storage(selected_property, self.location, 'name', new_name)
            case "2":
                is_valid_condition = False
                while is_valid_condition == False:
                    new_condition = input("Enter new conditions: ")
                    is_valid_condition = self.logic_wrapper.sanity_check_properties('condition', new_condition)
                    if is_valid_condition == True:
                        self.logic_wrapper.edit_existing_property_in_storage(selected_property, self.location, 'condition', new_condition)
            case "3":
                is_valid_price_to_fix = False
                while is_valid_price_to_fix == False:
                    new_price_to_fix = input("Enter new price to fix: ")
                    is_valid_price_to_fix = self.logic_wrapper.sanity_check_properties('price_to_fix', new_price_to_fix)
                    if is_valid_price_to_fix == True:
                        self.logic_wrapper.edit_existing_property_in_storage(selected_property, self.location, 'price to fix', new_price_to_fix)
            case "4":
                is_valid_price = False
                while is_valid_price == False:
                    new_price = input("Enter new property price: ")
                    is_valid_price = self.logic_wrapper.sanity_check_properties('price', new_price)
                    if is_valid_price == True:
                        self.logic_wrapper.edit_existing_property_in_storage(selected_property, self.location, 'price', new_price)
            case "b":
                print("Returning to the property list...")
                self.start_point_property_UI()
            case _:
                print("Invalid input. Please try again.")
        print("Property details updated successfully!")

    def display_property_work_requests(self, selected_property) -> print : #type hint to print because of kormakur >:)
        ''' Displays work requests for a property '''
        property_work_requests_table = PrettyTable(['Work Request ID', 'Description', 'Mark as Completed'])
        print("Work Requests for the selected property.")
        property_work_requests = self.logic_wrapper.get_property_work_requests(self.location, selected_property.property_id)
        for work_request in property_work_requests:
            property_work_requests_table.add_row([work_request.work_request_id, work_request.description, work_request.mark_as_completed])
        border_color = Fore.MAGENTA
        reset_color = Style.RESET_ALL
        property_work_requests_table.border = True
        property_work_requests_table.junction_char = f"{border_color}+{reset_color}"
        property_work_requests_table.horizontal_char = f"{border_color}-{reset_color}"
        property_work_requests_table.vertical_char = f"{border_color}|{reset_color}"
        print(property_work_requests_table)
        bause_breaker = input("\nPress Enter to return to the property list.")
        print('')
        self.start_point_property_UI()
        
    def display_property_maintenance_reports(self, selected_property):
        ''' Displays maintenance reports for a property '''
        property_maintenance_reports_table = PrettyTable(['Report ID', 'Report Name', 'Description', 'Status'])
        print("Maintenance Reports for the selected property.")
        property_maintenance_reports = self.logic_wrapper.get_property_maintenance_reports(self.location, selected_property.property_id)
        for maintenance_report in property_maintenance_reports:
            property_maintenance_reports_table.add_row([maintenance_report.report_id, maintenance_report.report_name, maintenance_report.maintenance_description, maintenance_report.report_status])
        border_color = Fore.MAGENTA
        reset_color = Style.RESET_ALL
        property_maintenance_reports_table.border = True
        property_maintenance_reports_table.junction_char = f"{border_color}+{reset_color}"
        property_maintenance_reports_table.horizontal_char = f"{border_color}-{reset_color}"
        property_maintenance_reports_table.vertical_char = f"{border_color}|{reset_color}"
        print(property_maintenance_reports_table)
        bbause_breaker = input("\nPress Enter to return to the property list.")
        print('')
        self.start_point_property_UI()

    def print_single_property(self, property):
        #Prints details of a single property
        single_property_table = PrettyTable(['Property ID', 'Name', 'Location', 'Condition', 'Price to Fix', 'Price'])
        single_property_table.add_row([property.property_id, property.name, property.location, property.condition, property.total_price_to_fix, property.property_price])
        border_color = Fore.MAGENTA
        reset_color = Style.RESET_ALL
        single_property_table.border = True
        single_property_table.junction_char = f"{border_color}+{reset_color}"
        single_property_table.horizontal_char = f"{border_color}-{reset_color}"
        single_property_table.vertical_char = f"{border_color}|{reset_color}"
        print(single_property_table)