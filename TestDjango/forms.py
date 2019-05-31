from django import forms

from TestDjango.models import Student


class StudentForms(forms.Form):
    # fields = ['student_id', 'first_name', 'last_name', 'place_of_birth', 'email', 'phone_number']
    student_id = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    place_of_birth = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=100)
