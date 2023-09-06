from django.shortcuts import render,HttpResponse
from .models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        gen = request.POST['gender']
        cla = request.POST['classname']
        regn = request.POST['reg']
        test = request.POST['test']
        if float(test)>100:
            return HttpResponse("Test Score Must Less Than 100 ")
        obj = Student()
        obj.name = name
        obj.email = email
        obj.dob = dob
        obj.gen = gen
        obj.stuClass = cla
        obj.reg = regn
        obj.test = test
        obj.save()
        return HttpResponse("<h1>Your Entry Have Been Saved</h1>")

    return render(request, 'index.html')

@login_required
def list_stu(request):
    obj = Student.objects.all()
    return render(request,'list.html',{'obj':obj})