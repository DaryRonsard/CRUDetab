from django import forms
from .models import Teacher

MATTER = [
    ('', ' Selectionnez une matière'),
    ('Math', 'Math'),
    ('Physique', 'Physique'),
    ('EPS', 'EPS'),
    ('Anglais', 'Anglais'),
    ('SVT', 'SVT'),
    ('Philosophie', 'Philosophie'),
    ('Français', 'Français')
]
GENDER = [
    (True, 'Homme'),
    (False, 'Femme')
]


# class TeacherForm(forms.Form):
#     MATTER = [
#         (' Selectionnez une matière', ' Selectionnez une matière'),
#         ('Math', 'Math'),
#         ('Physique', 'Physique'),
#         ('EPS', 'EPS'),
#         ('Anglais', 'Anglais'),
#         (' SVT', 'SVT'),
#         ('Philosophie', 'Philosophie'),
#         ('Français', 'Français')
#     ]
#     GENDER = [
#         (True, 'Homme'),
#         (False, 'Femme')
#     ]
#     first_name = forms.CharField(required=True, widget=forms.TextInput(
#         attrs={
#             'placeholder': 'First name'
#         }))
#     last_name = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'placeholder': 'Last name'
#         }
#     ))
#     birth_date = forms.DateField(widget=forms.DateInput(
#         attrs={
#             'type':'date',
#
#         }
#     ))
#     matter = forms.ChoiceField(choices=MATTER)
#     phone = forms.CharField(widget=forms.NumberInput(
#         attrs={
#             'min':'1',
#             'placeholder':'Number'
#         }))
#     city = forms.CharField(max_length=20,widget=forms.TextInput(
#         attrs={
#             'placeholder':'City'
#         }
#     ))
#     gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'birth_date', 'subject_taught', 'phone', 'city', 'gender']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date of Birth'}),
            'subject_taught': forms.Select(choices=MATTER),
            'phone': forms.NumberInput(attrs={'min': '1', 'placeholder': 'Number'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'gender': forms.RadioSelect(choices=GENDER),
        }
