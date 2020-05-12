from rest_framework import serializers
from .constants import EmployeeType


class Employee(object):
    def __init__(self, employee_id, age, date_of_joining, last_logged_in,
                 salary_in_inr, employee_type, first_name, is_retired,
                 is_best_employee=None, last_name=None
                 ):

        self.employee_id = employee_id                  # UUID
        self.age = age                                  # INT
        self.date_of_joining = date_of_joining          # DATE
        self.last_logged_in = last_logged_in            # DATETIME
        self.salary_in_inr = salary_in_inr              # FLOAT
        self.employee_type = employee_type              # ENUM - Possible values MANAGER,TECHNICIAN,DEVELOPER,SALES_MEMBER 
        self.first_name = first_name                    # CHAR
        self.last_name = last_name                      # CHAR
        self.is_retired = is_retired                    # BOOL
        self.is_best_employee = is_best_employee        # BOOL - Can be None as well

class EmployeeSerializer(serializers.Serializer):
    
    employee_id = serializers.UUIDField()
    age = serializers.IntegerField()
    date_of_joining = serializers.DateTimeField()
    last_logged_in = serializers.DateTimeField()
    salary_in_inr = serializers.FloatFiled()
    employee_type = serializers.ChoiceField([type.value for type in EmployeeType])
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    is_retired = serializers.BooleanField()
    is_best_employee = serializers.NullBooleanField()
