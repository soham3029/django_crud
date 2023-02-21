from rest_framework import serializers
from EmployeeApp.models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('departmentId', 'departmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employeeId', 'employeeName', 'department', 'dateOfJoining', 'profileImgName')