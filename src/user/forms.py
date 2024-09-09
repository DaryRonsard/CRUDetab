from django import forms
from .models import User



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["pseudo", "password"]
        widgets = {
            'pseudo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }
