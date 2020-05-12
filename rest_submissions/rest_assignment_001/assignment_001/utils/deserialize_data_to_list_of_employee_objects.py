from .employee import EmployeeSerializer


def deserialize_data_to_list_of_employee_objects(employees_data):

    serializer = EmployeeSerializer(data=employees_data, many=True)

    is_valid_data = serializer.is_valid()

    if is_valid_data:
        employees_objects = serializer.save()

    return employees_objects
