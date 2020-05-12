from .employeewith_company_details import EmployeeWithCompanyDetailsSerializer


def serialize_employee_with_company_object(employee_with_company_object):

    serialize = EmployeeWithCompanyDetailsSerializer(employee_with_company_object)

    return serialize.data