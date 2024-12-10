from Model_Classes.work_request_model import WorkRequest


class work_request_UI_menu:
    def __init__(self, logic_wrapper, rank, location, staff_id):
        self.logic_wrapper = logic_wrapper
        self.rank = rank
        self.location = location
        self.staff_id = staff_id

    # Completed.
    def start_point_work_requests_UI(self) -> str:
        """When an instance of this class is created, the class object calls this function first which in
        turn calls the function to load the work request menu and it's options for the user.
        """

        work_request_menu = self.menu_selection_logistics()
        if work_request_menu in ["q", "b"]:
            return work_request_menu

    # Completed. Can be beautified.
    def display_all_work_requests_printed(self, work_request_list: list):
        """Prints out all open work requests with their ID, Name and Description."""

        if len(work_request_list) == 0:
            print()
            print("{:>50}".format("No Work Requests To Display"))
            print()
        else:
            print(
                "{:0}{:>6}{:>5}{:>9}{:>12}".format(
                    "ID", "|", "Name", "|", "Description"
                )
            )
            print("-" * 70)
            for item in sorted(work_request_list):
                print(
                    "{:0}{:>3}{:>10}{:>4}{:>51}".format(
                        item.work_request_id, "|", item.name, "|", item.description
                    )
                )
            print("-" * 70)

    # Completed. Can be beautified.
    def display_selected_work_request_information(self, work_request: object):
        """Receives a single, user-selected work request and displays all of its information for them to read."""

        print("-" * 70)
        print("{:0}{:>14}{:<10}".format("Categories", "|", "Details"))
        print("-" * 35)
        print(
            "{:0}{:>9}{:<10}".format(
                "Work Request ID", "|", work_request.work_request_id
            )
        )
        print("{:0}{:>20}{:<10}".format("Name", "|", work_request.name))
        print("{:0}{:>13}{:<10}".format("Description", "|", work_request.description))
        print("{:0}{:>16}{:<10}".format("Location", "|", work_request.location))
        print("-" * 35)
        print(
            "{:0}{:>3}{:>10}".format(
                "Maintenance Report ID", "|", work_request.maintenance_report_id
            )
        )
        print("{:0}{:>16}{:<10}".format("Employee ID", "|", work_request.staff_id))
        print("{:0}{:>13}{:<10}".format("Property ID", "|", work_request.property_id))
        print(
            "{:0}{:>11}{:<10}".format("Contractor ID", "|", work_request.contractor_id)
        )
        print("-" * 35)
        print("{:0}{:>14}{:<10}".format("Start Date", "|", work_request.start_date))
        print(
            "{:0}{:>7}{:<10}".format(
                "Completition Date", "|", work_request.completition_date
            )
        )
        print(
            "{:0}{:>9}{:<10}".format(
                "Repititive Work", "|", str(work_request.repetitive_work)
            )
        )
        print(
            "{:0}{:>3}{:<10}".format(
                "Re-Open Interval Days", "|", work_request.reopen_interval
            )
        )
        print("-" * 35)
        print("{:0}{:>16}{:<10}".format("Priority", "|", work_request.priority))
        print("{:0}{:>7}{:<10}".format("Status", "|", work_request.work_request_status))
        print(
            "{:0}{:>7}{:<10}".format(
                "Needs Contractor", "|", str(work_request.need_contractor)
            )
        )
        print(
            "{:0}{:>11}{:<10}".format(
                "Completed", "|", str(work_request.mark_as_completed)
            )
        )
        print(
            "{:0}{:>4}{:<10}".format(
                "Accepted by Employee", "|", str(work_request.accepted_by_employee)
            )
        )
        print("-" * 70)

    # Completed. Can be beautified.
    def display_work_requests_menu_items(self) -> str:
        """Displays all open work requests and menu options depending on if the user logged in is an admin/manager
        or an employee. It then asks the user to select an option which is sent to be verified in the function
        below."""

        print()
        print(f"{self.rank} - Work Request Menu")
        print("-" * 70)
        print("{:>50}".format("[ Open and Ongoing Work Requests ]"))
        print()
        work_request_list = self.logic_wrapper.get_all_work_requests_at_location(
            self.rank, self.location, self.staff_id
        )
        self.display_all_work_requests_printed(work_request_list)
        if self.rank != "Employee":
            print(
                "{:0}{:>3}{:>15}{:>3}{:>19}".format(
                    "1. Select Request",
                    "|",
                    "2. Add Request",
                    "|",
                    "3. New Requests",
                )
            )
            print(
                "{:0}{:>3}{:>20}{:>3}{:>19}".format(
                    "4. Pending Requests", "|", "5. All Requests", "|", "6. Closed Requests"
                )
            )
            print()
            print("{:>20}".format("> Go Back: b, B"))
            print("{:>20}".format("> Quit System: q, Q"))
            print()
        else:
            print("{:0}{:>3}{:>20}".format("1. Select Request", "|", "2. New Requests"))
            print(
                "{:0}{:>3}{:>20}".format("3. Pending Requests", "|", "4. My Requests")
            )
            print()
            print("{:>20}".format("> Go Back: b, B"))
            print("{:>20}".format("> Quit System: q, Q"))
            print()
        user_choice = input("Select an Option: ").lower()
        return user_choice

    # Completed. Can be beautified.
    def menu_selection_logistics(self) -> str:
        """Calls the menu display function above and performs low-level logicistics to interpret the user input it received.
        If it's verified as an invalid input the system displays an error message and performs the operation again.
        """

        user_choice = ""
        while user_choice != "q":
            user_choice = self.display_work_requests_menu_items()
            match (user_choice, self.rank):
                case ("1", self.rank):
                    user_choice = self.select_work_request_by_id()

                case ("2", "Admin") | ("2", "Manager"):
                    user_choice = self.display_create_work_request_form()

                case ("2", "Employee") | ("3", "Admin") | ("3", "Manager"):
                    user_choice = self.display_and_select_new_work_requests()

                case ("3", "Employee") | ("4", "Admin") | ("3", "Manager"):
                    user_choice = self.display_and_select_pending_work_requests()

                case ("5", "Admin") | ("5", "Manager"):
                    user_choice = self.display_and_select_closed_work_requests()

                case ("4, Employee") | ("6", "Admin") | ("6", "Manager"):
                    user_choice = self.display_and_select_request_overview()

                case ("b", self.rank):
                    return "b"
                case ("q", self.rank):
                    return "q"
                case _:
                    print("Invalid Input, Please Try Again.")
        return user_choice

    # Completed. Can be beautified.
    def select_work_request_by_id(
        self, status: str = "", accepted_by_employee: bool = True
    ) -> str:
        """System asks the user to enter an ID of the work request they wish to select. If found, the system
        will display all of its information and directs them to the editing function below. Otherwise it gives
        an error message and restarts its operation."""

        while (
            work_request_selected := input("Enter Request ID: ")
        ) not in ["q", "b", "Q", "B"]:
            # if work_request_selected.lower() in ["b", "B"]:
            #     break
            if len(work_request_selected) < 3:
                print()
                print("Must Enter A Valid Work Request ID")
                print()
            if self.rank == "Employee":
                status = "Open"
            work_request = self.logic_wrapper.get_work_request_by_id(
                self.location,
                work_request_selected,
                status,
                accepted_by_employee
            )
            if work_request is not None:
                self.display_selected_work_request_information(work_request)
                edit_work_request = self.edit_work_request_logistics(work_request)
                if edit_work_request == "b":
                    continue
                return edit_work_request.lower()
            print()
            print("Work Request Can't Be Accessed At The Moment, Please Try Again.")
            print()
        return work_request_selected.lower()

    # Completed. Can be beautified.
    def edit_work_request_logistics(self, work_request_object) -> str:
        """Receives a single, user-selected work request and gives the user the ability to edit its information;
        the extent of which corresponding to the user's rank. Also verifies what can be edited based on what the
        work requests attributes are set as."""

        if self.rank != "Employee":
            edit_work_request = self.general_edit_work_request_selected_option(
                work_request_object
            )
            return edit_work_request.lower()

        if (
            work_request_object.mark_as_completed is True
            and work_request_object.work_request_status == "Pending"
        ):
            print()
            print("{:>20}".format("> Go Back: b, B"))
            print("{:>20}".format("> Quit System: q, Q"))
            print()
            while (
                go_back_or_quit := input("Select an Option: ").lower()
            ) not in ["q", "b"]:
                print()
                print("Nah Ah, You Can't Do That...")
                print()
            return go_back_or_quit.lower()

        if (
            work_request_object.accepted_by_employee is False
            and work_request_object.work_request_status == "New"
        ):
            accept_work_request = self.employee_accept_work_request_(
                work_request_object
            )
            return accept_work_request.lower()

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

        new_work_request = WorkRequest()
        print()
        print("[ New Work Request Form ]")
        print("-" * 70)
        print()
        print("{:>15}".format("> Go Back: b, B"))
        print("{:>20}".format("> Quit System: q, Q"))
        print()
        print("-" * 70)
        request_name = self.set_name_for_request(new_work_request)
        return request_name

    # Completed. Can be beautified.
    def set_name_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter a name for the work request they are creating. Goes through very simple input
        verification before setting the name attribute to what the user entered and passing the object down
        to the next function."""

        while (request_name := input("Request Name: ")) not in ["q", "b", "Q", "B"]:
            is_name_valid = self.logic_wrapper.sanity_check_low_level_logistics('name', request_name)
            if is_name_valid is True:
                new_work_request.set_name(request_name)
                request_description = self.set_description_for_request(new_work_request)
                if request_description == "b":
                    continue
                return request_description
            print()
            print("Invalid Input")
            print()
        return request_name.lower()

    # Completed. Can be beautified.
    def set_description_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter a description for the work request they are creating. Goes through very simple input
        verification before setting the description attribute to what the user entered and passing the object down
        to the next function."""

        while (request_description := input("Request Descriptition: ")) not in ["q", "b", "Q", "B"]:
            is_description_valid = self.logic_wrapper.sanity_check_low_level_logistics('description', request_description)
            if is_description_valid is True:
                new_work_request.set_description(request_description)
                property_id = self.set_property_id_for_request(new_work_request)
                if property_id == "b":
                    continue
                return property_id
            print()
            print("Invalid Input")
            print()
        return request_description.lower()

    # Completed. Can be beautified.
    def set_property_id_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter the property ID for the work request they are creating. Its then sent to the logic
        layer where the input is verified. If its verified as valid, it sets the property ID attribute to what the user
        entered before passing the object down to the next function. Otherwise it begins the operation again.
        """

        while (
            property_id := input("Assign A Property ID To The Request: ")
        ) not in ["q", "b", "Q", "B"]:
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
            print("Invalid Input")
            print()
        return property_id.lower()
            

    # Completed. Can be beautified.
    def set_start_date_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter the start date for the work request they are creating. Goes through very simple input
        verification before setting the start date attribute to what the user entered and passing the object down to
        the next function."""

        while (
            start_date := input("Set The Start Date: ")
        ) not in ["q", "b", "Q", "B"]:
            is_start_date_valid = self.logic_wrapper.sanity_check_low_level_logistics('start_date', start_date)
            if is_start_date_valid is True:
                new_work_request.set_start_date(start_date)
                completition_date = self.set_completition_date_for_request(
                    new_work_request
                )
                if completition_date == "b":
                    continue
                return completition_date
            print()
            print("Invalid Input")
            print()
        return start_date.lower()

    # Completed. Can be beautified.
    def set_completition_date_for_request(self, new_work_request: object) -> str:
        """Asks the user to enter the completition date for the work request they are creating. Goes through very simple input
        verification where, it has to either be nothing (since this field is not required to fill out) or exactly 8 characters long.
        The completion date attribute is then set to what the user entered and the object passed down to the next function.
        """

        while (
            completition_date := input("Set The Completition Date (Not Required): ")
        ) not in ["q", "b", "Q", "B"]:
            is_completition_date_valid = self.logic_wrapper.sanity_check_low_level_logistics('completition_date', completition_date)
            if is_completition_date_valid is True:
                new_work_request.set_completition_date(completition_date)
                repetitive_work = self.set_repetitive_work_for_request(new_work_request)
                if repetitive_work == "b":
                    continue
                return repetitive_work
            print()
            print("Completition Date Must Be Formatted Correctly")
            print()
        return completition_date.lower()

    # Completed. Can be beautified.
    def set_repetitive_work_for_request(self, new_work_request: object) -> str:

        while (
            repetitive_work := input("Mark Request Repititive? (Yes or No): ")
        ) not in ["q", "b", "Q", "B"]:
            is_set_repetitive_boolean = (
                self.logic_wrapper.sanity_check_boolean_input_work_requests(
                    repetitive_work
                )
            )
            if is_set_repetitive_boolean is True or is_set_repetitive_boolean is False:
                new_work_request.set_repetitive_work(is_set_repetitive_boolean)
                interval_days = self.set_interval_days_for_request(new_work_request)
                if interval_days == "b":
                    continue
                return interval_days
            print()
            print("Invalid Input")
            print()
        return repetitive_work.lower()

    # Completed. Can be beautified.
    def set_interval_days_for_request(self, new_work_request: object):
        while (
            interval_days := input("Set The Interval Of Days Until Request Re-Opens: ")
        ) not in ["q", "b", "Q", "B"]:                
            is_interval_days_valid = self.logic_wrapper.sanity_check_low_level_logistics('completition_date', interval_days)
            if is_interval_days_valid is True:
                new_work_request.set_reopen_interval(interval_days)
                set_priority = self.set_priority_for_request(new_work_request)
                if set_priority == "b":
                    continue
                return set_priority
            print()
            print("Invalid Input")
            print()
            continue
        return interval_days.lower()

    # Completed. Can be beautified.
    def set_priority_for_request(self, new_work_request: object):
        while (
            set_priority := input("Set The Request Priority (High, Medium or Low): ")
        ) not in ["q", "b", "Q", "B"]:
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
            print("Invalid Input")
            print()
        return set_priority.lower()

    # Completed. Can be beautified.
    def set_needs_contractor_for_request(self, new_work_request: object):
        while (
            needs_contractor := input("Request Needs Contractor? (Yes or No): ")
        ) not in ["q", "b", "Q", "B"]:
            is_needs_contractor_boolean = (
                self.logic_wrapper.sanity_check_boolean_input_work_requests(
                    needs_contractor
                )
            )
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
            print("Invalid Input")
            print()
        return needs_contractor.lower()

    # Completed. Can be beautified.
    def set_location_for_request(self, new_work_request: object):
        if self.rank == "Admin":
            while (
                set_location := input("Set Location for Work Request: ")
            ) not in ["q", "b", "Q", "B"]:
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
                print("Invalid Input")
                print()
            return set_location.lower()
        new_work_request.set_location(self.location)

    # Completed. Can be beautified.
    def work_request_confirmation(self, new_work_request: object) -> str:
        print()
        while (
            new_work_request_confirmation := input("Enter 1 to Confirm: ").lower()) != "1":
            if new_work_request_confirmation in ["q", "b", "Q", "B"]:
                return new_work_request_confirmation.lower()
            print("Sigma Sigma on the wall, who is the Skibidiest of them all")
        print("-" * 70)
        print()
        new_work_request.set_work_request_status("New")
        self.logic_wrapper.add_work_request(new_work_request)
        print("Work Request Has Been Created!")
        print()
        return ""

    # Completed. Can be beautified.
    def employee_accept_work_request_(self, work_request: object):
        """Allows the employee accept a new work request."""

        print("{:>20}".format("> Go Back: b, B"))
        print("{:>20}".format("> Quit System: q, Q"))
        print()
        print("-" * 70)

        while (
            accept_work_request := input("Aceept (Yes or No): ")
        ) not in ["q", "b", "Q", "B"]:
            if len(accept_work_request) < 2:
                print()
                print("This Field Is Required to Fill Out.")
                print()

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
                work_request.set_accepted_by_employee(is_accepted_boolean)
                work_request.set_staff_id(self.staff_id)
                self.logic_wrapper.edit_work_request(work_request)
                print()
                print("Work Request Has Been Accepted!")
                print()
                return
            else:
                print("Invalid")

            if is_accepted_boolean is False:
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    print("Mama they took my dingus")
                work_request.set_accepted_by_employee(is_accepted_boolean)
                self.logic_wrapper.edit_work_request(work_request)
                print()
                print("Work Request Has Been Rejected!")
                print()
                return
            else:
                print("Invalid")
        return accept_work_request.lower()

    # Completed. Can be beautified.
    def mark_work_request_completed(self, work_request: object):
        """Allows the user to mark a work request completed."""

        print()
        print("-" * 70)
        print()
        print("{:>20}".format("> Go Back: b, B"))
        print("{:>20}".format("> Quit System: q, Q"))
        print()
        print("-" * 70)
        while (
            mark_as_completed := input("Mark as Completed (Yes or No): ")
        ) not in ["q", "b", "Q", "B"]:
            if len(mark_as_completed) < 2:
                print()
                print("Invalid")
                print()
            while (
                completition_date := input("Set The Completition Date: ")
            ) not in ["q", "b", "Q", "B"]:
                if len(completition_date) == 8:
                    work_request.set_completition_date(completition_date)
                else:
                    print()
                    print("Completition Date Must Be Formatted Correctly")
                    print()
            if completition_date in ["q", "b", "Q", "B"]:
                return completition_date.lower()

            is_marked_completed_boolean = (
                self.logic_wrapper.sanity_check_boolean_input_work_requests(
                    mark_as_completed
                )
            )
            if is_marked_completed_boolean is True:
                print()
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    print("Mama they took my dingus")
                work_request.set_mark_as_done(is_marked_completed_boolean)
                if self.rank == "Employee":
                    work_request.set_work_request_status("Pending")
                else:
                    work_request.set_work_request_status("Closed")
                self.logic_wrapper.edit_work_request(work_request)
                print()
                print("Work Request Has Been Marked Completed!")
                print()
                break

            if is_marked_completed_boolean is False:
                print()
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    print("Mama they took my dingus")
                work_request.set_mark_as_done(is_marked_completed_boolean)
                work_request.set_work_request_status("Open")
                self.logic_wrapper.edit_work_request(work_request)
                print()
                print("Work Request Has Been Marked Not Completed.")
                print()
                break
            else:
                print("Mama they took my dingus")
        return mark_as_completed.lower()

    # Completed. Can be beautified.
    def general_edit_work_request_menu(self) -> str:
        """Displays all the categories that an admin or manager are able to edit about a work request they have selected.
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
        print("{:>18}".format("> Go Back: b, B"))
        print("{:>18}".format("> Quit System: q, Q"))
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
            category_to_edit = self.general_edit_work_request_menu()
            match category_to_edit:
                case "1":
                    category_to_edit = self.edit_employee_id_for_work_request(
                        work_request
                    )
                case "2":
                    category_to_edit = self.edit_property_id_for_request(work_request)
                case "3":
                    category_to_edit = self.edit_repitive_work_request(work_request)
                case "4":
                    category_to_edit = self.edit_priority_for_request(work_request)
                case "5":
                    category_to_edit = self.mark_work_request_completed(work_request)
                case "b":
                    return "b"
                case "q":
                    return "q"
                case _:
                    print("Mama they took my dingus")
        return category_to_edit.lower()

    # Completed. Can be beautified.
    def edit_employee_id_for_work_request(self, work_request: object):

        while (
            edit_employee_id_for_request := input("New Employee ID: ")
        ) not in ["q", "b", "Q", "B"]:
            is_employee_valid = self.logic_wrapper.sanity_check_staff_id(
                edit_employee_id_for_request
            )
            if is_employee_valid is True:
                print()
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    else:
                        print(
                            "Sigma Sigma on the wall, who is the Skibidiest of them all"
                        )
                work_request.set_staff_id(edit_employee_id_for_request)
                self.logic_wrapper.edit_work_request(work_request)
                return
            else:
                print("Mama they took my dingus")
        return edit_employee_id_for_request.lower()

    # Completed. Can be beautified.
    def edit_property_id_for_request(self, work_request: object):
        while (edit_property_id_for_request := input("New Property ID: ")
        ) not in ["q", "b", "Q", "B"]:
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
                    else:
                        print(
                            "Sigma Sigma on the wall, who is the Skibidiest of them all"
                        )
                work_request.set_property_id(edit_property_id_for_request)
                self.logic_wrapper.edit_work_request(work_request)
                return
            else:
                print("Mama they took my dingus")
        return edit_property_id_for_request.lower()

    # Completed. Can be beautified.
    def edit_repitive_work_request(self, work_request: object):
        while (
            edit_repitive_work_request := input("Is Repitive? (Yes or No): ")
        ) not in ["q", "b", "Q", "B"]:
            is_repetitive_boolean = (
                self.logic_wrapper.sanity_check_boolean_input_work_requests(
                    edit_repitive_work_request
                )
            )
            if is_repetitive_boolean is True or is_repetitive_boolean is False:
                print()
                while (
                    update_confirmation := input("Enter 1 to Confirm: ").lower()
                ) != "1":
                    if update_confirmation in ["q", "b", "Q", "B"]:
                        return update_confirmation.lower()
                    
                    print(
                        "Sigma Sigma on the wall, who is the Skibidiest of them all"
                        )
                work_request.set_repetitive_work(is_repetitive_boolean)
                self.logic_wrapper.edit_work_request(work_request)
                return        
            print("Mama they took my dingus")
        return edit_repitive_work_request.lower()

    # Completed. Can be beautified.
    def edit_priority_for_request(self, work_request: object):
        while (
            edit_priority_for_request := input("Priority for Request: ")
        ) not in ["q", "b", "Q", "B"]:
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
                    print(
                        "Sigma Sigma on the wall, who is the Skibidiest of them all"
                        )
                work_request.set_priority(edit_priority_for_request)
                self.logic_wrapper.edit_work_request(work_request)
                return
            print("Mama they took my dingus")
        return edit_priority_for_request.lower()

    """The functions below could very well be combined into one, larger function. """

    # Completed. Can be beautified.
    def display_and_select_request_overview(self):
        """Displays all work requests that have been accepted by an employee."""

        status = ""
        accepted_by_employee = True
        selected_work_request = ""
        while selected_work_request not in ["q", "b", "Q", "B"]:
            print()
            print("{:>50}".format("[ My Work Requests ]"))
            print("-" * 70)
            my_work_request_list = self.logic_wrapper.get_my_work_requests(
                self.rank, self.location, self.staff_id
            )
            self.display_all_work_requests_printed(my_work_request_list)
            print()
            print("{:>15}".format("> Go Back: b, B"))
            print("{:>18}".format("> Quit System: q, Q"))
            print("-" * 70)
            selected_work_request = self.select_work_request_by_id(
                status, accepted_by_employee
            )
        return selected_work_request.lower()

    # Completed. Can be beautifed.
    def display_and_select_new_work_requests(self):
        """Displays all new work requests that haven't been accepted by an employee."""

        status = "New"
        accepted_by_employee = False
        selected_work_request = ""
        while selected_work_request not in ["q", "b", "Q", "B"]:
            print()
            print("{:>50}".format("[ New Work Requests ]"))
            print("-" * 70)
            new_work_request_list = self.logic_wrapper.get_all_new_work_requests(
                self.location
            )
            self.display_all_work_requests_printed(new_work_request_list)
            print()
            print("{:>15}".format("> Go Back: b, B"))
            print("{:>18}".format("> Quit System: q, Q"))
            print("-" * 70)
            selected_work_request = self.select_work_request_by_id(
                status, accepted_by_employee
            )
        return selected_work_request.lower()

    # Completed. Can be beautifed.
    def display_and_select_pending_work_requests(self):
        """Prints out all pending work requests that haven't been marked closed by a manager or admin."""

        status = "Pending"
        accepted_by_employee = True
        selected_work_request = ""
        while selected_work_request not in ["q", "b", "Q", "B"]:
            print()
            print("{:>50}".format("[ Pending Work Requests ]"))
            print("-" * 70)
            pending_work_request_list = (
                self.logic_wrapper.get_all_pending_work_requests(
                    self.rank, self.location, self.staff_id
                )
            )
            self.display_all_work_requests_printed(pending_work_request_list)
            print()
            print("{:>15}".format("> Go Back: b, B"))
            print("{:>18}".format("> Quit System: q, Q"))
            print("-" * 70)
            selected_work_request = self.select_work_request_by_id(
                status, accepted_by_employee
            )
        return selected_work_request.lower()

    # Completed. Can be beautifed.
    def display_and_select_closed_work_requests(self):
        """Displats all closed work requests."""

        status = "Closed"
        accepted_by_employee = True
        selected_work_request = ""
        while selected_work_request not in ["q", "b", "Q", "B"]:
            print()
            print("{:>50}".format("[ Closed Work Requests ]"))
            print("-" * 70)
            closed_work_request_list = self.logic_wrapper.get_all_closed_work_requests(
                self.location
            )
            self.display_all_work_requests_printed(closed_work_request_list)
            print()
            print("{:>20}".format("> Go Back: b, B"))
            print("{:>20}".format("> Quit System: q, Q"))
            print("-" * 70)
            selected_work_request = self.select_work_request_by_id(
                status, accepted_by_employee
            )
        return selected_work_request.lower()