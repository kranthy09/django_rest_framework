from rest_framework import serializers
from .employee import Employee, EmployeeSerializer
from .company import CompanySerializer


class EmployeeWithCompanyDetails(Employee):
    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired, company,
                 is_best_employee=None, last_name=None):
        super().__init__(employee_id, age, date_of_joining, last_logged_in,
                         salary_in_inr, employee_type, first_name, is_retired,
                         is_best_employee, last_name)
        self.company = company                          # Company class instance 


class EmployeeWithCompanyDetailsSerializer(EmployeeSerializer):
    company = CompanySerializer()
