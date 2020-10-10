
from django.contrib import admin
from django.urls import path
from convert_pdf import views
urlpatterns = [
    path('list/employee', views.list_of_employee_pdf, name = 'employee-list-pdf_page'),
    path('list/designation', views.list_of_designation_pdf, name = 'designation-list-pdf_page'),
    path('list/filter/designation/<designation_name>', views.filter_of_designation_pdf, name = 'filter-of-designation-page'),
    path('list/of/title', views.list_of_title_pdf, name = 'title-list-pdf_page'),
    path('list/of/zone', views.list_of_zone_pdf, name = 'zone-list-pdf_page'),
    path('list/filter/zone/<zone_name>', views.filter_of_zone_pdf, name = 'filter-of-zone-page'),
    path('list/of/user', views.list_of_user_pdf, name = 'user-list-pdf_page'),

]