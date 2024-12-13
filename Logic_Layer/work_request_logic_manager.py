from datetime import datetime as dt
from datetime import date, timedelta


class work_request_logic_manager:

    def __init__(self, Storage_Layer_Wrapper):
        """Constructor for work request logic manager"""
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

    def sanity_check_work_request_property_id(self, property_id: str) -> bool:
        """Gets all properties from storage and compares the property ID given by the user and compares it
        to the ones that already exist."""

        all_properties = self.Storage_Layer_Wrapper.get_all_properties_at_location()
        for property in all_properties:
            if property.property_id == property_id:
                return True
        return False

    def sanity_check_boolean_input_work_requests(self, yes_or_no: str) -> bool:
        """Takes the input given by the user and returns True or False based on if the user had entered spefically
        yes/Yes or no/No. Otherwise it returns None."""

        if len(yes_or_no) < 2:
            return None
        match yes_or_no:
            case "yes" | "Yes":
                return True
            case "no" | "No":
                return False
            case _:
                return None

    def sanity_check_priority_for_request(self, priority: str) -> bool:
        """Takes the input given by the user and returns True if the user had entered spefically low/Low, medium/Medium
        or high/High. Otherwise it returns False."""

        match priority:
            case "high" | "High":
                return True
            case "medium" | "Medium":
                return True
            case "low" | "Low":
                return True
            case _:
                return False

    def sanity_check_request_low_level_logistics(
        self, category: str, value_to_be_verified: str
    ) -> bool:
        """Performs very simple logistics to verify user input, can be expanded to perform higher level logistics.
        bool: True if the user input passes the logisitics, False otherwise."""
        
        if category == "name":
            if len(value_to_be_verified) < 5:
                return False
            return True

        if category == "description":
            if len(value_to_be_verified) < 10:
                return False
            return True

        # Since the re-open interval days are only categorized after day, week and month
        # the logistics checks if the input given matches that. 
        if category == "reopen_interval":
            try:
                if int(value_to_be_verified) == 1:
                    return True
                if int(value_to_be_verified) == 7:
                    return True
                if int(value_to_be_verified) == 30:
                    return True
            except ValueError:
                return False

    def sanity_check_start_date(self, start_date_given: str) -> bool:
        """Checks if the start date given is 1. formatted correctly (DD-MM-YY) and 2. if it takes place or on the same day
        as the current date. A start can't happen in the past. Returns True if it passes both conditions, else False."""

        try:
            # Imported two modules to perform the logistics, able to compare two given dates including the current date.
            start_date = dt.strptime(start_date_given,"%d-%m-%y")
            current_date = dt.today()
            if start_date >= current_date:
                return True
            return False
        except ValueError:
            return False

    def sanity_check_completition_date(
        self, start_date: str, completition_date_given: str
    ) -> bool:
        """Checks if the completition date given is 1. formatted correctly (DD-MM-YY) and 2. if it takes place after or on the 
        same day as the start date. Returns True if it passes both conditions, else False. """

        try:
            start_date_to_compare = dt.strptime(start_date, "%d-%m-%y")
            completition_date_to_compare = dt.strptime(
                completition_date_given, "%d-%m-%y"
            )
            if completition_date_to_compare >= start_date_to_compare:
                return True
            return False
        except ValueError:
            return False

    def sanity_check_location_for_request(self, set_location: str) -> bool:
        """Gets all locations from storage and compares the input given by the user to the location names that already exist.
        If the one given matches with one in the storage, it returns True. Otherwise False. """

        all_locations = self.Storage_Layer_Wrapper.get_all_locations()
        for location in all_locations:
            if location.location == set_location:
                return True
        return False



    def sanity_check_employee_id_for_request(self, staff_id: str) -> bool:
        """Gets all employees from storage and compares the employee ID given by the user to the ones that already exist.
        If the one given matches with one in the storage, it returns True. Otherwise False. """

        all_employees = self.Storage_Layer_Wrapper.get_all_employees()
        for employee in all_employees:
            if employee.staff_id == staff_id:
                return True
        return False

    def set_id_for_work_request(self, Work_request: object) -> str:
        """Sets a new ID for a the work request that has been created."""

        # Initialises the ID to -1
        highest_id = -1
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:

            # Slices the work request ID string to only store the numbers 
            # that proceed WR in the variable.

            stripped_id = work_request.work_request_id[2:]

            highest_id = max(highest_id, int(stripped_id))

            # With each iteration, the highest ID is raised by 1 up until it 
            # reaches the end of the list.

        highest_id += 1
        new_work_request_id = "WR" + str(highest_id)
        Work_request.set_work_request_id(new_work_request_id)
        # Returns the work request now with the highest ID
        return Work_request


    def auto_re_open_work_request(self, work_request: object):
        """When an admin/manager marks a work request complete and said request is also set as repetitive True, it's first 
        passed to the edit request function where it's edited and then it's passed to this function where it is "re-added" 
        to the storage as the same request, only updated. """

        # Stores the interval days and start date values of the work request in two variables.
        interval_days = work_request.reopen_interval
        start_date = work_request.start_date

        # Using the dt.strptime and timedelta functions the date is converted to an integer that 
        # follows the conditions of the datetime system. 
        start_date_to_manipulate = dt.strptime(start_date, "%d-%m-%y")

        # The interval days are then added to the initial start date and a new start date is set.
        new_date = start_date_to_manipulate + timedelta(days=interval_days)

        # The new start date is then formatted once more to a string that follows the (DD-MM-YY)
        # format guidelines.
        new_date_formated = date.strftime(new_date, "%d-%m-%y")

        # The work request attributes below are then are then re-set before it is passed to the 
        # add to storage function.
        # Once there, it receives a new ID and is added to the storage.
        work_request.set_start_date(new_date_formated)
        work_request.set_work_request_id("")
        work_request.set_work_request_status("Open")
        work_request.set_completition_date("")
        self.add_work_request(work_request)

    def add_work_request(self, Work_request: object):
        """Adds a work request to the storage layer."""

        # Aets the ID for the work request and appends it to the list of all work requests 
        # before being sent to the storage wrapper where it's written into the file.
        Work_request_with_id = self.set_id_for_work_request(Work_request)
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        all_work_requests.append(Work_request_with_id)
        self.Storage_Layer_Wrapper.write_to_file_work_requests(all_work_requests)

    def edit_work_request(self, Work_request: object):
        """Receives a work request from the user that is compared to the one's in the storage before it takes 
        it's place and the list written back into storage. """

        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        # Iterates over the list of all work requests and finds the one with with the same ID as the one 
        # that was passed to this function. 
        for position, request in enumerate(all_work_requests):
            if request.work_request_id == Work_request.work_request_id:
                # Once found, the new work request takes the place of it's matching counterpart in the list.
                all_work_requests[position] = Work_request
        self.Storage_Layer_Wrapper.write_to_file_work_requests(all_work_requests)

    def get_work_request_by_date(
        self, rank: str, staff_id: str, location: str, work_request_date: str
    ) -> object:
        """Receives the rank of the user, their staff ID,  location and the given date to determine what request is sent back
        to the UI layer. By iterating over all work requests and comparing the values given and the ones in the storage, it returns
        the fist one that matches all. """

        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:
            # If the user is an admin/manager then they have access to all work requests in their location while
            # an employee does not. Only compares the given location and date.
            if rank != "Employee":
                if work_request.location == location and work_request_date in [
                    work_request.start_date,
                    work_request.completition_date,
                ]:
                    return work_request
            else:
                # If the user is an employee then they only have access to work requests they are attached to. On top of 
                # comparing the given location and date it will also compare the given staff ID so it can only find one 
                # that fulfills all three conditions.
                if (
                    work_request.staff_id == staff_id
                    and work_request.location == location
                    and work_request_date
                    in [work_request.start_date, work_request.completition_date]
                ):
                    return work_request

    def get_work_request_by_id(
        self, rank: str, staff_id: str, location: str, work_request_id: str,
    ) -> object:
        """Receives the rank of the user, their staff ID, location and work request ID to determine what request is sent back to
        the UI layer. By iterating over all work requests and comparing the values given and the ones in the storage, it returns
        the only one that matches all. """
         
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        
        for work_request in all_work_requests:
            # If the user is an admin/manager then they have access to all work requests in their location while
            # an employee does not. Only compares the given location and work request ID.
            if rank != "Employee":
                if (
                    work_request.location == location
                    and work_request.work_request_id == work_request_id
                ):
                    # Returns the work request that meets both conditions or none if no work request meets these conditions.
                    return work_request
            else:
                # If the user is an employee then they only have access to work requests they are attached to. On top of
                # comparing the given location and work request ID it will also compare the given staff ID so it can find
                # the only one that fulfills all three conditions.
                if (
                    work_request.staff_id == staff_id
                    and work_request.location == location
                    and work_request.work_request_id == work_request_id
                ):
                    # Returns the work request that meets all 3 conditions or none if no work request meets these conditions.
                    return work_request

    def get_all_work_requests_at_location(
        self, rank: str, location: str, staff_id: str
    ) -> list:
        """Receives the rank of the user, their staff ID and location to determine what requests are sent back to the UI layer. 
        By iterating over all work requests and comparing the values given and the ones in the storage, it returns a list of ones
        that meet all conditions. """

        # Creates an empty list that will only contain work requests that have met all 3 conditions.
        work_request_sorted_list = []
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:
            # If the user is an admin/manager then they have access to all open work requests in their location
            # while an employee does not. Only compares the given location, that they have been accepted by
            # employee and that their status is "Open".
            if rank != "Employee":
                if (
                    work_request.location == location
                    and work_request.accepted_by_employee is True
                    and work_request.work_request_status == "Open"
                ):
                    # Appends all work requests that meet all 3 conditions.
                    work_request_sorted_list.append(work_request)
            else:
                # If the user is an employee then they only have access to work requests they are attached to. On top of
                # comparing the given location, that they have been accepted by employee and that their status is "Open", 
                # it will also compare the given staff ID.
                if (
                    work_request.location == location
                    and work_request.accepted_by_employee is True
                    and work_request.work_request_status == "Open"
                    and work_request.staff_id == staff_id
                ):
                    # Appends all work requests that meet all 4 conditions.
                    work_request_sorted_list.append(work_request)

        # Retuns either an empty list or one that contains only the work requests that met all conditions given.
        return work_request_sorted_list

    def get_my_work_request(self, rank: str, location: str, staff_id: str) -> list:
        """Receives the rank of the user, their staff ID and location to determine what requests are sent back to the UI layer. 
        By iterating over all work requests and comparing the values given and the ones in the storage, it returns a list of ones
        that meet all conditions. """

        work_request_sorted_list = []
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:
            # If the user is an admin/manager then they have access to all open work requests in their location
            # while an employee does not. Only compares the given location and that they have been accepted by
            # employee.
            if rank != "Employee":
                if (
                    work_request.location == location
                    and work_request.accepted_by_employee is True
                ):
                    # Appends all work requests that meet both conditions.
                    work_request_sorted_list.append(work_request)
            else:
                # If the user is an employee then they only have access to work requests they are attached to. On top of
                # comparing the given location and that they have been accepted by employee, it will also compare the given staff ID.
                if (
                    work_request.location == location
                    and work_request.accepted_by_employee is True
                    and work_request.staff_id == staff_id
                ):
                    # Appends all work requests that meet all 3 conditions.
                    work_request_sorted_list.append(work_request)
       
        # Retuns the list that contains only the work requests that met all conditions given.
        return work_request_sorted_list

    def get_all_closed_work_requests_in_storage(self, location: str) -> list:
        """Receives the rank of the user and location to determine what requests are sent back to the UI layer. By iterating
        over all work requests and comparing the values given and the ones in the storage, it returns a list of ones that 
        meet all conditions. """
    
        work_request_sorted_list = []
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:
            # Only compares the given location, that they have been accepted by
            # employee and that their status is "Closed".
            if (
                work_request.location == location
                and work_request.work_request_status == "Closed"
                and work_request.accepted_by_employee is True
            ):
                # Appends all work requests that meet all 3 conditions.
                work_request_sorted_list.append(work_request)

        # Retuns either an empty list or one that contains only the work requests that met all conditions given.
        return work_request_sorted_list

    def get_all_pending_work_requests_in_storage(
        self, rank: str, location: str, staff_id: str
    ) -> list:
        """Receives the rank of the user, their staff ID and location to determine what requests are sent back to the UI layer. 
        By iterating over all work requests and comparing the values given and the ones in the storage, it returns a list of ones
        that meet all conditions. """

        work_request_sorted_list = []
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        # checks if the work request is pending, accepted by employee and the location is the same
        for work_request in all_work_requests:
            # If the user is an admin/manager then they have access to all open work requests in their location
            # while an employee does not. Only compares the given location, that they have been accepted by
            # employee and that their status is "Pending".
            if rank != "Employee":
                if (
                    work_request.location == location
                    and work_request.work_request_status == "Pending"
                    and work_request.accepted_by_employee is True
                ):
                    # Appends all work requests that meet all 4 conditions.
                    work_request_sorted_list.append(work_request)
            else:
                # If the user is an employee then they only have access to work requests they are attached to. On top of
                # comparing the given location, that they have been accepted by employee and that their status is "Pending",
                # it will also compare the given staff ID.
                if (
                    work_request.location == location
                    and work_request.work_request_status == "Pending"
                    and work_request.accepted_by_employee is True
                    and work_request.staff_id == staff_id
                ):
                    # Appends all work requests that meet all 4 conditions.
                    work_request_sorted_list.append(work_request)

        # Retuns either an empty list or one that contains only the work requests that met all conditions given.
        return work_request_sorted_list

    def get_all_new_work_requests_in_storage(self, location: str) -> list:
        """Receives a location to determine what requests are sent back to the UI layer. By iterating over all work requests
        and comparing the values given and the ones in the storage, it returns a list of ones that meet all conditions. """

        work_request_sorted_list = []
        all_work_requests = self.Storage_Layer_Wrapper.get_all_work_requests()
        for work_request in all_work_requests:
            # Only compares the given location, that they have been accepted by employee and that their status is "New".
            if (
                work_request.location == location
                and work_request.work_request_status == "New"
                and work_request.accepted_by_employee is False
            ):
                # Appends all work requests that that meet all 3 conditions.
                work_request_sorted_list.append(work_request)

        # Retuns either an empty list or one that contains only the work requests that met all conditions given.
        return work_request_sorted_list
