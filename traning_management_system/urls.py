
from django.contrib import admin
from django.urls import path, include
from employee import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name = 'user-login'),
    path('password-reset/', views.ChangePassword.as_view(), name='password-reset'),
    path('create-employee', views.create_employee, name = 'employee-create'),
    path('administration/', include('administration.urls'))

]
