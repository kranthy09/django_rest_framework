from .companywith_employees_details import CompanyWithEmployeesDetailsSerializer


def deserialize_data_to_company_with_employees_object(company_with_employees_data):

    serialize = CompanyWithEmployeesDetailsSerializer(data=company_with_employees_data)
    is_valid_data = serialize.is_valid()
    if is_valid_data:
        company_with_employees_object = serialize.save()
    
    return company_with_employees_object