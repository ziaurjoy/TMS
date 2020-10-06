from django.contrib import admin

# Register your models here.
from employee.models import Title,Designation,EmployeeInfo

admin.site.register(Title),
admin.site.register(Designation),
admin.site.register(EmployeeInfo),
