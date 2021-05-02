from django.urls import path
from .views import todoview, addtodo, deleteTodo

urlpatterns =[
    path('todoList/', todoview),

    path('addtodo/', addtodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo)

]