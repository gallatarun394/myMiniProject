from django.conf.urls import include,url
from Feedback_System import views

urlpatterns =[
    url(r'^student_register/',views.student_register,name='stu_reg'),
    url(r'^faculty_register/',views.faculty_register,name='fac_reg'),
    url(r'^$',views.home_page,name='homepage'),
]
