from django.contrib.auth.models import User
from django.shortcuts import render

import datetime
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Sum

# Create your views here.
from employee.models import EmployeeInfo, Designation, Title, Zone


def list_of_employee_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition'] = 'inline; attachment; filename=Expense' + str(datetime.datetime.now()) + '.pdf_page'
    response['Content-Transfer-Encoding'] = 'binary'
    employees = EmployeeInfo.objects.all().order_by('employee_designation')
    sum = employees.aggregate(Sum('id'))
    html_string = render_to_string(
        'backend/pdf_pages/list_of_employee.html', {'employees': employees, 'total': sum}
    )
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
        return response



def list_of_designation_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition'] = 'inline; attachment; filename=Expense' + str(datetime.datetime.now()) + '.pdf_page'
    response['Content-Transfer-Encoding'] = 'binary'
    designation = Designation.objects.all().order_by('id')
    sum = designation.aggregate(Sum('id'))
    html_string = render_to_string(
        'backend/pdf_pages/list_of_designation.html', {'designations': designation, 'total': sum}
    )
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
        return response


def filter_of_designation_pdf(request,designation_name):
    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition'] = 'inline; attachment; filename=Expense' + str(datetime.datetime.now()) + '.pdf_page'
    response['Content-Transfer-Encoding'] = 'binary'
    designation_obj = Designation.objects.get(designation=designation_name)
    employee = EmployeeInfo.objects.filter(employee_designation__designation=designation_obj)
    sum = employee.aggregate(Sum('id'))
    html_string = render_to_string(
        'backend/pdf_pages/list_of_employee.html', {'employees': employee,'designation_obj':designation_obj,'total': sum}
    )
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
        return response



def list_of_title_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition'] = 'inline; attachment; filename=Expense' + str(datetime.datetime.now()) + '.pdf_page'
    response['Content-Transfer-Encoding'] = 'binary'
    title = Title.objects.all()
    sum = title.aggregate(Sum('id'))
    html_string = render_to_string(
        'backend/pdf_pages/list_of_title.html', {'titles': title,'total': sum}
    )
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
        return response



def list_of_zone_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition'] = 'inline; attachment; filename=Expense' + str(datetime.datetime.now()) + '.pdf_page'
    response['Content-Transfer-Encoding'] = 'binary'
    zone = Zone.objects.all()
    sum = zone.aggregate(Sum('id'))
    html_string = render_to_string(
        'backend/pdf_pages/list_of_zone.html', {'zones': zone,'total': sum}
    )
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
        return response



def filter_of_zone_pdf(request,zone_name):
    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition'] = 'inline; attachment; filename=Expense' + str(datetime.datetime.now()) + '.pdf_page'
    response['Content-Transfer-Encoding'] = 'binary'
    zone_obj = Zone.objects.get(zone=zone_name)
    employee = EmployeeInfo.objects.filter(zone__zone=zone_obj)
    sum = employee.aggregate(Sum('id'))
    html_string = render_to_string(
        'backend/pdf_pages/list_of_employee.html', {'employees': employee,'zone_obj':zone_obj,'total': sum}
    )
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
        return response



def list_of_user_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content_Disposition'] = 'inline; attachment; filename=Expense' + str(datetime.datetime.now()) + '.pdf_page'
    response['Content-Transfer-Encoding'] = 'binary'
    user = User.objects.all()
    sum = user.aggregate(Sum('id'))
    html_string = render_to_string(
        'backend/pdf_pages/list_of_user.html', {'users': user,'total': sum}
    )
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
        return response