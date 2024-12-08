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

    def display_select_property(self):
        #Displays options for a selected property.
        #try:
            #you choose the property id for the properrty you looking for
            property_id = input("Enter the Property ID to select: ")
            # gets property by id
            selected_property = self.logic_wrapper.get_property_by_id(self.location, property_id)
            #if there is not property with the slected id you will get a message 
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
                    self.display_view_attached_options(selected_property)
                    #displays the attched options
                case "2":
                    self.display_edit_property_details(selected_property)
                    #lets you edit property details
                case "b":
                    #if you want to quit and return to the property list
                    print("Returning to the property list...")
                case _:
                    #if you put an invaild input
                    print("Invalid input. Please try again.")
        #except Exception:
         #   print("An error occurred")

    # Completed
    def display_add_property(self):
        '''Displays the add property form'''
        '''
        "property_id": "P3",
        "name": "suite",
        "location": "Reykjavik",
        "condition": "excellent",
        "total_price_to_fix": 1500.0,
        "property_price": 30
        '''
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

    def display_property_work_requests(self, selected_property) -> print : #type hint to print because of kormakur >:)
        ''' Displays work requests for a property '''
        print("Work Requests for the selected property.")
        property_work_requests = self.logic_wrapper.get_property_work_requests(self.location, selected_property.property_id)
        for work_request in property_work_requests:
            print(f'{work_request.work_request_id} - {work_request.description} - {work_request.mark_as_completed}')
        bause_breaker = input("\nPress Enter to return to the property list.")
        print('')
        self.start_point_property_UI()
        
    def display_property_maintenance_reports(self, selected_property):
        #Displays maintenance reports for a property.
        #need da code in here too gang 
        print("Maintenance Reports for the selected property.")
        property_maintenance_reports = self.logic_wrapper.get_property_maintenance_reports(self.location, selected_property.property_id)
        for maintenance_report in property_maintenance_reports:
            print(f'{maintenance_report.report_id} - {maintenance_report.report_name} - {maintenance_report.maintenance_description} - {maintenance_report.report_status}')
        bbause_breaker = input("\nPress Enter to return to the property list.")
        print('')
        self.start_point_property_UI()

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