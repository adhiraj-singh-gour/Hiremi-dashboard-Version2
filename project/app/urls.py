from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns = [
    path('',index,name="index"),
    path('superuser_login/',superuser_login,name="superuser_login"),
    path('otp_page/',otp_page,name="otp_page"),
    path('otp_verify/',otp_verify,name="otp_verify"),
    path('resend_otp/',resend_otp,name="resend_otp"),

    path('dashboard/',dashboard,name="dashboard"),
    path('mentorship/',mentorship,name="mentorship"),
    path('internship/',internship,name="internship"),
    path('fresher_Job/',fresher_Job,name="fresher_Job"),
    path('corporate_training/',corporate_training,name="corporate_training"),
    
    
]
