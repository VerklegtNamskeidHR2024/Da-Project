import json
from amenity_model import Amenity
from contractor_model import Contractor
from employee_model import Employee
from location_model import Location
from house_model import House
from location_model import Location
from maintenance_report_model import MaintenanceReport
from manager_model import Manager
from work_request_model import WorkRequest


# Reykjávík Nuuk Kulusuk Þórshöfn Tingwall Longyearbyen


person1 = employee_model.Employee('Hreimur', 123456789, 1234567, 'Reykjavik', 'Employee', 'hreimur69@gmail.com', 'E1234')
person2 = Employee('John Doe', 987654321, 7654321, 'Reykjavik', 'Employee', 'johndoe@example.com', 'E5678')
person3 = Employee('Jane Smith', 192837465, 5647382, 'Nuuk', 'Employee', 'janesmith@example.com', 'E9101')
person4 = Employee('Jokla Himiko', 102938475, 3847562, 'Nuuk', 'Employee', 'joklahimiko@example.com', 'E1121')
person5 = Employee('Bob Brown', 564738291, 9182736, 'Kulusuk', 'Employee', 'bobbrown@example.com', 'E3141')
person6 = Employee('Charlie Davis', 837465192, 2736451, 'Thorshofn', 'Employee', 'charliedavis@example.com', 'E5161')
person7 = Employee('Diana Evans', 475839201, 6473829, 'Thorshofn', 'Employee', 'dianaevans@example.com', 'E7181')
person8 = Employee('Eve Foster', 293847561, 9182734, 'Tingwall', 'Employee', 'evefoster@example.com', 'E9202')
person9 = Employee('Frank Green', 564738291, 3847562, 'Tingwall', 'Employee', 'frankgreen@example.com', 'E1223')
person10 = Employee('Grace Harris', 918273645, 2736451, 'Longyearbyen', 'Employee', 'graceharris@example.com', 'E3243')



persons = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10]
person_dict = [person.to_dict() for person in persons]

with open('Data/employee_storage.json', 'w') as file:
    json.dump(person_dict, file, indent=4)


amenity1 = Amenity('P123', 'Pool', 'Reykjavik', 1000.0, 'A pool')
amenity2 = Amenity('P456', 'Gym', 'New York', 2000.0, 'A gym')

amenities = [amenity1, amenity2]

with open('Data/amenities_storage.json', 'w') as amenityFile:
    json.dump([amenity.to_dict() for amenity in amenities], amenityFile, indent=4)

'''with open('Data/employee_storage.json', 'r') as file:
    persons = json.load(file)


search = input('Enter staff ID to search for: ')
for person in persons:
    if person['staff_id'] == search:
        print(person)
        break'''