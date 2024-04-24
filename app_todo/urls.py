from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.todo_add, name='todo_add'),
    path('delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),
    path('mark_complete/<int:todo_id>/', views.todo_mark_complete, name='todo_mark_complete'),
]
