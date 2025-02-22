from django.shortcuts import render, HttpResponse,redirect
from student.forms import *
# Create your views here.
def home(request):
    return render(request,'home.html')  
    # return HttpResponse('This is home page')

def register(request):
    data = student_registration.objects.all()
    context =  {'data':data}
    return render(request,'registration.html',context)  
    
    # return HttpResponse('This is home page')    

def all_students(request):
    data = student_registration.objects.all()
    context =  {'data':data}
    return render(request, 'all_students.html',context)

def stu_reg(request):
    form = Student_Registration_Form()
    submitted_data = None 
    if request.method=="POST":
        
        form = Student_Registration_Form(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('register') 

            # return redirect('register') 
            # return HttpResponse("Data Saved")
            # stu_name = form.cleaned_data['stu_name']
            # stu_mobile = form.cleaned_data['stu_mobile']
            # print(f"Name: {stu_name}")
            # print(f"Email: {stu_mobile}")
            # submitted_data = form.cleaned_data(form.cleaned_data ['stu_name', 'stu_mobile', 'stu_id'] )  # Retrieve cleaned form data
    else:
        form = Student_Registration_Form()            
    return render(request, 'stu_registration.html',{'form':form})
    # return render(request, 'stu_reg.html',{'form':form, "submitted_data": submitted_data})



