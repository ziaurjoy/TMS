
from django.contrib import admin
from django.urls import path, include
from employee import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name = 'user-login'),
    path('password-change/', views.ChangePassword.as_view(), name='password-change'),
    path('create-employee', views.create_employee, name = 'employee-create'),
    path('user/information', views.user_information, name = 'user-information'),

    path('administration/', include('administration.urls')),
    path('pdf_page/', include('convert_pdf.urls')),

]
