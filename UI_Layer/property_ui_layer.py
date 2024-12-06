
from Model_Classes.house_model import House
class property_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location

    def start_point_property_UI(self):
        
        #Entry point for the property UI.
        self.display_all_properties()

    def display_all_properties(self):   

        # NEEDS to be changed to match with other UI files!!!!
        #Displays the list of all properties and provides options
        print(f"{self.rank} - Properties Page")
        property_list = self.logic_wrapper.get_all_properties_at_location(self.location)
        print("-" * 85)
        print("{:>15}{:>10}{:>15}{:>10}{:>15}{:>15}".format("Id", "Name", "Location", "Condtion", "Price to fix", "Price"))
        print("-" * 85)

        for item in property_list:
            print("{:>15}{:>10}{:>15}{:>10}{:>15}{:>15}".format(item.property_id, item.name, item.location, item.condition, item.total_price_to_fix, item.property_price))
            
            # print(f"{item.name :> 15}|{item.phone_number :> 10}|{item.email :> 10}|{self.location :> 15}")
        print("-" * 85)

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

    def display_select_property(self) -> print:
        #Displays options for a selected property.
        try:
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
                    self.display_view_attached_options()
                    #displays the attched options
                case "2":
                    self.display_edit_property_details()
                    #lets you edit property details
                case "q":
                    #if you want to quit and return to the property list
                    print("Returning to the property list...")
                case _:
                    #if you put an invaild input
                    print("Invalid input. Please try again.")
        except Exception:
            print("An error occurred1")

    def display_add_property(self):
    # Handles adding a new property.
        try:
            # New property
        
            # The details you can add for the property
            #new_property.set_property_id(input("Enter Property ID: "))
            name = (input("Enter Property Name: "))
            condition = (input("Enter Property Condition: "))
            total_price_to_fix = (int(input("Enter Price to Fix: ")))
            property_price = (int(input("Enter Property Price: ")))
            if self.rank != "Admin":
                location = self.location
            else:
                location = (input("Enter Property Location: "))
            new_property.location = self.location
            new_property = House('', name, location, condition, total_price_to_fix, False, property_price, False)
        
            
            # Adds the property
            property_list = self.logic_wrapper.add_new_property_to_storage(self.rank, self.location, new_property)
            
            if property_list is not None:
                for obj in property_list:
                    print(obj)
                print("New property has been added successfully!")
            else:
                print("Failed to add new property.")
        except:
            # If you put an invalid input
            print("Invalid input.")


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
                self.display_property_maintenance_report()
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
                selected_property.name = new_name
            case "2":
                new_location = input("Enter new property location: ")
                #updates the property location
                selected_property.location = new_location
            case "3":
                new_condition = input("Enter new property condition: ")
                #updates the property condition
                selected_property.condition = new_condition
            case "4":
                try:
                    new_price_to_fix = int(input("Enter new price to fix: "))
                    #updates the property price to fix
                    selected_property.price_to_fix = new_price_to_fix
                except ValueError:
                    print("Invalid input.")
            case "5":
                try:
                    new_price = int(input("Enter new property price: "))
                    #updates the property price
                    selected_property.property_price = new_price
                except ValueError:
                    #occurs value error if you put a non numeric value
                    print("Invalid input.")
            case _:
                print("Invalid input.")
        print("Property details updated successfully!")

    

    def print_single_property(self, property):
        # Prints details of a single property
        print("-" * 30)
        print(f"{'Property ID':<20}: {property.property_id}")
        print(f"{'Name':<20}: {property.name}")
        print(f"{'Location':<20}: {property.location}")
        print(f"{'Condition':<20}: {property.condition}")
        print(f"{'Price to Fix':<20}: {property.total_price_to_fix}")
        print(f"{'Price':<20}: {property.property_price}")
        print("-" * 30)

    def display_property_work_requests(self, property):
        # Displays work requests for the selected property
        work_requests = self.logic_wrapper.get_work_requests_for_property(property.property_id)
        if work_requests:
            print("Work Requests for Property:")
            for request in work_requests:
                print(f"- {request}")
        else:
            print("No work requests found for this property.")

    def display_property_maintenance_report(self, property):
        # Displays maintenance report for the selected property
        maintenance_report = self.logic_wrapper.get_maintenance_report_for_property(property.property_id)
        if maintenance_report:
            print("Maintenance Report for Property:")
            print(maintenance_report)
        else:
            print("No maintenance report found for this property.")

    def display_property_employees(self, property):
        # Displays employees assigned to the selected property
        employees = self.logic_wrapper.get_employees_for_property(property.property_id)
        if employees:
            print("Employees assigned to the selected property:")
            for employee in employees:
                print(f"- {employee}")
        else:
            print("No employees assigned to this property.")

    def display_property_contractors(self, property):
        # Displays contractors assigned to the selected property
        contractors = self.logic_wrapper.get_contractors_for_property(property.property_id)
        if contractors:
            print("Contractors assigned to the selected property:")
            for contractor in contractors:
                print(f"- {contractor}")
        else:
            print("No contractors assigned to this property.")