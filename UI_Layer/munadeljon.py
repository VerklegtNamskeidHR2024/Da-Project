location_ID = "L121"
current_country = "Iceland"
current_location = "Keflavik"
current_airport = "KEF"
location_phone = "58-12345"
location_manager = "Hremmi"
amenity_list = ["Dungeon", "Pool"]
opening_hours = "6-9"
rank = "Admin"
def location_information():
    print()
    print("Keflavik")
    print("-" * 70)
    print("-" * 70)
    print(f"Location ID   | {location_ID}")
    print(f"Country       | {current_country}")
    print(f"Location      | {current_location}")
    print(f"Airport       | {current_airport}")
    print(f"Phone Number  | {location_phone}")
    print(f"Manager       | {location_manager}")
    print(f"Amenities     | {amenity_list}")
    print(f"Opening Hours | {opening_hours}") #Needs to fetch the information from data storage
    print("-" * 70) 
    print("{:>24}{:>5}".format(">Go to Home Page:", "home, Home"))
    print("{:>20}{:>5}".format(">Quit System:", "q, Q"))
    print("-" * 70)
    print("-" * 70)

def display_editing_form():
    print()
    print(current_location)
    print("-" * 70)
    print("-" * 70)
    print(f"Location ID   | {location_ID}")
    print(f"Country       | {current_country}")
    print(f"Location      | {current_location}")
    print(f"Airport       | {current_airport}")
    print(f"Phone Number  | {location_phone}")
    print(f"Manager       | {location_manager}")
    print(f"Amenities     | {amenity_list}")
    print(f"Opening Hours | {opening_hours}") #Needs to fetch the information from data storage
    print("-" * 70) 
    print("{:>24}{:>5}".format(">Go to Home Page:", "home, Home"))
    print("{:>20}{:>5}".format(">Quit System:", "q, Q"))

def show_ascii_nan_hq_monstrosity():
        
        print("{:>61}".format("==================="))
        print("{:>44}{:>13}{:>3}".format("|", "NaN Air HQ", "|"))
        print("{:>44}{:>9}{:>7}".format("|", current_airport, "|"))
        print("{:>14}{:>7}{:>15}{:>8}{:>10}{:>6}".format("___________", ".", ": : : :", "|", "_____","|"))
        print("{:>13}{:>12}{:>11}{:>5}{:>3}{:>10}{:>6}{:>4}".format("_\_(*)_/_", "___(*)___", ": : : :", "o o", "|", "| | |", "|", "_ ,"))
        print("{:0}{:>1}{:>31}".format("_______|-|_________/-\__________", ":", "_____|_|__|_____| | |_____| o-o"))

def display_selected_location_information_printed():
        
        location_information()

        show_ascii_nan_hq_monstrosity() #Needs to fetch data from storage to import as location_ID, current_country...
        print("-" * 70)
        if rank == "Admin":
            print("1. Edit location details")
            print("2. Add location")
            print("3. Show other locations")
        user_choice = input("Enter a command: ")
        match user_choice:
               case "1":
                    display_editing_form()

def display_editing_form():
    location_information()
    print("-" * 70)
    print("1. Phone Number")
    print("2. Manager")
    print("3. Amenities")
    print("4. Opening Hours")
    user_choice = input("Enter Editing Option: ")
    match user_choice:
        case "1":
            edited_location_phone = input("Enter a New Location Phone: ")
            return
        






        #Displays information about the location

display_selected_location_information_printed()

