from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from employee.models import EmployeeInfo

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))




# class ChangePassword(forms.Form):
#     old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'old_password'}))
#     _new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'new_password'}))
#     _reenter_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'reenter_password'}))
#
#     def clean(self):
#         old_password = self.cleaned_data.get('old_password')
#         new_password = self.cleaned_data.get('_new_password')
#         reenter_password = self.cleaned_data.get('_reenter_password')
#         # similarly old_password
#
#         if new_password and new_password != reenter_password or new_password == old_password:
#             # raise error
#             # get the user object and check from old_password list if any one matches with the new password raise error(read whole answer you would know)
#             return self.cleaned_data  # don't forget this.


class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeInfo
        fields = 'employee_id','name','employee_designation','title','zone','branch'





class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': "Old Password"})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': "New Password"})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': "New Password"})

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user

