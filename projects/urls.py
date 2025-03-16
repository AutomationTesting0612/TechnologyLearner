from django.urls import path
from .views import project_list, add_project, update_project, delete_project

urlpatterns = [
    path('', project_list, name='project_list'),
    path('add/', add_project, name='add_project'),
    path('projects/update/<int:pk>/', update_project, name='update_project'),
    path('projects/delete/<int:pk>/', delete_project, name='delete_project'),
]