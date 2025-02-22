from django.urls import path
from django.shortcuts import render, HttpResponse
from student.views import *


# def hello(request):
#     return HttpResponse("this is testing page")

urlpatterns = [
    # path("",home, name="home")
    path("",home),
    path("all_students/", all_students, name="all_students"),
    path("stu_reg/", stu_reg, name="stu_reg" ),
    path("registration/", register, name="register"),


    # path("hello/", hello, name="hello_name",)


]
