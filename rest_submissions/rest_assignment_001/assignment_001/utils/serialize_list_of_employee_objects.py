from .employee import EmployeeSerializer


def serialize_list_of_employee_objects(list_of_employee_objects):

    serializer = EmployeeSerializer(list_of_employee_objects, many=True)

    return serializer.data