from django.urls import path
from tasks.view import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('remove_tag/<int:task_id>/', views.remove_tag, name='remove_tag'),
]
