from django.contrib import admin
from student.models import student_registration

class Student_admin(admin.ModelAdmin):
    list_display = ['stu_name','stu_mobile']
admin.site.register(student_registration,Student_admin)

# Register your models here.
