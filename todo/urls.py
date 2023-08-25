
from django.urls import path 
from .  import views

urlpatterns = [
    #path('', views.crete_task, name  = 'create_task'),
    path('', views.apiOverview, name="api-overview"),
    path('create-task/', views.CreateTask, name  = 'create-task'),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('index/', views.index, name="todo"),
    path('del/<str:item_id>', views.remove, name="del"),
    
]