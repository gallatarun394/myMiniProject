from django import forms
from Feedback_System.models import Student, Faculty, Hod, Subject, Feedback
from django.core import validators


class NewStudentForm(forms.ModelForm):
    pwd = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = '__all__'

class NewFacultyForm(forms.ModelForm):
    pwd = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Faculty
        fields = '__all__'
