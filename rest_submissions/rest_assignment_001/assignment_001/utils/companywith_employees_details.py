from .company import Company
from .company import CompanySerializer
from .employee import EmployeeSerializer


class CompanyWithEmployeesDetails(Company):
    def __init__(self, name, registration_id, employees):
        super().__init__(name, registration_id)
        self.employees = employees                      # List of Employee class instances 


class CompanyWithEmployeesDetailsSerializer(CompanySerializer):
    employees = EmployeeSerializer(many=True)
