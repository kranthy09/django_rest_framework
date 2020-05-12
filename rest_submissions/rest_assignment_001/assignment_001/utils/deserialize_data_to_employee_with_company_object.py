from .employeewith_company_details import EmployeeWithCompanyDetailsSerializer


def deserialize_data_to_employee_with_company_object(employee_with_company_data):

    serialize = EmployeeWithCompanyDetailsSerializer(data=employee_with_company_data)

    is_valid_data = serialize.is_valid()

    if is_valid_data:
        employee_with_company_object = serialize.save()
    return employee_with_company_object
