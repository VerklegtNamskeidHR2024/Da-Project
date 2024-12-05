from Model_Classes.property_model import Property
 
class property_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location

    def start_point_property_UI(self):
        
        #Entry point for the property UI.
        self.display_all_properties()

    def display_all_properties(self):
        #Displays the list of all properties and provides options
        print(f"{self.rank} - Properties Page")

        # Fetch and print all properties
        property_list = self.logic_wrapper.get_all_properties(self.location)
        self.print_properties_from_list(property_list)
        #gives the option to add or select property 
        print("1. Select Property")
        print("2. Add Property")
        print("-" * 70)

        user_action = input("Select an Option:  ")
        #depending on your choice you will  be sent to the following places 
        match user_action:
            case "1":
                self.display_select_property()
            case "2":
                self.display_add_property()
            case "q":
                print("Returning to the main menu...")
            case _:
                print("Invalid input.Please try again.")

    def display_select_property(self):
        #Displays options for a selected property.
        try:
            #you choose the property id for the properrty you looking for
            property_id = input("Enter the Property ID to select: ")
            # gets property by id
            selected_property = self.logic_wrapper.get_property_by_id(self.location, property_id)
            #if there is not property with the slected id you will get a message 
            if not selected_property:
                print("No property found with the provided ID.")
                #adn it returns to the start point
                return
            # print for single selected property 
            self.print_single_property(selected_property)
            print("1. View Attached Items")
            print("2. Edit Property Details")
            # let you choose from the above 2.
            user_choice = input("Enter your choice: ")

            match user_choice:
                case "1":
                    self.display_view_attached_options()
                    #displays the attched options
                case "2":
                    self.display_edit_property_details(selected_property)
                    #lets you edit property details
                case "q":
                    #if you want to quit and return to the property list
                    print("Returning to the property list...")
                case _:
                    #if you put an invaild input
                    print("Invalid input. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_add_property(self):
        #Handles adding a new property.
        try:
            #new property
            new_property = Property()
            #the details you can add for the property
            new_property.property_id = input("Enter Property ID: ")
            new_property.property_name = input("Enter Property Name: ")
            new_property.property_location = input("Enter Property Location: ")
            new_property.property_condition = input("Enter Property Condition: ")
            new_property.price_to_fix = int(input("Enter Price to Fix: "))
            new_property.property_price = int(input("Enter Property Price: "))
            new_property.location = self.location
            # adds the property
            self.logic_wrapper.add_property(new_property)
            print("New property has been added successfully!")
        except ValueError:
            #if it you put an invaild input
            print("Invalid input. Please enter numeric values for prices.")
        except Exception as e:
            #if it occurs an exception error
            print(f"An error occurred: {e}")

    def display_view_attached_options(self):
        #Displays attached options for a property.
        print("-" * 70)
        print("1. Display Work Requests")
        print("2. Display Maintenance Reports")
        print("3. Display Employees")
        print("4. Display Contractors")
        print("-" * 70)
        #lets you choice from the above options
        attached_selection = input("Enter choice: ")
        match attached_selection:
            case "1":
                self.display_property_work_requests()
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
        print("2. Change Property Location")
        print("3. Change Property Condition")
        print("4. Change Price to Fix")
        print("5. Change Property Price")

        edit_choice = input("Select an option to edit: ")
        match edit_choice:
            case "1":
                new_name = input("Enter new property name: ")
                #updates the property name
                selected_property.property_name = new_name
            case "2":
                new_location = input("Enter new property location: ")
                #updates the property location
                selected_property.property_location = new_location
            case "3":
                new_condition = input("Enter new property condition: ")
                #updates the property condition
                selected_property.property_condition = new_condition
            case "4":
                try:
                    new_price_to_fix = int(input("Enter new price to fix: "))
                    #updates the property price to fix
                    selected_property.price_to_fix = new_price_to_fix
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            case "5":
                try:
                    new_price = int(input("Enter new property price: "))
                    #updates the property price
                    selected_property.property_price = new_price
                except ValueError:
                    #occurs value error if you put a non numeric value
                    print("Invalid input. Please enter a numeric value.")
            case _:
                print("Invalid input. No changes were made.")
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

    def print_properties_from_list(self, property_list):
        #Prints all properties from a list.
        print("-" * 111)
        print(f"{'ID':<10}|{'Property Name':<25}|{'Location':<20}|{'Condition':<20}|{'Total price to fix':<20}|{'Price':<20}")
        print("-" * 111)
        #takes the item from the property list 
        for item in property_list:
            print(f"{item.property_id:<10}|{item.name:<25}|{item.location:<20}|{item.condition:<20}|{item.total_price_to_fix:<20}|{item.property_price:<20}")
        print("-" * 111)
