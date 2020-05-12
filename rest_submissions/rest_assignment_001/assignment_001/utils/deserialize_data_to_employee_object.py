from .employee import EmployeeSerializer


def deserialize_data_to_employee_object(employee_data):

    serializer = EmployeeSerializer(data=employee_data)
    is_valid_data = serializer.is_valid()
    if is_valid_data:
        employee_object = serializer.save()

    return employee_object