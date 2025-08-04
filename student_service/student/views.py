from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from student.forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'testapp/student_list.html', {'students': students})


def student_form(request, student_id=None):
    if student_id:
        student = get_object_or_404(Student, pk=student_id)
    else:
        student = None

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list') 
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'testapp/student_form.html', {'form': form, 'student': student})


def student_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect('student_list')  
