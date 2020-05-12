from .employee import EmployeeSerializer


def serialize_employee_object(employee_object):

    serialize = EmployeeSerializer(employee_object)

    return serialize.data
