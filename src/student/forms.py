from django import forms
from .models import Student

CLASS = [
    ('', ' Selectionnez une classe'),
    ('Tle', 'Tle'),
    ('1ère', '1ère'),
    ('2nd', '2nd'),
    ('3ème', '3ème'),
    (' 4ème', '4ème'),
    ('5ème', '5ème'),
    ('6ème', '6ème')
]

GENDER = [
    (True, 'Homme'),
    (False, 'Femme')
]

# class StudentForm(forms.Form):
#     CLASS = [
#         (' Selectionnez une classe', ' Selectionnez une classe'),
#         ('Tle', 'Tle'),
#         ('1ère', '1ère'),
#         ('2nd', '2nd'),
#         ('3ème', '3ème'),
#         (' 4ème', '4ème'),
#         ('5ème', '5ème'),
#         ('6ème', '6ème')
#     ]
#     GENDER = [
#         ('0', 'Homme'),
#         ('1', 'Femme')
#     ]
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'placeholder': 'MON NOM',
#             'class':'name'

#         }
#     ))
#     birth_date = forms.DateField(widget=forms.DateInput(
#         attrs={
#             'type':'date',
#             'placeholder':'Date of Birth',

#         }
#     ))
#     classroom = forms.ChoiceField(choices=CLASS)
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
#     register = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'placeholder':'Register'
#         }

#     ))
#     gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())

gender = forms.BooleanField(widget=forms.RadioSelect(choices=GENDER))


class StudentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(StudentForm,self).__init__(*args, **kwargs)
    #     instance = kwargs.get('instance')
    #     if instance:
    #         if instance.gender == 0:
    #             self.fields['gender'].initial = 0
    #         self.fields['gender'].initial = 1

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birth_date', 'classroom', 'phone', 'city', 'register', 'gender']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date of Birth'}),
            'classroom': forms.Select(choices=CLASS, attrs={'placeholder': 'Classroom'}),
            'phone': forms.NumberInput(attrs={'min': '1', 'placeholder': 'Number'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'register': forms.TextInput(attrs={'placeholder': 'Register'}),
            'gender': forms.RadioSelect(choices=GENDER),
        }
