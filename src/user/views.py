from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserForm
from .models import User


# Create your views here.
def list_user(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:list-user')
        else:
            messages.error(request, 'Invalid')
    form = UserForm()
    return render(request, 'user/utilisateur.html', {'users': users,'form':form})


def login(request):
    pass


def logout(request):
    logout(request)
    redirect('user:login')


# def create_user(request, pk):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('user:list-user')
#         else:
#             messages.error(request,'Invalid')
#             form = UserForm()
#     return render(request, 'user/utilisateur.html', {'form': form, 'a': "&"})

def update_user(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:list-user')
    else:
        form = UserForm(instance=user)
    return render(request, 'user/useradd.html', context={'form': form})



def delete_user(request, pk):
    user = get_object_or_404(User, id=pk)
    user.delete()
    return redirect('user:list-user')

