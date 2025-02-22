from django.db import models

# Create your models here.

class student_registration(models.Model):
    stu_id = models.CharField(max_length=10)
    stu_name = models.CharField(max_length=30)
    # stu_mobile=models.BigIntegerField(max_length=10)
    stu_mobile=models.IntegerField(help_text = ("Enter 6 digit roll number"))
