from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm
# Create your views here.

def home(req):
    form=StudentForm()
    if req.method=='POST':
        form=StudentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    return render(req,'home.html',{'form':form})

def list(req):

    students=Student.objects.all()
    return render(req,'list.html',{'students':students})

def delete(req,pk):
    Student.objects.filter(pk=pk).delete()
    return redirect('list')

def update(req,pk):
    student=get_object_or_404(Student,pk=pk)
    form=StudentForm(instance=student)
    if req.method=='POST':
        form=StudentForm(req.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(req,'home.html',{'form':form})