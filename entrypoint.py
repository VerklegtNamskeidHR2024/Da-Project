#from UI_Layer.start_menu_ui_layer import main
from UI_Layer.start_menu_ui_layer import Main_Menu

def main():
    # selected_user = select_user_for_system()
    # selected_location = select_location_for_system()
    main = Main_Menu("", "")
    main.start_point()

if __name__ == "__main__":
    main()