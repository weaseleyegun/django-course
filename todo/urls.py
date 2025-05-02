from django.urls import path, include
from .views import *

urlpatterns = [
    path("update/<int:pk>/", TodoUpdateView.as_view()),
    path("create/", TodoCreateView.as_view()),
    path("list/", TodoListView.as_view()),
    path("<int:pk>/", TodoDetailView.as_view()),
    path("<str:name>/", todo_detail_name)
]