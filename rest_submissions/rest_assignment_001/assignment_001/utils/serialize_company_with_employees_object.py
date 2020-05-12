from .companywith_employees_details import\
    CompanyWithEmployeesDetailsSerializer


def serialize_company_with_employees_object(company_with_employees_object):

    serialize = CompanyWithEmployeesDetailsSerializer(
                        company_with_employees_object
                )

    return serialize.data