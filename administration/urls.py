
from django.contrib import admin
from django.urls import path
from administration import views
urlpatterns = [
    path('', views.administration, name = 'administration'),
    path('create/title', views.title_create, name = 'title-create'),
    path('title/list', views.title_list, name = 'title-list'),
    path('title/delete/<int:title_id>', views.title_delete, name = 'title-delete'),
    path('change/title/<int:title_id>', views.title_change, name = 'title-update'),
    path('create/designation', views.create_designation, name = 'create-designation'),
    path('designation/list', views.designation_list, name = 'designation-list'),
    path('update/designation/<int:designation_id>', views.update_designation, name = 'update-designation'),
    path('delete/designation/<int:designation_id>', views.delete_designation, name = 'delete-designation'),
    path('employee/list', views.employee_list, name = 'employee-list'),
    path('branch/<branch_name>', views.filter_of_branch, name = 'filter-of-branch'),
    path('employee/update/<int:employee_id>', views.employee_change, name = 'update-employee'),
    path('employee/delete/<int:employee_id>', views.employee_delete, name = 'delete-employee'),
    path('zone/create', views.create_zone, name = 'create-zone'),
    path('zone/list', views.zone_list, name = 'zone-list'),
    path('zone/<zone_name>', views.filter_of_zone, name = 'filter-of-zone'),
    path('zone/update/<int:zone_id>', views.update_zone, name = 'update-zone'),
    path('zone/delete/<int:zone_id>', views.delete_zone, name = 'delete-zone'),
    path('designation/<designation_name>', views.filter_of_designation, name = 'filter-of-designation'),
    path('registration', views.user_registration, name = 'registration'),
    path('registration/list', views.user_registration_list, name = 'registration-list'),



]