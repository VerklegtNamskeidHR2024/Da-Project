import json
from Model_Classes.amenity_model import Amenity
from Model_Classes.contractor_model import Contractor
from Model_Classes.employee_model import Employee
from Model_Classes.location_model import Location
from Model_Classes.house_model import House
from Model_Classes.location_model import Location
from Model_Classes.maintenance_report_model import MaintenanceReport
from Model_Classes.manager_model import Manager
from Model_Classes.work_request_model import WorkRequest
from Model_Classes.admin_model import Admin

# Reykjavík Nuuk Kulusuk Þórshöfn Tingwall Longyearbyen
admin1 = Admin('Hreimur', 12334546789, 5551234, 'Reykjavik', 'Admin', 'hreimur24@ru.is', 'A1')

manager1 = Manager('Hreimur', 12334546789, 5551234, 'Reykjavik', 'Manager', 'hreimur24@ru.is', 'M1')
manager2 = Manager('Hreimur', 12334546789, 5551234, 'Nuuk', 'Manager', 'hreimur24@ru.is', 'M2')
manager3 = Manager('Hreimur', 12334546789, 5551234, 'Kulusuk', 'Manager', 'hreimur24@ru.is', 'M3')
manager4 = Manager('Hreimur', 12334546789, 5551234, 'Thorshofn', 'Manager', 'hreimur24@ru.is', 'M4')
manager5 = Manager('Hreimur', 12334546789, 5551234, 'Tingwall', 'Manager', 'hreimur24@ru.is', 'M5')
manager6 = Manager('Hreimur', 12334546789, 5551234, 'Longyearbyen', 'Manager', 'hreimur24@ru.is', 'M6')

employee1 = Employee('Hreimur', 123456789, 1234567, 'Reykjavik', 'Employee', 'hreimur69@gmail.com', 'E1')
employee2 = Employee('John Doe', 987654321, 7654321, 'Reykjavik', 'Employee', 'johndoe@example.com', 'E5')
employee3 = Employee('Jane Smith', 192837465, 5647382, 'Nuuk', 'Employee', 'janesmith@example.com', 'E9')
employee4 = Employee('Jokla Himiko', 102938475, 3847562, 'Nuuk', 'Employee', 'joklahimiko@example.com', 'E2')
employee5 = Employee('Bob Brown', 564738291, 9182736, 'Kulusuk', 'Employee', 'bobbrown@example.com', 'E3')
employee6 = Employee('Charlie Davis', 837465192, 2736451, 'Thorshofn', 'Employee', 'charliedavis@example.com', 'E6')
employee7 = Employee('Diana Evans', 475839201, 6473829, 'Thorshofn', 'Employee', 'dianaevans@example.com', 'E7')
employee8 = Employee('Eve Foster', 293847561, 9182734, 'Tingwall', 'Employee', 'evefoster@example.com', 'E8')
employee9 = Employee('Frank Green', 564738291, 3847562, 'Tingwall', 'Employee', 'frankgreen@example.com', 'E10')
employee10 = Employee('Grace Harris', 918273645, 2736451, 'Longyearbyen', 'Employee', 'graceharris@example.com', 'E30')

property1 = House('P1', 'suite', 'Reykjavik', 'excellent', 1500.0, 30230)
property2 = House('P2', 'suite', 'Reykjavik', 'fair', 1200.0, 300)
property3 = House('P3', 'suite', 'Reykjavik', 'excellent', 1500.0, 30)
property4 = House('P4', 'suite', 'Reykjavik', 'fair', 1200.0, 30)
property5 = House('P5', 'suite', 'Reykjavik', 'excellent', 1500.0, 30)
property6 = House('P6', 'suite', 'Nuuk', 'fair', 1200.0, 300)
property7 = House('P7', 'suite', 'Nuuk', 'excellent', 1500.0, 300)
property8 = House('P8', 'suite', 'Nuuk', 'fair', 1200.0, 30)
property9 = House('P9', 'suite', 'Nuuk', 'excellent', 1500.0, 300000000)
property10 = House('P10', 'suite', 'Nuuk', 'fair', 1200.0, 30000000000)
property11 = House('P11', 'suite', 'Kulusuk', 'excellent', 1500.0, 30000000)
property12 = House('P12', 'suite', 'Kulusuk', 'excellent', 1500.0, 300000000)
property13 = House('P13', 'suite', 'Kulusuk', 'excellent', 1500.0, 3000000)
property14 = House('P14', 'suite', 'Kulusuk', 'excellent', 1500.0, 30000000000)
property15 = House('P15', 'suite', 'Kulusuk', 'excellent', 1500.0, 30000000000)
property16 = House('P16', 'suite', 'Thorshofn', 'excellent', 1500.0, 30000000)
property17 = House('P17', 'suite', 'Thorshofn', 'fair', 1200.0, 300000000)
property18 = House('P18', 'suite', 'Thorshofn', 'excellent', 1500.0, 30000000000)
property19 = House('P19', 'suite', 'Thorshofn', 'excellent', 1500.0, 30000000)
property20 = House('P20', 'suite', 'Thorshofn', 'excellent', 1500.0, 300000000)
property21 = House('P21', 'suite', 'Thorshofn', 'fair', 1200.0, 300000000)
property22 = House('P22', 'suite', 'Tingwall', 'excellent', 1500.0, 300000000)
property23 = House('P23', 'suite', 'Tingwall', 'excellent', 1500.0, 300000000)
property24 = House('P24', 'suite', 'Tingwall', 'excellent', 1500.0, 3000000)
property25 = House('P25', 'suite', 'Tingwall', 'excellent', 1500.0, 30000000)
property26 = House('P26', 'suite', 'Tingwall', 'fair', 1200.0, 30000000000)
property27 = House('P27', 'suite', 'Longyearbyen', 'excellent', 1500.0, 300000000)
property28 = House('P28', 'suite', 'Longyearbyen', 'excellent', 1500.0, 30000000)
property29 = House('P29', 'suite', 'Longyearbyen', 'excellent', 1500.0, 30000000)
property30 = House('P30', 'suite', 'Longyearbyen', 'fair', 1200.0, 30000000)

location1 = Location('Iceland', 'Reykjavik', 'KEF', '5551234', 'Tumi Krist', '8-16')
location2 = Location('Greenland', 'Nuuk', 'NUK', '5551234', 'Tumi Krist', '8-16')
location3 = Location('Greenland', 'Kulusuk', 'KLK', '5551234', 'Tumi Krist', '8-16')
location4 = Location('Faroe Islands', 'Thorshofn', 'FLT', '5551234', 'Tumi Krist', '8-16')
location5 = Location('Hjaltlandseyjar', 'Tingwall', 'SVB', '5551234', 'Tumi Krist', '8-16')
location6 = Location('Svalbard', 'Longyearbyen', 'SVB', '5551234', 'Tumi Krist', '8-16')

contractor1 = Contractor('C1', 'Daniela and Daughters', 'Daniela', '8-16', 1234567, 'Reykjavik', [])
contractor2 = Contractor('C2', 'Daniela and Daughters', 'Daniela', '8-16', 1234567, 'Nuuk', [])
contractor3 = Contractor('C3', 'Daniela and Daughters', 'Daniela', '8-16', 1234567, 'Tingwall', [])
contractor4 = Contractor('C4', 'Juicy Hreimur Construction', 'Hreimur', '8-16', 1234567, 'Reykjavik', [])

amenity1 = Amenity('A1', 'pool', 'Reykjavik', 'excellent', 1500.0, 'is a pool')
amenity2 = Amenity('A2', 'pool', 'Tingwall', 'fair', 1200.0, 'is a pool')
amenity3 = Amenity('A3', 'hot tub', 'Nuuk', 'excellent', 1500.0, 'is a hot tub')

work_request1 = WorkRequest('WR1', 'Fix HotTub', 'Hot tub was leaking ketchup for some odd reason?', 'MR2', 'E1', 'Reykjavik', 'P1','01-01-24','',False,0,'High','MR2','Pending',False,'',False)
work_request2 = WorkRequest('WR1', 'Fix roof', 'roof had giant hole in it', 'MR1', 'E1', 'Reykjavik', 'P1','01-01-24','',False,0,'High','MR2','Pending',False,'',False)

maintenance_report1 = MaintenanceReport('MR1', 'Fix the roof', 'Reykjavik', 'P4', 'E5', False, 'roof is leaking', 'Pending', '1234', True, 'C1', 'WR3')

admins = [admin1]
admin_dict = [admin.to_dict() for admin in admins]

managers = [manager1, manager2, manager3, manager4, manager5, manager6]
manager_dict = [manager.to_dict() for manager in managers]

employees = [employee1, employee2, employee3, employee4, employee5, employee6, employee7, employee8, employee9, employee10]
employee_dict = [employee.to_dict() for employee in employees]

amenities = [amenity1, amenity2, amenity3]
amenity_dict = [amenity.to_dict() for amenity in amenities]

properties = [property1, property2, property3, property4, property5, property6, property7, property8, property9, property10,
                property11, property12, property13, property14, property15, property16, property17, property18, property19, property20,
                property21, property22, property23, property24, property25, property26, property27, property28, property29, property30]
property_dict = [property.to_dict() for property in properties]


locations = [location1, location2, location3, location4, location5, location6]
location_dict = [location.to_dict() for location in locations]

contractors = [contractor1, contractor2, contractor3]
contractor_dict = [contractor.to_dict() for contractor in contractors]

work_requests = [work_request1, work_request2]
work_request_dict = [work_request.to_dict() for work_request in work_requests]

maintenance_reports = [maintenance_report1]
maintenance_report_dict = [maintenance_report.to_dict() for maintenance_report in maintenance_reports]

with open('Data/admin_storage.json', 'w') as file:
    json.dump(admin_dict, file, indent=4)

with open('Data/manager_storage.json', 'w') as file:
    json.dump(manager_dict, file, indent=4)

with open('Data/employee_storage.json', 'w') as file:
    json.dump(employee_dict, file, indent=4)

with open('Data/amenity_storage.json', 'w') as file:
    json.dump(amenity_dict, file, indent=4)

with open('Data/property_storage.json', 'w') as file:
    json.dump(property_dict, file, indent=4)

with open('Data/location_storage.json', 'w') as file:
    json.dump(location_dict, file, indent=4)

with open('Data/contractor_storage.json', 'w') as file:
    json.dump(contractor_dict, file, indent=4)

with open('Data/work_request_storage.json', 'w') as file:
    json.dump(work_request_dict, file, indent=4)

with open('Data/maintenance_report_storage.json', 'w') as file:
    json.dump(maintenance_report_dict, file, indent=4)

with open('Data/employee_storage.json', 'r') as file:
    persons = json.load(file)