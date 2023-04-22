from django.core import validators
from django import forms
from .models import User, Student

class StudentRegistration(forms.ModelForm):
    class Meta():
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        } 
            
class UserRegistration(forms.ModelForm):
    class Meta():
        model = Student
        fields = ['name', 'age', 'home_group']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'home_group': forms.TextInput(attrs={'class': 'form-control'}),
        } 