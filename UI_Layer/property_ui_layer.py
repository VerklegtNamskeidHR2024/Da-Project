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

    def start_point_property_UI(self) -> str:
        
        #Entry point for the property UI.
        properties_menu = self.properties_menu_logistics()
        if properties_menu in ["q", "b"]:
            return properties_menu 

    def display_properties_menu(self) -> str:   

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

    def properties_menu_logistics(self) -> str:
        user_action = ""
        while user_action != "q":
        #depending on your choice you will  be sent to the following places 
            user_action = self.display_properties_menu()
            match (user_action, self.rank):
                case ("1", self.rank):
                    user_action = self.display_select_property()
                case ("2", "Admin") | ("2", "Manager"):
                    user_action = self.display_add_property()
                case ("2", "Employee"):
                    print("Mjá")
                    # user_action = self.display_add_amenity()
                case "b":
                    return "b"
                case "q":
                    return "q"
                case _:
                    print("Invalid input.Please try again.")
        return user_action

    def display_select_property(self) -> str:
        #Displays options for a selected property.
        # You choose the property id for the properrty you looking for
        # kormakur fix this cant do sanity check on property id brother!
        while (property_id_selected := input("Enter the Property ID to select: ").strip()) not in ["q", "b", "Q", "B"]:
        # Gets property by id
            is_valid = self.logic_wrapper.sanity_check_properties('property_id', property_id_selected)
            if is_valid == False:
                print()
                print("Invalid property ID. Please try again.")
                print()
                continue
            if len(property_id_selected) < 2:
                print()
                print("Must Enter A Valid Property ID")
                print()
            selected_property = self.logic_wrapper.get_property_by_id(self.location, property_id_selected)

            # If there is not property with the slected id you will get a message.
            if not selected_property:
                print("No property found with the provided ID.")
                #and it returns to the start point
            # print for single selected property 
            self.print_single_property(selected_property)
            print("1. View Attached Items")
            print("2. Edit Property Details")
            # let you choose from the above 2.
            selected_property_options = self.selected_property_logistics(selected_property)
            if selected_property_options == "b":
                continue
            return selected_property_options.lower()
        return property_id_selected.lower()

    def selected_property_logistics(self, selected_property: object) -> str:
        while (user_choice := input("Enter your choice: ").lower()) not in ["q", "b", "Q", "B"]:
            match user_choice:
                case "1":
                    # Displays the attched options
                    user_choice = self.display_view_attached_options(selected_property)
                case "2":
                    # Lets you edit property details
                    user_choice = self.display_edit_property_details(selected_property)
                case "b":
                    # Goes back to the previous page  
                    return "b"
                    # Exits and turns off the system
                case "q":
                    return "q"
                case _:
                    # If you put an invaild input
                    print("Invalid input. Please try again.")
        return user_choice.lower()

    def display_add_property(self):
        '''Displays the form to add a new property.'''
        
        new_property = House()
        print()
        print("[ New Property Form ]")
        print("-" * 70)
        print()
        print("{:>15}".format("> Go Back: b, B"))
        print("{:>20}".format("> Quit System: q, Q"))
        print()
        print("-" * 70)
        property_name = self.set_name_for_property(new_property)
        return property_name


    def set_name_for_property(self, new_property: object) -> str:

        while (property_name := input("Enter the property name: ")) not in ["q", "b", "Q", "B"]:
            is_valid_name = self.logic_wrapper.sanity_check_properties('name', property_name)
            if is_valid_name == False:
                print()
                print("Invalid name. Please try again.")
                print()
                continue
            new_property.set_name(property_name)
            if self.rank == "Admin":
                location_for_property = self.set_location_name_for_properties(new_property)
                if location_for_property in ["b", "B"]:
                    continue
                return location_for_property
        return property_name.lower()


    def set_location_name_for_properties(self, new_property: object) -> str:

        if self.rank == "Admin":
            while (new_location := input("Enter the property location: ")) not in ["q", "b", "Q", "B"]:
                is_valid_location = self.logic_wrapper.sanity_check_properties('location', new_location)
                if is_valid_location == False:
                    print()
                    print("Invalid location. Please try again.")
                    print()
                    continue
                new_property.set_location(new_location)
                property_condition = self.set_condition_for_property(new_property)
                if property_condition == "b":
                    continue
                return property_condition
            return new_location.lower()
        
        new_property.set_location(self.location)


    def set_condition_for_property(self, new_property: object) -> str:

        while (new_condition := input("Enter the property condition: ")) not in ["q", "b", "Q", "B"]:
            is_valid_condition = self.logic_wrapper.sanity_check_properties('condition', new_condition)
            if is_valid_condition == False:
                print()
                print("Invalid condition. Please try again.")
                print()
                continue
            new_property.set_condition(new_condition)
            property_price = self.set_property_price_to_fix(new_property) 
            if property_price == "b":
                continue
            return property_price
        return new_condition.lower()
    

    def set_property_price_to_fix(self, new_property: object) -> str:
        while (new_price_to_fix := input("Enter the price to fix: ")) not in ["q", "b", "Q", "B"]:
            is_valid_price_to_fix = self.logic_wrapper.sanity_check_properties('price_to_fix', new_price_to_fix)
            if is_valid_price_to_fix == False:
                print()
                print("Invalid price to fix. Please try again.")
                print()
                continue
            new_property.set_total_price_to_fix(new_price_to_fix)
            new_price = self.set_property_price(new_property)
            if new_price == "b":
                continue
            return new_price
        return new_price_to_fix.lower()


    def set_property_price(self, new_property: object) -> str:
        while (new_price := input("Enter the property price: ")) not in ["q", "b", "Q", "B"]:
            is_valid_price = self.logic_wrapper.sanity_check_properties('price', new_price)
            if is_valid_price == False:
                print()
                print("Invalid price. Please try again.")
                print()
                continue
            new_property.set_property_price(new_price)
            confirmation = self.property_creation_confirmation(new_property)
            if confirmation == "b":
                continue
            return confirmation
        return new_price.lower()


    def property_creation_confirmation(self, new_property: object) -> str:
        print()
        while (
            new_property_confirmation := input("Enter 1 to Confirm: ").lower()) != "1":
            if new_property_confirmation in ["q", "b", "Q", "B"]:
                return new_property_confirmation.lower()
            print("Sigma Sigma on the wall, who is the Skibidiest of them all")
        print("-" * 70)
        print()
        self.logic_wrapper.add_new_property_to_storage(self.rank, self.location, new_property)
        print("Property Has Been Created!")
        print()
        return ""
        

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


    def display_view_attached_options(self, selected_property: object) -> str:
        #Displays attached options for a property.
        print("-" * 70)
        print("1. Display Work Requests")
        print("2. Display Maintenance Reports")
        print("-" * 70)
        #lets you choice from the above options
        while (attached_selection := input("Enter choice: ").lower()) not in ["q", "b", "Q", "B"]:
            match attached_selection:
                case "1":
                    self.display_property_work_requests(selected_property)
                case "2":
                    self.display_property_maintenance_reports(selected_property)
                case "b":
                    return "b"
                case "q":
                    return "q"
                case _:
                    print("Invalid input. Please try again.")
        return attached_selection.lower()


    def display_edit_property_details(self, selected_property: object) -> str:
        #allows editing of property details.
        print(f"Editing details for Property ID: {selected_property.property_id}")
        print("1. Change Property Name")
        print("2. Change Property Condition")
        print("3. Change Price to Fix")
        print("4. Change Property Price")

        edit_choice = input("Select an option to edit: ").lower()
        return edit_choice
        
        
    def edit_property_logistics(self, selected_property: object) -> str:
        edit_choice = ""
        while edit_choice != "q":
            edit_choice = self.display_edit_property_details(selected_property)
            match edit_choice:
                case "1":
                    edit_choice = self.edit_property_name(selected_property)
                case "2":
                    edit_choice = self.edit_property_conditions(selected_property)
                case "3":
                    edit_choice = self.edit_price_to_fix(selected_property)
                case "4":
                    edit_choice = self.edit_property_price(selected_property)
                case "b":
                    return "b"
                case "q":
                    return "q"
                case _:
                    print("Invalid input. Please try again.")
        return edit_choice.lower()
        

    def edit_property_name(self, selected_property: object) -> str:

        while (new_name := input("Enter new property name: ")) not in ["q", "b", "Q", "B"]:
            is_valid_name = self.logic_wrapper.sanity_check_properties('name', new_name)
            if is_valid_name == True:
                self.logic_wrapper.edit_existing_property_in_storage(selected_property, self.location, 'name', new_name)
                print("Property details updated successfully!")
                break
        return new_name.lower()
            
            
    def edit_property_conditions(self, selected_property: object) -> str:

        while (new_condition := input("Enter new conditions: ")) not in ["q", "b", "Q", "B"]:
            is_valid_condition = self.logic_wrapper.sanity_check_properties('condition', new_condition)
            if is_valid_condition == True:
                self.logic_wrapper.edit_existing_property_in_storage(selected_property, self.location, 'condition', new_condition)
                print("Property details updated successfully!")
                break
        return new_condition.lower()


    def edit_price_to_fix(self, selected_property: object) -> str:

        is_valid_price_to_fix = False
        while (new_price_to_fix := input("Enter new price to fix: ")) not in ["q", "b", "Q", "B"]:
            is_valid_price_to_fix = self.logic_wrapper.sanity_check_properties('price_to_fix', new_price_to_fix)
            if is_valid_price_to_fix == True:
                self.logic_wrapper.edit_existing_property_in_storage(selected_property, self.location, 'price to fix', new_price_to_fix)
                print("Property details updated successfully!")
                break
        return new_price_to_fix.lower()
    

    def edit_property_price(self, selected_property: object) -> str:

        while (new_price := input("Enter new property price: ")) not in ["q", "b", "Q", "B"]:
            is_valid_price = self.logic_wrapper.sanity_check_properties('price', new_price)
            if is_valid_price == True:
                self.logic_wrapper.edit_existing_property_in_storage(selected_property, self.location, 'price', new_price)
                print("Property details updated successfully!")
                break
        return new_price.lower()
            
                

    def display_property_work_requests(self, selected_property: str) -> str : #type hint to print because of kormakur >:)
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
        print("{:>20}".format("> Go Back: b, B"))
        print("{:>20}".format("> Quit System: q, Q"))
        while (property_work_requests_sub_menu := input("Select An Option: ").lower()) not in ["q", "b", "Q", "B"]:
            print("Sigma Sigma on the wall, who is the Skibidiest of them all")
        return property_work_requests_sub_menu.lower()
        
    def display_property_maintenance_reports(self, selected_property: object) -> str:
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
        print("{:>20}".format("> Go Back: b, B"))
        print("{:>20}".format("> Quit System: q, Q"))
        while (property_maintenance_reports_sub_menu := input("Select An Option: ").lower()) not in ["q", "b", "Q", "B"]:
            print("Sigma Sigma on the wall, who is the Skibidiest of them all")
        return property_maintenance_reports_sub_menu.lower()

    def print_single_property(self, property: object):
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