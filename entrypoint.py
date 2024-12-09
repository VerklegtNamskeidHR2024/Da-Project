#from UI_Layer.start_menu_ui_layer import main
from UI_Layer.start_menu_ui_layer import Main_Menu
from prettytable import PrettyTable 
from colorama import Fore, Style, init
init()

""" def create_location_table():
    locations_table = PrettyTable()
    locations_table.field_names = ['ID',"Country", "Location Name"]
    locations_table.add_row(['1',"Iceland", "Reykjavik"])
    locations_table.add_row(['2',"Greenland", "Nuuk"])
    locations_table.add_row(['3',"Greenland", "Kulusuk"])
    locations_table.add_row(['4',"Faroe Islands", "Torshavn"])
    locations_table.add_row(['5',"Shetland Islands", "Tingwall"])
    locations_table.add_row(['6',"Svalbard", "Longyearbyen"])
        
    border_color = Fore.BLUE
    reset_color = Style.RESET_ALL
    locations_table.border = True
    locations_table.junction_char = f"{border_color}+{reset_color}"
    locations_table.horizontal_char = f"{border_color}-{reset_color}"
    locations_table.vertical_char = f"{border_color}|{reset_color}"

    print(locations_table) """

def main():
    main = Main_Menu("", "")
    main.start_point()
    
if __name__ == "__main__":
    main()