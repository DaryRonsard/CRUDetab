from django.urls import path
from .views import list_user, login, update_user, delete_user

app_name = 'user'

urlpatterns = [
    path('', list_user, name='list-user'),
    path('login', login, name='login'),
    path('edit/<int:pk>/', update_user, name='update-user'),
    path('delete/<int:pk>/', delete_user, name='delete-user'),

]
