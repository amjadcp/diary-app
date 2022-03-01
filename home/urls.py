from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('calendar', calendar, name='calendar'),
    path('create-diary', create_diary, name='create-diary'),
    path('edit-diary', edit_diary, name='edit-diary'),
    path('del-diary', del_diary, name='del-diary'),
    path('search', search, name='search'),
]
