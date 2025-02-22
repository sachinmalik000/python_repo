from student.models  import * 
from django import forms

class Student_Registration_Form(forms.ModelForm):
    class Meta:
        model = student_registration
        fields = "__all__"
    