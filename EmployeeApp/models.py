from django.db import models

# Create your models here.

class Department(models.Model):
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=500)


class Employee(models.Model):
    employeeId = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=500)
    department = models.CharField(max_length=500)
    dateOfJoining = models.DateField()
    profileImgName = models.CharField(max_length=500)