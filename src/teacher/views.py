from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeacherForm
from .models import Teacher
from django.contrib import messages


# Create your views here.
def list_teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'professeur/professeur.html', {'teachers': teachers})


def create_teacher(request):
    if request.method == 'POST':
        print('1')
        form = TeacherForm(request.POST)
        if form.is_valid():
            print('2')
            form.save()
            #messages.success(request, 'L\'enseignant a été ajouter avec succès.')
            return redirect('teacher:list-teacher')
        else:
            messages.error(request, 'warning')
    else:
        form = TeacherForm()
    return render(request, 'professeur/add.html', {'form': form})


def update_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('list-teacher')
            #messages.success(request, 'L\'enseignant a été mis à jour avec succès.')
        else:
            messages.error(request, 'warning')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'professeur/professeur.html', {'form': form})


def delete_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher:list-teacher')
