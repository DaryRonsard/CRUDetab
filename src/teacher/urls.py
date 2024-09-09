from django.urls import path
from .views import list_teacher, create_teacher, update_teacher, delete_teacher

app_name = 'teacher'

urlpatterns = [
    path('', list_teacher, name='list-teacher'),
    path('add/', create_teacher, name='create-teacher'),
    path('update/<int:id>/', update_teacher, name='update-teacher'),
    path('delete/<int:id>/', delete_teacher, name='delete-teacher'),
]
