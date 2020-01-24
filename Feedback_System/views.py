from django.shortcuts import render
from django import forms
from django.core import validators
# from django.http import HttpResponse
# from Feedback_System.models import Student, Faculty, Hod, Subject, Feedback
from Feedback_System.forms import NewStudentForm, NewFacultyForm
# Create your views here.
#############################################################################
def home_page(request):
    intro = {
            'one' : "Welcome to ONLINE FEEDBACK SYSTEM!",
            'two' : "Give the feedback to the faculty teaching you ",
            'three' : "View neccessary details here .. "
    }
    return render(request,'Feedback_System/home_page.html',context = intro)

#############################################################################
def thankyou(request):
    dic = {
        'wish' : "Thanks For Registering ..",
        'redirect' : "Please redirect to Login Page !!",
    }
    return render(request,'Feedback_System/thankyou.html',context =dic)

#############################################################################
def student_register(request):
    new_stu = NewStudentForm()

    if request.method == 'POST':
        new_stu = NewStudentForm(request.POST)

        if new_stu.is_valid():
            new_stu.save(commit=True)
            return thankyou(request)
        else:
            raise forms.ValidationError("Please Check the Details you've entered !!!")
    return render(request,'Feedback_System/student_register.html',{'stu_reg_form' : new_stu })

# #############################################################################
def faculty_register(request):
    new_fac = NewFacultyForm()

    if request.method == 'POST':
        new_fac = NewFacultyForm(request.POST)

        if new_fac.is_valid():
            new_fac.save(commit=True)
            return thankyou(request)
        else:
            raise forms.ValidationError("Please Check the Details you've entered !!!")

    return render(request,'Feedback_System/faculty_register.html',context={'fac_reg_form' : new_fac})

# #############################################################################
# def student_login(request):
#
#     return render(request,'Feedback_System/student_login.html',context={'stu_log_form' : stu_log_form})
#
# #############################################################################
# def faculty_login(request):
#
#     return render(request,'Feedback_System/faculty_login.html',context={'fac_log_form' : fac_log_form})
