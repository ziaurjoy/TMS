
from django import forms

from employee.models import Title, Designation, Zone


class TitleCreateForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = '__all__'
        widgets = {
           'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'})
        }



class DesignationCreateForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = '__all__'
        widgets = {
           'designation':forms.TextInput(attrs={'class':'form-control','placeholder':'Designation'})
        }

class ZoneCreateForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = '__all__'
        widgets = {
            'zone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zone Name...'})
        }