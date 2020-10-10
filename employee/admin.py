from django.contrib import admin

# Register your models here.
from employee.models import Title,Designation,EmployeeInfo,Zone

admin.site.register(Title),
admin.site.register(Zone),
admin.site.register(Designation),
admin.site.register(EmployeeInfo),
