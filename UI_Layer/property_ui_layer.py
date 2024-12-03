class property_UI_menu:
    def __init__(self, logic_wrapper, rank, location):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location



    def display_all_properties():
        print()
        print("Properties")
        print("-" * 70)
        print("Nr |Address | Name | ID")
        print("-" * 70)
        print("1 | Karfavogur 5 | Hús 1 | 20")
        print("2 | Karfavogur 6 | Hús 2 | 21") 
        print()
        print("1. Select Property")
        print("2. Add Property")
        print("-" * 70)

    def select_property():
        property_options = int(input("Select an Option: "))
        if property_options == 1:
            pass
        elif property_options == 2:
            pass
        
    

    def display_selected_property():
        print()
        print("Property Information")
        print("-" * 70)
        print("Name: jehf")
        print("Address: jfsab")
        print("Location: fskjf")
        print("ID: fdsv")
        print("Price: dfgg")
        print("Condition: gdsf")
        print("-" * 70)
        print("1. View Attached")
        print("2. Edit Property Details")


    def choose_property_action():
        attached_or_edit = int(input("Enter Choice: "))

    def add_property():
        property_id = input("Enter property ID: ")
        property_name = input("Enter property name: ")
        property_location = input("Enter property location: ")
        property_condition = input("Enter property condition: ")
        property_price_to_fix = int(input("Enter price to fix: "))
        property_price = int(input("Enter property price"))

    def view_attached_options():
        print()
        print("-" * 70)
        print("1. Display Work Requests")
        print("2. Display Maintenance Reports")
        print("3. Display Employees")
        print("4. Display Contractors")
        print("-" * 70)
    
    def choose_attached():
        attached_selection = int(input("Enter choice: "))
        if attached_selection == 1:
            pass
        elif attached_selection == 2:
            pass
        elif attached_selection == 3:
            pass
        elif attached_selection == 4:
            pass
    
    def display_property_work_requests():
        pass

    def display_property_maintenance_reports():
        pass

    def display_property_employees():
        pass

    def display_property_contractors():
        pass

