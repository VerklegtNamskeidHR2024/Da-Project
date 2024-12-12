from Model_Classes.work_request_model import WorkRequest
import os
from prettytable import PrettyTable
from colorama import Fore, Style, init
import time
init()


class work_request_UI_menu:
    def __init__(self, logic_wrapper, rank, location, staff_id):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        self.staff_id = staff_id


    def start_point_work_requests_UI(self) -> str:
        """When an instance of this class is created, the class object calls this function first which in
        turn calls the function to load the work request menu and it's options for the user.
        """
        self.clear_screen()
        # In almost all functions that receive, and verifies user input are while loops that repeatedly asks the user
        # for specific input. These while loops are held together on the condition that the user either fullfills the
        # neccesary requirements to proceed or that they don't enter q/Q or b/B.
        #
        #
        # Outside of each while loop are return statments that pass back any input that the user had entered. In all cases,
        # except 2, has no affect on the user experience while navigating this menu. Only when the input given is either
        # q/Q or b/B do these while loops and return statments influence the flow of the user experience.
        #
        #
        # When q/Q are entered, at any point while navigating this menu, it is always returned back to this point. Once here,
        # it passes the necessary verification to be returned back to the home page menu where, once again, it is returned one
        # final time to the quit system function that displays the exit message and stops running the script.
        #
        #
        work_request_menu = self.menu_selection_logistics()
        if work_request_menu in ["q", "b"]:
            self.clear_screen()
            return work_request_menu

    def clear_screen(self):
        ''' Clears the screen '''
        os.system('cls' if os.name == 'nt' else 'clear')


    def display_all_work_requests_printed(self, work_request_list: list):
        """Displays out all open work requests with their ID, Name and Description."""

        if len(work_request_list) < 1:
            print()
            print("{:>50}".format(Fore.RED + "No Work Requests To Display" + Style.RESET_ALL))
            print()
            return ""
        try:
            work_request_table = PrettyTable(
                ["ID", "Name", "Description", "Start Date", "Priority"]
            )
            for work_request in sorted(work_request_list):
                work_request_table.add_row(
                    [
                        work_request.work_request_id,
                        work_request.name,
                        work_request.description,
                        work_request.start_date,
                        work_request.priority,
                    ]
                )
            border_color = Fore.MAGENTA
            reset_color = Style.RESET_ALL
            work_request_table.border = True
            work_request_table.junction_char = f"{border_color}+{reset_color}"
            work_request_table.horizontal_char = f"{border_color}-{reset_color}"
            work_request_table.vertical_char = f"{border_color}|{reset_color}"
            print(work_request_table)
        except ValueError:
            print()
            print("{:>50}".format(Fore.RED + "No Work Requests To Display" + Style.RESET_ALL))
            print()
            return ""


    # Completed. Can be beautified.
    def display_selected_work_request_information(self, work_request: object):
        """Receives a single, user-selected work request and displays all of its information for them to read."""

        try: 
            single_work_request_table = PrettyTable(
                [
                    "Work Request ID",
                    "Name",
                    "Description",
                    "Location",
                    "Maintenance Report ID",
                    "Employee ID",
                    "Property ID",
                    "Contractor ID",
                    "Start Date",
                    "Completition Date",
                    "Repititive Work",
                    "Re-Open Interval Days",
                    "Needs Contractor",
                    "Completed",
                    "Accepted by Employee",
                ]
            )
            single_work_request_table.add_row(
                [
                    work_request.work_request_id,
                    work_request.name,
                    work_request.description,
                    work_request.location,
                    work_request.maintenance_report_id,
                    work_request.staff_id,
                    work_request.property_id,
                    work_request.contractor_id,
                    work_request.start_date,
                    work_request.completition_date,
                    str(work_request.repetitive_work),
                    work_request.priority,
                    work_request.reopen_interval,
                    work_request.priority,
                    work_request.work_request_status,
                    str(work_request.need_contractor),
                    str(work_request.mark_as_completed),
                    str(work_request.accepted_by_employee),
                ]
            )
            border_color = Fore.BLUE
            reset_color = Style.RESET_ALL
            single_work_request_table.border = True
            single_work_request_table.junction_char = f"{border_color}+{reset_color}"
            single_work_request_table.horizontal_char = f"{border_color}-{reset_color}"
            single_work_request_table.vertical_char = f"{border_color}|{reset_color}"
            print(single_work_request_table)
        except ValueError:
            return ""

    # Completed. Can be beautified.
    def display_work_requests_menu_items(self) -> str:
        """Displays all open work requests and menu options depending on if the user logged in is an admin/manager
        or an employee. It then asks the user to select an option which is returned to be verified in the logistics
        menu below."""

        print()
        print(f"{self.rank} - Work Request Menu")
        print("-" * 80)
        print("{:>50}".format(Fore.BLUE + "[ Open and Ongoing Work Requests ]" + Style.RESET_ALL))
        work_request_list = self.logic_wrapper.get_all_work_requests_at_location(
            self.rank, self.location, self.staff_id
        )
        self.display_all_work_requests_printed(work_request_list)
        if self.rank != "Employee":
            print("1. Search Request")
            print("2. Add Request")
            print("3. New Requests")
            print("4. Pending Requests")
            print("5. Closed Requests")
            print("6. All Requests")
            print("_" * 80)
            print()
            print("{:>18}".format("Back - [ b, B ]"))
            print("{:>18}".format("Quit - [ q, Q ]"))
            print()
        else:
            print("1. Search Request")
            print("2. New Requests")
            print("3. Pending Requests")
            print("4. My Requests")
            print()
            print("{:>18}".format("Back - [ b, B ]"))
            print("{:>18}".format("Quit - [ q, Q ]"))
            print()
        user_choice = input("Select an Option: ").lower()
        return user_choice

    # Completed.
    def menu_selection_logistics(self) -> str:
        """Performs low-level logicistics to interpret the user input it received. If valid, it calls the function corresponding
        to what the user selected. Otherwise it will display an error message and performs the operation again.
        """

        user_choice = ""
        while user_choice != "q":
            # The user input is returned to this variable and then verified.
            user_choice = self.display_work_requests_menu_items()
            match (user_choice, self.rank):
                # In all cases below, if the function returns "b" then the the loop starts again, however if it receives "q"
                # then the loop breaks and is returned back to the start point; shutting the program off.
                #
                #
                # If option 1 is selected, the user goes to the search work request sub-menu.
                case ("1", self.rank):
                    self.clear_screen()
                    user_choice = self.search_work_request_menu_logistics()
                    self.clear_screen()

                # If option 2 is selected, the admin/manager goes to the create work request sub-menu.
                case ("2", "Admin") | ("2", "Manager"):
                    self.clear_screen()
                    user_choice = self.display_create_work_request_form()
                    self.clear_screen()

                # If option 2 is selected for employees and option 3 for admins/manager, they go to the new work request sub-menu.
                case ("2", "Employee") | ("3", "Admin") | ("3", "Manager"):
                    self.clear_screen()
                    user_choice = self.display_and_select_new_work_requests()
                    self.clear_screen()

                # If option 3 is selected for employees and option 4 for admins/manager, they go to the pending work request sub-menu.
                case ("3", "Employee") | ("4", "Admin") | ("4", "Manager"):
                    self.clear_screen()
                    user_choice = self.display_and_select_pending_work_requests()
                    self.clear_screen()

                # If option 5 is selected for admins/manager, they go to the closed work request sub-menu.
                case ("5", "Admin") | ("5", "Manager"):
                    self.clear_screen()
                    user_choice = self.display_and_select_closed_work_requests()
                    self.clear_screen()

                # If option 4 is selected for for employees and option 6 for admins/manager, they go to either the my work requests
                # or all work requests sub-menu. The difference is system priveledges, employees can only view and interact with work
                # requests they are attached to, while admins/managers can see all in their current location.
                case ("4, Employee") | ("6", "Admin") | ("6", "Manager"):
                    self.clear_screen()
                    user_choice = self.display_and_select_request_overview()
                    self.clear_screen()

                # If b is entered, it is returned back to the start_point_work_requests_UI function which brings the
                # user back to the home page.
                case ("b", self.rank):
                    return "b"

                # If q is entered, it is returned back to the start_point_work_requests_UI function which turns off
                # program.
                case ("q", self.rank):
                    return "q"

                # Any other input is except the one's listed above are treated as errors and the user given a message to notify them.
                case _:
                    print(Fore.RED + "Invalid Input, Please Try Again." + Style.RESET_ALL)
                    time.sleep(0.5)
                    self.clear_screen()
        self.clear_screen()
        return user_choice.lower()

    # Completed. Can be beautified.
    def search_work_request_menu(self) -> str:
        """Displays the two options to search for a work request and returns the input to the logistics menu for verification."""

        print("-" * 70)
        print("Search By: ")
        print("{:>14}".format(" 1. ID"))
        print("{:>16}".format(" 2. Date"))
        print("-" * 70)
        user_choice = input("Select An Option: ").lower()
        return user_choice

    # Completed. Can be beautified.
    def search_work_request_menu_logistics(self) -> str:
        """Performs low-level logicistics to interpret the user input it received. If valid, it calls the function corresponding
        to what the user selected. Otherwise it will display an error message and performs the operation again.
        """

        user_choice = ""
        while user_choice != "q":
            user_choice = self.search_work_request_menu()
            match user_choice:
                # In both cases below, if the function returns "b" then the the loop starts again, however if it receives "q"
                # then the loop breaks and is returned back to the start point; shutting the program off.
                #
                #
                # If option 2 is selected, the user goes to search for a work request by ID.
                case "1":
                    user_choice = self.select_work_request_by_id()
                    self.clear_screen()

                # If option 1 is selected, the user goes the search a work request by date.
                case "2":
                    user_choice = self.select_work_request_by_date()
                    self.clear_screen()

                # If b is entered, it is returned back to the start_point_work_requests_UI function which brings the
                # user back to the home page.
                case "b":
                    return "b"

                # If q is entered, it is returned back to the start_point_work_requests_UI function which turns off
                # program.
                case "q":
                    return "q"

                # Any other input is except the one's listed above are treated as errors and the user given a message to notify them.
                case _:
                    print(Fore.RED + "Invalid Input. Please Try Again." + Style.RESET_ALL)
        
        return user_choice.lower()

    # # Completed. Can be beautified.
    def select_work_request_by_date(self) -> str:
        """Repeatedly asks the user for a date (start or completed) until it receives one of acceptable length, which is then
        sent to the logic wrapper to try and find a work request that has a matching date. If found, it displays all of it's information
        and passes the work request down to the edit logistics."""

        # If the user input is q, b, Q, B then the loop breaks.
        while (work_request_selected_by_date := input("Enter Date: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            if len(work_request_selected_by_date) < 8:
                print()
                print(Fore.RED + "Date Must Be Formatted Correctly" + Style.RESET_ALL)
                print()
                continue
            # Logic layer function to return a work request with the date that the user had entered.
            work_request = self.logic_wrapper.get_work_request_by_date(
                self.rank, self.staff_id, self.location, work_request_selected_by_date
            )
            if work_request is not None:
                self.display_selected_work_request_information(work_request)

                # Good example to expand how the quit and back function works. Since this function calls the edit logistics function, it
                # can receive any returned strings and store them in a variable. If it receives "b" then this loop starts over allowing the
                # user to go back from editing to searching.
                #
                edit_work_request = self.edit_work_request_logistics(work_request)
                if edit_work_request == "b":
                    continue
                return edit_work_request.lower()
            #
            # However if it receives q then that string is returned all the way back to the start point, shutting the program off.
            # Any other string is non-consequential since it doesn't fulfill the if statement in the start point function.

            print()
            print(Fore.RED + "Work Request Can't Be Accessed At The Moment, Please Try Again." + Style.RESET_ALL)
            print()
        return work_request_selected_by_date.lower()

    # # Completed. Can be beautified.
    def select_work_request_by_id(self) -> str:
        """Repeatedly asks the user for an ID until it receives one of acceptable length, which is then sent to the logic wrapper to
        try and find a work request that has a matching ID. If found, the system will display all of its information and pass it down
        to the editing logistic. Otherwise it gives an error message and restarts its operation.
        """

        while (work_request_selected := input("Enter Request ID: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            if len(work_request_selected) < 3:
                print()
                print(Fore.RED + "Must Enter A Valid Work Request ID" + Style.RESET_ALL)
                print()
                continue
            work_request = self.logic_wrapper.get_work_request_by_id(
                self.rank, self.staff_id, self.location, work_request_selected
            )
            if work_request is not None:
                self.clear_screen()
                edit_work_request = self.edit_work_request_logistics(work_request)
                if edit_work_request == "b":
                    continue
                return edit_work_request.lower()
            print()
            print(Fore.RED + "Work Request Can't Be Accessed At The Moment, Please Try Again." + Style.RESET_ALL)
            print()
        return work_request_selected.lower()

    # Completed. Can be beautified.
    def edit_work_request_logistics(self, work_request_object) -> str:
        """Receives a single, user-selected work request and gives the user the ability to edit its information;
        the extent of which corresponding to the user's rank. Also verifies what can be edited based on what the
        work requests attributes are set as."""

        # If the user is logged in as either an admin or manager they are given more editing options, which is what this
        # function provides.
        if self.rank != "Employee":
            edit_work_request = self.general_edit_work_request_selected_option(
                work_request_object
            )
            return edit_work_request.lower()

        # If the user logged in is an employee [below only]
        #
        #
        # If the work request is pending, then there is nothing for them to edit.
        if (
            work_request_object.mark_as_completed is True
            and work_request_object.work_request_status == "Pending"
        ):
            while (go_back_or_quit := input("Select an Option: ").lower()) not in [
                "q",
                "b",
            ]:
                print()
                print(Fore.RED + "Ah Ah, You Can't Do That..." + Style.RESET_ALL)
                print()
            return go_back_or_quit.lower()

        # If the work request has not been accepted by an employee, meaning that it is new, then they are directed to the
        # accept work request function, where they can accept or reject it.
        if (
            work_request_object.accepted_by_employee is False
            and work_request_object.work_request_status == "New"
        ):
            accept_work_request = self.employee_accept_work_request_(
                work_request_object
            )
            return accept_work_request.lower()

        # If a work request is currently on-going, the user is directed to the function where they can mark it completed
        # or not.
        if (
            work_request_object.mark_as_completed is False
            and work_request_object.work_request_status == "Open"
        ):
            mark_completed = self.mark_work_request_completed(work_request_object)
            return mark_completed.lower()

    # Completed. Can be beautified.
    def display_create_work_request_form(self) -> str:
        """When this function is called, it begins by creating a new instance of a work request which is then passed down to the
        functions below where many of its attributes are set by the user."""

        self.clear_screen()
        new_work_request = WorkRequest()
        print()
        print("{:>50}".format(Fore.BLUE + "[ New Work Request Form ]" + Style.RESET_ALL))
        print("_" * 70)
        print()
        print("-" * 70)
        #
        # Returns the variable back to the work request main menu into the variable user choice.
        request_name = self.set_name_for_request(new_work_request)
        return request_name

    # Completed. Can be beautified.
    def set_name_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter a name for the work request they are creating. Goes through very simple input
        verification before setting the name attribute to what the user entered and passing the object down
        to the next function."""

        while (request_name := input("Request Name: ")) not in ["q", "b", "Q", "B"]:
            # Sends the input to the logic wrapper for verification.
            is_name_valid = self.logic_wrapper.sanity_check_request_low_level_logistics(
                "name", request_name
            )
            if is_name_valid is True:
                # The name attribute of the WorkRequest instance is set to whatever the user entered after passing the
                # input verification.
                new_work_request.set_name(request_name)
                print()
                request_description = self.set_description_for_request(new_work_request)
                if request_description == "b":
                    continue
                return request_description
            print()
            print(Fore.RED + "Name Must Be Longer Than Five Characters." + Style.RESET_ALL)
            print()

        # When the while loop breaks, it returns the input back the create work request form which in turn retuns said same input back to
        # the work request main menu.
        return request_name.lower()

    # Completed. Can be beautified.
    def set_description_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter a description for the work request they are creating. Goes through very simple input
        verification before setting the description attribute to what the user entered and passing the object down
        to the next function."""

        while (request_description := input("Request Descriptition: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Sends the input to the logic wrapper for verification.
            is_description_valid = (
                self.logic_wrapper.sanity_check_request_low_level_logistics(
                    "description", request_description
                )
            )
            if is_description_valid is False:
                print()
                print(Fore.RED + "Description Must Be Longer Than Five Characters." + Style.RESET_ALL)
                print()
                continue
            new_work_request.set_description(request_description)
            # Another good example to expand how the quit and back function works. Since this function calls the one below and can receive
            # any returned strings, if it receives "b" then this loop starts over allowing the user to re-do what they wrote.
            #
            property_id = self.set_property_id_for_request(new_work_request)
            if property_id == "b":
                continue
            return property_id
        #
        # However if it receives q then that string is returned all the way back to the start point, shutting the program off.
        # Any other string is non-consequential since it doesn't fulfill the if statement in the start point function.

        return request_description.lower()

    # Completed. Can be beautified.
    def set_property_id_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter the property ID for the work request they are creating. Its then sent to the logic
        layer where the input is verified. If its verified as valid, it sets the property ID attribute to what the user
        entered before passing the object down to the next function. Otherwise it begins the operation again.
        """

        while (property_id := input("Assign A Property ID To The Request: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Sends the input to the logic wrapper for verification.
            is_property_id_valid = (
                self.logic_wrapper.sanity_check_work_request_property_id(property_id)
            )
            if is_property_id_valid is True:
                new_work_request.set_property_id(property_id)
                start_date = self.set_start_date_for_request(new_work_request)
                if start_date == "b":
                    continue
                return start_date
            print()
            print(Fore.RED + "Invalid Input" + Style.RESET_ALL)
            print()
        return property_id.lower()

    # Completed. Can be beautified.
    def set_start_date_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter the start date for the work request they are creating. Goes through the logic wrapper that
        verifies if the start date entered is formatted correctly. If valid, the start date attribute is then set to what the user
        had entered and the object is then passed down to the next function."""

        while (start_date := input("Set The Start Date (DD-MM-YY): ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Sends the input to the logic wrapper for verification.
            is_start_date_valid = self.logic_wrapper.sanity_check_start_date(start_date)
            if is_start_date_valid is True:
                new_work_request.set_start_date(start_date)
                repetitive_request = self.set_repetitive_work_for_request(
                    new_work_request
                )
                if repetitive_request == "b":
                    continue
                return repetitive_request
            print()
            print(Fore.RED + "Start Date Must Be Formatted Correctly" + Style.RESET_ALL)
            print()
        return start_date.lower()

    # Completed. Can be beautified.
    def set_repetitive_work_for_request(self, new_work_request: object) -> str:
        """Repeatedly asks the user for input in the form of "Yes" or "No" until it passes the sanity check (verification).
        If it passes, then the class objects is repetitive attroibute is set to either True or False based on if the user
        entered Yes (True) or No (False)."""

        while (
            repetitive_work := input("Mark Request Repititive? (Yes or No): ")
        ) not in ["q", "b", "Q", "B"]:
            # Sends the input to the logic wrapper for verification.
            is_set_repetitive_boolean = (
                self.logic_wrapper.sanity_check_boolean_input_work_requests(
                    repetitive_work
                )
            )
            # Since a request can be repetitive or not, the class instance attribute is set to
            # either True or False based on if the user entered Yes or No.
            #
            # However if marked repetitive, then it has to assign an interval of days until it
            # re-opens.
            if is_set_repetitive_boolean is True:
                new_work_request.set_repetitive_work(is_set_repetitive_boolean)
                interval_days = self.set_interval_days_for_request(new_work_request)
                if interval_days == "b":
                    continue
                return interval_days
            if is_set_repetitive_boolean is False:
                set_priority = self.set_priority_for_request(new_work_request)
                if set_priority == "b":
                    continue
                return set_priority
            print()
            print(Fore.RED + "Invalid Input" + Style.RESET_ALL)
            print()
        return repetitive_work.lower()

    # Completed. Can be beautified.
    def set_interval_days_for_request(self, new_work_request: object) -> str:
        """Repeatedly asks the user for input that is passed down to, and verified in the logic wrapper. If it receives either
        1, 7 or 30 then the class attribute for re-open interval is set to one of the 3 and the user goes to the next category.
        """

        while (
            interval_days := input(
                "Set The Interval Of Days Until Request Re-Opens (1, 7 or 30 Days): "
            )
        ) not in ["q", "b", "Q", "B"]:
            # Sends the input to the logic wrapper for verification.
            is_interval_days_valid = (
                self.logic_wrapper.sanity_check_request_low_level_logistics(
                    "reopen_interval", interval_days
                )
            )
            if is_interval_days_valid is True:
                new_work_request.set_reopen_interval(int(interval_days))
                set_priority = self.set_priority_for_request(new_work_request)
                if set_priority == "b":
                    continue
                return set_priority
            print()
            print(Fore.RED + "Invalid Input" + Style.RESET_ALL)
            print()
            continue
        return interval_days.lower()

    # Completed. Can be beautified.
    def set_priority_for_request(self, new_work_request: object):
        """Repeatedly asks the user for one of 3 priorities to assign to the request (High, Medium or Low). Each input given is passed
        down into the logic wrapper where it is verified to either True or False, where if True the class objects priority attribute is
        set to one of the 3."""

        while (
            set_priority := input("Set The Request Priority (High, Medium or Low): ")
        ) not in ["q", "b", "Q", "B"]:
            # Sends the input to the logic wrapper for verification.
            is_priority_set_valid = (
                self.logic_wrapper.sanity_check_priority_for_request(set_priority)
            )
            if is_priority_set_valid is True:
                new_work_request.set_priority(set_priority)
                needs_contractor = self.set_needs_contractor_for_request(
                    new_work_request
                )
                if needs_contractor == "b":
                    continue
                return needs_contractor
            print()
            print(Fore.RED + "Invalid Input" + Style.RESET_ALL)
            print()
        return set_priority.lower()

    # Completed. Can be beautified.
    def set_needs_contractor_for_request(self, new_work_request: object):
        """Repeatedly asks the user for input in the form of "Yes" or "No" until it passes the sanity check (verification).
        If it passes, then the class objects is repetitive attribute is set to either True or False based on if the user
        entered Yes (True) or No (False)."""

        while (
            needs_contractor := input("Request Needs Contractor? (Yes or No): ")
        ) not in ["q", "b", "Q", "B"]:
            # Sends the input to the logic wrapper for verification.
            is_needs_contractor_boolean = (
                self.logic_wrapper.sanity_check_boolean_input_work_requests(
                    needs_contractor
                )
            )
            # Since a request can or can not need a contractor, the class instance attribute is set to
            # either True or False based on if the user entered Yes or No.
            if (
                is_needs_contractor_boolean is True
                or is_needs_contractor_boolean is False
            ):
                new_work_request.set_need_contractor(needs_contractor)
                set_location = self.set_location_for_request(new_work_request)
                if set_location == "b":
                    continue
                return set_location
            print()
            print(Fore.RED + "Invalid Input" + Style.RESET_ALL)
            print()
        return needs_contractor.lower()

    # Completed. Can be beautified.
    def set_location_for_request(self, new_work_request: object):
        """When assigning the location for the request, it first checks if the user logged in is an admin or manager. If the user
        logged in as a manager then the work request is automatically assigned to whatever location they're in. However if the
        the user logged in is an admin then they can decide what location is to be assigned to the request. The function
        repeatedly asks for input which is put put through a verification until the location given is registered valid.
        """

        if self.rank == "Admin":
            while (set_location := input("Set Location for Work Request: ")) not in [
                "q",
                "b",
                "Q",
                "B",
            ]:
                # Sends the input to the logic wrapper for verification.
                is_set_location_valid = (
                    self.logic_wrapper.sanity_check_location_for_request(set_location)
                )
                if is_set_location_valid is True:
                    new_work_request.set_location(set_location)
                    confirmation = self.work_request_confirmation(new_work_request)
                    if confirmation == "b":
                        continue
                    return confirmation
                print()
                print(Fore.RED + "Invalid Input" + Style.RESET_ALL)
                print()
            return set_location.lower()
        new_work_request.set_location(self.location)
        confirmation = self.work_request_confirmation(new_work_request)
        return confirmation

    # Completed. Can be beautified.
    def work_request_confirmation(self, new_work_request: object) -> str:
        """Once the user has gone through all of the necessary categories, he is asked to enter 1 to confirm the creation of the
        work request. Once entered, the work request is sent to the logic wrapper and the user is goes back to the work request menu.
        """

        print()
        while (
            new_work_request_confirmation := input("Enter 1 to Confirm: ").lower()
        ) != "1":
            if new_work_request_confirmation in ["q", "b", "Q", "B"]:
                return new_work_request_confirmation.lower()
            print(Fore.RED + "Sigma Sigma on the wall, who is the Skibidiest of them all" + Style.RESET_ALL)
        print("-" * 70)
        print()
        # Since this is a new work request, its status attribute is set to "New" as well before being sent to
        # the logic wrapper.
        new_work_request.set_work_request_status("New")
        self.logic_wrapper.add_work_request(new_work_request)
        print(Fore.BLUE + "Work Request Has Been Created!" + Style.RESET_ALL)
        print()
        self.clear_screen()
        return ""

    # Completed. Can be beautified.
    def employee_accept_work_request_(self, work_request: object):
        """After having selected a work request, if its status is marked "New", the employee viewing it can either
        accept it or reject it. By rejecting it, it's status remains unchanged. However if accepted then the employee's
        staff ID is automatically assigned to it before being sent to the logic wrapper.
        """

        while (accept_work_request := input("Aceept (Yes or No): ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:

            # Sends the input to the logic wrapper for verification.
            is_accepted_boolean = (
                self.logic_wrapper.sanity_check_boolean_input_work_requests(
                    accept_work_request
                )
            )
            if is_accepted_boolean is True:
                print()
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    print("Mama they took my dingus")
                work_request.set_accepted_by_employee(True)
                work_request.set_staff_id(self.staff_id)
                self.logic_wrapper.edit_work_request(work_request)
                print()
                print(Fore.BLUE + "Work Request Has Been Accepted!" + Style.RESET_ALL)
                print()
                return ""
            print("Must Enter Either Yes or No")

            if is_accepted_boolean is False:
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    print(Fore.RED + "Mama they took my dingus" + Style.RESET_ALL )
                print()
                print(Fore.BLUE + "Work Request Has Been Rejected!" + Style.RESET_ALL)
                print()
                return ""
        return accept_work_request.lower()

    # Completed. Can be beautified.
    def mark_work_request_completed(self, work_request: object):
        """After having selected a work request, if its status is marked "Open" or "Pending" for an admin/manager, the user
        viewing it can either mark it completed or not by "Yes" or "No". If No is entered, then the work request attribute
        marked completed is set to False. If True, then the class object is passed down into the function below.
        """

        while (mark_as_completed := input("Mark as Completed (Yes or No): ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Sends the input to the logic wrapper for verification.
            is_marked_completed_boolean = (
                self.logic_wrapper.sanity_check_boolean_input_work_requests(
                    mark_as_completed
                )
            )
            if is_marked_completed_boolean is False:
                print()
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    print("Mama they took my dingus")
                    continue
                work_request.set_mark_as_completed(False)
                work_request.set_work_request_status("Open")

                # Sends the work request object with the new data to be the logic wrapper.
                self.logic_wrapper.edit_work_request(work_request)
                print()
                print(Fore.BLUE + "Work Request Has Been Marked Not Completed!" + Style.RESET_ALL)
                print()
                return ""

            if is_marked_completed_boolean is True:
                mark_as_completed_true = self.mark_work_request_completed_true(
                    work_request
                )
                if mark_as_completed_true == "b":
                    continue
                return mark_as_completed_true
        self.clear_screen()
        return mark_as_completed


    def mark_work_request_completed_true(self, work_request: object) -> str:
        """If the selected work request is marked completed as True, then the user needs to enter the completition date for when it
        was completed. Said input is put through verification, if it passes the completition date and marked completed attribute are
        set to whatever the user entered and True respectively."""

        while (
            completition_date := input("Set The Completition Date (DD-MM-YY): ")
        ) not in ["q", "b", "Q", "B"]:
            # Sends the input to the logic wrapper for verification.
            start_date = work_request.start_date
            is_completition_date_valid = (
                self.logic_wrapper.sanity_check_completition_date(
                    start_date, completition_date
                )
            )
            if is_completition_date_valid is True:
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    print("Mama they took my dingus")
                work_request.set_mark_as_completed(True)
                work_request.set_completition_date(completition_date)

                # If the user is logged in as an Employee, then the status of the work request is set to "Pending".
                # For the status to set to "Closed", the user needs to be logged in as either an admin or manager.
                if self.rank == "Employee":
                    work_request.set_work_request_status("Pending")
                else:
                    work_request.set_work_request_status("Closed")

                # Sends the work request object with the new data to be the logic wrapper.
                self.logic_wrapper.edit_work_request(work_request)

                # If the work request is marked repetitive as True, then it sent again to the logic wrapper to be
                # "created again" as an "Open" request with a new start date.
                if work_request.repetitive_work is True:
                    self.logic_wrapper.auto_re_open_work_request(work_request)
                print()
                print(Fore.BLUE + "Work Request Has Been Marked Completed!" + Style.RESET_ALL)
                print()
                return ""
            print()
            print(Fore.RED + "Completition Date Must Be Formatted Correctly" + Style.RESET_ALL)
            print()
            continue
        self.clear_screen()
        return completition_date.lower()

    # Completed. Can be beautified.
    def general_edit_work_request_menu(self) -> str:
        """Displays all the categories that an admin/manager are able to edit about a work request they have selected.
        It then asks them to select one of the 5, where the input is then sent to, and verified in the function below.
        """

        print()
        print("Choose a Category To Edit")
        print("-" * 70)
        print("{:>15}".format("> 1. Employee ID"))
        print("{:>15}".format("> 2. Property ID"))
        print("{:>15}".format("> 3. Mark Repitive"))
        print("{:>15}".format("> 4. Priority"))
        print("{:>15}".format("> 5. Mark Completed"))
        print()
        print("{:>10}".format("Back - [ b, B ]"))
        print("{:>10}".format("Quit - [ q, Q ]"))
        print()
        print("-" * 70)
        category_to_edit = input("Choose a Category to Edit: ").lower()
        return category_to_edit.lower()

    # Completed. Can be beautified.
    def general_edit_work_request_selected_option(self, work_request: object) -> str:
        """Calls the edit menu function above and performs low-level logicistics to interpret the user input it received.
        If it's verified as an invalid input the system displays an error message and performs the operation again.
        """

        category_to_edit = ""
        while category_to_edit != "q":
            self.display_selected_work_request_information(work_request)
            category_to_edit = self.general_edit_work_request_menu()
            match category_to_edit:
                # In all cases below, if the function returns "b" then the the loop starts again, however if it receives "q"
                # then the loop breaks and is returned back to the start point; shutting the program off.
                #
                #
                # If option 1 is selected, the user goes to edit what employee ID is assigned to the work request.
                case "1":
                    category_to_edit = self.edit_employee_id_for_work_request(
                        work_request
                    )

                # If option 2 is selected, the user goes to edit what property ID is assigned to the work request.
                case "2":
                    category_to_edit = self.edit_property_id_for_request(work_request)

                # If option 3 is selected, the user goes to edit wheather or not the work request is repetitive.
                case "3":
                    category_to_edit = self.edit_repitive_work_request(work_request)

                # If option 4 is selected, the user goes to edit what priority the request is set to.
                case "4":
                    category_to_edit = self.edit_priority_for_request(work_request)

                # If option 5 is selected, the user goes to edit weather or not the work request is completed.
                case "5":
                    category_to_edit = self.mark_work_request_completed(work_request)

                # If b is entered, it is returned back to the start_point_work_requests_UI function which brings the
                # user back to the home page.
                case "b":
                    return "b"

                # If q is entered, it is returned back to the start_point_work_requests_UI function which turns off
                # program.
                case "q":
                    return "q"

                # Any other input is except the one's listed above are treated as errors and the user given a message to notify them.
                case _:
                    print(Fore.RED + "Invalid Input. Please Try Again." + Style.RESET_ALL)

        return category_to_edit.lower()

    # Completed. Can be beautified.
    def edit_employee_id_for_work_request(self, work_request: object):
        """Repeatedly asks the user for an employee ID they want to assign to the work request instead of the one currently on it.
        Said input goes through the logic wrapper for verification and if it passes, the work request staff ID attribute is updated
        with the one the user entered."""

        while (edit_employee_id_for_request := input("New Employee ID: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Sends the input to the logic wrapper for verification.
            is_employee_valid = self.logic_wrapper.sanity_check_employee_id_for_request(
                edit_employee_id_for_request
            )
            if is_employee_valid is True:
                print()
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    print(Fore.RED + "Sigma Sigma on the wall, who is the Skibidiest of them all" + Style.RESET_ALL)
                work_request.set_staff_id(edit_employee_id_for_request)

                # Sends the work request object with the new data to be the logic wrapper.
                self.logic_wrapper.edit_work_request(work_request)
                self.clear_screen()
                print()
                print(Fore.BLUE + "New Employee ID Has Been Assigned To Request!" + Style.RESET_ALL)
                print()
                return ""
            print(Fore.RED + "No Employee ID Was Found. Please Try Again." + Style.RESET_ALL)
        self.clear_screen()
        return edit_employee_id_for_request.lower()

    # Completed. Can be beautified.
    def edit_property_id_for_request(self, work_request: object):
        """Repeatedly asks the user for a property ID they want to re-assign to the work request. Said input goes through the
        logic wrapper for verification and if it passes, the work request property ID attribute is updated with the one the user entered.
        """

        while (edit_property_id_for_request := input("New Property ID: ")) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Sends the input to the logic wrapper for verification.
            is_property_id_valid = (
                self.logic_wrapper.sanity_check_work_request_property_id(
                    edit_property_id_for_request
                )
            )
            if is_property_id_valid is True:
                print()
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    print()
                    print(Fore.RED + "Sigma Sigma on the wall, who is the Skibidiest of them all" + Style.RESET_ALL)
                    print()
                work_request.set_property_id(edit_property_id_for_request)

                # Sends the work request object with the new data to be the logic wrapper.
                self.logic_wrapper.edit_work_request(work_request)
                self.clear_screen()
                print()
                print(Fore.BLUE + "New Property ID Has Been Assigned To Request!" + Style.RESET_ALL)
                print()
                return ""
            print(Fore.RED + "No Property ID Was Found. Please Try Again." + Style.RESET_ALL)
        self.clear_screen()
        return edit_property_id_for_request.lower()

    # Completed. Can be beautified.
    def edit_repitive_work_request(self, work_request: object):
        """Repeatedly asks the user for a property ID they want to re-assign to the work request. Said input goes through the
        logic wrapper for verification and if it passes, the work request property ID attribute is updated with the one the user
        entered."""

        while (
            edit_repitive_work_request := input("Mark It Repitive? (Yes or No): ")
        ) not in ["q", "b", "Q", "B"]:

            # Sends the input to the logic wrapper for verification.
            is_repetitive_boolean = (
                self.logic_wrapper.sanity_check_boolean_input_work_requests(
                    edit_repitive_work_request
                )
            )
            if is_repetitive_boolean is False:
                print()
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    print()
                    print(Fore.RED + "Sigma Sigma on the wall, who is the Skibidiest of them all" + Style.RESET_ALL)
                    print()
                work_request.set_repetitive_work(is_repetitive_boolean)

                # If the request was marked repetitive, then it had a number of interval days that now needs to
                # be set back to 0.
                work_request.set_reopen_interval(0)

                # Sends the work request object with the new data to be the logic wrapper.
                self.logic_wrapper.edit_work_request(work_request)
                self.clear_screen()
                print()
                print(Fore.BLUE + "Work Request Has Been Marked Not Repetitive!" + Style.RESET_ALL)
                print()
                return ""
            
            if is_repetitive_boolean is True:
                print()
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()

                    print("Sigma Sigma on the wall, who is the Skibidiest of them all")
                work_request.set_repetitive_work(is_repetitive_boolean)
                self.clear_screen()
                print()
                print(Fore.BLUE + "Work Request Has Been Marked Repetitive!" + Style.RESET_ALL)
                print()
                return ""
            print(Fore.RED + "Input Must Be In The Form of Yes or No" + Style.RESET_ALL)
        self.clear_screen()
        return edit_repitive_work_request.lower()

    # Completed. Can be beautified.
    def edit_priority_for_request(self, work_request: object):
        """Repeatedly asks the user to enter one of 3 priorities they want to re-assign to the work request. Said input goes through the
        logic wrapper for verification and if it passes, the work request property ID attribute is updated with the one the user entered.
        """

        while (
            edit_priority_for_request := input(
                "Priority for Request? (High, Medium or Low): "
            )
        ) not in [
            "q",
            "b",
            "Q",
            "B",
        ]:
            # Sends the input to the logic wrapper for verification.
            is_priority_valid = self.logic_wrapper.sanity_check_priority_for_request(
                edit_priority_for_request
            )
            if is_priority_valid is True:
                print()
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    print()
                    print(Fore.RED + "Sigma Sigma on the wall, who is the Skibidiest of them all" + Style.RESET_ALL)
                    print()
                work_request.set_priority(edit_priority_for_request)
                # Sends the work request object with the new data to be the logic wrapper.
                self.logic_wrapper.edit_work_request(work_request)
                self.clear_screen()
                print()
                print(Fore.BLUE + "New Priority Has Been Assigned To The Work Request!" + Style.RESET_ALL)
                print()
                return ""
            print(Fore.RED + "Priority Given Must Be Either High, Medium or Low" + Style.RESET_ALL)
        self.clear_screen()
        return edit_priority_for_request.lower()

    # Completed. Can be beautified.
    def display_and_select_request_overview(self):
        """If the user logged in as an employee, then this will displays all the work requests have the employees staff ID attached to
        them. However if the user is an admin/manager, then this will display all work requests in their location, regardless of status
        """

        selected_work_request = ""
        while selected_work_request not in ["q", "b", "Q", "B"]:
            print()
            print("{:>50}".format("[ My Work Requests ]"))
            print("-" * 70)
            # Sorted list based on if the user is an employee or not
            my_work_request_list = self.logic_wrapper.get_my_work_requests(
                self.rank, self.location, self.staff_id
            )
            self.display_all_work_requests_printed(my_work_request_list)
            print()
            print("{:>10}".format("Back - [ b, B ]"))
            print("{:>10}".format("Quit - [ q, Q ]"))
            print("-" * 70)
            # Calls the function to search for a specific work request
            selected_work_request = self.search_work_request_menu_logistics()
        return selected_work_request.lower()

    # Completed. Can be beautifed.
    def display_and_select_new_work_requests(self):
        """Displays all new work requests that haven't been accepted by an employee in the current location that the user
        has selected."""

        selected_work_request = ""
        while selected_work_request not in ["q", "b", "Q", "B"]:
            print()
            print("{:>50}".format(Fore.BLUE + "[ New Work Requests ]" + Style.RESET_ALL))
            print("-" * 80)
            # Sorted list of all work requests who's status is "New"
            new_work_request_list = self.logic_wrapper.get_all_new_work_requests(
                self.location
            )
            self.display_all_work_requests_printed(new_work_request_list)
            print()
            print("{:>10}".format("Back - [ b, B ]"))
            print("{:>10}".format("Quit - [ q, Q ]"))
            print("-" * 70)
            # Calls the function to search for a specific work request
            selected_work_request = self.search_work_request_menu_logistics()
        return selected_work_request.lower()

    # Completed. Can be beautifed.
    def display_and_select_pending_work_requests(self):
        """Prints out all pending work requests that haven't been marked closed by a manager or an admin."""

        selected_work_request = ""
        while selected_work_request not in ["q", "b", "Q", "B"]:
            print()
            print("{:>50}".format(Fore.BLUE + "[ Pending Work Requests ]" + Style.RESET_ALL))
            print("-" * 80)
            # Sorted list of all work requests whos status is "Pending"
            pending_work_request_list = (
                self.logic_wrapper.get_all_pending_work_requests(
                    self.rank, self.location, self.staff_id
                )
            )
            self.display_all_work_requests_printed(pending_work_request_list)
            print()
            print("{:>10}".format("Back - [ b, B ]"))
            print("{:>10}".format("Quit - [ q, Q ]"))
            print("-" * 70)
            # Calls the function to search for a specific work request
            selected_work_request = self.search_work_request_menu_logistics()
        return selected_work_request.lower()

    # Completed. Can be beautifed.
    def display_and_select_closed_work_requests(self):
        """Displats all closed work requests. This option is only available to an admin or manager."""

        selected_work_request = ""
        while selected_work_request not in ["q", "b", "Q", "B"]:
            print()
            print("{:>50}".format(Fore.BLUE + "[ Closed Work Requests ]" + Style.RESET_ALL))
            print("-" * 80)
            # Sorted list of all work requests whos status is "Closed"
            closed_work_request_list = self.logic_wrapper.get_all_closed_work_requests(
                self.location
            )
            self.display_all_work_requests_printed(closed_work_request_list)
            print()
            print("{:>10}".format("Back - [ b, B ]"))
            print("{:>10}".format("Quit - [ q, Q ]"))
            print("-" * 70)

            # Calls the function to search for a specific work request
            selected_work_request = self.search_work_request_menu_logistics()
        return selected_work_request.lower()