import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from administration.forms import TitleCreateForm, DesignationCreateForm, ZoneCreateForm
from employee.forms import CreateEmployeeForm
from employee.models import Title, Zone, EmployeeInfo, Designation



def administration(request):
    return render(request,'backend/pages/administration.html')

def user_registration(requset):
    form = UserCreationForm()
    if requset.method == "POST":
        form = UserCreationForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('registration-list')
    context = {
        'form':form
    }
    return render(requset,'backend/pages/registration.html',context)


def user_registration_list(request):
    registrations = User.objects.all()
    context = {'registrations': registrations}
    return render(request,'backend/pages/registration_list.html',context)




def title_create(requset):
    form = TitleCreateForm()
    if requset.method == "POST":
        form = TitleCreateForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('title-list')
    context = {
        'form': form
    }
    return render(requset, 'backend/pages/create_title.html', context)



def title_change(requset,title_id):
    title = Title.objects.get(id=title_id)
    form = TitleCreateForm(instance=title)
    if requset.method == "POST":
        form = TitleCreateForm(requset.POST,instance=title)
        if form.is_valid():
            form.save()
            return redirect('administration')
    context = {
        'form': form
    }
    return render(requset, 'backend/pages/create_title.html', context)


def title_list(request):
    titles = Title.objects.all()
    return render(request,'backend/pages/title_list.html',context={'titles': titles})

def title_delete(request,title_id):
    title = Title.objects.get(id = title_id)
    title.delete()
    return redirect('title-list')


def employee_list(request):
    employees = EmployeeInfo.objects.all()
    context = {'employees': employees}
    return render(request,'backend/pages/employee_list.html',context)


def employee_change(requset,employee_id):
    employee = EmployeeInfo.objects.get(id=employee_id)
    form = CreateEmployeeForm(instance=employee)
    if requset.method == "POST":
        form = CreateEmployeeForm(requset.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('administration')
    context = {
        'form': form
    }
    return render(requset, 'registration/employee_create.html', context)

def employee_delete(request,employee_id):
    employee = EmployeeInfo.objects.get(id = employee_id)
    employee.delete()
    return redirect('employee-list')


def filter_of_branch(request,branch_name):
    branch_obj = EmployeeInfo.objects.filter(branch = branch_name)
    context = {'branch_objs': branch_obj}
    return render(request,'backend/pages/branch_filter.html',context)

def filter_of_zone(request,zone_name):
    zone_obj = Zone.objects.get(zone = zone_name)
    employee = EmployeeInfo.objects.filter(zone__zone=zone_obj)
    context = {'employees': employee,'zone_obj': zone_obj}
    return render(request, 'backend/pages/zone_filter.html', context)

def filter_of_designation(request,designation_name):
    designation_obj = Designation.objects.get(designation = designation_name)

    employee = EmployeeInfo.objects.filter(employee_designation__designation=designation_obj)
    context = {'employees': employee,'designation': designation_obj}
    return render(request, 'backend/pages/designation_filter.html', context)



def designation_list(request):
    designations = Designation.objects.all()
    context = {'designations': designations}
    return render(request,'backend/pages/designation_list.html',context)



def create_designation(request):
    form = DesignationCreateForm()
    if request.method == 'POST':
        form = DesignationCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('designation-list')
    context = {'form':form}
    return render(request,'backend/pages/create_designation.html',context)

def update_designation(requset,designation_id):
    designation = Designation.objects.get(id=designation_id)
    form = DesignationCreateForm(instance=designation)
    if requset.method == "POST":
        form = DesignationCreateForm(requset.POST,instance=designation)
        if form.is_valid():
            form.save()
            return redirect('designation-list')
    context = {
        'form': form
    }
    return render(requset, 'backend/pages/create_designation.html', context)

def delete_designation(request,designation_id):
    designation = Designation.objects.get(id = designation_id)
    designation.delete()
    return redirect('designation-list')




def zone_list(request):
    zone = Zone.objects.all()
    context = {'zones': zone}
    return render(request,'backend/pages/zone_list.html',context)

def create_zone(requset):
    form = ZoneCreateForm()
    if requset.method == "POST":
        form = ZoneCreateForm(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('zone-list')
    context = {
        'form': form
    }
    return render(requset, 'backend/pages/create_zone.html', context)


def update_zone(requset,zone_id):
    zone = Zone.objects.get(id=zone_id)
    form = ZoneCreateForm(instance=zone)
    if requset.method == "POST":
        form = ZoneCreateForm(requset.POST,instance=zone)
        if form.is_valid():
            form.save()
            return redirect('zone-list')
    context = {
        'form': form
    }
    return render(requset, 'backend/pages/create_zone.html', context)

def delete_zone(request,zone_id):
    zone = Zone.objects.get(id = zone_id)
    zone.delete()
    return redirect('zone-list')








# def search(request):
#     if request.method == 'POST':
#         search_keyword = request.POST['search']
#         search_posts = EmployeeInfo.objects.filter(title__title = search_keyword)
#         return render(request,'backend/pages/search_title.html',context={'search_posts': search_posts})
#     else:
#         return render(request, 'backend/.html')


# def title_filter_zone(request,zone_name):
#     print(zone_name)
#     # zone = Zone.objects.get(zone = zone_name)
#     # print(zone)
#     # titles = EmployeeInfo.objects.filter(zone = zone)
#     # print(titles)
#     # context = {'titles' : titles}
#     return render(request,'backend/pages/zone_filter.html')



