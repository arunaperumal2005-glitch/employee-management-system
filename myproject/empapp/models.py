from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position=models.CharField(max_length=100)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    date_joined=models.DateField(default='2026-01-01')
    def __str__(self):
        return self.name