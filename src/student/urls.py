from django.urls import path
from .views import student_list, create_student, update_student, delete_student

app_name = 'student'

urlpatterns = [
    path('', student_list , name='student-list'),
    path('add/', create_student, name='create-student'),
    path('edit/<int:id>/', update_student, name='update-student'),
    path('delete/<int:id>/', delete_student, name='delete-student'),

]
