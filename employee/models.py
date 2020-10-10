from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Title(models.Model):
    title = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class Designation(models.Model):
    designation = models.CharField(max_length=50,unique=True)


    def __str__(self):
        return self.designation


class IsChangedPassword(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    is_changed = models.BooleanField(default=False)


class Members(models.Model):
    # rest fields..
    old_passwords = models.TextField(blank=True, default='')


class Zone(models.Model):
    zone = models.CharField(max_length=30)
    def __str__(self):
        return self.zone

class EmployeeInfo(models.Model):
    users = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    employee_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    employee_designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=True, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name



