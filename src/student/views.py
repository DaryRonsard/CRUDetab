from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm
from .models import Student


# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/index.html', {'students': students})


def create_student(request):
    if request.method == 'POST':

        form = StudentForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('student:student-list')
        else:
            messages.error(request, "une Erreur est surevenu")
    else:
        form = StudentForm()
    context = {'form': form}
    return render(request, 'student/ajoueEleve.html', context)


def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:student-list')
        else:
            messages.error(request, "une Erreur est surevenu")
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/ajoutEleve.html', {'form': form})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student:student-list')
