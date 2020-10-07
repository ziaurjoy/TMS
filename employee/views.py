from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from employee.forms import CreateEmployeeForm, UserLoginForm, MyPasswordChangeForm

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def user_login(request):
    forms = UserLoginForm()
    if request.method == 'POST':
        forms = UserLoginForm(request.POST)
        if forms.is_valid():
            user = authenticate(
                username = forms.cleaned_data['username'],
                password = forms.cleaned_data['password']
            )
            if user:
                login(request,user)
                return redirect('password-reset')
    context = {'form': forms}
    return render(request,'registration/login.html',context)



class ChangePassword(LoginRequiredMixin,TemplateView):
    form_class = MyPasswordChangeForm
    def get(self, request, *args, **kwargs):
        form = self.form_class(self.request.user)
        return render(request, 'registration/password.html',{'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # return render(request, 'password.html', {'form': form, 'password_changed': True})
            return redirect('employee-create')
        else:
            return render(request, 'registration/password.html', {'form': form, 'password_changed': False})



def create_employee(request):
    form = CreateEmployeeForm()
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            old_form = form.save(commit=False)
            old_form.users = User.objects.get(pk=request.user.id)
            old_form.save()

    context = {"form": form}
    return render(request, 'registration/employee_create.html', context)








# def usercreate(request):
#     forms = UserCreationForm()
#     if request.method == 'POST':
#         forms = UserCreationForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             redirect('login')
#     return render(request, 'create.html', context={'form': forms})
#
#








