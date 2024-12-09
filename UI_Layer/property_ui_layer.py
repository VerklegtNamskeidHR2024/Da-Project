
from Model_Classes.house_model import House
 
class property_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        self.dash_length = 79

    def start_point_property_UI(self):
        
        #Entry point for the property UI.
        self.display_all_properties()

    def display_all_properties(self):   

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
        print("2. Add Property")
        print("-" * self.dash_length)

        user_action = input("Select an Option:  ")
        #depending on your choice you will  be sent to the following places 
        match user_action:
            case "1":
                self.display_select_property()
            case "2":
                self.display_add_property()
            case "q":
                print("Returning to the main menu...")
                #code need to be implemeneted in hegr to return to the main menu
            case _:
                print("Invalid input.Please try again.")

    def display_select_property(self) -> print:
        #Displays options for a selected property.
        #try:
            #you choose the property id for the properrty you looking for
            property_id = input("Enter the Property ID to select: ")
            # gets property by id
            selected_property = self.logic_wrapper.get_property_by_id(self.location, self.rank, property_id)
            self.print_single_property(selected_property)
            #if there is not property with the slected id you will get a message 
            if not selected_property:
                print("No property found with the provided ID.")
                #and it returns to the start point
                return
            
            #if there is a property with the selected id you will get the following options
            print("1. View Attached Items")
            print("2. Edit Property Details")
            # let you choose from the above 2.
            user_choice = input("Enter your choice: ")

            match user_choice:
                case "1":
                    self.display_view_attached_options(selected_property)
                    #displays the attched options
                case "2":
                    self.display_edit_property_details()
                    #lets you edit property details
                case "b":
                    #if you want to quit and return to the property list
                    print("Returning to the property list...")
                case _:
                    #if you put an invaild input
                    print("Invalid input. Please try again.")
        except Exception:
            print("An error occurred")

    def display_add_property(self):
    # Handles adding a new property.
        try:
            # New property
            new_property = House()
            # The details you can add for the property
            new_property.set_property_id(input("Enter Property ID: "))
            new_property.set_name(input("Enter Property Name: "))
            new_property.set_condition(input("Enter Property Condition: "))
            new_property.set_total_price_to_fix(int(input("Enter Price to Fix: ")))
            # new_property.set_property_price(int(input("Enter Property Price: ")))
            if self.rank != "Admin":
                new_property.set_location(self.location)
            else:
                new_property.set_location(input("Enter Property Location: "))
            new_property.location = self.location
            
            # Adds the property
            property_list = self.logic_wrapper.add_new_property_to_storage(self.rank, self.location, new_property)
            
            if property_list is not None:
                for obj in property_list:
                    print(obj)
                print("New property has been added successfully!")
            else:
                print("Failed to add new property.")
        except ValueError:
            # If you put an invalid input
            print("Invalid input.")


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
                self.display_property_maintenance_reports()
            case "3":
                self.display_property_employees()
            case "4":
                self.display_property_contractors()
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

    def display_property_work_requests(self):
        #Displays work requests for a property.
        #need da code  for the work requests in here 
        print("Work Requests for the selected property.")

    def display_property_maintenance_reports(self):
        #Displays maintenance reports for a property.
        #need da code in here too gang 
        print("Maintenance Reports for the selected property.")

    def display_property_employees(self):
        #Displays employees assigned to a property.
        #code...
        print("Employees assigned to the selected property.")

    def display_property_contractors(self):
        """Displays contractors assigned to a property."""
        print("Contractors assigned to the selected property.")

    def print_single_property(self, property):
        #Prints details of a single property
        print("-" * 30)
        print(f"{'Property ID':<20}: {property.property_id}")
        print(f"{'Name':<20}: {property.name}")
        print(f"{'Location':<20}: {property.location}")
        print(f"{'Condition':<20}: {property.condition}")
        print(f"{'Price to Fix':<20}: {property.total_price_to_fix}")
        print(f"{'Price':<20}: {property.property_price}")
        print("-" * 30)

    
